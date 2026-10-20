"""Users and their access tokens (cv.users, cv.access_tokens), and the
commvault-tokens CLI. Token fields are the ones POST /V4/AccessToken/Renew
answers with on 11 SP46; the listing's wrapper key is not yet seen on a
CommServe, which is why the SDK looks for it rather than assuming it."""

from __future__ import annotations

import io
import json
import os
from datetime import UTC, datetime
from pathlib import Path

import pytest
import respx
from sdk_primer import ServerError

from commvault_sdk import ChangesNotAllowed, CommvaultClient, CommvaultError
from commvault_sdk.access_tokens import access_token_from_entry
from commvault_sdk.cli import main, read_env_file

BASE = "https://cs.test/commandcenter/api"
RENEWABLE = 1796450399  # 2026-12-05 05:59:59 UTC


def _users() -> dict:
    return {
        "users": [
            {"userEntity": {"userId": 1, "userName": "admin"}, "enableUser": True, "email": "a@x"},
            {"userEntity": {"userId": 5, "userName": "blt-collector"}, "enableUser": True},
        ]
    }


def _token(token_id: int, name: str, user_id: int, **extra: object) -> dict:
    return {
        "accessTokenId": token_id,
        "tokenName": name,
        "userId": user_id,
        "tokenType": 2,
        "createdTime": 1792193858,
        "lastUsedTime": 1792251399,
        "tokenExpiryTimestamp": 1792180020,
        "enableIPAllowListFeature": False,
        "renewableUntilTimestamp": RENEWABLE,
        **extra,
    }


def test_a_token_is_read_without_its_secret() -> None:
    token = access_token_from_entry(
        _token(7, "blt", 5, accessToken="SECRET", refreshToken="ALSO", allowedIPs=["10.0.0.0/24"])
    )
    assert token.token_id == 7
    assert token.name == "blt"
    assert token.user_id == 5
    assert token.scope == "All"
    assert token.renewable_until == datetime(2026, 12, 5, 5, 59, 59, tzinfo=UTC)
    assert token.allowed_ips == ["10.0.0.0/24"]
    assert token.created_at == datetime.fromtimestamp(1792193858, tz=UTC)
    assert token.last_used_at == datetime.fromtimestamp(1792251399, tz=UTC)
    assert "SECRET" not in token.model_dump_json()
    assert "ALSO" not in token.model_dump_json()


def test_renewable_within() -> None:
    token = access_token_from_entry(_token(7, "blt", 5))
    assert token.renewable_within(30, now=datetime(2026, 11, 10, tzinfo=UTC))
    assert not token.renewable_within(30, now=datetime(2026, 10, 17, tzinfo=UTC))


@respx.mock
def test_everyone_lists_each_users_tokens_and_reports_refusals() -> None:
    respx.get(f"{BASE}/User").respond(json=_users())
    respx.get(f"{BASE}/V4/AccessToken", params={"userId": "1"}).respond(
        json={"tokens": [_token(3, "lab", 1)]}
    )
    respx.get(f"{BASE}/V4/AccessToken", params={"userId": "5"}).respond(
        403, json={"errorMessage": "not allowed"}
    )
    with CommvaultClient(BASE, access_token="tok") as cv:
        result = list(cv.access_tokens.everyone())
    (admin, admin_tokens), (blt, blt_tokens) = result
    assert admin.name == "admin"
    assert isinstance(admin_tokens, list)
    assert [(t.token_id, t.user_name) for t in admin_tokens] == [(3, "admin")]
    assert blt.name == "blt-collector"
    assert not isinstance(blt_tokens, list)


@respx.mock
def test_the_list_is_found_under_another_key() -> None:
    respx.get(f"{BASE}/V4/AccessToken").respond(json={"accessTokenInfo": [_token(3, "lab", 1)]})
    with CommvaultClient(BASE, access_token="tok") as cv:
        assert [t.token_id for t in cv.access_tokens.list()] == [3]


@respx.mock
def test_no_tokens() -> None:
    respx.get(f"{BASE}/V4/AccessToken", params={"userId": "1"}).respond(json={})
    with CommvaultClient(BASE, access_token="tok") as cv:
        assert cv.access_tokens.list(1) == []


def test_changes_need_allow_changes() -> None:
    with CommvaultClient(BASE, access_token="tok") as cv:
        with pytest.raises(ChangesNotAllowed):
            cv.access_tokens.delete(3)


@respx.mock
def test_rotate_creates_the_same_kind_of_token_then_deletes_the_old_one() -> None:
    create = respx.post(f"{BASE}/V4/AccessToken").respond(
        json={
            "error": {"errorCode": 0},
            "tokenInfo": _token(9, "blt", 5, accessToken="NEW", refreshToken="NEWR"),
        }
    )
    delete = respx.delete(f"{BASE}/V4/AccessToken/7").respond(json={"errorCode": 0})
    old = access_token_from_entry(_token(7, "blt", 5, allowedIPs=["10.0.0.5"]))
    with CommvaultClient(BASE, access_token="tok", allow_changes=True) as cv:
        issued = cv.access_tokens.rotate(old)
    sent = json.loads(create.calls.last.request.content)
    assert sent == {
        "tokenName": "blt",
        "userId": 5,
        "tokenType": 2,
        "renewableUntilTimestamp": RENEWABLE,
        "allowedIPs": ["10.0.0.5"],
    }
    assert delete.called
    assert issued.token.token_id == 9
    assert issued.tokens.access_token == "NEW"
    assert issued.tokens.refresh_token == "NEWR"


@respx.mock
def test_rotate_keeps_the_new_token_when_the_old_one_will_not_go() -> None:
    respx.post(f"{BASE}/V4/AccessToken").respond(
        json={"tokenInfo": _token(9, "blt", 5, accessToken="NEW", refreshToken="NEWR")}
    )
    respx.delete(f"{BASE}/V4/AccessToken/7").respond(json={"errorCode": 5, "errorMessage": "no"})
    old = access_token_from_entry(_token(7, "blt", 5))
    with CommvaultClient(BASE, access_token="tok", allow_changes=True) as cv:
        issued = cv.access_tokens.rotate(old)
    assert issued.tokens.access_token == "NEW"


@respx.mock
def test_a_refused_create_is_an_error() -> None:
    respx.post(f"{BASE}/V4/AccessToken").respond(
        json={"error": {"errorCode": 1, "errorMessage": "Token name already exists"}}
    )
    with CommvaultClient(BASE, access_token="tok", allow_changes=True) as cv:
        with pytest.raises(CommvaultError, match="already exists"):
            cv.access_tokens.create("blt")


@respx.mock
def test_an_http_refusal_carries_commvaults_reason() -> None:
    respx.post(f"{BASE}/V4/AccessToken").respond(
        403, json={"errorCode": 5, "errorMessage": "Not allowed to create a token for this user"}
    )
    with CommvaultClient(BASE, access_token="tok", allow_changes=True) as cv:
        with pytest.raises(CommvaultError, match="Not allowed to create a token"):
            cv.access_tokens.create("blt", user_id=5)


@respx.mock
def test_an_http_refusal_without_a_reason_is_raised_as_it_came() -> None:
    respx.post(f"{BASE}/V4/AccessToken").respond(500)
    with CommvaultClient(BASE, access_token="tok", allow_changes=True) as cv:
        with pytest.raises(ServerError):
            cv.access_tokens.create("blt")


# --- the CLI


@pytest.fixture
def no_cv_env(monkeypatch: pytest.MonkeyPatch) -> pytest.MonkeyPatch:
    """The CLI reads CV_* from the environment too; keep the shell's out."""
    for key in [k for k in os.environ if k.startswith("CV_")]:
        monkeypatch.delenv(key)
    return monkeypatch


def _env(tmp_path: Path) -> Path:
    env = tmp_path / "cs.env"
    env.write_text(
        f'# a CommCell\nCV_BASE_URL={BASE}\nCV_ACCESS_TOKEN="tok"\nCV_REFRESH_TOKEN=never-used\n'
    )
    return env


def test_read_env_file(tmp_path: Path) -> None:
    assert read_env_file(_env(tmp_path)) == {
        "CV_BASE_URL": BASE,
        "CV_ACCESS_TOKEN": "tok",
        "CV_REFRESH_TOKEN": "never-used",
    }


@respx.mock
def test_cli_list(
    tmp_path: Path, capsys: pytest.CaptureFixture[str], no_cv_env: pytest.MonkeyPatch
) -> None:
    respx.get(f"{BASE}/User").respond(json=_users())
    respx.get(f"{BASE}/V4/AccessToken", params={"userId": "1"}).respond(
        json={"tokens": [_token(3, "lab", 1)]}
    )
    respx.get(f"{BASE}/V4/AccessToken", params={"userId": "5"}).respond(
        json={"tokens": [_token(7, "blt", 5)]}
    )
    assert main(["--env-file", str(_env(tmp_path)), "list"]) == 0
    out = capsys.readouterr().out
    assert "admin" in out and "blt-collector" in out and "2026-12-05" in out

    assert (
        main(["--env-file", str(_env(tmp_path)), "list", "--user", "blt-collector", "--json"]) == 0
    )
    listed = json.loads(capsys.readouterr().out)
    assert [t["token_id"] for t in listed["tokens"]] == [7]


@respx.mock
def test_cli_check_exits_3_when_a_token_is_near_its_end(
    tmp_path: Path, no_cv_env: pytest.MonkeyPatch
) -> None:
    respx.get(f"{BASE}/User").respond(json=_users())
    respx.get(f"{BASE}/V4/AccessToken").respond(json={"tokens": [_token(7, "blt", 5)]})
    env = str(_env(tmp_path))
    assert main(["--env-file", env, "list", "--renewable-within", "100000", "--check"]) == 3
    assert main(["--env-file", env, "list", "--renewable-within", "0", "--check"]) == 0


@respx.mock
def test_cli_rotate_writes_the_new_pair_privately(
    tmp_path: Path, no_cv_env: pytest.MonkeyPatch
) -> None:
    respx.get(f"{BASE}/User").respond(json=_users())
    respx.get(f"{BASE}/V4/AccessToken", params={"userId": "5"}).respond(
        json={"tokens": [_token(7, "blt", 5)]}
    )
    respx.post(f"{BASE}/V4/AccessToken").respond(
        json={"tokenInfo": _token(9, "blt", 5, accessToken="NEW", refreshToken="NEWR")}
    )
    respx.delete(f"{BASE}/V4/AccessToken/7").respond(json={"errorCode": 0})
    out = tmp_path / "new.env"
    code = main(
        [
            "--env-file",
            str(_env(tmp_path)),
            "rotate",
            "7",
            "--user",
            "blt-collector",
            "--out",
            str(out),
            "--yes",
        ]
    )
    assert code == 0
    assert out.stat().st_mode & 0o777 == 0o600
    assert read_env_file(out)["CV_ACCESS_TOKEN"] == "NEW"
    assert read_env_file(out)["CV_REFRESH_TOKEN"] == "NEWR"


def test_cli_delete_without_a_terminal_needs_yes(
    tmp_path: Path, no_cv_env: pytest.MonkeyPatch
) -> None:
    with respx.mock:
        respx.get(f"{BASE}/User").respond(json=_users())
        respx.get(f"{BASE}/V4/AccessToken", params={"userId": "5"}).respond(
            json={"tokens": [_token(7, "blt", 5)]}
        )
        delete = respx.delete(f"{BASE}/V4/AccessToken/7")
        no_cv_env.setattr("sys.stdin", io.StringIO())
        with pytest.raises(SystemExit, match="--yes"):
            main(["--env-file", str(_env(tmp_path)), "delete", "7", "--user", "blt-collector"])
        assert not delete.called
