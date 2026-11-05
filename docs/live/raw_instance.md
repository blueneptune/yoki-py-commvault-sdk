# `cv.raw.instance`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:50 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_databases_instances` - GET /databases/instances

```python
cv.raw.instance.get_databases_instances()
```

**On the wire**

- `GET /databases/instances` -> **200** (0.22 s)

  <details><summary>Answer</summary>

  ```json
  {
    "dbInstance": [
      {
        "cloudVendorType": 0,
        "notReadyReason": "",
        "flags": 0,
        "description": "",
        "slaStatus": 1,
        "clientType": 1,
        "noDBs": 15,
        "applicationSize": 113246208,
        "vmHypType": 0,
        "dbInstanceFlags": 0,
        "logBackupTime": 1793904560,
        "slaCategoryDescription": "Protected",
        "sla": "Met",
        "version": "",
        "backupSize": 242352128,
        "isCloudDB": false,
        "isSnapEnabled": 0,
        "backupTime": 1793889993,
        "vmGUID": "",
        "status": "Ready",
        "instance": {
          "clientName": "host-13",
          "instanceName": "host-13",
          "displayName": "host-13",
          "instanceId": 6,
          "clientId": 15,
          "appName": "SQL Server",
          "applicationId": 81
        },
        "plan": {
          "planName": "plan-01",
          "planId": 1
        },
        "lastBackupJobInfo": {
          "jobID": 1503,
          "failureReasonIds": "",
          "commCellID": 2,
          "failureReasonMessageEnglish": "",
          "status": 1,
          "startTime": {
            "time": 1793889993
          },
          "endTime": {
            "time": 1793890284
          }
        }
      },
      {
        "cloudVendorType": 0,
        "notReadyReason": "Last backup failed. Please review the failure and take corrective action as needed.",
        "flags": 0,
        "description": "",
        "slaStatus": 1,
        "clientType": 1,
        "noDBs": 13,
        "applicationSize": 85983232,
        "vmHypType": 0,
        "dbInstanceFlags": 0,
        "logBackupTime": 1793645372,
        "slaCategoryDescription": "Protected",
        "sla": "Met",
        "version": "",
        "backupSize": 209059840,
        "isCloudDB": false,
        "isSnapEnabled": 0,
        "backupTime": 1793644988,
        "vmGUID": "",
        "status": "Not Ready",
        "instance": {
          "clientName": "host-14",
          "instanceName": "host-14",
          "displayName": "host-14",
          "instanceId": 7,
          "clientId": 16,
          "appName": "SQL Server",
          "applicationId": 81
        },
        "plan": {
          "planName": "plan-01",
          "planId": 1
        },
        "lastBackupJobInfo": {
          "jobID": 1491,
          "failureReasonIds": "515,",
          "commCellID": 2,
          "failureReasonMessageEnglish": "Another backup is running for client [host-14], iDataAgent [SQL Server], Instance [host-14], Subclient [default].<br/>Source: commserve-02, Process: JobManager",
          "status": 9,
          "startTime": {
            "time": 1793826011
          },
          "endTime": {
            "time": 1793826011
          }
        }
      }
    ],
    "error": {
      "errorMessage": "",
      "errorCode": 0
    }
  }
  ```

  </details>

## `get_instance_by_name_client_name_client_name_app_name_app_name_instance_name_instance_name`

GET /instance/byName(clientName={clientName},appName={appName}),instanceName={instanceName}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.instance.get_instance_by_name_client_name_client_name_app_name_app_name_instance_name_instance_name(...)
```
