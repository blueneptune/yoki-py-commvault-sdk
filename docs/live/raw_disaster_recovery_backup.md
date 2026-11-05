# `cv.raw.disaster_recovery_backup`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:37 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_commcell_dr_backup_options` - GET /Commcell/DRBackup/Options

```python
cv.raw.disaster_recovery_backup.get_commcell_dr_backup_options()
```

**On the wire**

- `GET /Commcell/DRBackup/Options` -> **200** (0.30 s)

  <details><summary>Answer</summary>

  ```json
  {
    "properties": {
      "DRDumpLocation": "H:\\commvaultdata\\DR",
      "isUserAccountEnabled": false,
      "uploadBackupMetadataToCloud": true,
      "uploadBackupMetadataToCloudLib": false,
      "enableLogBackup": false,
      "UseLocalDrive": true,
      "enableDatabasesBackupCompression": false,
      "UseNetworkShare": false,
      "region": "",
      "DRNumFulls": 5,
      "cloudLibrary": {
        "libraryName": "",
        "_type_": 9,
        "libraryId": 0
      },
      "pattern": {
        "active_end_occurence": 0,
        "freq_subday_interval": 0,
        "freq_type": 4,
        "patternId": 3,
        "flags": 0,
        "description": "",
        "active_end_time": 0,
        "active_start_time_window": 0,
        "active_end_date": 0,
        "skipOccurence": 0,
        "skipDayNumber": 0,
        "active_start_time": 36000,
        "freq_restart_interval": 0,
        "active_start_date": 1437091200,
        "freq_interval": 1,
        "freq_relative_interval": 0,
        "name": "",
        "freq_recurrence_factor": 1,
        "calendar": {
          "calendarName": "Standard",
          "calendarId": 1
        },
        "timeZone": {
          "TimeZoneID": 1000,
          "TimeZoneName": "CommServe Time Zone"
        }
      },
      "cloudCredentials": "<masked>"
    }
  }
  ```

  </details>

## `get_commcell_dr_backup_properties` - GET /Commcell/DRBackup/Properties

```python
cv.raw.disaster_recovery_backup.get_commcell_dr_backup_properties()
```

**On the wire**

- `GET /Commcell/DRBackup/Properties` -> **200** (0.16 s)

  <details><summary>Answer</summary>

  ```json
  {
    "drBackupInfo": {
      "prePostProcessSettings": {
        "preScanProcess": "",
        "postBackupProcess": "",
        "postScanProcess": "",
        "runPostScanProcess": false,
        "preBackupProcess": "",
        "runPostBackupProcess": false,
        "impersonateUser": {
          "userName": ""
        }
      },
      "exportSettings": {
        "wildCardSetting": "",
        "uploadBackupMetadataToCloud": true,
        "backupMetadataFolder": "H:\\commvaultdata\\DR",
        "isUseVSS": true,
        "numberOfMetadata": 5,
        "uploadBackupMetadataToCloudLib": false,
        "cloudLibrary": {
          "libraryName": "",
          "libraryId": 0
        },
        "storagePolicy": {
          "storagePolicyName": "storage-policy-01",
          "storagePolicyId": 4
        },
        "cloudCredentials": "<masked>"
      }
    }
  }
  ```

  </details>
