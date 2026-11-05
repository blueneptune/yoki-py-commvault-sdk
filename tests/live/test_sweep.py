"""Every read in the generated layer (`cv.raw`), against the real CommServe.

One test per GET operation. A path that takes an id - `/Client/{clientId}`
- gets one from the listing above it (`/Client`), so the sweep reaches as
deep as the CommServe has things to show. Each call's answer goes on the
page for its area: docs/live/raw_<area>.md.

A call Commvault answers with an error is skipped, with Commvault's own
words: usually a feature this CommServe does not use (a cloud, an
application it has no clients for) - the page says which, and coverage
counts only real answers.
"""

from __future__ import annotations

import inspect
import re
from collections.abc import Iterator
from functools import cache
from typing import Any

import pytest
from sdk_primer import SDKError

from commvault_sdk import CommvaultClient

from .recorder import Entry

# GETs that start work or hand back large files rather than describe
# something; read with care, not swept.
NOT_SWEPT = re.compile(
    r"download|/logs?\b|joblogs|sendlogs|export|/files\b|/content|refresh|/streams?\b|"
    r"/action/|browse|preview|/retire|/release|/reconfigure|/sync|/test|/validate|"
    r"/run\b|/start|/stop|install|upgrade|/push|/check",
    re.I,
)


def _operations() -> list[tuple[str, str, str]]:
    """(area, method name, path template) for every raw GET."""
    cv = CommvaultClient("https://unused.invalid/commandcenter/api", access_token="-")
    found = []
    for area, group in vars(cv.raw).items():
        for name, method in inspect.getmembers(group, inspect.ismethod):
            match = re.match(r"`GET ([^`]+)`", inspect.getdoc(method) or "")
            if match and not name.startswith("_"):
                found.append((area, name, match.group(1)))
    # The calls without parameters first: their answers fill the id pool
    # the deeper calls draw on.
    return sorted(found, key=lambda op: (op[2].count("{"), op[0], op[1]))


OPERATIONS = _operations()
_cache: dict[str, Any] = {}


ID_KEY = re.compile(r"(^id$|Id$|^guid$)")


def _lists(value: Any, depth: int = 0) -> Iterator[list[Any]]:
    """Lists of objects in an answer, outermost first."""
    if depth > 4:
        return
    if isinstance(value, list) and value and isinstance(value[0], dict):
        yield value
    if isinstance(value, dict):
        for v in value.values():
            yield from _lists(v, depth + 1)


def _id_in(item: Any, want: str, depth: int = 0) -> str | None:
    """An id in one listed object: the key the path parameter is named
    for (clientId for {clientId}) if it is there, else the first id."""
    if not isinstance(item, dict) or depth > 3:
        return None
    for key, value in item.items():
        if key.lower() == want.lower() and isinstance(value, (int, str)) and value not in ("", 0):
            return str(value)
    for key, value in item.items():
        if ID_KEY.search(key) and isinstance(value, (int, str)) and value not in ("", 0):
            return str(value)
    for value in item.values():
        found = _id_in(value, want, depth + 1)
        if found:
            return found
    return None


def _first_ids(answer: Any, want: str = "") -> list[str]:
    """Ids from a listing, whatever its shape (Commvault has many)."""
    for items in _lists(answer):
        ids = [i for i in (_id_in(item, want) for item in items[:3]) if i]
        if ids:
            return ids
    return []


@cache
def _by_template() -> dict[str, tuple[str, str]]:
    """Listings by path, ignoring case: Commvault's paths are not case
    sensitive and its description spells them both ways."""
    return {_shape(template): (area, name) for area, name, template in OPERATIONS}


def _shape(template: str) -> str:
    return re.sub(r"\{[^}]+\}", "{}", template.partition("?")[0]).lower().rstrip("/")


# Every id seen in any answer so far, by its key (planid -> [3, 7]): the
# fallback for a parameter whose path has no listing right above it.
_pool: dict[str, list[str]] = {}


def _harvest(value: Any, depth: int = 0) -> None:
    if depth > 6:
        return
    if isinstance(value, dict):
        for key, v in value.items():
            if ID_KEY.search(key) and isinstance(v, (int, str)) and v not in ("", 0, "0"):
                seen = _pool.setdefault(key.lower(), [])
                if str(v) not in seen and len(seen) < 5:
                    seen.append(str(v))
            else:
                _harvest(v, depth + 1)
    elif isinstance(value, list):
        for v in value[:5]:
            _harvest(v, depth + 1)


def _resolve(cv: CommvaultClient, template: str) -> list[str] | None:
    """Values for the template's path parameters: from the listing above
    each one where there is one, else an id of that name seen in an
    earlier answer - or None if the CommServe has nothing there."""
    params = re.findall(r"\{[^}]+\}", template)
    values: list[str] = []
    for param in params:
        want = param.strip("{}")
        prefix = template.split(param)[0].rstrip("/")
        parent = _by_template().get(_shape(prefix))
        ids: list[str] = []
        if parent is not None:
            parent_values = values[: prefix.count("{")]
            key = f"{_shape(prefix)}|{parent_values}"
            if key not in _cache:
                area, name = parent
                try:
                    _cache[key] = getattr(getattr(cv.raw, area), name)(*parent_values)
                except SDKError:
                    _cache[key] = None
                _harvest(_cache[key])
            ids = _first_ids(_cache[key], want)
        if not ids:
            ids = _pool.get(want.lower(), [])
        if not ids:
            return None
        values.append(ids[0])
    return values


def _why(error: SDKError) -> str:
    """Commvault's own account of a refusal: status and message (an error
    it put inside a 200 has no status, only the message)."""
    if error.status_code is None:
        return str(error).split(": ", 1)[-1][:300]
    message = error.server_message or ""
    return f"{error.status_code}" + (f" - {message}" if message else "")


@pytest.mark.parametrize(
    ("area", "name", "template"), OPERATIONS, ids=[f"{a}.{n}" for a, n, _ in OPERATIONS]
)
def test_get(cv: CommvaultClient, record: Entry, area: str, name: str, template: str) -> None:
    record.page = f"raw_{area}"
    record.title = f"`{name}` - GET {template}"
    # The call, not this test's source, on the page - also when skipped.
    record.code = f"cv.raw.{area}.{name}(...)"
    if NOT_SWEPT.search(template):
        pytest.skip("not swept: starts work or returns a file")
    values = _resolve(cv, template)
    if values is None:
        pytest.skip("nothing on this server to look at here")
    shown = ", ".join(repr(v) for v in values)
    record.code = f"cv.raw.{area}.{name}({shown})"
    try:
        answer = getattr(getattr(cv.raw, area), name)(*values)
    except SDKError as error:
        pytest.skip(f"Commvault answered: {_why(error)}")
    _cache[f"{_shape(template)}|{values}"] = answer
    _harvest(answer)
