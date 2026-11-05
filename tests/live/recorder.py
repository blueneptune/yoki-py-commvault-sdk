"""What the live tests keep: every request and answer, masked, written up
as docs/live/ pages - and which of the spec's operations were proven.

- `Recorder` is an httpx transport wrapped round the real one: it hands
  every request on and keeps a copy of the exchange.
- `Masker` replaces what identifies the lab - host names, addresses, user
  names, policy and storage names, anything key- or certificate-like -
  with stable placeholders. This repository is public. A page that
  still contains a known name after masking is not written.
- `write_pages` and `write_coverage` turn a run into Markdown.
"""

from __future__ import annotations

import base64
import inspect
import json
import re
import textwrap
import time
from collections.abc import Callable, Iterable
from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import httpx

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs" / "live"


@dataclass
class Exchange:
    method: str
    url: httpx.URL
    request_body: bytes
    status: int
    content_type: str
    body: bytes
    seconds: float


class Recorder(httpx.BaseTransport):
    def __init__(self, inner: httpx.BaseTransport) -> None:
        self.inner = inner
        self.exchanges: list[Exchange] = []

    def handle_request(self, request: httpx.Request) -> httpx.Response:
        started = time.monotonic()
        response = self.inner.handle_request(request)
        response.read()
        self.exchanges.append(
            Exchange(
                method=request.method,
                url=request.url,
                request_body=request.content,
                status=response.status_code,
                content_type=response.headers.get("content-type", ""),
                body=response.content,
                seconds=time.monotonic() - started,
            )
        )
        return response

    def close(self) -> None:
        self.inner.close()


# Keys whose values are never shown, whatever they hold.
SECRET_KEY = re.compile(
    r"password|passwd|secret|token|apikey|api_key|fingerprint|serial|certificate|"
    r"privatekey|licen[cs]e|signature|^key$|credential|^pem$|crl|keystore|passphrase|authcode",
    re.I,
)
IPV4 = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")
IPV6 = re.compile(r"\b(?:[0-9a-f]{1,4}:){3,7}[0-9a-f]{1,4}\b", re.I)
EMAIL = re.compile(r"\b[\w.+-]+@[\w-]+\.[\w.-]+\b")
HEX_PAIRS = re.compile(r"\b(?:[0-9A-F]{2}:){7,}[0-9A-F]{2}\b", re.I)
PEM = re.compile(r"-----BEGIN ([A-Z ]+)-----.*?-----END \1-----", re.S)
# Text hex-encoded into ids (NetBackup does it to disk volume names;
# kept here for any product that does the same).
HEX_TEXT = re.compile(r"\b(?:[0-9A-F]{2}){6,}\b")
BASE64_TEXT = re.compile(r"[A-Za-z0-9+/]{16,}={0,2}")
# host.domain - a name ending in a domain suffix a lab or company uses
# (not code like cv.raw.job.list_job, nor example.com placeholders).
FQDN = re.compile(
    r"\b(?:[A-Za-z0-9-]+\.)+"
    r"(?:home|lab|local|lan|corp|internal|intra|intranet|private|com|net|org|io|dev|cloud|[a-z]{2})"
    r"\b(?!\.)",
    re.I,
)

# A host name worth learning from free text: one in a lab's own domain.
# (Answers are full of dotted words - subclient.id, test.py - that the
# wider FQDN pattern, used for masking, would take for hosts.)
LAB_FQDN = re.compile(
    r"\b(?:[A-Za-z0-9-]+\.)+(?:home|lab|local|lan|corp|internal|intra|intranet|private)\b(?!\.)",
    re.I,
)

# Keys whose values name something in the lab: masked wherever they turn
# up, with a placeholder of their kind.
IDENTIFYING = {
    "hostname": "host",
    "clientname": "host",
    "servername": "host",
    "mediaservername": "host",
    "destinationmediaservername": "host",
    "destinationstorageunitname": "storage-unit",
    "storageunitname": "storage-unit",
    "storageservername": "storage-server",
    # Not displayName or commonName: Commvault puts a displayName on
    # everything, labels and tabs included; its real objects are named by
    # clientName, hostName and the entity names below.
    "vmname": "asset",
    "instancename": "asset",
    "databasename": "database",
    "vcenter": "vcenter",
    "vcentername": "vcenter",
    "esxihost": "host",
    "esxhost": "host",
    "datacenter": "datacenter",
    "cluster": "cluster",
    "clustername": "cluster",
    "datastore": "datastore",
    "datastorename": "datastore",
    "resourcepool": "resource-pool",
    "folder": "folder",
    "username": "user",
    "user": "user",
    "principal": "user",
    "domainname": "domain",
    "policyname": "policy",
    # Commvault
    "commcellname": "commcell",
    "commcell": "commcell",
    "csname": "commcell",
    "cshostname": "host",
    "netname": "host",
    "hostnamedisplay": "host",
    "mediaagentname": "media-agent",
    "mediaagent": "media-agent",
    "libraryname": "library",
    "storagepoolname": "storage-pool",
    "storagepolicyname": "storage-policy",
    "copyname": "storage-copy",
    "planname": "plan",
    "subclientname": "subclient",
    "backupsetname": "backupset",
    "clientgroupname": "client-group",
    "mountpath": "mount-path",
    "mountpathname": "mount-path",
    "email": "user",
    "fullname": "user",
    "usergroupname": "user-group",
    "companyname": "company",
    "providerdomainname": "domain",
}


# Commvault's V4 answers name things as {"plan": {"id": 3, "name": ...}}:
# a plain `name` is a lab name when its parent is one of these.
ENTITY_PARENTS = {
    "client": "host",
    "clients": "host",
    "cliententity": "host",
    "clientgroup": "client-group",
    "servergroup": "client-group",
    "server": "host",
    "servers": "host",
    "mediaagent": "media-agent",
    "mediaagents": "media-agent",
    "accessnode": "host",
    "accessnodes": "host",
    "hypervisor": "hypervisor",
    "hypervisors": "hypervisor",
    "vm": "asset",
    "virtualmachines": "asset",
    "plan": "plan",
    "plans": "plan",
    "storagepool": "storage-pool",
    "storagepools": "storage-pool",
    "storage": "storage-pool",
    "library": "library",
    "libraries": "library",
    "storagepolicy": "storage-policy",
    "user": "user",
    "users": "user",
    "usergroup": "user-group",
    "usergroups": "user-group",
    "commcell": "commcell",
    "company": "company",
    "companies": "company",
    "credential": "credential",
    "credentials": "credential",
    "subclient": "subclient",
    "backupset": "backupset",
}


# The product's own words, never a lab's name (a CommServe's client can
# be called "CommServ"; the pages say "Commvault" throughout).
PRODUCT_WORDS = {
    "commvault",
    "commserv",
    "commserve",
    "commcell",
    "metallic",
    "mediaagent",
    # and the page's own words (<details><summary>Answer</summary>)
    "details",
    "summary",
    "answer",
}
# Public domains answers link to (documentation, cloud endpoints): not
# the lab's hosts.
PUBLIC_DOMAINS = (
    "commvault.com",
    "metallic.io",
    "microsoft.com",
    "windows.net",
    "azure.com",
    "amazonaws.com",
    "aws.amazon.com",
    "google.com",
    "googleapis.com",
    "oracle.com",
    "salesforce.com",
    "example.com",
)


def _entity_name(item: Any) -> str | None:
    """The `name` of a real object - one with an id beside it - not a
    label such as {"name": "Summary"}."""
    if not isinstance(item, dict) or not isinstance(item.get("name"), str):
        return None
    if any(re.search(r"(^id$|Id$|^guid$)", str(k)) for k in item):
        return str(item["name"])
    return None


def _matcher(name: str) -> str:
    """A name of six characters or more is masked wherever it appears -
    also inside another name, as a host name in 1M_<host>_DS3; a shorter
    one only as a word of its own, so masking "blue" leaves "bluetooth"."""
    if len(name) >= 6:
        return re.escape(name)
    return r"(?<![A-Za-z0-9])" + re.escape(name) + r"(?![A-Za-z0-9])"


class Masker:
    """Stable placeholders: the same real name always becomes the same
    placeholder within a run, so a page still reads sensibly."""

    def __init__(self) -> None:
        self.names: dict[str, str] = {}
        self._counts: dict[str, int] = {}
        self._addresses: dict[str, str] = {}
        self._pattern: re.Pattern[str] | None = None
        self.prefixes: list[str] = []
        # Where each name was learned (the key), for the leak guard's message.
        self.source: dict[str, str] = {}

    def learn(self, value: Any, key: str = "") -> None:
        """Find the names in an answer before anything is written, so a
        name met on one page is masked on all of them."""
        kind = IDENTIFYING.get(key.lower())
        if kind and isinstance(value, str):
            self.add(value, kind)
            self.source.setdefault(value, key)
        elif isinstance(value, dict):
            parent = ENTITY_PARENTS.get(key.lower())
            if parent:
                self.add(_entity_name(value), parent)
                self.source.setdefault(str(_entity_name(value)), f"{key}.name")
            for k, v in value.items():
                self.learn(v, k)
        elif isinstance(value, list):
            for v in value:
                self.learn(v, key)
            if ENTITY_PARENTS.get(key.lower()):
                for v in value:
                    self.add(_entity_name(v), ENTITY_PARENTS[key.lower()])
                    self.source.setdefault(str(_entity_name(v)), f"{key}[].name")
        if isinstance(value, str):
            for name in LAB_FQDN.findall(value):
                if not IPV4.fullmatch(name) and not name.lower().endswith(PUBLIC_DOMAINS):
                    self.add(name, "host")
                    self.source.setdefault(name, "text")

    def came_from(self, short: str) -> str | None:
        """For a short name: the dotted name it was cut from, and its key."""
        for full, key in self.source.items():
            if full.lower().startswith(short.lower() + "."):
                return f"{full} ({key})"
        return None

    def add(self, real: str | None, kind: str, *, short: bool = True) -> None:
        """Mask `real` (any case) as `<kind>-NN`. Our own bltlive-*
        objects are made up, so they stay as they are."""
        if (
            not real
            or len(real) < 3
            or real.lower().startswith("bltlive")
            or real.lower() in PRODUCT_WORDS
            or real in self.names
        ):
            return
        self._counts[kind] = self._counts.get(kind, 0) + 1
        self.names[real] = f"{kind}-{self._counts[kind]:02d}"
        # Short names inside FQDNs too: backup01.lab.example -> primary-01.
        if short and "." in real and not IPV4.fullmatch(real):
            first = real.split(".")[0]
            if len(first) >= 3 and first not in self.names and first.lower() not in PRODUCT_WORDS:
                self.names[first] = self.names[real]
        self._pattern = None

    def _hex(self, match: re.Match[str]) -> str:
        """Mask inside hex-encoded text, and encode it again."""
        try:
            decoded = bytes.fromhex(match.group(0)).decode("ascii")
        except ValueError:
            return match.group(0)
        if not decoded.isprintable():
            return match.group(0)
        masked = self.text(decoded)
        return match.group(0) if masked == decoded else masked.encode().hex().upper()

    def _host(self, match: re.Match[str]) -> str:
        real = match.group(0)
        if real.lower().endswith(PUBLIC_DOMAINS) or IPV4.fullmatch(real):
            return real
        # Masked whole; its first part (subclient of subclient.id) is a
        # name of its own only when the domain is a lab's.
        self.add(real, "host", short=bool(LAB_FQDN.fullmatch(real)))
        return self.names.get(real, real)

    def _named(self, real: str) -> str:
        if real.lower().startswith("bltlive"):
            return real
        self.add(real, "name")
        return self.names.get(real, real)

    def _address(self, match: re.Match[str]) -> str:
        real = match.group(0)
        if real.startswith(("0.", "127.", "255.")) or real in ("0.0.0.0",):
            return real
        return self._addresses.setdefault(real, f"192.0.2.{len(self._addresses) + 1}")

    def text(self, value: str) -> str:
        if self.names:
            if self._pattern is None:
                ordered = sorted(self.names, key=len, reverse=True)
                self._pattern = re.compile("|".join(_matcher(n) for n in ordered), re.I)
            lower = {k.lower(): v for k, v in self.names.items()}
            value = self._pattern.sub(lambda m: lower[m.group(0).lower()], value)
        value = PEM.sub(lambda m: f"<{m.group(1).lower()} masked>", value)
        value = HEX_TEXT.sub(self._hex, value)
        for prefix in self.prefixes:
            value = re.sub(
                rf"(?<![A-Za-z0-9]){re.escape(prefix)}[A-Za-z0-9.-]*",
                lambda m: self._named(m.group(0)),
                value,
                flags=re.I,
            )
        value = EMAIL.sub("someone@example.com", value)
        value = FQDN.sub(self._host, value)
        value = HEX_PAIRS.sub("<hex>", value)
        value = IPV6.sub("2001:db8::1", value)
        return IPV4.sub(self._address, value)

    def data(self, value: Any, key: str = "") -> Any:
        if key and SECRET_KEY.search(key) and value not in (None, "", [], {}):
            return "<masked>"
        if isinstance(value, dict):
            return {self.text(k): self.data(v, k) for k, v in value.items()}
        if isinstance(value, list):
            return [self.data(v, key) for v in value]
        if isinstance(value, str):
            return self.text(value)
        return value

    def leaks(self, page: str) -> list[str]:
        """Known names still in a finished page - should be none. Hex- and
        base64-encoded text is decoded and looked at too."""
        decoded = []
        for chunk in HEX_TEXT.findall(page):
            decoded.append(bytes.fromhex(chunk).decode("latin-1"))
        for chunk in BASE64_TEXT.findall(page):
            try:
                decoded.append(base64.b64decode(chunk + "=" * (-len(chunk) % 4)).decode("latin-1"))
            except ValueError:
                pass
        written = page
        page = page + "\n" + "\n".join(decoded)
        found = [n for n in self.names if re.search(_matcher(n), page, re.I)]
        found += [
            p for p in self.prefixes if re.search(rf"(?<![A-Za-z0-9]){re.escape(p)}", page, re.I)
        ]
        # Host-shaped text on the page as written (decoded bytes are full
        # of accidental a.bc shapes); known names are checked in both.
        found += [h for h in FQDN.findall(written) if not h.lower().endswith(PUBLIC_DOMAINS)]
        return found


def shorten(value: Any, items: int = 3, chars: int = 400) -> Any:
    """Long lists cut to their first few, long strings cut: enough to show
    the shape of an answer without pages of it."""
    if isinstance(value, dict):
        return {k: shorten(v, items, chars) for k, v in value.items()}
    if isinstance(value, list):
        kept = [shorten(v, items, chars) for v in value[:items]]
        if len(value) > items:
            kept.append(f"... {len(value) - items} more")
        return kept
    if isinstance(value, str) and len(value) > chars:
        return value[:chars] + f"... ({len(value)} characters)"
    return value


@dataclass
class Entry:
    """One test, as it will appear on its page."""

    module: str
    name: str
    function: Callable[..., Any]
    exchanges: list[Exchange] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)
    results: list[Any] = field(default_factory=list)
    outcome: str = "passed"
    reason: str = ""
    # Set by a test that stands for many (the sweep): its own heading and
    # code in place of the function's docstring and source.
    title: str = ""
    code: str = ""
    page: str = ""

    def note(self, text: str) -> None:
        self.notes.append(text)

    def result(self, value: Any) -> Any:
        """Show `value` on the page as what the call gave back."""
        self.results.append(value)
        return value


def _jsonable(value: Any) -> Any:
    if hasattr(value, "model_dump"):
        return value.model_dump(mode="json", exclude={"raw"})
    if isinstance(value, datetime):
        return value.isoformat()
    if isinstance(value, (list, tuple)):
        return [_jsonable(v) for v in value]
    if isinstance(value, dict):
        return {str(k): _jsonable(v) for k, v in value.items()}
    return value


def _pretty(value: Any) -> str:
    return json.dumps(shorten(value), indent=2, default=str, ensure_ascii=False)


def _body(exchange: Exchange, masker: Masker) -> str:
    if not exchange.body:
        return "(no body)"
    try:
        return "```json\n" + _pretty(masker.data(json.loads(exchange.body))) + "\n```"
    except ValueError:
        return "```\n" + masker.text(exchange.body.decode(errors="replace")[:1500]) + "\n```"


def _request_line(exchange: Exchange, base_path: str, masker: Masker) -> str:
    path = exchange.url.path.removeprefix(base_path) or "/"
    query = exchange.url.query.decode()
    target = masker.text(path + (f"?{httpx.QueryParams(query)}" if query else ""))
    return f"`{exchange.method} {target}` -> **{exchange.status}** ({exchange.seconds:.2f} s)"


def _source(function: Callable[..., Any]) -> str:
    lines = textwrap.dedent(inspect.getsource(function)).splitlines()
    # Drop the def line and the docstring: the page has them as prose.
    body = "\n".join(lines[1:])
    doc = inspect.getdoc(function)
    if doc:
        body = re.sub(r'^\s*"""(?:.|\n)*?"""\n', "", body, count=1)
    return textwrap.dedent(body).strip()


def _heading(doc: str) -> tuple[str, str]:
    """A test's docstring as a heading - its first sentence, or the
    first clause of a long one - and the rest as the text below it."""
    paragraph, _, rest = doc.strip().partition("\n\n")
    paragraph = " ".join(paragraph.split())
    head, sep, tail = paragraph.partition(". ")
    if len(head) > 90:
        for mark in ("; ", ": ", " - "):
            if mark in head:
                head, _, more = head.partition(mark)
                tail = (more[0].upper() + more[1:] + sep + tail).strip()
                break
    body = "\n\n".join(part for part in (tail.strip(), rest.strip()) if part)
    return head.rstrip(".:;"), body


def write_pages(
    records: Iterable[Entry],
    masker: Masker,
    *,
    title_of: dict[str, str],
    header: str,
    base_path: str,
) -> list[Path]:
    """One page per test module, in docs/live/."""
    records = list(records)
    for record in records:
        for exchange in record.exchanges:
            for body in (exchange.body, exchange.request_body):
                try:
                    masker.learn(json.loads(body)) if body else None
                except ValueError:
                    pass
        for value in record.results:
            masker.learn(_jsonable(value))
    by_module: dict[str, list[Entry]] = {}
    for record in records:
        by_module.setdefault(record.page or record.module, []).append(record)
    DOCS.mkdir(parents=True, exist_ok=True)
    written = []
    for module, tests in sorted(by_module.items()):
        name = module.removeprefix("test_")
        default = name.replace("_", " ").capitalize()
        if name.startswith("raw_"):
            default = f"`cv.raw.{name.removeprefix('raw_')}`: every read, live"
        out = [f"# {title_of.get(module, default)}", "", header, ""]
        for record in tests:
            doc = record.title or inspect.getdoc(record.function) or record.name
            first, rest = _heading(doc)
            out += [f"## {masker.text(first)}", ""]
            if rest:
                out += [masker.text(rest), ""]
            if record.outcome != "passed":
                why = f": {masker.text(record.reason)}" if record.reason else ""
                out += [f"> **{record.outcome.upper()}** on this run{why}", ""]
            code = masker.text(record.code) if record.code else _source(record.function)
            out += ["```python", code, "```", ""]
            for text in record.notes:
                out += [masker.text(text), ""]
            if record.exchanges:
                out += ["**On the wire**", ""]
                for exchange in record.exchanges:
                    out += [
                        "- " + _request_line(exchange, base_path, masker),
                    ]
                    if exchange.request_body:
                        out += [
                            "",
                            "  Sent:",
                            "",
                            textwrap.indent(_body_of_request(exchange, masker), "  "),
                        ]
                    out += [
                        "",
                        "  <details><summary>Answer</summary>",
                        "",
                        textwrap.indent(_body(exchange, masker), "  "),
                        "",
                        "  </details>",
                        "",
                    ]
            for value in record.results:
                out += [
                    "**What the SDK gave back**",
                    "",
                    "```json",
                    _pretty(masker.data(_jsonable(value))),
                    "```",
                    "",
                ]
        page = "\n".join(out).rstrip() + "\n"
        leaks = masker.leaks(page)
        if leaks:
            # Kept out of git (docs/live/.raw is ignored), to see where.
            refused = DOCS / ".raw" / f"{name}.refused.md"
            refused.parent.mkdir(parents=True, exist_ok=True)
            refused.write_text(page)
            where = [
                (n, masker.names.get(n), masker.source.get(n) or masker.came_from(n))
                for n in sorted(leaks)[:5]
            ]
            raise RuntimeError(f"docs/live/{name}.md not written: unmasked names {where}")
        path = DOCS / f"{name}.md"
        path.write_text(page)
        written.append(path)
    return written


def _body_of_request(exchange: Exchange, masker: Masker) -> str:
    try:
        return "```json\n" + _pretty(masker.data(json.loads(exchange.request_body))) + "\n```"
    except ValueError:
        return "```\n(form or binary body)\n```"


def spec_operations(path: Path) -> list[tuple[str, str, str, re.Pattern[str]]]:
    """(area, method, path template, matcher) for each operation."""
    rows = []
    for line in path.read_text().splitlines()[1:]:
        area, method, template, _ = line.split("\t")
        # Commvault's paths are not case sensitive; a few carry a fixed
        # query (/clients/count?type=vm), matched on the path alone.
        bare = template.partition("?")[0]
        pattern = re.compile("^" + re.sub(r"\\\{[^}]+\\\}", "[^/]+", re.escape(bare)) + "/?$", re.I)
        rows.append((area, method, template, pattern))
    return rows


def write_coverage(
    exchanges: Iterable[Exchange], spec: Path, *, base_path: str, header: str
) -> Path:
    """docs/live/coverage.md: which of the spec's operations a live run
    called and got a good answer from."""
    operations = spec_operations(spec)
    proven: set[tuple[str, str]] = set()
    for exchange in exchanges:
        if exchange.status >= 400:
            continue
        path = exchange.url.path.removeprefix(base_path)
        # The most specific template wins: /config/policies/{name} over
        # /config/{anything}.
        matches = [
            (area, template)
            for area, method, template, pattern in operations
            if method == exchange.method and pattern.match(path)
        ]
        if matches:
            area, template = min(matches, key=lambda m: m[1].count("{"))
            proven.add((exchange.method, template))
    areas: dict[str, list[tuple[str, str, bool]]] = {}
    for area, method, template, _ in operations:
        areas.setdefault(area, []).append((method, template, (method, template) in proven))
    total = len(operations)
    done = sum(1 for rows in areas.values() for *_, ok in rows if ok)
    out = [
        "# Coverage, proven live",
        "",
        header,
        "",
        f"**{done} of {total}** operations in the server's own API description were "
        "called by the live tests and answered without an error. (Commvault publishes it at\n"
        "api.commvault.com; scripts/spec.py reads it from there.)",
        "",
        "| Area | Proven | Operations |",
        "|---|---|---|",
    ]
    for area, rows in sorted(areas.items(), key=lambda a: -len(a[1])):
        ok = sum(1 for *_, good in rows if good)
        out.append(f"| {area} | {ok} | {len(rows)} |")
    out += ["", "## Proven", ""]
    for area, rows in sorted(areas.items()):
        good = [f"- `{m} {t}`" for m, t, ok in rows if ok]
        if good:
            out += [f"### {area}", "", *good, ""]
    DOCS.mkdir(parents=True, exist_ok=True)
    page = DOCS / "coverage.md"
    page.write_text("\n".join(out).rstrip() + "\n")
    return page


def stamp(release: str, api_version: str) -> str:
    when = datetime.now(UTC).strftime("%Y-%m-%d %H:%M UTC")
    return (
        f"> Recorded from a real Commvault {release} CommServe ({api_version}) on {when}, "
        "by `pytest -m live` (tests/live). Generated - do not edit; names and addresses "
        "are masked."
    )
