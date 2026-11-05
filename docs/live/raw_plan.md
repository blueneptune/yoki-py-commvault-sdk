# `cv.raw.plan`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:37 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_plan_eligible` - GET /V2/Plan/Eligible

```python
cv.raw.plan.get_plan_eligible()
```

**On the wire**

- `GET /V2/Plan/Eligible` -> **200** (0.14 s)

  <details><summary>Answer</summary>

  ```json
  {
    "plans": [
      {
        "numCopies": 1,
        "type": 2,
        "subtype": 33554437,
        "numAssocEntities": 0,
        "parent": {},
        "plan": {
          "planSummary": ",AssociatedEntitiesCount:0",
          "planName": "bltlive-11051646-plan-2",
          "planId": 2
        }
      },
      {
        "numCopies": 1,
        "type": 2,
        "subtype": 33554437,
        "numAssocEntities": 0,
        "parent": {},
        "plan": {
          "planSummary": ",AssociatedEntitiesCount:0",
          "planName": "bltlive-11051831-plan",
          "planId": 3
        }
      },
      {
        "numCopies": 1,
        "type": 2,
        "subtype": 33554437,
        "numAssocEntities": 16,
        "rpoInMinutes": 1440,
        "parent": {},
        "plan": {
          "planSummary": "RPOHours:24,NumberOfCopies:1,PrimaryStorageRetention:1 Month,PrimaryStorageType:Disk,AssociatedEntitiesCount:16",
          "planName": "plan-01",
          "planId": 1
        }
      }
    ]
  }
  ```

  </details>

## `get_plan_ids` - GET /V4/PlanIds

```python
cv.raw.plan.get_plan_ids()
```

**On the wire**

- `GET /V4/PlanIds` -> **200** (0.10 s)

  <details><summary>Answer</summary>

  ```json
  {
    "entities": [
      {
        "name": "plan-01",
        "id": 1
      },
      {
        "name": "bltlive-11051831-plan-2",
        "id": 3
      }
    ]
  }
  ```

  </details>

## `list_plan` - GET /Plan

```python
cv.raw.plan.list_plan()
```

**On the wire**

- `GET /Plan` -> **200** (0.17 s)

  <details><summary>Answer</summary>

  ```json
  {
    "plans": [
      {
        "numCopies": 1,
        "description": "plan-01",
        "type": 2,
        "numDevices": 0,
        "storageTarget": "storage-pool-01",
        "subtype": 33554437,
        "isElastic": false,
        "numAssocEntities": 16,
        "searchType": 0,
        "restrictions": 1,
        "numCompanies": 0,
        "planStatusFlag": 0,
        "rpoInMinutes": 0,
        "isEntityExtractionEnabled": false,
        "numUsers": 0,
        "backupInRegion": false,
        "supportedWorkloads": {},
        "storage": {
          "storagePolicy": {
            "storagePolicyId": 3
          },
          "copy": [
            {
              "copyType": 1,
              "deviceType": 1,
              "active": 1,
              "isArchiveStorage": false,
              "issubclient-01": 1,
              "isSnapCopy": 0,
              "dataRetentionLockDays": 0,
              "isMirrorCopy": 0,
              "wormStorageFlag": 96,
              "poolRetentionPeriodDays": -1,
              "isSourceBackupCopy": 0,
              "storageClass": "",
              "copyPrecedence": 1,
              "storagePoolType": 1,
              "isSourceCatalog": 0,
              "storageType": 1,
              "dedupeFlags": {
                "enableDASHFull": 1,
                "pauseAndRecoverCurrentDDB": 1,
                "useGlobalDedupStore": 1,
                "automaticallyPauseAndRecoverDDB": 1,
                "enableDeduplication": 1,
                "enableClientSideDedup": 1
              },
              "retentionRules": {
                "retainBackupDataForCycles": 1,
                "jobs": 0,
                "retainArchiverDataForDays": -1,
                "retainBackupDataForDays": 30,
                "retentionFlags": {
                  "enableDataAging": 1,
                  "jobBasedRetention": 0
                }
              },
              "StoragePolicyCopy": {
                "copyId": 2,
                "copyName": "Primary"
              },
              "extendedFlags": {
                "overRideGACPRetention": 1
              },
              "region": {
                "displayName": "",
                "regionName": "",
                "regionId": 0
              },
              "drivePool": {
                "drivePoolId": 1,
                "drivePoolName": "DrivePool(commserve-02)1"
              },
              "copyFlags": {},
              "library": {
                "libraryName": "storage-pool-01",
                "libraryId": 1
              },
              "startTime": {
                "time": -1
              },
              "useGlobalPolicy": {
                "storagePolicyName": "storage-pool-01",
                "storagePolicyId": 2
              }
            }
          ]
        },
        "permissions": [
          {
            "permissionId": 31
          }
        ],
        "targetApps": [],
        "plan": {
          "planType": 2,
          "planSummary": "RPOHours:0,NumberOfCopies:1,AssociatedEntitiesCount:16,PrimaryStorageType:Disk",
          "planName": "plan-01",
          "planSubtype": 33554437,
          "_type_": 158,
          "planId": 1
        },
        "planOwner": {
          "userName": "user-38",
          "userId": 1,
          "_type_": 13
        }
      },
      {
        "numCopies": 1,
        "description": "bltlive-11051831-plan",
        "type": 2,
        "numDevices": 0,
        "storageTarget": "storage-pool-01",
        "subtype": 33554437,
        "isElastic": false,
        "numAssocEntities": 0,
        "searchType": 0,
        "restrictions": 1,
        "numCompanies": 0,
        "planStatusFlag": 0,
        "rpoInMinutes": 0,
        "isEntityExtractionEnabled": false,
        "numUsers": 0,
        "backupInRegion": false,
        "supportedWorkloads": {},
        "storage": {
          "storagePolicy": {
            "storagePolicyId": 6
          },
          "copy": [
            {
              "copyType": 1,
              "deviceType": 1,
              "active": 1,
              "isArchiveStorage": false,
              "issubclient-01": 1,
              "isSnapCopy": 0,
              "dataRetentionLockDays": 0,
              "isMirrorCopy": 0,
              "wormStorageFlag": 96,
              "poolRetentionPeriodDays": -1,
              "isSourceBackupCopy": 0,
              "storageClass": "",
              "copyPrecedence": 1,
              "storagePoolType": 1,
              "isSourceCatalog": 0,
              "storageType": 1,
              "dedupeFlags": {
                "enableDASHFull": 1,
                "pauseAndRecoverCurrentDDB": 1,
                "useGlobalDedupStore": 1,
                "automaticallyPauseAndRecoverDDB": 1,
                "enableDeduplication": 1,
                "enableClientSideDedup": 1
              },
              "retentionRules": {
                "retainBackupDataForCycles": 1,
                "jobs": 0,
                "retainArchiverDataForDays": -1,
                "retainBackupDataForDays": 7,
                "retentionFlags": {
                  "enableDataAging": 1,
                  "jobBasedRetention": 0
                }
              },
              "StoragePolicyCopy": {
                "copyId": 5,
                "copyName": "Primary"
              },
              "extendedFlags": {
                "overRideGACPRetention": 1
              },
              "region": {
                "displayName": "",
                "regionName": "",
                "regionId": 0
              },
              "drivePool": {
                "drivePoolId": 1,
                "drivePoolName": "DrivePool(commserve-02)1"
              },
              "copyFlags": {},
              "library": {
                "libraryName": "storage-pool-01",
                "libraryId": 1
              },
              "startTime": {
                "time": -1
              },
              "useGlobalPolicy": {
                "storagePolicyName": "storage-pool-01",
                "storagePolicyId": 2
              }
            }
          ]
        },
        "permissions": [
          {
            "permissionId": 31
          }
        ],
        "targetApps": [],
        "plan": {
          "planType": 2,
          "planSummary": "RPOHours:0,NumberOfCopies:1,AssociatedEntitiesCount:0,PrimaryStorageType:Disk",
          "planName": "bltlive-11051831-plan-2",
          "planSubtype": 33554437,
          "_type_": 158,
          "planId": 3
        },
        "planOwner": {
          "userName": "Administrator",
          "userId": 2,
          "_type_": 13
        }
      }
    ]
  }
  ```

  </details>

## `list_plan_summary` - GET /V4/Plan/Summary

```python
cv.raw.plan.list_plan_summary()
```

**On the wire**

- `GET /V4/Plan/Summary` -> **200** (0.20 s)

  <details><summary>Answer</summary>

  ```json
  {
    "plansCount": 2,
    "plans": [
      {
        "planType": "Server",
        "searchType": "METADATA",
        "derivable": false,
        "description": "plan-01",
        "RPO": 0,
        "associatedEntities": 16,
        "numberOfCopies": 1,
        "status": "ENABLED",
        "plan": {
          "name": "plan-01",
          "id": 1
        }
      },
      {
        "planType": "Server",
        "searchType": "METADATA",
        "derivable": false,
        "description": "bltlive-11051831-plan",
        "RPO": 0,
        "associatedEntities": 0,
        "numberOfCopies": 1,
        "status": "ENABLED",
        "plan": {
          "name": "bltlive-11051831-plan-2",
          "id": 3
        }
      }
    ]
  }
  ```

  </details>

## `list_plan_v2` - GET /v2/Plan

```python
cv.raw.plan.list_plan_v2()
```

**On the wire**

- `GET /v2/Plan` -> **200** (0.13 s)

  <details><summary>Answer</summary>

  ```json
  {
    "plans": [
      {
        "numCopies": 1,
        "description": "plan-01",
        "type": 2,
        "numDevices": 0,
        "storageTarget": "storage-pool-01",
        "subtype": 33554437,
        "isElastic": false,
        "numAssocEntities": 16,
        "searchType": 0,
        "restrictions": 1,
        "numCompanies": 0,
        "planStatusFlag": 0,
        "rpoInMinutes": 0,
        "isEntityExtractionEnabled": false,
        "numUsers": 0,
        "backupInRegion": false,
        "supportedWorkloads": {},
        "storage": {
          "storagePolicy": {
            "storagePolicyId": 3
          },
          "copy": [
            {
              "copyType": 1,
              "deviceType": 1,
              "active": 1,
              "isArchiveStorage": false,
              "issubclient-01": 1,
              "isSnapCopy": 0,
              "dataRetentionLockDays": 0,
              "isMirrorCopy": 0,
              "wormStorageFlag": 96,
              "poolRetentionPeriodDays": -1,
              "isSourceBackupCopy": 0,
              "storageClass": "",
              "copyPrecedence": 1,
              "storagePoolType": 1,
              "isSourceCatalog": 0,
              "storageType": 1,
              "dedupeFlags": {
                "enableDASHFull": 1,
                "pauseAndRecoverCurrentDDB": 1,
                "useGlobalDedupStore": 1,
                "automaticallyPauseAndRecoverDDB": 1,
                "enableDeduplication": 1,
                "enableClientSideDedup": 1
              },
              "retentionRules": {
                "retainBackupDataForCycles": 1,
                "jobs": 0,
                "retainArchiverDataForDays": -1,
                "retainBackupDataForDays": 30,
                "retentionFlags": {
                  "enableDataAging": 1,
                  "jobBasedRetention": 0
                }
              },
              "StoragePolicyCopy": {
                "copyId": 2,
                "copyName": "Primary"
              },
              "extendedFlags": {
                "overRideGACPRetention": 1
              },
              "region": {
                "displayName": "",
                "regionName": "",
                "regionId": 0
              },
              "drivePool": {
                "drivePoolId": 1,
                "drivePoolName": "DrivePool(commserve-02)1"
              },
              "copyFlags": {},
              "library": {
                "libraryName": "storage-pool-01",
                "libraryId": 1
              },
              "startTime": {
                "time": -1
              },
              "useGlobalPolicy": {
                "storagePolicyName": "storage-pool-01",
                "storagePolicyId": 2
              }
            }
          ]
        },
        "permissions": [
          {
            "permissionId": 31
          }
        ],
        "targetApps": [],
        "plan": {
          "planType": 2,
          "planSummary": "RPOHours:0,NumberOfCopies:1,AssociatedEntitiesCount:16,PrimaryStorageType:Disk",
          "planName": "plan-01",
          "planSubtype": 33554437,
          "_type_": 158,
          "planId": 1
        },
        "planOwner": {
          "userName": "user-38",
          "userId": 1,
          "_type_": 13
        }
      },
      {
        "numCopies": 1,
        "description": "bltlive-11051831-plan",
        "type": 2,
        "numDevices": 0,
        "storageTarget": "storage-pool-01",
        "subtype": 33554437,
        "isElastic": false,
        "numAssocEntities": 0,
        "searchType": 0,
        "restrictions": 1,
        "numCompanies": 0,
        "planStatusFlag": 0,
        "rpoInMinutes": 0,
        "isEntityExtractionEnabled": false,
        "numUsers": 0,
        "backupInRegion": false,
        "supportedWorkloads": {},
        "storage": {
          "storagePolicy": {
            "storagePolicyId": 6
          },
          "copy": [
            {
              "copyType": 1,
              "deviceType": 1,
              "active": 1,
              "isArchiveStorage": false,
              "issubclient-01": 1,
              "isSnapCopy": 0,
              "dataRetentionLockDays": 0,
              "isMirrorCopy": 0,
              "wormStorageFlag": 96,
              "poolRetentionPeriodDays": -1,
              "isSourceBackupCopy": 0,
              "storageClass": "",
              "copyPrecedence": 1,
              "storagePoolType": 1,
              "isSourceCatalog": 0,
              "storageType": 1,
              "dedupeFlags": {
                "enableDASHFull": 1,
                "pauseAndRecoverCurrentDDB": 1,
                "useGlobalDedupStore": 1,
                "automaticallyPauseAndRecoverDDB": 1,
                "enableDeduplication": 1,
                "enableClientSideDedup": 1
              },
              "retentionRules": {
                "retainBackupDataForCycles": 1,
                "jobs": 0,
                "retainArchiverDataForDays": -1,
                "retainBackupDataForDays": 7,
                "retentionFlags": {
                  "enableDataAging": 1,
                  "jobBasedRetention": 0
                }
              },
              "StoragePolicyCopy": {
                "copyId": 5,
                "copyName": "Primary"
              },
              "extendedFlags": {
                "overRideGACPRetention": 1
              },
              "region": {
                "displayName": "",
                "regionName": "",
                "regionId": 0
              },
              "drivePool": {
                "drivePoolId": 1,
                "drivePoolName": "DrivePool(commserve-02)1"
              },
              "copyFlags": {},
              "library": {
                "libraryName": "storage-pool-01",
                "libraryId": 1
              },
              "startTime": {
                "time": -1
              },
              "useGlobalPolicy": {
                "storagePolicyName": "storage-pool-01",
                "storagePolicyId": 2
              }
            }
          ]
        },
        "permissions": [
          {
            "permissionId": 31
          }
        ],
        "targetApps": [],
        "plan": {
          "planType": 2,
          "planSummary": "RPOHours:0,NumberOfCopies:1,AssociatedEntitiesCount:0,PrimaryStorageType:Disk",
          "planName": "bltlive-11051831-plan-2",
          "planSubtype": 33554437,
          "_type_": 158,
          "planId": 3
        },
        "planOwner": {
          "userName": "Administrator",
          "userId": 2,
          "_type_": 13
        }
      }
    ]
  }
  ```

  </details>

## `get_plan_access_policies` - GET /v2/Plan/{PlanId}/AccessPolicies

> **SKIPPED** on this run: Commvault answered: 500

```python
cv.raw.plan.get_plan_access_policies('3')
```

**On the wire**

- `GET /v2/Plan/3/AccessPolicies` -> **500** (0.28 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

## `get_plan_alerts` - GET /v2/Plan/{PlanId}/Alerts

```python
cv.raw.plan.get_plan_alerts('3')
```

**On the wire**

- `GET /v2/Plan/3/Alerts` -> **200** (0.21 s)

  <details><summary>Answer</summary>

  ```json
  {}
  ```

  </details>

## `get_plan_associated_entities` - GET /v2/Plan/{PlanId}/AssociatedEntities

```python
cv.raw.plan.get_plan_associated_entities('3')
```

**On the wire**

- `GET /v2/Plan/3/AssociatedEntities` -> **200** (0.09 s)

  <details><summary>Answer</summary>

  ```json
  {
    "associatedEntitiesCount": {
      "snapSubclients": 0
    }
  }
  ```

  </details>

## `get_plan_backup_destination` - GET /V4/Plan/BackupDestination/{BackupDestinationId}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.plan.get_plan_backup_destination(...)
```

## `get_plan_backup_destination_clients`

GET /V4/Plan/BackupDestination/{backupDestinationId}/Clients

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.plan.get_plan_backup_destination_clients(...)
```

## `get_plan_backup_destination_jobs`

GET /V4/Plan/BackupDestination/{backupDestinationId}/Jobs

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.plan.get_plan_backup_destination_jobs(...)
```

## `get_plan_by_plan_id` - GET /v2/Plan/{PlanId}

```python
cv.raw.plan.get_plan_by_plan_id('3')
```

**On the wire**

- `GET /v2/Plan/3` -> **200** (0.17 s)

  <details><summary>Answer</summary>

  ```json
  {
    "plan": {
      "definesTIPolicy": {
        "definesEntity": false,
        "overrideEntity": 0
      },
      "storageResourcePoolMap": [
        {
          "storage": {
            "storagePoolName": "storage-pool-01",
            "storagePoolId": 2
          }
        }
      ],
      "definesStorage": {
        "definesEntity": true,
        "overrideEntity": 0
      },
      "securityAssociations": {
        "ownerAssociations": {},
        "tagWithCompany": {
          "providerId": 0,
          "providerDomainName": "Commcell"
        }
      },
      "featureInfo": {
        "edgedriveInfo": {
          "enableNotificationsForShares": false,
          "auditDriveActivities": false,
          "edgeDriveAssociations": {}
        },
        "definesEdgeDriveInfo": {
          "definesEntity": false,
          "overrideEntity": 2
        }
      },
      "inheritance": {
        "isSealed": true,
        "enforcedEntities": [
          8,
          128,
          4096
        ]
      },
      "storage": {
        "issubclient-01CopyDistributedStorage": false,
        "storagePolicy": {
          "storagePolicyName": "bltlive-11051831-plan-2",
          "storagePolicyId": 6
        }
      },
      "definesSchedule": {
        "definesEntity": false,
        "overrideEntity": 0
      },
      "laptop": {
        "dlpFeature": false,
        "edgeDriveFeature": false,
        "archivingFeature": false,
        "accessPolicies": {
          "categoryPermission": {}
        },
        "definesAccessPolicies": {
          "definesEntity": false,
          "overrideEntity": 0
        },
        "content": {
          "definesSubclientContentMac": {
            "definesEntity": false,
            "overrideEntity": 0
          },
          "definesSubclientContentLin": {
            "definesEntity": false,
            "overrideEntity": 0
          },
          "definesSubclientWin": {
            "definesEntity": false,
            "overrideEntity": 0
          },
          "definesSubclientArcRulesWin": {
            "definesEntity": false,
            "overrideEntity": 0
          },
          "definesSubclientRetentionWin": {
            "definesEntity": false,
            "overrideEntity": 0
          },
          "definesSubclientArcRulesLin": {
            "definesEntity": false,
            "overrideEntity": 0
          },
          "definesSubclientRetentionLin": {
            "definesEntity": false,
            "overrideEntity": 0
          },
          "definesSubclientContentWin": {
            "definesEntity": false,
            "overrideEntity": 0
          },
          "definesSubclientRetentionMac": {
            "definesEntity": false,
            "overrideEntity": 0
          },
          "definesSubclientMac": {
            "definesEntity": false,
            "overrideEntity": 0
          },
          "definesSubclientLin": {
            "definesEntity": false,
            "overrideEntity": 0
          }
        },
        "users": {}
      },
      "operationWindow": {
        "ruleId": 0
      },
      "replicationTargets": {},
      "database": {
        "slaInMinutes": 0,
        "rpoInMinutes": 0,
        "daysBetweenAutoConvertBackup": 7,
        "scheduleLog": {},
        "storageLog": {},
        "definesScheduleLog": {
          "definesEntity": false,
          "overrideEntity": 0
        },
        "definesStorageLog": {
          "definesEntity": false,
          "overrideEntity": 0
        }
      },
      "options": {
        "optimizeForInstantClone": false,
        "threatAnalysisFlags": 0,
        "o365PlanTier": 20,
        "forcedArchiving": false,
        "bCloudModeEnabled": false,
        "edgeDriveQuota": 100,
        "supportedWorkloads": {},
        "encryptionInfo": {
          "encryptKeyLength": 128,
          "directMediaAccess": 0,
          "cipherType": 2,
          "encryptionSettings": 3
        },
        "ownerPermissions": {},
        "planActivityControl": {},
        "slaOptions": {
          "inheritedSLA": {
            "slaDays": 7,
            "entityType": 1
          }
        },
        "autoRetireDevices": {
          "retireDevicesAfterDays": 183,
          "forceDeleteDevicesAfterDays": 365
        }
      },
      "definition": {
        "possible": [
          1,
          2,
          4,
          "... 45 more"
        ],
        "required": [
          1
        ]
      },
      "storageProps": {},
      "definesEEPolicy": {
        "definesEntity": false,
        "overrideEntity": 0
      },
      "summary": {
        "planTier": 0,
        "type": 2,
        "slaInterval": 0,
        "numDevices": 0,
        "subtype": 33554437,
        "isElastic": false,
        "isGlobalConfigTemplate": false,
        "slaInMinutes": 0,
        "restrictions": 1,
        "isS3Plan": false,
        "planStatusFlag": 0,
        "rpoInMinutes": 0,
        "numUsers": 0,
        "addons": {
          "snapStatus": 2,
          "filesystem": false
        },
        "permissions": [
          {
            "permissionId": 1
          },
          {
            "permissionId": 2
          },
          {
            "permissionId": 3
          },
          "... 55 more"
        ],
        "plan": {
          "planType": 2,
          "GUID": "75EAE7A8-E773-4567-8681-1B30D84F80F4",
          "planName": "bltlive-11051831-plan-2",
          "planSubtype": 33554437,
          "_type_": 158,
          "planId": 3,
          "entityInfo": {
            "companyId": 0,
            "companyName": ""
          }
        },
        "planOwner": {
          "userName": "Administrator",
          "userId": 2,
          "_type_": 13
        }
      },
      "fullOperationWindow": {
        "ruleId": 0
      },
      "definesArchivingServicePolicy": {
        "definesEntity": false,
        "overrideEntity": 0
      },
      "alerts": {},
      "schedule": {},
      "indexCopy": {
        "schedule": {
          "task": {}
        }
      },
      "office365Info": {
        "o365Exchange": {
          "definesMBRetention": {
            "definesEntity": false,
            "overrideEntity": 0
          },
          "definesMBCleanup": {
            "definesEntity": false,
            "overrideEntity": 0
          },
          "definesMBArchiving": {
            "definesEntity": false,
            "overrideEntity": 0
          }
        },
        "o365CloudOffice": {
          "definesCABackup": {
            "definesEntity": false,
            "overrideEntity": 0
          },
          "definesCARetention": {
            "definesEntity": false,
            "overrideEntity": 0
          },
          "definesCACleanup": {
            "definesEntity": false,
            "overrideEntity": 0
          }
        }
      },
      "parentInheritSettings": {
        "schedule": {
          "definesEntity": false
        },
        "storage": {
          "definesEntity": false
        },
        "content": {
          "definesEntity": false
        }
      },
      "associatedEntitiesCount": {
        "snapSubclients": 0
      },
      "eDiscoveryInfo": {
        "definesAnalyticsIndexServer": {
          "definesEntity": false,
          "overrideEntity": 0
        },
        "definesContentAnalyzerClient": {
          "definesEntity": false,
          "overrideEntity": 0
        }
      },
      "exchange": {
        "definesMBRetention": {
          "definesEntity": false,
          "overrideEntity": 0
        },
        "definesMBCleanup": {
          "definesEntity": false,
          "overrideEntity": 0
        },
        "definesMBArchiving": {
          "definesEntity": false,
          "overrideEntity": 0
        },
        "definesMBJournal": {
          "definesEntity": false,
          "overrideEntity": 0
        }
      },
      "definesCIPolicy": {
        "definesEntity": false,
        "overrideEntity": 0
      },
      "snapInfo": {
        "backupCopyRPO": 240,
        "snapTask": {}
      }
    }
  }
  ```

  </details>

## `get_plan_features` - GET /v2/Plan/{PlanId}/Features

```python
cv.raw.plan.get_plan_features('3')
```

**On the wire**

- `GET /v2/Plan/3/Features` -> **200** (0.17 s)

  <details><summary>Answer</summary>

  ```json
  {}
  ```

  </details>

## `get_plan_incremental_plan` - GET /V5/Plan/{planId}/IncrementalPlan

> **SKIPPED** on this run: Commvault answered: 403

```python
cv.raw.plan.get_plan_incremental_plan('1')
```

**On the wire**

- `GET /V5/Plan/1/IncrementalPlan` -> **403** (0.01 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

## `get_plan_log_plan` - GET /V5/Plan/{planId}/LogPlan

> **SKIPPED** on this run: Commvault answered: 403

```python
cv.raw.plan.get_plan_log_plan('1')
```

**On the wire**

- `GET /V5/Plan/1/LogPlan` -> **403** (0.01 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

## `get_plan_media_agents` - GET /V4/Plan/{planId}/MediaAgents

```python
cv.raw.plan.get_plan_media_agents('1')
```

**On the wire**

- `GET /V4/Plan/1/MediaAgents` -> **200** (0.07 s)

  <details><summary>Answer</summary>

  ```json
  {
    "mediaAgentsList": [
      {
        "hostname": "commserve-02",
        "clientName": "commserve-02",
        "regionName": "",
        "name": "commserve-02",
        "offlineSince": 0,
        "id": 2,
        "isPackageInstalled": true,
        "isServiceEnabled": false,
        "s3EndpointProperties": {
          "offlineSince": 0,
          "s3Ports": "",
          "enabled": false
        }
      }
    ]
  }
  ```

  </details>

## `get_plan_operations` - GET /v2/Plan/{PlanId}/Operations

> **SKIPPED** on this run: Commvault answered: 400

```python
cv.raw.plan.get_plan_operations('3')
```

**On the wire**

- `GET /v2/Plan/3/Operations` -> **400** (0.06 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

## `get_plan_summary` - GET /v4/Plan/Summary/{planId}

```python
cv.raw.plan.get_plan_summary('1')
```

**On the wire**

- `GET /v4/Plan/Summary/1` -> **200** (0.24 s)

  <details><summary>Answer</summary>

  ```json
  {
    "planType": "Server",
    "serverPlan": {
      "rpo": {
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
                  "applyRetentionOn": "PRIMARY_COPY"
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
      },
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
  }
  ```

  </details>

## `get_plan_backup_destination_associations`

GET /V4/Plan/{planId}/BackupDestination/{backupDestinationId}/Associations

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.plan.get_plan_backup_destination_associations(...)
```

## `get_plan_by_plan_id_entity_name` - GET /v2/Plan/{PlanId}/{entityName}

```python
cv.raw.plan.get_plan_by_plan_id_entity_name('3', '2')
```

**On the wire**

- `GET /v2/Plan/3/2` -> **200** (0.26 s)

  <details><summary>Answer</summary>

  ```json
  {
    "definesSubclientContentMac": {
      "definesEntity": false,
      "overrideEntity": 0
    },
    "definesSubclientContentLin": {
      "definesEntity": false,
      "overrideEntity": 0
    },
    "definesSubclientWin": {
      "definesEntity": false,
      "overrideEntity": 0
    },
    "definesSubclientArcRulesWin": {
      "definesEntity": false,
      "overrideEntity": 0
    },
    "definesSubclientRetentionWin": {
      "definesEntity": false,
      "overrideEntity": 0
    },
    "definesSubclientArcRulesLin": {
      "definesEntity": false,
      "overrideEntity": 0
    },
    "definesSubclientRetentionLin": {
      "definesEntity": false,
      "overrideEntity": 0
    },
    "definesSubclientContentWin": {
      "definesEntity": false,
      "overrideEntity": 0
    },
    "definesSubclientRetentionMac": {
      "definesEntity": false,
      "overrideEntity": 0
    },
    "definesSubclientMac": {
      "definesEntity": false,
      "overrideEntity": 0
    },
    "definesSubclientLin": {
      "definesEntity": false,
      "overrideEntity": 0
    }
  }
  ```

  </details>
