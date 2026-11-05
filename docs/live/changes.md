# Changes

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:50 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## A server group with no servers in it: create, read back, change its description, delete

```python
name = f"{PREFIX}-servers"
created = cv.raw.server_group.post_server_group(
    body={"name": name, "description": "bltlive: made by the SDK's live tests"}
)
group_id = _id_of(_named(cv.raw.server_group.list_server_group(), "serverGroups"), name)
group = cv.raw.server_group.get_server_group(group_id)
assert name in str(group)

# The update names the group's type (one with servers picked by hand
# is MANUAL); a body with the description alone is answered 500.
cv.raw.server_group.put_server_group(
    group_id,
    body={
        "serverGroupType": "MANUAL",
        "serverGroup": {"id": group_id, "name": name},
        "description": "bltlive: changed by the SDK's live tests",
    },
)
changed = cv.raw.server_group.get_server_group(group_id)
record.result({"created": created, "description": _find(changed, "description")})
assert "changed" in str(_find(changed, "description"))

cv.raw.server_group.delete_server_group(group_id)
remaining = [n for _, n in _named(cv.raw.server_group.list_server_group(), "serverGroups")]
assert name not in remaining
```

**On the wire**

- `POST /V4/ServerGroup` -> **200** (3.13 s)

  Sent:

  ```json
  {
    "name": "bltlive-11051848-servers",
    "description": "bltlive: made by the SDK's live tests"
  }
  ```

  <details><summary>Answer</summary>

  ```json
  {
    "serverGroupInfo": {
      "GUID": "27660170-6A34-42C7-AEDC-5C8CAE778AEB",
      "name": "bltlive-11051848-servers",
      "id": 13
    }
  }
  ```

  </details>

- `GET /V4/ServerGroup` -> **200** (0.19 s)

  <details><summary>Answer</summary>

  ```json
  {
    "serverGroups": [
      {
        "name": "client-group-01",
        "id": 1,
        "description": "",
        "serverCount": 1,
        "association": "AUTOMATIC",
        "isSyncInProgress": false,
        "company": {
          "id": 0,
          "name": ""
        }
      },
      {
        "name": "client-group-02",
        "id": 2,
        "description": "",
        "serverCount": 0,
        "association": "AUTOMATIC",
        "isSyncInProgress": false,
        "company": {
          "id": 0,
          "name": ""
        }
      },
      {
        "name": "client-group-03",
        "id": 3,
        "description": "",
        "serverCount": 1,
        "association": "AUTOMATIC",
        "isSyncInProgress": false,
        "company": {
          "id": 0,
          "name": ""
        }
      },
      "... 5 more"
    ]
  }
  ```

  </details>

- `GET /V4/ServerGroup/13` -> **200** (1.34 s)

  <details><summary>Answer</summary>

  ```json
  {
    "serverGroup": {
      "name": "bltlive-11051848-servers",
      "id": 13
    },
    "description": "bltlive: made by the SDK's live tests",
    "general": {
      "region": {
        "name": "Not set",
        "id": 0
      },
      "enableDataEncryption": false,
      "autoDiscover": false
    },
    "security": [],
    "activityControl": {
      "databackup": true,
      "dataRestore": true,
      "dataAging": true
    },
    "associatedServers": [],
    "fileExceptions": {},
    "blackoutWindow": []
  }
  ```

  </details>

- `PUT /V4/ServerGroup/13` -> **200** (1.73 s)

  Sent:

  ```json
  {
    "serverGroupType": "MANUAL",
    "serverGroup": {
      "id": 13,
      "name": "bltlive-11051848-servers"
    },
    "description": "bltlive: changed by the SDK's live tests"
  }
  ```

  <details><summary>Answer</summary>

  ```json
  {
    "errorMessage": "Server group updated successfully",
    "errorCode": 0
  }
  ```

  </details>

- `GET /V4/ServerGroup/13` -> **200** (1.39 s)

  <details><summary>Answer</summary>

  ```json
  {
    "serverGroup": {
      "name": "bltlive-11051848-servers",
      "id": 13
    },
    "description": "bltlive: changed by the SDK's live tests",
    "general": {
      "region": {
        "name": "Not set",
        "id": 0
      },
      "enableDataEncryption": false,
      "autoDiscover": false
    },
    "security": [],
    "activityControl": {
      "databackup": true,
      "dataRestore": true,
      "dataAging": true
    },
    "associatedServers": [],
    "fileExceptions": {},
    "blackoutWindow": []
  }
  ```

  </details>

- `DELETE /V4/ServerGroup/13` -> **200** (0.96 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorMessage": "",
    "errorCode": 0
  }
  ```

  </details>

- `GET /V4/ServerGroup` -> **200** (0.20 s)

  <details><summary>Answer</summary>

  ```json
  {
    "serverGroups": [
      {
        "name": "client-group-01",
        "id": 1,
        "description": "",
        "serverCount": 1,
        "association": "AUTOMATIC",
        "isSyncInProgress": false,
        "company": {
          "id": 0,
          "name": ""
        }
      },
      {
        "name": "client-group-02",
        "id": 2,
        "description": "",
        "serverCount": 0,
        "association": "AUTOMATIC",
        "isSyncInProgress": false,
        "company": {
          "id": 0,
          "name": ""
        }
      },
      {
        "name": "client-group-03",
        "id": 3,
        "description": "",
        "serverCount": 1,
        "association": "AUTOMATIC",
        "isSyncInProgress": false,
        "company": {
          "id": 0,
          "name": ""
        }
      },
      "... 4 more"
    ]
  }
  ```

  </details>

**What the SDK gave back**

```json
{
  "created": {
    "serverGroupInfo": {
      "GUID": "27660170-6A34-42C7-AEDC-5C8CAE778AEB",
      "name": "bltlive-11051848-servers",
      "id": 13
    }
  },
  "description": "bltlive: changed by the SDK's live tests"
}
```

## A user group with nobody in it and no permissions

Create, read back, change, delete (nothing it owns to hand over).

```python
name = f"{PREFIX}-users"
created = cv.raw.user_group.post_user_group_2(
    body={"name": name, "description": "bltlive: made by the SDK's live tests"}
)
group_id = _id_of(_named(cv.raw.user_group.list_user_group_v4(), "userGroups"), name)
# V4 names the new value: `newDescription` (and `newName`); a plain
# `description` is accepted and ignored.
cv.raw.user_group.put_user_group(
    group_id, body={"newDescription": "bltlive: changed by the SDK's live tests"}
)
changed = cv.raw.user_group.get_user_group_v4(group_id)
record.result({"created": created, "description": _find(changed, "description")})
assert "changed" in str(_find(changed, "description"))

cv.raw.user_group.delete_user_group_v4(group_id, skip_owner_ship_transfer=True)
remaining = [n for _, n in _named(cv.raw.user_group.list_user_group_v4(), "userGroups")]
assert name not in remaining
```

**On the wire**

- `POST /V4/UserGroup` -> **200** (1.84 s)

  Sent:

  ```json
  {
    "name": "bltlive-11051848-users",
    "description": "bltlive: made by the SDK's live tests"
  }
  ```

  <details><summary>Answer</summary>

  ```json
  {
    "id": 12,
    "name": "bltlive-11051848-users",
    "GUID": "EB50222E-4801-4658-ACFC-3E0725AC82D7"
  }
  ```

  </details>

- `GET /V4/UserGroup` -> **200** (0.21 s)

  <details><summary>Answer</summary>

  ```json
  {
    "userGroups": [
      {
        "id": 1,
        "name": "master",
        "GUID": "52F0152D-42C3-4CF1-8397-0B630F0E710E",
        "serviceType": "UNKNOWN",
        "description": "Administrative Group",
        "provider": {
          "id": 0,
          "name": ""
        },
        "enabled": true,
        "allowMultipleCompanyMembers": false,
        "company": {
          "id": 0,
          "name": ""
        }
      },
      {
        "id": 7,
        "name": "user-group-01",
        "GUID": "1257F0EC-7176-4B01-9CC8-57AC452B2800",
        "serviceType": "UNKNOWN",
        "description": "",
        "provider": {
          "id": 0,
          "name": ""
        },
        "enabled": true,
        "allowMultipleCompanyMembers": false,
        "company": {
          "id": 0,
          "name": ""
        }
      },
      {
        "id": 12,
        "name": "bltlive-11051848-users",
        "GUID": "EB50222E-4801-4658-ACFC-3E0725AC82D7",
        "serviceType": "UNKNOWN",
        "description": "bltlive: made by the SDK's live tests",
        "provider": {
          "id": 0,
          "name": ""
        },
        "enabled": true,
        "allowMultipleCompanyMembers": false,
        "company": {
          "id": 0,
          "name": ""
        }
      }
    ]
  }
  ```

  </details>

- `PUT /V4/UserGroup/12` -> **200** (2.51 s)

  Sent:

  ```json
  {
    "newDescription": "bltlive: changed by the SDK's live tests"
  }
  ```

  <details><summary>Answer</summary>

  ```json
  {
    "errorCode": 0,
    "errorString": "Successful"
  }
  ```

  </details>

- `GET /V4/UserGroup/12` -> **200** (0.65 s)

  <details><summary>Answer</summary>

  ```json
  {
    "id": 12,
    "name": "bltlive-11051848-users",
    "GUID": "EB50222E-4801-4658-ACFC-3E0725AC82D7",
    "description": "bltlive: changed by the SDK's live tests",
    "enabled": true,
    "serviceType": "UNKNOWN",
    "email": "",
    "enableTwoFactorAuthentication": "DISABLED_AT_COMPANY",
    "enableLocalAuthentication": "DISABLED_AT_COMPANY",
    "laptopAdmins": false,
    "enforceFSQuota": false,
    "azureGUID": "",
    "eligibleToAllowMultipleCompanyMembers": true,
    "allowMultipleCompanyMembers": false,
    "company": {
      "id": 0,
      "name": ""
    },
    "users": []
  }
  ```

  </details>

- `DELETE /V4/UserGroup/12?skipOwnerShipTransfer=true` -> **200** (0.76 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorString": "Successful",
    "errorCode": 0
  }
  ```

  </details>

- `GET /V4/UserGroup` -> **200** (0.22 s)

  <details><summary>Answer</summary>

  ```json
  {
    "userGroups": [
      {
        "id": 1,
        "name": "master",
        "GUID": "52F0152D-42C3-4CF1-8397-0B630F0E710E",
        "serviceType": "UNKNOWN",
        "description": "Administrative Group",
        "provider": {
          "id": 0,
          "name": ""
        },
        "enabled": true,
        "allowMultipleCompanyMembers": false,
        "company": {
          "id": 0,
          "name": ""
        }
      },
      {
        "id": 7,
        "name": "user-group-01",
        "GUID": "1257F0EC-7176-4B01-9CC8-57AC452B2800",
        "serviceType": "UNKNOWN",
        "description": "",
        "provider": {
          "id": 0,
          "name": ""
        },
        "enabled": true,
        "allowMultipleCompanyMembers": false,
        "company": {
          "id": 0,
          "name": ""
        }
      }
    ]
  }
  ```

  </details>

**What the SDK gave back**

```json
{
  "created": {
    "id": 12,
    "name": "bltlive-11051848-users",
    "GUID": "EB50222E-4801-4658-ACFC-3E0725AC82D7"
  },
  "description": "bltlive: changed by the SDK's live tests"
}
```

## A server plan that protects nothing

Created with one backup destination on a storage pool already there (kept 7 days), read back, renamed, deleted.

Only with CV_LIVE_PLANS=yes as well. A CommServe can require an
administrator to authorize deleting a plan: the delete then answers
412 ("An email has been sent to the administrator to authorize the
delete plan request") and the plan goes once they accept. Seen on the
lab CommServe, 2026-11-05.

> **SKIPPED** on this run: deleting a plan may need an administrator's approval: CV_LIVE_PLANS=yes

```python
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
```
