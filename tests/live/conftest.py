"""Live tests: the SDK against a real CommServe.

Not run by plain `pytest` (pyproject's addopts leave out the `live`
mark). They connect the way the lab does - its own access token, renewed
and written back to its file under its lock (yoki-commvault-lab) - so
they never take a copy of a token that lives somewhere else:

    uv run --with-editable ../yoki-commvault-lab pytest -m live

- CV_LIVE_COMMCELL (default cv-toaster) and CV_LIVE_CONFIG_DIR (default
  ../yoki-commvault-lab/config) say which token file.
- CV_LIVE_CHANGES=yes also runs the tests that create, change and delete
  things - only ever their own `bltlive-<run>-*` objects, removed again
  at the end.
- CV_LIVE_DOCS=0 skips writing docs/live/.
- CV_LIVE_MASK="a,b" masks more names than the run finds by itself;
  CV_LIVE_MASK_PREFIXES="lab01" masks every word starting with one.

Every request and answer is recorded (recorder.py) and written up, masked,
as docs/live/<module>.md, with docs/live/coverage.md against
spec/operations-<release>.tsv (scripts/spec.py).
"""

from __future__ import annotations

import os
import ssl
from collections.abc import Generator, Iterator
from datetime import UTC, datetime
from pathlib import Path

import httpx
import pytest

from commvault_sdk import CommvaultClient

from .recorder import ROOT, Entry, Masker, Recorder, stamp, write_coverage, write_pages

RUN = datetime.now(UTC).strftime("%m%d%H%M")
PREFIX = f"bltlive-{RUN}"

_records: list[Entry] = []
_state: dict[str, object] = {}

TITLES = {
    "test_commserve": "The CommServe: version, identity, what it runs",
}


def pytest_collection_modifyitems(items: list[pytest.Item]) -> None:
    here = Path(__file__).parent
    for item in items:
        if here in Path(str(item.fspath)).parents:
            item.add_marker(pytest.mark.live)


def changes_allowed() -> bool:
    return os.environ.get("CV_LIVE_CHANGES") == "yes"


@pytest.fixture(scope="session")
def recorder() -> Recorder:
    rec = Recorder(httpx.HTTPTransport(verify=_verify()))
    _state["recorder"] = rec
    return rec


def _verify() -> bool | ssl.SSLContext:
    try:
        from commvault_lab.settings import load_settings
    except ImportError:
        return True
    settings = load_settings(_commcell(), _config_dir())
    if settings.cv_ca_bundle:
        return ssl.create_default_context(cafile=str(settings.cv_ca_bundle))
    return bool(settings.cv_verify_tls)


def _commcell() -> str:
    return os.environ.get("CV_LIVE_COMMCELL", "cv-toaster")


def _config_dir() -> Path:
    default = ROOT.parent / "yoki-commvault-lab" / "config"
    return Path(os.environ.get("CV_LIVE_CONFIG_DIR", str(default)))


@pytest.fixture(scope="session")
def cv(recorder: Recorder) -> Iterator[CommvaultClient]:
    try:
        from commvault_lab.connect import commvault_client
        from commvault_lab.settings import load_settings
    except ImportError:
        pytest.exit(
            "Live tests connect through yoki-commvault-lab: "
            "uv run --with-editable ../yoki-commvault-lab pytest -m live",
            returncode=2,
        )
    commcell, config_dir = _commcell(), _config_dir()
    client = commvault_client(
        load_settings(commcell, config_dir),
        commcell,
        config_dir,
        allow_changes=changes_allowed(),
        transport=recorder,
    )
    _state["base_path"] = httpx.URL(str(client.api.base_url)).path
    with client:
        yield client


@pytest.fixture(scope="session")
def commserve(cv: CommvaultClient) -> dict[str, object]:
    info = cv.commcell.info()
    sp = info.get("currentSPVersion")
    _state["release"] = f"11.{sp}" if sp else "unknown"
    _state["version"] = str(info.get("csVersionInfo") or "")
    return info


@pytest.fixture(scope="session")
def masker(cv: CommvaultClient, commserve: dict[str, object]) -> Masker:
    """Everything that names the lab, learned from the CommServe itself
    before any test runs; whatever else the answers name is learned from
    them before the pages are written."""
    m = Masker()
    m.add(httpx.URL(str(cv.api.base_url)).host, "commserve")
    m.add(str(commserve.get("hostName") or ""), "commserve")
    commcell = commserve.get("commcell")
    if isinstance(commcell, dict):
        m.add(str(commcell.get("commCellName") or ""), "commcell")
    m.learn(commserve)
    m.prefixes = [
        p.strip() for p in os.environ.get("CV_LIVE_MASK_PREFIXES", "").split(",") if p.strip()
    ]
    for extra in os.environ.get("CV_LIVE_MASK", "").split(","):
        m.add(extra.strip(), "name")
    _state["masker"] = m
    return m


@pytest.fixture
def changes() -> None:
    if not changes_allowed():
        pytest.skip("creates and deletes bltlive objects: set CV_LIVE_CHANGES=yes")


@pytest.fixture(autouse=True)
def record(request: pytest.FixtureRequest, recorder: Recorder, masker: Masker) -> Iterator[Entry]:
    """The test's page entry; the exchanges it caused are added after it."""
    entry = Entry(
        module=request.module.__name__.rsplit(".", 1)[-1],
        name=request.node.nodeid,
        function=request.function,
    )
    start = len(recorder.exchanges)
    _records.append(entry)  # now, so the call's report can mark it
    yield entry
    entry.exchanges = recorder.exchanges[start:]


@pytest.hookimpl(wrapper=True)
def pytest_runtest_makereport(
    item: pytest.Item, call: pytest.CallInfo[None]
) -> Generator[None, pytest.TestReport, pytest.TestReport]:
    report = yield
    if report.when == "call" and report.outcome != "passed":
        for entry in _records:
            if entry.name == item.nodeid:
                entry.outcome = report.outcome
                longrepr = report.longrepr
                if report.skipped and isinstance(longrepr, tuple):
                    entry.reason = str(longrepr[2]).removeprefix("Skipped: ")
    return report


def pytest_sessionfinish(session: pytest.Session, exitstatus: int) -> None:
    if not _records or os.environ.get("CV_LIVE_DOCS") == "0":
        return
    recorder = _state["recorder"]
    masker = _state["masker"]
    assert isinstance(recorder, Recorder) and isinstance(masker, Masker)
    base_path = str(_state["base_path"])
    release = str(_state.get("release") or "unknown")
    header = stamp(release, str(_state.get("version", "?")))
    write_pages(_records, masker, title_of=TITLES, header=header, base_path=base_path)
    spec = ROOT / "spec" / f"operations-{release}.tsv"
    if spec.exists():
        write_coverage(
            (e for r in _records for e in r.exchanges), spec, base_path=base_path, header=header
        )
