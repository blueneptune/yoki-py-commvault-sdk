# `cv.raw.disk_storage`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:37 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `list_storage_disk` - GET /V4/Storage/Disk

```python
cv.raw.disk_storage.list_storage_disk()
```

**On the wire**

- `GET /V4/Storage/Disk` -> **200** (0.21 s)

  <details><summary>Answer</summary>

  ```json
  {
    "diskStorage": [
      {
        "id": 2,
        "name": "storage-pool-01",
        "storagePoolType": "DEDUPLICATION",
        "status": "Online",
        "capacity": 1048572,
        "freeSpace": 1025530,
        "usableFreeSpace": 1005050,
        "company": {
          "id": 0,
          "name": ""
        },
        "tags": []
      }
    ]
  }
  ```

  </details>

## `get_storage_disk` - GET /V4/Storage/Disk/{storagePoolId}

```python
cv.raw.disk_storage.get_storage_disk('2')
```

**On the wire**

- `GET /V4/Storage/Disk/2` -> **200** (0.74 s)

  <details><summary>Answer</summary>

  ```json
  {
    "id": 2,
    "name": "storage-pool-01",
    "general": {
      "capacity": 1048572,
      "freeSpace": 1025530,
      "sizeOnDisk": 24144,
      "dedupeSavingsPercent": 86.91
    },
    "backupLocations": [
      {
        "id": 1,
        "name": "mount-path-02",
        "status": "Ready"
      }
    ],
    "encryption": {
      "encrypt": false,
      "cipher": "NotEncrypted",
      "keyLength": 0,
      "keyProvider": {
        "id": 1,
        "name": "Built-in"
      }
    },
    "security": [],
    "associatedPlans": [
      {
        "planName": "plan-01",
        "planId": 1
      },
      {
        "planName": "bltlive-11051831-plan-2",
        "planId": 3
      }
    ]
  }
  ```

  </details>

## `get_storage_disk_backup_location`

GET /V4/Storage/Disk/{storagePoolId}/BackupLocation/{backupLocationId}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.disk_storage.get_storage_disk_backup_location(...)
```

## `get_storage_disk_backup_location_access_path_media_agents`

GET /V4/Storage/Disk/{storagePoolId}/BackupLocation/{backupLocationId}/AccessPath/MediaAgents

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.disk_storage.get_storage_disk_backup_location_access_path_media_agents(...)
```
