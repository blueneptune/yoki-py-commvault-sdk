# `cv.raw.databases`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:50 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_databases` - GET /V4/Databases

```python
cv.raw.databases.get_databases()
```

**On the wire**

- `GET /V4/Databases` -> **200** (0.42 s)

  <details><summary>Answer</summary>

  ```json
  {
    "databases": [
      {
        "applicationId": 81,
        "name": "database-03",
        "instance": {
          "id": 6,
          "name": "host-13"
        },
        "server": {
          "id": 15,
          "name": "host-13"
        },
        "vendor": "NOT_APPLICABLE",
        "databaseEngine": "SQL_SERVER",
        "recoveryModel": "FULL",
        "SLAStatus": "MET",
        "lastBackupSize": 16777216,
        "lastBackupTime": 1793904466,
        "plan": {
          "id": 1,
          "name": "plan-01"
        },
        "company": {
          "id": 0,
          "name": ""
        }
      },
      {
        "applicationId": 81,
        "name": "database-04",
        "instance": {
          "id": 6,
          "name": "host-13"
        },
        "server": {
          "id": 15,
          "name": "host-13"
        },
        "vendor": "NOT_APPLICABLE",
        "databaseEngine": "SQL_SERVER",
        "recoveryModel": "FULL",
        "SLAStatus": "MET",
        "lastBackupSize": 16777216,
        "lastBackupTime": 1793904485,
        "plan": {
          "id": 1,
          "name": "plan-01"
        },
        "company": {
          "id": 0,
          "name": ""
        }
      },
      {
        "applicationId": 81,
        "name": "database-05",
        "instance": {
          "id": 6,
          "name": "host-13"
        },
        "server": {
          "id": 15,
          "name": "host-13"
        },
        "vendor": "NOT_APPLICABLE",
        "databaseEngine": "SQL_SERVER",
        "recoveryModel": "FULL",
        "SLAStatus": "MET",
        "lastBackupSize": 16777216,
        "lastBackupTime": 1793904505,
        "plan": {
          "id": 1,
          "name": "plan-01"
        },
        "company": {
          "id": 0,
          "name": ""
        }
      },
      "... 25 more"
    ]
  }
  ```

  </details>
