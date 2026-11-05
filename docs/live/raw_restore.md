# `cv.raw.restore`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:37 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_client_2_hierarchy` - GET /Client/2/Hierarchy

```python
cv.raw.restore.get_client_2_hierarchy()
```

**On the wire**

- `GET /Client/2/Hierarchy` -> **200** (0.16 s)

  <details><summary>Answer</summary>

  ```json
  {
    "entity": [
      {
        "workloadId": 2,
        "subclientId": 7,
        "displayName": "commserve-02",
        "clientId": 2,
        "instanceName": "asset-01",
        "appName": "Windows File System",
        "applicationId": 33,
        "clientName": "commserve-02",
        "backupsetId": 3,
        "instanceId": 1,
        "subclientName": "subclient-02",
        "backupsetName": "backupset-01"
      },
      {
        "workloadId": 2,
        "subclientId": 8,
        "displayName": "commserve-02",
        "clientId": 2,
        "instanceName": "asset-01",
        "appName": "Windows File System",
        "applicationId": 33,
        "clientName": "commserve-02",
        "backupsetId": 3,
        "instanceId": 1,
        "subclientName": "subclient-05",
        "backupsetName": "backupset-01"
      },
      {
        "workloadId": 2,
        "subclientId": 9,
        "displayName": "commserve-02",
        "clientId": 2,
        "instanceName": "asset-01",
        "appName": "Windows File System",
        "applicationId": 33,
        "clientName": "commserve-02",
        "backupsetId": 3,
        "instanceId": 1,
        "subclientName": "subclient-03",
        "backupsetName": "backupset-01"
      }
    ]
  }
  ```

  </details>

## `get_recall` - GET /Recall

> **SKIPPED** on this run: Commvault answered: 500

```python
cv.raw.restore.get_recall()
```

**On the wire**

- `GET /Recall` -> **500** (0.06 s)

  <details><summary>Answer</summary>

  (no body)

  </details>
