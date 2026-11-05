# `cv.raw.file_server`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:50 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_backupsets` - GET /Backupsets

```python
cv.raw.file_server.get_backupsets()
```

**On the wire**

- `GET /Backupsets` -> **200** (0.11 s)

  <details><summary>Answer</summary>

  ```json
  {
    "overview": {
      "vmsCount": 0,
      "unixServersCount": 0,
      "nasFilersCount": 0,
      "windowsServersCount": 0,
      "fsCount": 0,
      "databasesCount": 0,
      "cloudAppsCount": 0
    },
    "backupsetProperties": [
      {
        "applicationSize": 0,
        "lastBackupTime": 0,
        "commonBackupSet": {
          "slaCategory": 0,
          "slaStatus": 3,
          "isDeleted": false,
          "isFanInBackupSet": false,
          "slaCategoryDescription": "",
          "isbackupset-01": true,
          "isMining": false
        },
        "backupSetEntity": {
          "clientName": "host-02",
          "instanceName": "asset-01",
          "displayName": "host-02",
          "backupsetId": 7,
          "_type_": 6,
          "instanceId": 1,
          "backupsetGUID": "D8313A81-59C2-485A-ABBA-3AD0CA6645E4",
          "clientId": 4,
          "appName": "Linux File System",
          "backupsetName": "backupset-01",
          "applicationId": 29
        }
      },
      {
        "applicationSize": 0,
        "lastBackupTime": 0,
        "commonBackupSet": {
          "slaCategory": 0,
          "slaStatus": 3,
          "isDeleted": false,
          "isFanInBackupSet": false,
          "slaCategoryDescription": "",
          "isbackupset-01": true,
          "isMining": false
        },
        "backupSetEntity": {
          "clientName": "host-04",
          "instanceName": "asset-01",
          "displayName": "host-04",
          "backupsetId": 11,
          "_type_": 6,
          "instanceId": 1,
          "backupsetGUID": "2607B78A-3774-4E69-914E-6E81D9129431",
          "clientId": 6,
          "appName": "Linux File System",
          "backupsetName": "backupset-01",
          "applicationId": 29
        }
      },
      {
        "applicationSize": 0,
        "lastBackupTime": 0,
        "commonBackupSet": {
          "slaCategory": 0,
          "slaStatus": 3,
          "isDeleted": false,
          "isFanInBackupSet": false,
          "slaCategoryDescription": "",
          "isbackupset-01": true,
          "isMining": false
        },
        "backupSetEntity": {
          "clientName": "host-03",
          "instanceName": "asset-01",
          "displayName": "host-03",
          "backupsetId": 9,
          "_type_": 6,
          "instanceId": 1,
          "backupsetGUID": "5C490865-D01F-42F7-8165-6D7579067D55",
          "clientId": 5,
          "appName": "Linux File System",
          "backupsetName": "backupset-01",
          "applicationId": 29
        }
      },
      "... 8 more"
    ]
  }
  ```

  </details>

## `get_plan_content` - GET /Plan/{planId}/content

> **SKIPPED** on this run: not swept: starts work or returns a file

```python
cv.raw.file_server.get_plan_content(...)
```

## `get_subclient_browse` - GET /subclient/{subclientId}/Browse

> **SKIPPED** on this run: not swept: starts work or returns a file

```python
cv.raw.file_server.get_subclient_browse(...)
```
