# `cv.raw.server_group`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:37 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `list_server_group` - GET /V4/ServerGroup

```python
cv.raw.server_group.list_server_group()
```

**On the wire**

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
      "... 4 more"
    ]
  }
  ```

  </details>

## `get_server_group` - GET /V4/ServerGroup/{serverGroupId}

```python
cv.raw.server_group.get_server_group('1')
```

**On the wire**

- `GET /V4/ServerGroup/1` -> **200** (1.35 s)

  <details><summary>Answer</summary>

  ```json
  {
    "serverGroup": {
      "name": "client-group-01",
      "id": 1
    },
    "description": "Select CS, MA, WebConsole, WebServer, Index Gateway, Index Store, client-group-02.",
    "general": {
      "region": {
        "name": "Not set",
        "id": 0
      },
      "enableDataEncryption": false,
      "autoDiscover": false
    },
    "security": [
      {
        "userGroup": {
          "id": 1,
          "name": "user-group-01"
        },
        "isCreatorAssociation": true,
        "role": {
          "id": 1,
          "name": "user-group-01"
        }
      }
    ],
    "activityControl": {
      "databackup": true,
      "dataRestore": true,
      "dataAging": true
    },
    "associatedServers": [
      {
        "id": 2,
        "name": "commserve-02",
        "version": "11 SP46.30",
        "os": "Windows Server 2025 Datacenter",
        "updateStatus": "Needs Update"
      }
    ],
    "fileExceptions": {},
    "blackoutWindow": []
  }
  ```

  </details>

## `get_server_group_dc_plan` - GET /V4/ServerGroup/{serverGroupId}/DCPlan

```python
cv.raw.server_group.get_server_group_dc_plan('1')
```

**On the wire**

- `GET /V4/ServerGroup/1/DCPlan` -> **200** (0.08 s)

  <details><summary>Answer</summary>

  ```json
  {
    "name": "",
    "id": 0
  }
  ```

  </details>
