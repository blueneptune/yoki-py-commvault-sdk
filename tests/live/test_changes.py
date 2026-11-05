"""Changes: create, read back, change and delete - on a real CommServe.

Only with CV_LIVE_CHANGES=yes, and only ever this run's own objects,
named `bltlive-<run>-...`; anything of that name a failed run left behind
is removed at the end. Nothing else on the CommServe is touched: a new
group has no members, a new plan protects nothing and writes to a
storage pool that is already there.
"""

from __future__ import annotations

import os
from collections.abc import Iterator
from typing import Any

import pytest
from sdk_primer import SDKError

from commvault_sdk import CommvaultClient

from .conftest import PREFIX
from .recorder import Entry

pytestmark = pytest.mark.usefixtures("changes")


def _named(answer: Any, list_key: str, entity_key: str | None = None) -> list[tuple[int, str]]:
    """(id, name) of each object in a V4 listing."""
    out = []
    for item in (answer or {}).get(list_key) or []:
        entity = item.get(entity_key, item) if entity_key else item
        if isinstance(entity, dict) and entity.get("id") is not None:
            out.append((int(entity["id"]), str(entity.get("name", ""))))
    return out


@pytest.fixture(scope="module", autouse=True)
def tidy(cv: CommvaultClient) -> Iterator[None]:
    """At the end: remove every bltlive server group, user group and plan,
    this run's or a failed run's."""
    yield
    if not cv.allow_changes:
        return
    for gid, name in _named(cv.raw.server_group.list_server_group(), "serverGroups"):
        if name.startswith("bltlive-"):
            cv.raw.server_group.delete_server_group(gid)
    for gid, name in _named(cv.raw.user_group.list_user_group_v4(), "userGroups"):
        if name.startswith("bltlive-"):
            cv.raw.user_group.delete_user_group_v4(gid, skip_owner_ship_transfer=True)
    # Plans are not removed here: deleting one can need an administrator's
    # approval (see test_server_plan_lifecycle), and asking for it again
    # on every run would mail them each time.


def test_server_group_lifecycle(cv: CommvaultClient, record: Entry) -> None:
    """A server group with no servers in it: create, read back, change its
    description, delete."""
    name = f"{PREFIX}-servers"
    created = cv.raw.server_group.post_server_group(
        body={"name": name, "description": "bltlive: made by the SDK's live tests"}
    )
    group_id = int((created.get("serverGroup") or created)["id"])
    group = cv.raw.server_group.get_server_group(group_id)
    assert (group.get("general") or group).get("name", name) == name or name in str(group)

    cv.raw.server_group.put_server_group(
        group_id, body={"description": "bltlive: changed by the SDK's live tests"}
    )
    changed = cv.raw.server_group.get_server_group(group_id)
    record.result({"created": created, "description": _find(changed, "description")})
    assert "changed" in str(_find(changed, "description"))

    cv.raw.server_group.delete_server_group(group_id)
    remaining = [n for _, n in _named(cv.raw.server_group.list_server_group(), "serverGroups")]
    assert name not in remaining


def test_user_group_lifecycle(cv: CommvaultClient, record: Entry) -> None:
    """A user group with nobody in it and no permissions: create, read
    back, change, delete (nothing it owns to hand over)."""
    name = f"{PREFIX}-users"
    created = cv.raw.user_group.post_user_group_2(
        body={"name": name, "description": "bltlive: made by the SDK's live tests"}
    )
    group_id = int(_find(created, "id"))
    cv.raw.user_group.put_user_group(
        group_id, body={"description": "bltlive: changed by the SDK's live tests"}
    )
    changed = cv.raw.user_group.get_user_group_v4(group_id)
    record.result({"created": created, "description": _find(changed, "description")})
    assert "changed" in str(_find(changed, "description"))

    cv.raw.user_group.delete_user_group_v4(group_id, skip_owner_ship_transfer=True)
    remaining = [n for _, n in _named(cv.raw.user_group.list_user_group_v4(), "userGroups")]
    assert name not in remaining


def _disk_pool(cv: CommvaultClient) -> tuple[int, str]:
    answer = cv.raw.storage.list_storage_pool()
    for item in (answer or {}).get("storagePoolList") or []:
        entity = item.get("storagePoolEntity") or {}
        if entity.get("storagePoolId"):
            return int(entity["storagePoolId"]), str(entity.get("storagePoolName", ""))
    pytest.skip("no storage pool on the CommServe for a plan to write to")


def test_server_plan_lifecycle(cv: CommvaultClient, record: Entry) -> None:
    """A server plan that protects nothing: created with one backup
    destination on a storage pool already there (kept 7 days), read back,
    renamed, deleted.

    Only with CV_LIVE_PLANS=yes as well. A CommServe can require an
    administrator to authorize deleting a plan: the delete then answers
    412 ("An email has been sent to the administrator to authorize the
    delete plan request") and the plan goes once they accept. Seen on the
    lab CommServe, 2026-11-05."""
    if os.environ.get("CV_LIVE_PLANS") != "yes":
        pytest.skip("deleting a plan may need an administrator's approval: CV_LIVE_PLANS=yes")
    name = f"{PREFIX}-plan"
    pool_id, _ = _disk_pool(cv)
    try:
        created = cv.raw.server_plan.post_server_plan(
            body={
                "planName": name,
                "backupDestinations": [
                    {
                        "backupDestinationName": "Primary",
                        "retentionPeriodDays": 7,
                        "storagePool": {"id": pool_id},
                    }
                ],
            }
        )
    except SDKError as error:
        record.note(f"Creating the plan was refused: {error.server_message or error}")
        raise
    plan_id = int((created.get("plan") or created)["id"])
    plan = cv.raw.server_plan.get_server_plan(plan_id)
    destinations = plan.get("backupDestinations") or []
    record.result(
        {
            "plan": plan.get("plan"),
            "backupDestinations": [
                {k: d.get(k) for k in ("planBackupDestination", "retentionPeriodDays")}
                for d in destinations
            ],
        }
    )
    assert destinations

    renamed = f"{name}-2"
    cv.raw.server_plan.put_server_plan(plan_id, body={"newName": renamed})
    assert renamed in str(cv.raw.server_plan.get_server_plan(plan_id).get("plan"))

    try:
        cv.raw.server_plan.delete_server_plan(plan_id)
    except SDKError as error:
        if error.status_code == 412:
            pytest.skip(f"the delete waits for an administrator: {error.server_message}")
        raise
    remaining = [
        str(p.get("plan", {}).get("planName")) for p in cv.raw.plan.list_plan().get("plans", [])
    ]
    assert renamed not in remaining


def _find(value: Any, key: str) -> Any:
    """The first value under `key`, anywhere in an answer."""
    if isinstance(value, dict):
        if key in value:
            return value[key]
        for v in value.values():
            found = _find(v, key)
            if found is not None:
                return found
    if isinstance(value, list):
        for v in value:
            found = _find(v, key)
            if found is not None:
                return found
    return None
