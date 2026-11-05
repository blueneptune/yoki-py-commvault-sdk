# `cv.raw.laptop_plan`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 16:43 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_laptop_plan` - GET /V4/LaptopPlan/{planId}

> **SKIPPED** on this run: Commvault answered: 400 - Plan not found

```python
cv.raw.laptop_plan.get_laptop_plan('1')
```

**On the wire**

- `GET /V4/LaptopPlan/1` -> **400** (0.07 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorMessage": "Plan not found",
    "errorCode": 2
  }
  ```

  </details>

## `get_laptop_plan_backup_destinations` - GET /V4/LaptopPlan/{planId}/BackupDestinations

```python
cv.raw.laptop_plan.get_laptop_plan_backup_destinations('1')
```

**On the wire**

- `GET /V4/LaptopPlan/1/BackupDestinations` -> **200** (0.16 s)

  <details><summary>Answer</summary>

  ```json
  {
    "backupdestinations": [
      {
        "retentionPeriodDays": 30,
        "retentionRuleType": "RETENTION_PERIOD",
        "backupStartTime": -1,
        "overrideRetentionSettings": true,
        "copyType": "SYNCHRONOUS",
        "copyPrecedence": 1,
        "snapRecoveryPoints": 0,
        "storagePoolTypeForCopy": "GlobalDedupeStoragePolicy",
        "issubclient-01": true,
        "storageType": "DISK",
        "enableDataAging": true,
        "dataRetentionLockDays": 0,
        "planBackupDestination": {
          "name": "storage-copy-01",
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

## `list_laptop_plan_storage_policy` - GET /V5/LaptopPlan/{planId}/StoragePolicy

> **SKIPPED** on this run: Commvault answered: 403

```python
cv.raw.laptop_plan.list_laptop_plan_storage_policy('1')
```

**On the wire**

- `GET /V5/LaptopPlan/1/StoragePolicy` -> **403** (0.02 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

## `get_laptop_plan_storage_policy`

GET /V5/LaptopPlan/{planId}/StoragePolicy/{storagePolicyId}

> **SKIPPED** on this run: Commvault answered: 403

```python
cv.raw.laptop_plan.get_laptop_plan_storage_policy('1', '4')
```

**On the wire**

- `GET /V5/LaptopPlan/1/StoragePolicy` -> **403** (0.01 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

- `GET /V5/LaptopPlan/1/StoragePolicy/4` -> **403** (0.01 s)

  <details><summary>Answer</summary>

  (no body)

  </details>
