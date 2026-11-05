"""Fetch Commvault's own API description, and list its operations.

Commvault publishes its REST API at https://api.commvault.com/docs/: a
site generated from its OpenAPI files - a core file (OpenAPI3, mostly
the V4 API) and about a hundred more by subject (Client Operations, Job
Operations, Kubernetes, ...) - one version per Service Pack ("Latest
(SP46)", SP44, SP40, ...). The OpenAPI files themselves are not
served; each operation's page carries its operation object (method,
path, parameters, body, answers) in that page's script, as a JavaScript
object literal. This reads them - parsing the literal, never running the
script - and writes:

- spec/<release>/operations.json - every operation, rebuilt from the
  pages, once each (not committed: Commvault's text);
- spec/operations-<release>.tsv - one line per operation, each once
  (an operation in the core file and a subject file counts once, under
  the subject): area, method, path, operationId (committed). The area
  is the subject file's name, or for the core file the operation's
  first tag. The SDK's live
  coverage is measured against it; diffing two releases' lists shows
  what changed.

    uv run python scripts/spec.py              # the latest Service Pack
    uv run python scripts/spec.py --sp 44      # an older one
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any

import httpx

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://api.commvault.com"
CORE = "OpenAPI3"
# Other Commvault products' APIs on the same site, served by their own
# services, not by a CommServe.
OTHER_PRODUCTS = {"ClumioAPIs", "CloudRewindAPIs"}


class Literal:
    """A reader for one JavaScript object literal as a minifier writes it:
    {a:1,"b-c":"x",d:!0,e:void 0,f:[1,2]}. Values only - an expression
    it does not know (a function, a variable) is an error, so nothing
    that is not plain data gets through."""

    WORDS = {"true": True, "false": False, "null": None}

    def __init__(self, text: str, at: int) -> None:
        self.s, self.i = text, at

    def value(self) -> Any:
        s, i = self.s, self.i
        c = s[i]
        if c == "{":
            return self.obj()
        if c == "[":
            return self.arr()
        if c in "\"'`":
            return self.string()
        if s.startswith("!0", i):
            self.i += 2
            return True
        if s.startswith("!1", i):
            self.i += 2
            return False
        if s.startswith("void 0", i):
            self.i += 6
            return None
        m = re.compile(r"-?(?:\d+\.?\d*(?:e[+-]?\d+)?|\.\d+(?:e[+-]?\d+)?)", re.I).match(s, i)
        if m:
            self.i = m.end()
            n = m.group()
            return float(n) if any(ch in n for ch in ".eE") else int(n)
        m = re.compile(r"[A-Za-z_$][\w$]*").match(s, i)
        if m and m.group() in self.WORDS:
            self.i = m.end()
            return self.WORDS[m.group()]
        raise ValueError(f"not plain data at {i}: {s[i : i + 40]!r}")

    def string(self) -> str:
        quote = self.s[self.i]
        self.i += 1
        out = []
        while True:
            c = self.s[self.i]
            if c == "\\":
                nxt = self.s[self.i + 1]
                if nxt == "u":
                    out.append(chr(int(self.s[self.i + 2 : self.i + 6], 16)))
                    self.i += 6
                    continue
                if nxt == "x":
                    out.append(chr(int(self.s[self.i + 2 : self.i + 4], 16)))
                    self.i += 4
                    continue
                out.append({"n": "\n", "t": "\t", "r": "\r", "b": "\b", "f": "\f"}.get(nxt, nxt))
                self.i += 2
                continue
            if c == quote:
                self.i += 1
                return "".join(out)
            if quote == "`" and c == "$" and self.s[self.i + 1] == "{":
                raise ValueError("template expression")
            out.append(c)
            self.i += 1

    def key(self) -> str:
        c = self.s[self.i]
        if c in "\"'":
            return self.string()
        m = re.compile(r"[\w$]+").match(self.s, self.i)
        if not m:
            raise ValueError(f"bad key at {self.i}")
        self.i = m.end()
        return m.group()

    def obj(self) -> dict[str, Any]:
        self.i += 1
        out: dict[str, Any] = {}
        while self.s[self.i] != "}":
            k = self.key()
            if self.s[self.i] != ":":
                raise ValueError(f"expected ':' at {self.i}")
            self.i += 1
            out[k] = self.value()
            if self.s[self.i] == ",":
                self.i += 1
        self.i += 1
        return out

    def arr(self) -> list[Any]:
        self.i += 1
        out: list[Any] = []
        while self.s[self.i] != "]":
            out.append(self.value())
            if self.s[self.i] == ",":
                self.i += 1
        self.i += 1
        return out


def operation_in(script: str) -> dict[str, Any]:
    """The page's operation object: the literal after `api:` that has a
    method and a path."""
    for m in re.finditer(r"\bapi:\{", script):
        try:
            found = Literal(script, m.end() - 1).value()
        except (ValueError, IndexError):
            continue
        if isinstance(found, dict) and "method" in found and "path" in found:
            return found
    raise ValueError("no operation object on the page")


def area_of(name: str) -> str:
    """A file's or tag's name as an area: "Job Operations" and
    "JobOperations" are both `job`, "AWS-DB-Redshift-operations" is
    `aws_db_redshift`."""
    text = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "_", name)
    text = re.sub(r"[^A-Za-z0-9]+", "_", text).strip("_").lower()
    text = re.sub(r"_?operations?$", "", text) or "general"
    return re.sub(r"_+", "_", text)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--sp", help="Service Pack (44, 40, ...); default the latest")
    args = parser.parse_args()
    version = f"SP{args.sp}" if args.sp else "latest"
    with httpx.Client(base_url=SITE, timeout=60, follow_redirects=True) as http:
        page = http.get(f"/docs/{version}/commvault-rest-api-public/")
        page.raise_for_status()
        # A Service Pack's site may live on its own host (api-lts-sp44...).
        site = f"{page.url.scheme}://{page.url.host}"
        label = re.search(r"Latest \(SP(\d+)\)", page.text)
        sp = args.sp or (label.group(1) if label else None)
        if not sp:
            print("Could not tell which Service Pack the site describes; pass --sp.")
            return 1
        release = f"11.{sp}"
        main_js = re.search(r'src="(/assets/js/main\.[0-9a-f]+\.js)"', page.text)
        runtime_js = re.search(r'src="(/assets/js/runtime~main\.[0-9a-f]+\.js)"', page.text)
        if not main_js or not runtime_js:
            print("The site's layout has changed: no main/runtime script on the page.")
            return 1
        bundle = http.get(site + main_js.group(1)).text
        runtime = http.get(site + runtime_js.group(1)).text
        # route (file, page) -> content key -> chunk id -> file name
        routes = re.findall(
            rf'"/docs/{version}/api/cv/([^/"]+)/([a-z0-9-]+)/-[0-9a-f]+":'
            r'\{"__comp":"[0-9a-f]+","content":"([0-9a-f]+)"\}',
            bundle,
        )
        chunk_of = {key: cid for cid, key in re.findall(r'(\d+):"([0-9a-f]{8})"', runtime)}
        hashes = dict(re.findall(r'(\d+):"([0-9a-f]{8})"', runtime.split('[e]+".js"')[0]))

        def fetch(route: tuple[str, str, str]) -> tuple[str, dict[str, Any] | None]:
            file, _slug, key = route
            if file in OTHER_PRODUCTS:
                return file, None
            cid = chunk_of.get(key)
            if cid is None:
                return file, None
            answer = http.get(f"{site}/assets/js/{key}.{hashes.get(cid, '')}.js")
            if answer.status_code != 200:
                return file, None
            try:
                return file, operation_in(answer.text)
            except ValueError:
                return file, None  # a file's or a tag's index page

        with ThreadPoolExecutor(max_workers=4) as pool:
            found = list(pool.map(fetch, sorted(set(routes))))

    # Each operation once: the same call can be in the core file and a
    # subject file, and in two subject files with its parameter spelled
    # differently ({clientId}, {ClientId}) - Commvault's paths are not
    # case sensitive.
    ops: dict[tuple[str, str], dict[str, Any]] = {}
    files = set()
    for file, op in found:
        if op is None or file in OTHER_PRODUCTS:
            continue
        files.add(file)
        method, path = op.pop("method"), op.pop("path")
        for noise in ("postman", "jsonRequestBodyExample", "info", "servers", "securitySchemes"):
            op.pop(noise, None)
        key = (method, re.sub(r"\{[^}]+\}", "{}", path).lower())
        area = area_of(str((op.get("tags") or ["untagged"])[0]) if file == CORE else file)
        if key not in ops or ops[key]["file"] == CORE:
            ops[key] = {"area": area, "method": method, "path": path, "file": file, "op": op}
    target = ROOT / "spec" / release
    target.mkdir(parents=True, exist_ok=True)
    listed = sorted(ops.values(), key=lambda o: (o["area"], o["path"], o["method"]))
    (target / "operations.json").write_text(json.dumps(listed, indent=1, sort_keys=True))
    rows = [
        (o["area"], o["method"].upper(), o["path"], str(o["op"].get("operationId", "")))
        for o in listed
    ]
    out = ROOT / "spec" / f"operations-{release}.tsv"
    out.write_text("area\tmethod\tpath\toperationId\n" + "".join("\t".join(r) + "\n" for r in rows))
    skipped = sum(1 for _, op in found if op is None)
    print(
        f"Commvault {release}: {len(rows)} operations in {len(files)} files, from "
        f"{len(found)} pages ({skipped} were index pages or other products)"
        f" -> {out.relative_to(ROOT)}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
