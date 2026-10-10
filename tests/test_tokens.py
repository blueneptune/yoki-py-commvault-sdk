"""Access-token renewal: when it happens, and that the new pair reaches
the .env file intact."""

from __future__ import annotations

import json
from datetime import UTC, datetime, timedelta

import httpx
import pytest
import respx
from sdk_primer import AuthenticationError, ServerError

from commvault_sdk import CommvaultClient, TokenSet

BASE = "https://cs.test/commandcenter/api"
RENEWED = {
    "accessToken": "new-access",
    "refreshToken": "new-refresh",
    "tokenExpiryTimestamp": 1_800_000_000,
    "renewableUntilTimestamp": 1_805_000_000,
}


def _commserv_by_token() -> respx.Route:
    """A CommServe that only accepts the renewed token."""

    def handler(request: httpx.Request) -> httpx.Response:
        if request.headers.get("Authtoken") == "Bearer new-access":
            return httpx.Response(200, json={"hostName": "CS"})
        return httpx.Response(401, json={"errorMessage": "Access denied", "errorCode": 5})

    return respx.get(f"{BASE}/CommServ").mock(side_effect=handler)


@respx.mock
def test_a_401_renews_saves_and_retries() -> None:
    commserv = _commserv_by_token()
    renew = respx.post(f"{BASE}/V4/AccessToken/Renew").respond(json=RENEWED)
    saved: list[TokenSet] = []

    tokens = TokenSet("old-access", "old-refresh")
    with CommvaultClient(
        BASE, access_token=tokens, on_token_renew=lambda t, raw: saved.append(t)
    ) as client:
        assert client.commcell.info() == {"hostName": "CS"}
        client.commcell.info()

    # One renewal, carrying the old pair; later calls reuse the new token.
    assert renew.call_count == 1
    assert json.loads(renew.calls[0].request.content) == {
        "accessToken": "old-access",
        "refreshToken": "old-refresh",
    }
    assert commserv.call_count == 3  # 401, retry, second call
    assert saved == [
        TokenSet(
            "new-access",
            "new-refresh",
            datetime.fromtimestamp(1_800_000_000, tz=UTC),
            datetime.fromtimestamp(1_805_000_000, tz=UTC),
        )
    ]


@respx.mock
def test_a_token_known_to_be_expiring_is_renewed_before_it_is_used() -> None:
    commserv = _commserv_by_token()
    respx.post(f"{BASE}/V4/AccessToken/Renew").respond(json=RENEWED)

    tokens = TokenSet(
        "old-access", "old-refresh", expires_at=datetime.now(UTC) + timedelta(minutes=1)
    )
    with CommvaultClient(BASE, access_token=tokens) as client:
        client.commcell.info()

    assert commserv.call_count == 1  # never sent the dying token


@respx.mock
def test_renewal_falls_back_to_no_header_when_the_old_token_is_rejected() -> None:
    _commserv_by_token()
    renew = respx.post(f"{BASE}/V4/AccessToken/Renew").mock(
        side_effect=[httpx.Response(401), httpx.Response(200, json=RENEWED)]
    )

    with CommvaultClient(BASE, access_token=TokenSet("old-access", "old-refresh")) as client:
        client.commcell.info()

    assert "Authtoken" in renew.calls[0].request.headers
    assert "Authtoken" not in renew.calls[1].request.headers


@respx.mock
def test_refused_renewal_says_to_create_a_new_token() -> None:
    _commserv_by_token()
    respx.post(f"{BASE}/V4/AccessToken/Renew").respond(
        json={"errorCode": 7, "errorMessage": "Refresh token is invalid"}
    )
    tokens = TokenSet("old-access", "old-refresh", renewable_until=datetime(2020, 1, 1, tzinfo=UTC))

    with (
        CommvaultClient(BASE, access_token=tokens) as client,
        pytest.raises(AuthenticationError, match="Refresh token is invalid.*2020-01-01"),
    ):
        client.commcell.info()


@respx.mock
def test_without_a_refresh_token_a_401_is_just_a_failure() -> None:
    _commserv_by_token()
    renew = respx.post(f"{BASE}/V4/AccessToken/Renew").respond(json=RENEWED)

    with (
        CommvaultClient(BASE, access_token="old-access") as client,
        pytest.raises(AuthenticationError),
    ):
        client.commcell.info()
    assert renew.call_count == 0


@respx.mock
def test_a_maintenance_page_is_an_error_not_an_empty_result() -> None:
    respx.post(f"{BASE}/Jobs").respond(
        200, html="<html><title>Scheduled Maintenance - Your Data is Safe</title></html>"
    )
    with (
        CommvaultClient(BASE, access_token="tok") as client,
        pytest.raises(ServerError, match="maintenance"),
    ):
        list(client.jobs.iter_pages(lookup_seconds=60))
