"""The CommServe itself: what it is and what it runs."""

from __future__ import annotations

from commvault_sdk import CommvaultClient

from .recorder import Entry


def test_info(cv: CommvaultClient, commserve: dict[str, object], record: Entry) -> None:
    """`cv.commcell.info()` - the CommServe's version, Service Pack and
    operating system: what the live pages are stamped with."""
    record.result({k: commserve.get(k) for k in ("csVersionInfo", "currentSPVersion", "osType")})
    assert commserve.get("currentSPVersion")


def test_packages(cv: CommvaultClient, record: Entry) -> None:
    """`cv.commcell.packages()` - the software packages it can push to a
    client."""
    packages = cv.commcell.packages()
    record.result(packages[:5])
    assert packages


def test_clients(cv: CommvaultClient, record: Entry) -> None:
    """`cv.clients.list()` - every client: servers, MediaAgents, the
    CommServe itself."""
    clients = cv.clients.list()
    record.result(clients[:3])
    assert clients


def test_storage(cv: CommvaultClient, record: Entry) -> None:
    """`cv.storage.disk()` - disk storage pools, with capacity and use:
    what blt's storage monitoring will read."""
    record.result(cv.storage.disk()[:3])


def test_plans(cv: CommvaultClient, record: Entry) -> None:
    """`cv.plans.list()` - the plans: what protects what."""
    record.result(cv.plans.list()[:3])
