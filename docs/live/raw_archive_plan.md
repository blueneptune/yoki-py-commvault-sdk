# `cv.raw.archive_plan`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:50 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_archive_plan` - GET /V4/ArchivePlan/{planId}

> **SKIPPED** on this run: Commvault answered: 400 - Plan not found

```python
cv.raw.archive_plan.get_archive_plan('1')
```

**On the wire**

- `GET /V4/ArchivePlan/1` -> **400** (0.07 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorMessage": "Plan not found",
    "errorCode": 2
  }
  ```

  </details>

## `get_archive_plan_backup_destinations` - GET /V4/ArchivePlan/{planId}/BackupDestinations

```python
cv.raw.archive_plan.get_archive_plan_backup_destinations('1')
```

**On the wire**

- `GET /V4/ArchivePlan/1/BackupDestinations` -> **200** (0.18 s)

  <details><summary>Answer</summary>

  ```json
  {
    "backupdestinations": [
      {
        "copyPrecedence": 1,
        "retentionPeriodDays": 30,
        "storagePoolTypeForCopy": "GlobalDedupeStoragePolicy",
        "overrideRetentionSettings": true,
        "isDefault": true,
        "copyType": "SYNCHRONOUS",
        "storageType": "DISK",
        "enableDataAging": true,
        "planBackupDestination": {
          "name": "Primary",
          "id": 2
        },
        "storagePool": {
          "isArchiveStorage": false,
          "storageClass": "",
          "retentionPeriodDays": -1,
          "wormStoragePoolFlag": 96,
          "name": "storage-pool-01",
          "id": 2,
          "type": "DEDUPLICATION",
          "deviceType": {
            "name": "MAGNETIC",
            "id": 1
          },
          "region": {
            "displayName": "",
            "name": "",
            "id": 0
          }
        }
      }
    ]
  }
  ```

  </details>

## `list_archive_plan_storage_policy` - GET /V5/ArchivePlan/{planId}/StoragePolicy

> **SKIPPED** on this run: Commvault answered: 403

```python
cv.raw.archive_plan.list_archive_plan_storage_policy('1')
```

**On the wire**

- `GET /V5/ArchivePlan/1/StoragePolicy` -> **403** (0.01 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

## `get_archive_plan_storage_policy`

GET /V5/ArchivePlan/{planId}/StoragePolicy/{storagePolicyId}

> **SKIPPED** on this run: Commvault answered: 403

```python
cv.raw.archive_plan.get_archive_plan_storage_policy('1', '4')
```

**On the wire**

- `GET /V5/ArchivePlan/1/StoragePolicy` -> **403** (0.02 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

- `GET /V5/ArchivePlan/1/StoragePolicy/4` -> **403** (0.01 s)

  <details><summary>Answer</summary>

  (no body)

  </details>
