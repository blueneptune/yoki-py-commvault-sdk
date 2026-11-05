# `cv.raw.instances`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 16:43 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_instances` - GET /V4/Instances

```python
cv.raw.instances.get_instances()
```

**On the wire**

- `GET /V4/Instances` -> **200** (0.17 s)

  <details><summary>Answer</summary>

  ```json
  {
    "instances": [
      {
        "id": 6,
        "name": "host-13",
        "server": "host-13",
        "client": {
          "id": 15,
          "name": "host-13"
        },
        "vendor": "NOT_APPLICABLE",
        "databaseEngine": "SQL_SERVER",
        "status": "READY",
        "lastBackup": {
          "jobId": 1503,
          "status": "COMPLETED",
          "time": 1793889993
        },
        "applicationSize": 113246208,
        "plan": {
          "id": 1,
          "name": "plan-01"
        },
        "SLAStatus": "MET_SLA",
        "company": {
          "id": 0,
          "name": ""
        }
      },
      {
        "id": 7,
        "name": "host-14",
        "server": "host-14",
        "client": {
          "id": 16,
          "name": "host-14"
        },
        "vendor": "NOT_APPLICABLE",
        "databaseEngine": "SQL_SERVER",
        "status": "NOT_READY",
        "notReadyReason": "Last backup failed. Please review the failure and take corrective action as needed.",
        "lastBackup": {
          "jobId": 1491,
          "status": "FAILED_TO_START",
          "time": 1793826011,
          "failureReason": "Another backup is running for client [host-14], iDataAgent [SQL Server], Instance [host-14], Subclient [subclient-01].<br/>Source: commserve-02, Process: JobManager"
        },
        "applicationSize": 85983232,
        "plan": {
          "id": 1,
          "name": "plan-01"
        },
        "SLAStatus": "MET_SLA",
        "company": {
          "id": 0,
          "name": ""
        }
      }
    ]
  }
  ```

  </details>

## `get_oracle_instance_rmanbrowse` - GET /V4/oracle/instance/{instanceId}/rmanbrowse

> **SKIPPED** on this run: not swept: starts work or returns a file

```python
cv.raw.instances.get_oracle_instance_rmanbrowse(...)
```
