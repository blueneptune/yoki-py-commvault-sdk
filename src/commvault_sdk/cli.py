"""`commvault-tokens`: list, rotate and delete the access tokens of every
user on a CommServe.

    commvault-tokens --env-file config/cv-toaster.env list
    commvault-tokens --env-file config/cv-toaster.env list --renewable-within 30 --check
    commvault-tokens --env-file config/cv-toaster.env rotate 17 --out new-token.env
    commvault-tokens --env-file config/cv-toaster.env delete 17

Settings are the CV_* keys of blt's and the lab's CommCell files, from
`--env-file` or the environment (the environment wins): CV_BASE_URL,
CV_USERNAME, CV_PASSWORD, CV_ACCESS_TOKEN, CV_VERIFY_TLS, CV_CA_BUNDLE,
CV_DEPLOYMENT.

It signs in with CV_USERNAME and CV_PASSWORD (asked for when the
password is not set). Given CV_ACCESS_TOKEN instead, it uses that token
*without* its refresh token: a renewal replaces the pair, and a CLI run
that renewed someone else's token would leave them holding a dead one.
So a token that has expired is an error here, not a renewal.

`list` only reads. `rotate` and `delete` change the CommServe and ask
before doing so unless given --yes.
"""

from __future__ import annotations

import argparse
import getpass
import json
import os
import sys
from collections.abc import Sequence
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from sdk_primer import SDKError

from .access_tokens import AccessToken, IssuedToken, User
from .client import CommvaultClient

EXIT_FOUND = 3


def read_env_file(path: Path) -> dict[str, str]:
    """KEY=VALUE lines; blank lines and # comments skipped, quotes taken off."""
    values: dict[str, str] = {}
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip().removeprefix("export ").strip()
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "'\"":
            value = value[1:-1]
        values[key] = value
    return values


def settings(env_file: Path | None) -> dict[str, str]:
    values = read_env_file(env_file) if env_file else {}
    values.update({k: v for k, v in os.environ.items() if k.startswith("CV_") and v})
    return {k: v for k, v in values.items() if v.strip()}


def _true(value: str | None, default: bool = True) -> bool:
    if value is None:
        return default
    return value.strip().lower() not in ("0", "false", "no", "off")


def connect(values: dict[str, str], *, allow_changes: bool) -> CommvaultClient:
    base_url = values.get("CV_BASE_URL")
    if not base_url:
        raise SystemExit("CV_BASE_URL is not set (in --env-file or the environment)")
    username = values.get("CV_USERNAME")
    password = values.get("CV_PASSWORD")
    access_token = values.get("CV_ACCESS_TOKEN")
    if username and not password and not access_token:
        password = getpass.getpass(f"Commvault password for {username}: ")
    if not access_token and not (username and password):
        raise SystemExit(
            "Set CV_USERNAME (and CV_PASSWORD, or be asked for it), or CV_ACCESS_TOKEN"
        )
    ca_bundle = values.get("CV_CA_BUNDLE")
    deployment = values.get("CV_DEPLOYMENT", "software")
    return CommvaultClient(
        base_url,
        username=None if access_token and not password else username,
        password=None if access_token and not password else password,
        # The access token alone, never its refresh token: see the module
        # docstring.
        access_token=access_token if access_token and not password else None,
        verify_tls=_true(values.get("CV_VERIFY_TLS")),
        ca_bundle=Path(ca_bundle) if ca_bundle else None,
        deployment="saas" if deployment == "saas" else "software",
        allow_changes=allow_changes,
    )


def _date(value: datetime | None) -> str:
    return value.strftime("%Y-%m-%d %H:%M") if value else "-"


def _row(token: AccessToken) -> dict[str, Any]:
    return {
        "user": token.user_name,
        "user_id": token.user_id,
        "token_id": token.token_id,
        "name": token.name,
        "scope": token.scope,
        "expires_at": token.expires_at.isoformat() if token.expires_at else None,
        "renewable_until": token.renewable_until.isoformat() if token.renewable_until else None,
        "created_at": token.created_at.isoformat() if token.created_at else None,
        "last_used_at": token.last_used_at.isoformat() if token.last_used_at else None,
        "allowed_ips": token.allowed_ips,
        "api_endpoints": token.api_endpoints,
    }


def _table(rows: list[list[str]]) -> str:
    widths = [max(len(r[i]) for r in rows) for i in range(len(rows[0]))]
    return "\n".join(
        "  ".join(c.ljust(w) for c, w in zip(r, widths, strict=True)).rstrip() for r in rows
    )


def cmd_list(cv: CommvaultClient, args: argparse.Namespace) -> int:
    now = datetime.now(UTC)
    found: list[AccessToken] = []
    hidden: list[tuple[User, str]] = []
    for user, tokens in cv.access_tokens.everyone():
        if args.user and user.name.lower() != args.user.lower():
            continue
        if not isinstance(tokens, list):
            hidden.append((user, str(tokens)))
            continue
        for token in tokens:
            if args.renewable_within is None or token.renewable_within(args.renewable_within, now):
                found.append(token)

    if args.json:
        print(
            json.dumps(
                {
                    "tokens": [_row(t) for t in found],
                    "not_visible": [
                        {"user": u.name, "user_id": u.user_id, "error": e} for u, e in hidden
                    ],
                },
                indent=2,
            )
        )
    else:
        if found:
            rows = [
                [
                    "USER",
                    "ID",
                    "NAME",
                    "SCOPE",
                    "CREATED",
                    "LAST USED",
                    "EXPIRES",
                    "RENEWABLE UNTIL",
                    "IP LIMIT",
                ]
            ]
            for t in sorted(found, key=lambda t: ((t.user_name or "").lower(), t.token_id)):
                rows.append(
                    [
                        t.user_name or str(t.user_id or "-"),
                        str(t.token_id),
                        t.name or "-",
                        t.scope or "-",
                        _date(t.created_at),
                        _date(t.last_used_at),
                        _date(t.expires_at),
                        _date(t.renewable_until),
                        ", ".join(t.allowed_ips) or "-",
                    ]
                )
            print(_table(rows))
        else:
            print(
                "No access tokens"
                + (
                    f" renewable for less than {args.renewable_within:g} days"
                    if args.renewable_within is not None
                    else ""
                )
            )
        for user, error in hidden:
            print(f"! {user.name}: tokens not visible to this login ({error})", file=sys.stderr)
    return EXIT_FOUND if args.check and found else 0


def _find(cv: CommvaultClient, token_id: int, user: str | None) -> AccessToken:
    user_id = None
    if user:
        found_user = cv.users.find(user)
        if found_user is None:
            raise SystemExit(f"No user called {user!r}")
        user_id = found_user.user_id
    token = cv.access_tokens.get(token_id, user_id)
    if token is None:
        raise SystemExit(f"No access token {token_id}" + (f" for {user}" if user else ""))
    if token.user_name is None and user:
        token = token.model_copy(update={"user_name": user})
    return token


def _confirm(prompt: str, yes: bool) -> None:
    if yes:
        return
    if not sys.stdin.isatty():
        raise SystemExit("Not a terminal: pass --yes to confirm")
    if input(f"{prompt} [y/N] ").strip().lower() not in ("y", "yes"):
        raise SystemExit("Nothing changed")


def _describe(token: AccessToken) -> str:
    return f"token {token.token_id} {token.name!r} of {token.user_name or token.user_id}"


def _write_issued(issued: IssuedToken, out: Path | None) -> None:
    t = issued.tokens
    lines = [
        f"CV_ACCESS_TOKEN={t.access_token}",
        f"CV_REFRESH_TOKEN={t.refresh_token or ''}",
        f"CV_TOKEN_EXPIRES_AT={t.expires_at.isoformat() if t.expires_at else ''}",
        f"CV_TOKEN_RENEWABLE_UNTIL={t.renewable_until.isoformat() if t.renewable_until else ''}",
    ]
    if out is None:
        print("\n".join(lines))
        print("\nCommvault shows this pair once. Store it now.", file=sys.stderr)
        return
    fd = os.open(out, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(fd, "w") as handle:
        handle.write("\n".join(lines) + "\n")
    print(f"New pair written to {out} (mode 600). Commvault shows it once.", file=sys.stderr)


def cmd_rotate(cv: CommvaultClient, args: argparse.Namespace) -> int:
    if args.out and args.out.exists():
        raise SystemExit(f"{args.out} already exists")
    token = _find(cv, args.token_id, args.user)
    _only_its_owner_may_create(cv, token, args.signed_in_as)
    _confirm(
        f"Rotate {_describe(token)}? Whatever uses it stops working until given the new pair.",
        args.yes,
    )
    issued = cv.access_tokens.rotate(token)
    print(f"Rotated {_describe(token)}: new token {issued.token.token_id}", file=sys.stderr)
    _write_issued(issued, args.out)
    return 0


def _only_its_owner_may_create(
    cv: CommvaultClient, token: AccessToken, signed_in_as: str | None
) -> None:
    """Commvault creates a token only for the user asking, or for a service
    account (403 otherwise), so a rotate by anyone else would fail at its
    first step. Say so before asking, rather than after."""
    if signed_in_as is None or token.user_id is None:
        return
    if (token.user_name or "").lower() == signed_in_as.lower():
        return
    owner = cv.users.get(token.user_id)
    if owner is None or owner.is_service_account is not False:
        return
    raise SystemExit(
        f"Only {owner.name} can rotate {_describe(token)}: Commvault creates tokens "
        "only for the user asking, or for a service account. Delete it instead, "
        f"and have {owner.name} issue a new one."
    )


def cmd_delete(cv: CommvaultClient, args: argparse.Namespace) -> int:
    token = _find(cv, args.token_id, args.user)
    _confirm(f"Delete {_describe(token)}? Whatever uses it stops working at once.", args.yes)
    cv.access_tokens.delete(token.token_id)
    print(f"Deleted {_describe(token)}", file=sys.stderr)
    return 0


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="commvault-tokens", description="Access tokens of every user on a CommServe."
    )
    p.add_argument(
        "--env-file", type=Path, help="a CommCell file of CV_* settings (blt's or the lab's format)"
    )
    sub = p.add_subparsers(dest="command", required=True)

    ls = sub.add_parser("list", help="every user's tokens (read-only)")
    ls.add_argument("--user", help="only this user's")
    ls.add_argument(
        "--renewable-within",
        type=float,
        metavar="DAYS",
        help="only tokens that stop being renewable within DAYS",
    )
    ls.add_argument(
        "--check",
        action="store_true",
        help=f"exit {EXIT_FOUND} if any token is listed (for scheduled checks)",
    )
    ls.add_argument("--json", action="store_true", help="JSON instead of a table")
    ls.set_defaults(func=cmd_list, changes=False)

    rot = sub.add_parser("rotate", help="replace a token with a new one, then delete the old one")
    rot.add_argument("token_id", type=int)
    rot.add_argument("--user", help="the token's user (saves searching every user)")
    rot.add_argument(
        "--out", type=Path, help="write the new pair here (mode 600) instead of to stdout"
    )
    rot.add_argument("--yes", action="store_true", help="do not ask")
    rot.set_defaults(func=cmd_rotate, changes=True)

    rm = sub.add_parser("delete", help="revoke a token")
    rm.add_argument("token_id", type=int)
    rm.add_argument("--user", help="the token's user (saves searching every user)")
    rm.add_argument("--yes", action="store_true", help="do not ask")
    rm.set_defaults(func=cmd_delete, changes=True)
    return p


def main(argv: Sequence[str] | None = None) -> int:
    args = parser().parse_args(argv)
    try:
        values = settings(args.env_file)
        # Who the login is, when it is a username and password (see connect).
        token_only = values.get("CV_ACCESS_TOKEN") and not values.get("CV_PASSWORD")
        args.signed_in_as = None if token_only else values.get("CV_USERNAME")
        cv = connect(values, allow_changes=args.changes)
        try:
            return int(args.func(cv, args))
        finally:
            cv.close()
    except SDKError as error:
        print(f"commvault-tokens: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
