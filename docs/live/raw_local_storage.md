# `cv.raw.local_storage`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:37 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `list_storage_local` - GET /V4/Storage/Local

```python
cv.raw.local_storage.list_storage_local()
```

**On the wire**

- `GET /V4/Storage/Local` -> **200** (0.21 s)

  <details><summary>Answer</summary>

  ```json
  {
    "localStorage": [
      {
        "id": 2,
        "name": "storage-pool-01",
        "storagePoolType": "DEDUPLICATION",
        "status": "Online",
        "capacity": 1048572,
        "freeSpace": 1025530,
        "libraryVendorType": 1,
        "storageType": "DISK",
        "company": {
          "id": 0,
          "name": ""
        }
      }
    ]
  }
  ```

  </details>

## `get_storage_local` - GET /V4/Storage/Local/{storagePoolId}

> **SKIPPED** on this run: Commvault answered: 403

```python
cv.raw.local_storage.get_storage_local('2')
```

**On the wire**

- `GET /V4/Storage/Local/2` -> **403** (0.01 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

## `get_storage_local_backup_location`

GET /V4/Storage/Local/{storagePoolId}/BackupLocation/{backupLocationId}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.local_storage.get_storage_local_backup_location(...)
```

## `get_storage_local_backup_location_access_path_media_agents`

GET /V4/Storage/Local/{storagePoolId}/BackupLocation/{backupLocationId}/AccessPath/MediaAgents

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.local_storage.get_storage_local_backup_location_access_path_media_agents(...)
```
