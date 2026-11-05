"""The generated layer (commvault_sdk.raw): every one of its calls sends
the method and path its docstring names, a read-only client refuses every
call that is not a GET, and an error inside a 200 is raised."""

from __future__ import annotations

import inspect
import re
from collections.abc import Iterator

import httpx
import pytest
import respx

from commvault_sdk import CommvaultClient
from commvault_sdk._base import ChangesNotAllowed, CommvaultError

BASE = "https://cs.test/commandcenter/api"


def calls() -> Iterator[tuple[str, str, str, str]]:
    client = CommvaultClient(BASE, access_token="t")
    for area_name, area in vars(client.raw).items():
        for name, method in inspect.getmembers(area, inspect.ismethod):
            if name.startswith("_"):
                continue
            doc = inspect.getdoc(method) or ""
            match = re.match(r"`(GET|POST|PUT|PATCH|DELETE) (\S+(?: \S+)*?)`", doc)
            assert match, f"{area_name}.{name} has no `METHOD /path` docstring"
            yield area_name, name, match.group(1), match.group(2)


CALLS = list(calls())


def test_every_operation_is_there() -> None:
    assert len(CALLS) == 1487


@pytest.mark.parametrize(("area", "name", "verb", "template"), CALLS, ids=lambda v: str(v))
def test_sends_its_method_and_path(area: str, name: str, verb: str, template: str) -> None:
    # Some paths carry a fixed query string (/clients/count?type=vm).
    template_path, _, fixed_query = template.partition("?")
    pattern = re.compile(
        "^/commandcenter/api"
        + re.sub(r"\\\{[^}]+\\\}", "[^/]+", re.escape(template_path)).replace("\\ ", " ")
        + "/?$",
        re.I,
    )
    with respx.mock(base_url=BASE, assert_all_called=False) as router:
        route = router.route().respond(200, json={})
        cv = CommvaultClient(BASE, access_token="t", allow_changes=True)
        method = getattr(getattr(cv.raw, area), name)
        args = [
            f"x{i}"
            for i, p in enumerate(inspect.signature(method).parameters.values())
            if p.kind is inspect.Parameter.POSITIONAL_OR_KEYWORD
        ]
        method(*args)
    request: httpx.Request = route.calls.last.request
    assert request.method == verb
    assert pattern.match(request.url.path), (request.url.path, template)
    if fixed_query and "{" not in fixed_query:
        assert fixed_query.split("=")[0] in request.url.query.decode()


def test_read_only_client_refuses_changes() -> None:
    cv = CommvaultClient(BASE, access_token="t")
    with pytest.raises(ChangesNotAllowed):
        cv.raw.job.post_job_action_kill(1)


def test_error_inside_a_200_is_raised() -> None:
    with respx.mock(base_url=BASE, assert_all_called=False) as router:
        router.route().respond(200, json={"errorCode": 2, "errorMessage": "No such job"})
        cv = CommvaultClient(BASE, access_token="t")
        with pytest.raises(CommvaultError, match="No such job"):
            cv.raw.job.get_job(1)


def test_query_booleans_are_lower_case() -> None:
    with respx.mock(base_url=BASE, assert_all_called=False) as router:
        route = router.route().respond(200, json={})
        CommvaultClient(BASE, access_token="t").raw.job.list_job(client_id=True)
    assert "clientId=true" in str(route.calls.last.request.url)


def test_fixed_query_is_sent_with_the_path() -> None:
    with respx.mock(base_url=BASE, assert_all_called=False) as router:
        route = router.route().respond(200, json={})
        CommvaultClient(BASE, access_token="t").raw.dashboard.get_clientsclount()
    url = route.calls.last.request.url
    assert url.path == "/commandcenter/api/clients/count"
    assert url.params["type"] == "fileserver,vm,laptop"
