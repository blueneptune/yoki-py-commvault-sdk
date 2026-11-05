# `cv.raw.server_plan`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 16:43 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_server_plan` - GET /V4/ServerPlan/{planId}

```python
cv.raw.server_plan.get_server_plan('1')
```

**On the wire**

- `GET /V4/ServerPlan/1` -> **200** (0.18 s)

  <details><summary>Answer</summary>

  ```json
  {
    "allowPlanOverride": false,
    "planTier": "SILVER",
    "settings": {
      "fileSearch": {}
    },
    "backupContent": {},
    "databaseOptions": {
      "logBackupRPOMins": 240,
      "runFullBackupEvery": 7,
      "commitFrequencyInHours": 8,
      "useDiskCacheForLogBackups": false
    },
    "workload": {},
    "backupDestinationIds": [
      2
    ],
    "rpo": {
      "fullBackupWindow": [
        {
          "startTime": 0,
          "endTime": 86340,
          "dayOfWeek": [
            "SUNDAY",
            "MONDAY",
            "TUESDAY",
            "... 4 more"
          ]
        }
      ],
      "SLA": {
        "inheritedSLAPeriod": 7,
        "useSystemsubclient-01SLA": true,
        "inheritedFrom": "COMMCELL",
        "SLAPeriod": 3
      },
      "backupFrequency": {
        "schedules": [
          {
            "scheduleName": "",
            "forDatabasesOnly": false,
            "backupType": "INCREMENTAL",
            "policyId": 40,
            "scheduleId": 41,
            "scheduleOption": {
              "retentionOption": {
                "retentionType": "STORAGE_POLICY_subclient-01",
                "applyRetentionOn": "storage-copy-01_COPY"
              }
            },
            "schedulePattern": {
              "endDate": 0,
              "frequency": 1,
              "repeatUntilTime": 0,
              "calendarName": "Standard",
              "calendarId": 1,
              "scheduleFrequencyType": "DAILY",
              "jobStaggerDurationInMins": 0,
              "startTime": 75600,
              "noOfTimes": 0,
              "repeatIntervalInMinutes": 0,
              "startDate": 1791158400,
              "timezone": {
                "id": 1001
              }
            }
          },
          {
            "scheduleName": "Synthetic Fulls",
            "forDatabasesOnly": false,
            "backupType": "SYNTHETICFULL",
            "policyId": 40,
            "additionalInfo": "Projected to run every [30] days based on configuration [Retention period] on backup destination [storage-copy-01].",
            "scheduleId": 42,
            "schedulePattern": {
              "endDate": 0,
              "daysBetweenSyntheticFulls": 90,
              "calendarName": "Standard",
              "calendarId": 1,
              "scheduleFrequencyType": "AUTOMATIC",
              "jobStaggerDurationInMins": 0,
              "startTime": 0,
              "noOfTimes": 0,
              "startDate": 1791158400,
              "timezone": {
                "id": 1000
              }
            }
          },
          {
            "scheduleName": "",
            "forDatabasesOnly": true,
            "backupType": "TRANSACTIONLOG",
            "policyId": 39,
            "scheduleId": 40,
            "scheduleOption": {
              "logsDiskUtilizationPercent": 80,
              "logFilesThreshold": 50,
              "deleteLogsByAppLvlConfig": false,
              "commitFrequencyInHours": 8,
              "useDiskCacheForLogBackups": false
            },
            "schedulePattern": {
              "endDate": 0,
              "maxBackupIntervalInMins": 240,
              "calendarName": "Standard",
              "calendarId": 1,
              "scheduleFrequencyType": "AUTOMATIC",
              "jobStaggerDurationInMins": 0,
              "startTime": 0,
              "noOfTimes": 0,
              "startDate": 1791158400,
              "timezone": {
                "id": 1000
              }
            }
          }
        ]
      },
      "backupWindow": [
        {
          "startTime": 0,
          "endTime": 86340,
          "dayOfWeek": [
            "SUNDAY",
            "MONDAY",
            "TUESDAY",
            "... 4 more"
          ]
        }
      ]
    },
    "associatedEntities": [
      {
        "name": "File System",
        "count": 10,
        "id": 29
      },
      {
        "name": "File System",
        "count": 4,
        "id": 33
      }
    ],
    "backupDestinations": [
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
        },
        "storagePolicy": {
          "name": "plan-01",
          "id": 3
        }
      }
    ],
    "permissions": [
      {
        "id": 1
      },
      {
        "id": 2
      },
      {
        "id": 3
      },
      "... 55 more"
    ],
    "snapshotOptions": {
      "syncError": "",
      "backupCopyRPOMins": 240
    },
    "additionalProperties": {
      "RPO": 1440,
      "status": "ENABLED",
      "addons": {
        "fileSystem": false,
        "database": true,
        "snapStatus": "INCOMPLETE"
      }
    },
    "plan": {
      "name": "plan-01",
      "id": 1
    }
  }
  ```

  </details>

## `get_server_plan_backup_destination_source_copy_eligible`

GET /V5/ServerPlan/{planId}/BackupDestination/SourceCopy/Eligible

```python
cv.raw.server_plan.get_server_plan_backup_destination_source_copy_eligible('1')
```

**On the wire**

- `GET /V5/ServerPlan/1/BackupDestination/SourceCopy/Eligible` -> **200** (0.09 s)

  <details><summary>Answer</summary>

  ```json
  {
    "copy": [
      {
        "issubclient-01": true,
        "copyType": "SYNCHRONOUS",
        "backupDestination": {
          "name": "storage-copy-01",
          "id": 2
        }
      }
    ]
  }
  ```

  </details>

## `get_server_plan_backup_destinations` - GET /V4/ServerPlan/{planId}/BackupDestinations

```python
cv.raw.server_plan.get_server_plan_backup_destinations('1')
```

**On the wire**

- `GET /V4/ServerPlan/1/BackupDestinations` -> **200** (0.15 s)

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

## `get_server_plan_rpo` - GET /V4/ServerPlan/{planId}/RPO

```python
cv.raw.server_plan.get_server_plan_rpo('1')
```

**On the wire**

- `GET /V4/ServerPlan/1/RPO` -> **200** (0.14 s)

  <details><summary>Answer</summary>

  ```json
  {
    "schedules": [
      {
        "scheduleName": "",
        "forDatabasesOnly": false,
        "backupType": "INCREMENTAL",
        "policyId": 40,
        "scheduleId": 41,
        "scheduleOption": {
          "retentionOption": {
            "retentionType": "STORAGE_POLICY_subclient-01",
            "applyRetentionOn": "storage-copy-01_COPY"
          }
        },
        "schedulePattern": {
          "endDate": 0,
          "frequency": 1,
          "repeatUntilTime": 0,
          "calendarName": "Standard",
          "calendarId": 1,
          "scheduleFrequencyType": "DAILY",
          "jobStaggerDurationInMins": 0,
          "startTime": 75600,
          "noOfTimes": 0,
          "repeatIntervalInMinutes": 0,
          "startDate": 1791158400,
          "timezone": {
            "id": 1001
          }
        }
      },
      {
        "scheduleName": "Synthetic Fulls",
        "forDatabasesOnly": false,
        "backupType": "SYNTHETICFULL",
        "policyId": 40,
        "scheduleId": 42,
        "schedulePattern": {
          "endDate": 0,
          "daysBetweenSyntheticFulls": 90,
          "calendarName": "Standard",
          "calendarId": 1,
          "scheduleFrequencyType": "AUTOMATIC",
          "jobStaggerDurationInMins": 0,
          "startTime": 0,
          "noOfTimes": 0,
          "startDate": 1791158400,
          "timezone": {
            "id": 1000
          }
        }
      },
      {
        "scheduleName": "",
        "forDatabasesOnly": true,
        "backupType": "TRANSACTIONLOG",
        "policyId": 39,
        "scheduleId": 40,
        "scheduleOption": {
          "logsDiskUtilizationPercent": 80,
          "logFilesThreshold": 50,
          "deleteLogsByAppLvlConfig": false,
          "commitFrequencyInHours": 8,
          "useDiskCacheForLogBackups": false
        },
        "schedulePattern": {
          "endDate": 0,
          "maxBackupIntervalInMins": 240,
          "calendarName": "Standard",
          "calendarId": 1,
          "scheduleFrequencyType": "AUTOMATIC",
          "jobStaggerDurationInMins": 0,
          "startTime": 0,
          "noOfTimes": 0,
          "startDate": 1791158400,
          "timezone": {
            "id": 1000
          }
        }
      }
    ]
  }
  ```

  </details>

## `list_server_plan_storage_policy` - GET /V5/ServerPlan/{planId}/StoragePolicy

> **SKIPPED** on this run: Commvault answered: 403

```python
cv.raw.server_plan.list_server_plan_storage_policy('1')
```

**On the wire**

- `GET /V5/ServerPlan/1/StoragePolicy` -> **403** (0.01 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

## `get_server_plan_backup_destination`

GET /V5/ServerPlan/{planId}/BackupDestination/{BackupDestinationId}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.server_plan.get_server_plan_backup_destination(...)
```

## `get_server_plan_storage_policy`

GET /V5/ServerPlan/{planId}/StoragePolicy/{storagePolicyId}

> **SKIPPED** on this run: Commvault answered: 403

```python
cv.raw.server_plan.get_server_plan_storage_policy('1', '4')
```

**On the wire**

- `GET /V5/ServerPlan/1/StoragePolicy` -> **403** (0.02 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

- `GET /V5/ServerPlan/1/StoragePolicy/4` -> **403** (0.01 s)

  <details><summary>Answer</summary>

  (no body)

  </details>
