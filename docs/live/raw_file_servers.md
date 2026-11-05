# `cv.raw.file_servers`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:50 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_file_servers` - GET /V4/FileServers

```python
cv.raw.file_servers.get_file_servers()
```

**On the wire**

- `GET /V4/FileServers` -> **200** (0.38 s)

  <details><summary>Answer</summary>

  ```json
  {
    "fileServerCount": 11,
    "fileServers": [
      {
        "id": 2,
        "name": "commserve-02",
        "displayName": "commserve-02",
        "hostName": "commserve-02",
        "GUID": "2DCFEA81-1B84-4E4D-ADB4-C317F96A112E",
        "cloudVendor": "NOT_APPLICABLE",
        "regionName": "NOT_APPLICABLE",
        "configured": true,
        "type": "WINDOWS",
        "lastBackup": {
          "jobId": 1498,
          "status": "COMPLETED",
          "time": 1793847612,
          "lastSuccessfulBackup": 1793847612
        },
        "applicationSize": 574504329,
        "plan": {
          "id": 0,
          "name": ""
        },
        "SLA": {
          "status": "MISSED_SLA",
          "reason": "Backup job failed"
        },
        "status": "ONLINE",
        "company": {
          "id": 0,
          "name": ""
        }
      },
      {
        "id": 4,
        "name": "host-02",
        "displayName": "host-02",
        "hostName": "host-02",
        "GUID": "99CA0BBB-F13D-4DEA-9778-08A913D3FEFA",
        "cloudVendor": "NOT_APPLICABLE",
        "regionName": "NOT_APPLICABLE",
        "configured": true,
        "type": "UNIX",
        "lastBackup": {
          "jobId": 1480,
          "status": "COMPLETED",
          "time": 1793826011,
          "lastSuccessfulBackup": 1793826011
        },
        "applicationSize": 262481,
        "plan": {
          "id": 0,
          "name": ""
        },
        "SLA": {
          "status": "MISSED_SLA",
          "reason": "No Finished Job within SLA Period"
        },
        "status": "ONLINE",
        "company": {
          "id": 0,
          "name": ""
        }
      },
      {
        "id": 5,
        "name": "host-03",
        "displayName": "host-03",
        "hostName": "host-03",
        "GUID": "33592F99-2C33-46FE-AC6F-E387EB4BA162",
        "cloudVendor": "NOT_APPLICABLE",
        "regionName": "NOT_APPLICABLE",
        "configured": true,
        "type": "UNIX",
        "lastBackup": {
          "jobId": 1481,
          "status": "COMPLETED",
          "time": 1793826011,
          "lastSuccessfulBackup": 1793826011
        },
        "applicationSize": 262481,
        "plan": {
          "id": 0,
          "name": ""
        },
        "SLA": {
          "status": "MISSED_SLA",
          "reason": "No Finished Job within SLA Period"
        },
        "status": "ONLINE",
        "company": {
          "id": 0,
          "name": ""
        }
      },
      "... 8 more"
    ]
  }
  ```

  </details>
