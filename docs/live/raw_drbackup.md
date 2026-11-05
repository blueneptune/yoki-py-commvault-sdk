# `cv.raw.drbackup`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:50 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_dr_backup_backup_destination_source_copy_eligible`

GET /V4/DRBackup/BackupDestination/SourceCopy/Eligible

```python
cv.raw.drbackup.get_dr_backup_backup_destination_source_copy_eligible()
```

**On the wire**

- `GET /V4/DRBackup/BackupDestination/SourceCopy/Eligible` -> **200** (0.08 s)

  <details><summary>Answer</summary>

  ```json
  {
    "copy": [
      {
        "isMirrorCopy": false,
        "copyPrecedence": 1,
        "isActive": true,
        "isSourceBackupCopy": false,
        "isDefault": true,
        "isSnapCopy": false,
        "isSourceCatalog": false,
        "copyType": "SYNCHRONOUS",
        "backupDestination": {
          "name": "Primary",
          "id": 3
        }
      }
    ]
  }
  ```

  </details>

## `get_dr_backup_backup_destinations` - GET /V4/DRBackup/BackupDestinations

```python
cv.raw.drbackup.get_dr_backup_backup_destinations()
```

**On the wire**

- `GET /V4/DRBackup/BackupDestinations` -> **200** (0.15 s)

  <details><summary>Answer</summary>

  ```json
  {
    "backupdestinations": [
      {
        "retentionPeriodDays": 15,
        "retentionRuleType": "RETENTION_PERIOD",
        "backupStartTime": -1,
        "overrideRetentionSettings": true,
        "complianceLock": true,
        "copyType": "SYNCHRONOUS",
        "copyPrecedence": 1,
        "snapRecoveryPoints": 0,
        "useExtendedRetentionRules": true,
        "storagePoolTypeForCopy": "GlobalStoragePolicy",
        "isDefault": true,
        "storageType": "DISK",
        "enableDataAging": true,
        "dataRetentionLockDays": 0,
        "planBackupDestination": {
          "name": "Primary",
          "id": 3
        },
        "storagePool": {
          "isArchiveStorage": false,
          "storageClass": "",
          "retentionPeriodDays": -1,
          "wormStoragePoolFlag": 97,
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
        },
        "extendedRetentionRules": {
          "firstExtendedRetentionRule": {
            "retentionPeriodDays": 90,
            "type": "WEEKLY_FULLS"
          },
          "secondExtendedRetentionRule": {
            "retentionPeriodDays": 180,
            "type": "MONTHLY_FULLS"
          }
        }
      }
    ]
  }
  ```

  </details>

## `get_dr_backup_regions` - GET /V4/DRBackup/Regions

```python
cv.raw.drbackup.get_dr_backup_regions()
```

**On the wire**

- `GET /V4/DRBackup/Regions` -> **200** (0.27 s)

  <details><summary>Answer</summary>

  ```json
  {
    "defaultRegion": "eastus2",
    "regions": [
      {
        "regionCode": "australiaeast",
        "displayName": "Australia East"
      },
      {
        "regionCode": "australiasoutheast",
        "displayName": "Australia Southeast"
      },
      {
        "regionCode": "brazilsouth",
        "displayName": "Brazil South"
      },
      "... 22 more"
    ]
  }
  ```

  </details>

## `get_dr_backup_storage_policy` - GET /V4/DRBackup/StoragePolicy

```python
cv.raw.drbackup.get_dr_backup_storage_policy()
```

**On the wire**

- `GET /V4/DRBackup/StoragePolicy` -> **200** (0.08 s)

  <details><summary>Answer</summary>

  ```json
  {
    "name": "storage-policy-01",
    "id": 4
  }
  ```

  </details>

## `get_dr_backup_backup_destination`

GET /V4/DRBackup/BackupDestination/{BackupDestinationId}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.drbackup.get_dr_backup_backup_destination(...)
```
