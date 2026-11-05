"""Generate commvault_sdk.raw: one method per operation in Commvault's
own API description (fetched by scripts/spec.py into spec/<release>/).

    uv run python scripts/generate.py 11.46

`cv.raw.<area>.<call>(...)` is the whole API, thinly: path parameters
are positional, query parameters and headers keyword-only, a request
body is `body=`; the answer comes back decoded (JSON, text or bytes),
and an error Commvault puts inside a 200 is raised. Reads go through
the retrying transport; everything else is refused by a read-only
client and sent once. The hand-written groups (`cv.jobs`, `cv.clients`,
...) sit on top for what blt uses.

Names come from the path - Commvault's operationIds are partly prose -
with the version segment (V4, v1, api) left out:

    GET    /V4/Plan/Summary             get_plan_summary
    GET    /Client                      list_client (a /Client/{id} below it)
    GET    /Client/{clientId}           get_client
    DELETE /V4/ServerPlan/{planId}      delete_server_plan
    POST   /Job/{jobId}/action/kill     post_job_action_kill

A segment followed by a parameter is made singular; clashes get
`_by_<parameter>`, then a number.
"""

from __future__ import annotations

import json
import keyword
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any
from urllib.parse import parse_qsl

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "src" / "commvault_sdk" / "raw"
VERSION_SEGMENTS = {"v1", "v2", "v4", "v5", "api"}
LISTING = {"limit", "offset", "start", "filter", "sort", "fq", "pagingconfig", "search", "q"}
BUILTINS = {
    "filter",
    "id",
    "type",
    "format",
    "input",
    "hash",
    "object",
    "list",
    "dir",
    "max",
    "min",
}


def snake(text: str) -> str:
    text = re.sub(r"[^A-Za-z0-9]+", "_", text)
    text = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "_", text)
    text = re.sub(r"(?<=[A-Z])(?=[A-Z][a-z])", "_", text)
    return re.sub(r"_+", "_", text).strip("_").lower()


def singular(word: str) -> str:
    for plural, one in (("policies", "policy"), ("ies", "y"), ("sses", "ss"), ("xes", "x")):
        if word.endswith(plural):
            return word[: -len(plural)] + one
    if word.endswith("s") and not word.endswith(("ss", "us", "is")):
        return word[:-1]
    return word


def py_name(name: str) -> str:
    n = snake(name) or "value"
    if n[0].isdigit():
        n = "p_" + n
    if keyword.iskeyword(n) or n in BUILTINS:
        n += "_"
    return n


def path_params(path: str) -> list[str]:
    return list(dict.fromkeys(re.findall(r"\{([^}]+)\}", path)))


def call_name(method: str, path: str, listing: bool) -> str:
    segments = [s for s in path.strip("/").split("/") if s and s.lower() not in VERSION_SEGMENTS]
    words: list[str] = []
    for i, seg in enumerate(segments):
        if seg.startswith("{"):
            continue
        # byName(clientName='{x}') -> by_name
        seg = re.sub(r"\(.*\)$", "", seg)
        nxt = segments[i + 1] if i + 1 < len(segments) else ""
        word = snake(seg)
        words.append(singular(word) if nxt.startswith("{") else word)
    ends_with_param = bool(segments) and segments[-1].startswith("{")
    verb = {"get": "list" if listing and not ends_with_param else "get"}.get(method, method)
    return f"{verb}_{'_'.join(w for w in words if w) or 'root'}"


def accept_for(answers: list[str]) -> str | None:
    """An Accept to send when the operation does not answer JSON."""
    if not answers or any("json" in a for a in answers):
        return None
    return answers[0].split(";")[0]


def normalise(entry: dict[str, Any]) -> dict[str, Any]:
    op = entry["op"]
    # A few calls (the dashboard's canned reports) carry a fixed query in
    # the path itself: /clients/count?type=fileserver,vm,laptop.
    path, _, fixed = entry["path"].partition("?")
    path = "/" + path.lstrip("/")
    entry = {**entry, "path": path}
    params = [p for p in op.get("parameters") or [] if p.get("in") in ("path", "query", "header")]
    named = {p["name"] for p in params if p.get("in") == "path"}
    # A parameter in the path that the description forgot to declare.
    params += [{"name": n, "in": "path"} for n in path_params(entry["path"]) if n not in named]
    # Declared in the path but spelled differently there: the path wins.
    in_path = {n.lower(): n for n in path_params(entry["path"])}
    for p in params:
        if p.get("in") == "path" and p["name"] not in in_path.values():
            p["name"] = in_path.get(p["name"].lower(), p["name"])
    params = [p for p in params if p.get("in") != "path" or p["name"] in in_path.values()]
    body = op.get("requestBody") or {}
    answers: list[str] = []
    for code, response in (op.get("responses") or {}).items():
        if str(code).startswith("2"):
            answers += list((response or {}).get("content") or {})
    return {
        "method": entry["method"],
        "path": entry["path"],
        "params": params,
        "body": list(body.get("content") or {}),
        "answers": answers,
        "fixed": dict(parse_qsl(fixed, keep_blank_values=True)) if fixed else {},
        "summary": summary_of(op),
        "op_id": str(op.get("operationId") or "").strip(),
        "deprecated": bool(op.get("deprecated")),
        "version": version_of(entry["path"]),
    }


def summary_of(op: dict[str, Any]) -> str:
    """One line on what the call does: the summary, or Commvault's
    prose operationId ("Get Job Summary of a Job"), or the description's
    first sentence."""
    for text in (op.get("summary"), op.get("operationId")):
        if text and " " in str(text).strip():
            return " ".join(str(text).split())
    words = " ".join(str(op.get("description") or "").split())
    words = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", words)
    return words.split(". ")[0][:160]


def version_of(path: str) -> str:
    first = path.strip("/").split("/")[0].lower()
    return first if re.fullmatch(r"v\d+", first) else ""


def shape(path: str) -> str:
    return re.sub(r"\{[^}]+\}", "{}", path).lower().rstrip("/")


def render_area(
    area: str, entries: list[dict[str, Any]], release: str, collections: set[str]
) -> tuple[str, str]:
    ops = [normalise(e) for e in entries]
    names: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for op in ops:
        query = {p["name"].lower() for p in op["params"] if p["in"] == "query"}
        # A listing: it pages or filters, or there is a /{id} below it.
        listing = bool(query & LISTING) or shape(op["path"]) in collections
        name = call_name(op["method"], op["path"], listing)
        if op["fixed"] and op["op_id"] and " " not in op["op_id"]:
            # One path, many canned queries: named by Commvault's own id.
            name = py_name(op["op_id"]).rstrip("_")
        names[name].append(op)
    final: list[tuple[str, dict[str, Any]]] = []
    for name, group in names.items():
        if len(group) == 1:
            final.append((name, group[0]))
            continue
        # The same resource at two API versions (/Plan, /v2/Plan, /V4/Plan):
        # the newer ones are named for their version.
        if len({op["version"] for op in group}) == len(group):
            final += [(name + (f"_{op['version']}" if op["version"] else ""), op) for op in group]
            continue
        for op in group:
            pp = [p["name"] for p in op["params"] if p["in"] == "path"]
            final.append((name + ("_by_" + "_".join(snake(p) for p in pp) if pp else ""), op))
    seen: dict[str, int] = defaultdict(int)
    out = []
    for name, op in sorted(final, key=lambda x: (x[1]["path"], x[1]["method"])):
        seen[name] += 1
        out.append(render_op(f"{name}_{seen[name]}" if seen[name] > 1 else name, op))
    cls = "".join(w.capitalize() for w in area.split("_"))
    header = (
        f'"""Commvault {release} API, area `{area}`: every operation, thinly.\n\n'
        "Generated by scripts/generate.py from Commvault's own API description\n"
        f'(spec/{release}/operations.json). Do not edit.\n"""\n\n'
        "from __future__ import annotations\n\n"
        "from typing import Any\n\n"
        "from .._base import Resource\n\n\n"
        f"class {cls}(Resource):\n"
        f'    """`{area}`: {len(ops)} operations."""\n'
    )
    return header + "\n".join(out), cls


def render_op(name: str, op: dict[str, Any]) -> str:
    params = op["params"]
    pps = [p for p in params if p["in"] == "path"]
    others = [p for p in params if p["in"] in ("query", "header")]
    sig = ["self"]
    used = set()
    for p in pps:
        n = py_name(p["name"])
        while n in used:
            n += "_"
        used.add(n)
        p["py"] = n
        sig.append(f"{n}: str | int")
    kw = []
    seen_names = set()
    for p in others:
        if (p["in"], p["name"]) in seen_names:
            continue
        seen_names.add((p["in"], p["name"]))
        n = py_name(p["name"])
        while n in used or n in ("body", "files"):
            n += "_"
        used.add(n)
        p["py"] = n
        kw.append(f"{n}: Any = None")
    others = [p for p in others if "py" in p]
    multipart = any(t.startswith("multipart/") for t in op["body"])
    form = any(t.startswith("application/x-www-form-urlencoded") for t in op["body"])
    if op["body"]:
        kw.append("files: Any = None" if multipart else "body: Any = None")
    if kw:
        sig += ["*", *kw]
    path_expr = op["path"].replace("\\", "\\\\").replace('"', '\\"')
    for p in pps:
        path_expr = path_expr.replace("{" + p["name"] + "}", "{" + p["py"] + "}")
    # Literal braces elsewhere would be read as f-string fields.
    lines = [f"    def {name}({', '.join(sig)}) -> Any:"]
    doc = f"`{op['method'].upper()} {op['path']}`"
    if op["summary"]:
        doc += f" - {op['summary'].rstrip('.')}."
    if op["deprecated"]:
        doc += " Deprecated."
    q = [p["name"] for p in others if p["in"] == "query"]
    h = [p["name"] for p in others if p["in"] == "header"]
    detail = []
    if op["fixed"]:
        detail.append("Always sends: " + "&".join(f"{k}={v}" for k, v in op["fixed"].items()) + ".")
    if q:
        detail.append("Query: " + ", ".join(q) + ".")
    if h:
        detail.append("Headers: " + ", ".join(h) + ".")
    if op["body"]:
        detail.append("Body: " + ", ".join(sorted({t.split(";")[0] for t in op["body"]})) + ".")
    doc = doc.replace("\\", "\\\\").replace('"""', "'''")
    text = doc + (("\n\n        " + " ".join(detail)) if detail else "")
    lines.append(f'        """{text}"""')
    lines.append(f'        path = f"{path_expr}"' if pps else f'        path = "{path_expr}"')
    call = [f'"{op["method"].upper()}"', "path"]
    if q or op["fixed"]:
        fixed = [f"{json.dumps(k)}: {json.dumps(v)}" for k, v in op["fixed"].items()]
        given = [f'"{p["name"]}": {p["py"]}' for p in others if p["in"] == "query"]
        call.append("params={" + ", ".join(fixed + given) + "}")
    if h:
        call.append(
            "headers={"
            + ", ".join(f'"{p["name"]}": {p["py"]}' for p in others if p["in"] == "header")
            + "}"
        )
    if op["body"]:
        call.append("files=files" if multipart else ("form=body" if form else "body=body"))
    accept = accept_for(op["answers"])
    if accept:
        call.append(f'accept="{accept}"')
    if op["method"] != "get":
        call.append("change=True")
    lines.append(f"        return self._call({', '.join(call)})")
    return "\n".join(lines) + "\n"


def main() -> int:
    release = sys.argv[1] if len(sys.argv) > 1 else "11.46"
    source = ROOT / "spec" / release / "operations.json"
    if not source.exists():
        print(f"No {source.relative_to(ROOT)} - run scripts/spec.py first.")
        return 1
    by_area: dict[str, list[dict[str, Any]]] = defaultdict(list)
    entries = json.loads(source.read_text())
    for entry in entries:
        by_area[entry["area"]].append(entry)
    # Paths with a /{id} directly below them anywhere in the API.
    collections = {
        shape(e["path"]).rsplit("/", 1)[0] for e in entries if shape(e["path"]).endswith("/{}")
    }
    OUT.mkdir(parents=True, exist_ok=True)
    for old in OUT.glob("*.py"):
        old.unlink()
    areas = []
    for area in sorted(by_area):
        module = py_name(area).rstrip("_")
        text, cls = render_area(area, by_area[area], release, collections)
        (OUT / f"{module}.py").write_text(text)
        areas.append((module, cls, len(by_area[area])))
    total = sum(a[2] for a in areas)
    init = [
        f'"""Every operation of the Commvault {release} API, one method each, by area:\n'
        "`cv.raw.job.list_job()`, `cv.raw.plan.get_plan_summary()`, ...\n\n"
        f"{total} operations in {len(areas)} areas. Generated by scripts/generate.py from\n"
        'Commvault\'s own API description. Do not edit.\n"""\n',
        "from __future__ import annotations\n",
        "from typing import TYPE_CHECKING\n",
    ]
    init += [f"from .{m} import {c}" for m, c, _ in areas]
    init += [
        "",
        "if TYPE_CHECKING:",
        "    from ..client import CommvaultClient",
        "",
        f'RELEASE = "{release}"',
        "",
        "",
        "class Raw:",
        '    """The whole API, by area."""',
        "",
        "    def __init__(self, client: CommvaultClient) -> None:",
    ]
    init += [f"        self.{m} = {c}(client)" for m, c, _ in areas]
    (OUT / "__init__.py").write_text("\n".join(init) + "\n")
    print(f"commvault_sdk.raw: {total} operations in {len(areas)} areas (Commvault {release})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
