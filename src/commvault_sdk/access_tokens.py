"""The CommServe's users, and their access tokens: `cv.users` and
`cv.access_tokens`.

Command Center shows a user only their own access tokens. The API lists
them per user (GET /V4/AccessToken?userId=), so an administrator can
see every token in the CommCell by asking for each user in turn - which
is what `AccessTokens.everyone()` does. Whether a user may ask for
someone else's depends on that user's role; a refusal for one user is
reported for that user and does not stop the rest.

Rotating a token is Commvault's create-then-revoke: a new token with the
same name, scope and limits for the same user, then the old one deleted.
The new pair is returned exactly once (Commvault never shows it again);
whoever rotates is responsible for getting it to the service that uses
the token. The old pair stops working the moment it is deleted.

Request shapes are cvpysdk's (security/user.py); the field names of a
token are those of GET /V4/AccessToken on 11 SP46 (seen 2026-10-17:
`{"tokens": [...]}`, each with accessTokenId, tokenName, tokenType,
userId, createdTime, lastUsedTime, tokenExpiryTimestamp,
renewableUntilTimestamp, allowedIPs, enableIPAllowListFeature).
"""

from __future__ import annotations

from collections.abc import Iterator
from datetime import UTC, datetime
from typing import Any

from loguru import logger
from pydantic import BaseModel, Field
from sdk_primer import SDKError

from ._base import CommvaultError, Entities, Names, Resource
from .auth import TokenSet

# Spelled out because both groups have a method called `list`, which
# would otherwise shadow the built-in in their annotations (see _base).
Tokens = list["AccessToken"]
UserList = list["User"]

# tokenType, as Command Center names the scopes.
SCOPES = {
    0: "All",
    1: "Microsoft SCIM",
    2: "All",
    3: "Custom",
    4: "1-Touch",
    5: "Hyperscale",
}

# Never kept in AccessToken.raw: a listing that carries a token's secret
# would otherwise put it in every log line and JSON dump of the model.
_SECRET_KEYS = {"accesstoken", "refreshtoken", "token"}


def _from_epoch(value: Any) -> datetime | None:
    try:
        seconds = int(value)
    except (TypeError, ValueError):
        return None
    return datetime.fromtimestamp(seconds, tz=UTC) if seconds > 0 else None


def _object(value: Any) -> dict[str, Any]:
    return value if isinstance(value, dict) else {}


def _without_secrets(entry: dict[str, Any]) -> dict[str, Any]:
    return {k: v for k, v in entry.items() if k.lower() not in _SECRET_KEYS}


class User(BaseModel):
    """One CommServe user, from GET /User."""

    user_id: int
    name: str
    full_name: str | None = None
    email: str | None = None
    enabled: bool | None = None
    raw: dict[str, Any] = Field(default_factory=dict)


def user_from_entry(entry: dict[str, Any]) -> User:
    """One entry of GET /User's `users` as a User."""
    entity = entry.get("userEntity") or {}
    enabled = entry.get("enableUser")
    return User(
        user_id=int(entity["userId"]),
        name=str(entity.get("userName") or ""),
        full_name=entry.get("fullName") or None,
        email=entry.get("email") or None,
        enabled=bool(enabled) if enabled is not None else None,
        raw=entry,
    )


class AccessToken(BaseModel):
    """One access token: who it belongs to, its scope and its dates. Never
    the token itself - see IssuedToken for the one time that is seen."""

    token_id: int
    name: str | None = None
    user_id: int | None = None
    user_name: str | None = None
    token_type: int | None = None
    scope: str | None = None
    expires_at: datetime | None = None
    renewable_until: datetime | None = None
    refresh_expires_at: datetime | None = None
    created_at: datetime | None = None
    # When the token was last used to call the API: the age of a token
    # nobody uses any more.
    last_used_at: datetime | None = None
    allowed_ips: list[str] = Field(default_factory=list)
    api_endpoints: list[str] = Field(default_factory=list)
    raw: dict[str, Any] = Field(default_factory=dict)

    def renewable_within(self, days: float, now: datetime | None = None) -> bool:
        """Whether the token can no longer be renewed `days` from now - the
        date after which whoever uses it needs a new one."""
        if self.renewable_until is None:
            return False
        now = now or datetime.now(UTC)
        return (self.renewable_until - now).total_seconds() <= days * 86400


def access_token_from_entry(entry: dict[str, Any], user_name: str | None = None) -> AccessToken:
    """One token as GET /V4/AccessToken lists it, or the `tokenInfo` of a
    create or update, as an AccessToken."""
    token_type = entry.get("tokenType")
    if isinstance(token_type, dict):
        token_type = token_type.get("id", token_type.get("value"))
    try:
        token_type = int(token_type) if token_type is not None else None
    except (TypeError, ValueError):
        token_type = None
    user = _object(entry.get("user"))
    user_id = entry.get("userId", user.get("userId") or user.get("id"))
    token_id = entry.get("accessTokenId", entry.get("tokenId", entry.get("id")))
    if token_id is None:
        raise KeyError("accessTokenId")
    return AccessToken(
        token_id=int(token_id),
        name=entry.get("tokenName") or entry.get("name") or None,
        user_id=int(user_id) if user_id not in (None, "") else None,
        user_name=user_name or user.get("userName") or user.get("name") or None,
        token_type=token_type,
        scope=SCOPES.get(token_type) if token_type is not None else None,
        expires_at=_from_epoch(entry.get("tokenExpiryTimestamp")),
        renewable_until=_from_epoch(entry.get("renewableUntilTimestamp")),
        refresh_expires_at=_from_epoch(entry.get("refreshTokenExpiryTimestamp")),
        created_at=_from_epoch(entry.get("createdTime", entry.get("tokenCreatedTimestamp"))),
        last_used_at=_from_epoch(entry.get("lastUsedTime")),
        allowed_ips=list(entry.get("allowedIPs") or []),
        api_endpoints=list(entry.get("apiEndpoints") or []),
        raw=_without_secrets(entry),
    )


class IssuedToken(BaseModel):
    """A token just created (or rotated): what it is, and its pair. The
    pair is shown once by Commvault and never again."""

    token: AccessToken
    tokens: TokenSet


def _token_entries(body: dict[str, Any]) -> Entities:
    """The token list in a GET /V4/AccessToken answer. The key it sits
    under is taken from the first list of token-shaped objects found, so
    the call does not depend on one spelling of it."""
    for key in ("tokens", "accessTokens", "tokenInfo", "accessTokenList"):
        value = body.get(key)
        if isinstance(value, list):
            return [v for v in value if isinstance(v, dict)]
    for value in body.values():
        if isinstance(value, list) and value and all(isinstance(v, dict) for v in value):
            if any("accessTokenId" in v or "tokenName" in v for v in value):
                return value
    return []


def _issued(body: dict[str, Any], what: str) -> IssuedToken:
    info = _object(body.get("tokenInfo")) or body
    if not info.get("accessToken"):
        raise CommvaultError(f"{what}: Commvault answered without a token")
    token = access_token_from_entry(info)
    return IssuedToken(
        token=token,
        tokens=TokenSet(
            access_token=str(info["accessToken"]),
            refresh_token=str(info["refreshToken"]) if info.get("refreshToken") else None,
            expires_at=token.expires_at,
            renewable_until=token.renewable_until,
        ),
    )


class Users(Resource):
    def list(self) -> UserList:
        """Every user on the CommServe."""
        body = self._list("/User")
        users: UserList = []
        for entry in body.get("users") or []:
            try:
                users.append(user_from_entry(entry))
            except (KeyError, TypeError, ValueError) as error:
                logger.warning("Skipping a user the SDK could not read ({}): {}", error, entry)
        return users

    def find(self, name: str) -> User | None:
        wanted = name.lower()
        return next((u for u in self.list() if u.name.lower() == wanted), None)


class AccessTokens(Resource):
    def list(self, user_id: int | None = None, *, user_name: str | None = None) -> Tokens:
        """A user's access tokens; without `user_id`, those of the user this
        client is signed in as."""
        path = "/V4/AccessToken" if user_id is None else f"/V4/AccessToken?userId={user_id}"
        body = self._list(path)
        tokens: Tokens = []
        for entry in _token_entries(body):
            try:
                tokens.append(access_token_from_entry(entry, user_name))
            except (KeyError, TypeError, ValueError) as error:
                logger.warning(
                    "Skipping an access token the SDK could not read ({}): {}",
                    error,
                    _without_secrets(entry),
                )
        return tokens

    def everyone(self) -> Iterator[tuple[User, Tokens | SDKError]]:
        """Each user on the CommServe and their tokens - or, for a user whose
        tokens this login may not see, the error Commvault gave."""
        for user in self.users():
            try:
                yield user, self.list(user.user_id, user_name=user.name)
            except SDKError as error:
                logger.warning("Could not list the access tokens of {}: {}", user.name, error)
                yield user, error

    def users(self) -> UserList:
        return Users(self._client).list()

    def get(self, token_id: int, user_id: int | None = None) -> AccessToken | None:
        """One token by id, from its user's listing (Commvault has no call
        for a single token)."""
        if user_id is not None:
            return next((t for t in self.list(user_id) if t.token_id == token_id), None)
        for _user, tokens in self.everyone():
            if isinstance(tokens, list):
                found = next((t for t in tokens if t.token_id == token_id), None)
                if found:
                    return found
        return None

    def create(
        self,
        name: str,
        *,
        user_id: int | None = None,
        token_type: int | None = None,
        renewable_until: datetime | None = None,
        expires_at: datetime | None = None,
        api_endpoints: Names | None = None,
        allowed_ips: Names | None = None,
    ) -> IssuedToken:
        """A new token, for `user_id` or for the signed-in user. A change."""
        body: dict[str, Any] = {"tokenName": name}
        if user_id is not None:
            body["userId"] = user_id
        if token_type is not None:
            body["tokenType"] = token_type
        if renewable_until is not None:
            body["renewableUntilTimestamp"] = int(renewable_until.timestamp())
        if expires_at is not None:
            body["tokenExpiryTimestamp"] = int(expires_at.timestamp())
        if api_endpoints:
            body["apiEndpoints"] = api_endpoints
        if allowed_ips:
            body["allowedIPs"] = allowed_ips
        return _issued(self._change("POST", "/V4/AccessToken", body), "POST /V4/AccessToken")

    def update(
        self,
        token_id: int,
        *,
        name: str | None = None,
        renewable_until: datetime | None = None,
        expires_at: datetime | None = None,
        allowed_ips: Names | None = None,
    ) -> AccessToken:
        """Rename a token or change its dates or IP allow-list. A change."""
        body: dict[str, Any] = {}
        if name is not None:
            body["tokenName"] = name
        if renewable_until is not None:
            body["renewableUntilTimestamp"] = int(renewable_until.timestamp())
        if expires_at is not None:
            body["tokenExpiryTimestamp"] = int(expires_at.timestamp())
        if allowed_ips is not None:
            body["allowedIPs"] = allowed_ips
        if not body:
            raise ValueError(
                "update needs at least one of name, renewable_until, expires_at, allowed_ips"
            )
        data = self._change("PUT", f"/V4/AccessToken/{token_id}", body)
        info = _object(data.get("tokenInfo")) or data
        return access_token_from_entry({"accessTokenId": token_id, **info})

    def delete(self, token_id: int) -> None:
        """Revoke a token: it stops working at once, for whoever holds it.
        A change."""
        self._change("DELETE", f"/V4/AccessToken/{token_id}")

    def rotate(self, token: AccessToken) -> IssuedToken:
        """Replace `token` with a new one of the same name, scope and limits
        for the same user, then revoke the old one. A change.

        If the old one cannot be revoked, the new one is still returned -
        it exists and its pair would otherwise be lost - and the failure
        is logged; the old token then has to be deleted separately."""
        renewable_until = token.renewable_until
        if renewable_until is not None and renewable_until <= datetime.now(UTC):
            renewable_until = None
        issued = self.create(
            token.name or f"rotated-{token.token_id}",
            user_id=token.user_id,
            token_type=token.token_type,
            renewable_until=renewable_until,
            api_endpoints=token.api_endpoints or None,
            allowed_ips=token.allowed_ips or None,
        )
        try:
            self.delete(token.token_id)
        except SDKError as error:
            logger.error(
                "Created token {} to replace {}, but could not delete {}: {}",
                issued.token.token_id,
                token.token_id,
                token.token_id,
                error,
            )
        return issued
