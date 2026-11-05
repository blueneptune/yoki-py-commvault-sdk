# `cv.raw.db2_database`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:37 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_backupset_db2_storage_groups` - GET /Backupset/{BackupsetID}/DB2StorageGroups

```python
cv.raw.db2_database.get_backupset_db2_storage_groups('7')
```

**On the wire**

- `GET /Backupset/7/DB2StorageGroups` -> **200** (0.12 s)

  <details><summary>Answer</summary>

  ```json
  {
    "groupInfo": {},
    "error": {
      "errorMessage": "",
      "errorCode": 0
    }
  }
  ```

  </details>

## `get_client_discover_db2_instances` - GET /Client/{ClientID}/DiscoverDB2Instances

> **SKIPPED** on this run: Commvault answered: error 1: Discover Operation failed. Please check if services are running on the client.

```python
cv.raw.db2_database.get_client_discover_db2_instances('2')
```

**On the wire**

- `GET /Client/2/DiscoverDB2Instances` -> **200** (0.14 s)

  <details><summary>Answer</summary>

  ```json
  {
    "error": {
      "errorString": "Discover Operation failed. Please check if services are running on the client.",
      "errorCode": 1
    }
  }
  ```

  </details>
