# `cv.raw.storage`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 16:43 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_drive_controller` - GET /DriveController

```python
cv.raw.storage.get_drive_controller()
```

**On the wire**

- `GET /DriveController` -> **200** (0.18 s)

  <details><summary>Answer</summary>

  ```json
  {
    "mountPathInfo": {
      "mediaAgents": "",
      "mountPathUsedForLogCaching": false,
      "dataServerType": 0,
      "mountPathType": 4294967295,
      "jobIds": "",
      "preventDataBlockReferences": false,
      "driveId": 0,
      "disabledForNewWrite": false,
      "libraryVendorId": -1,
      "mountPathId": 0,
      "mountPathName": "mount-path-01",
      "enabledMP": false,
      "status": "Offline (Device is not enabled or there are no controller/share paths that are online.)",
      "rpStoreLibraryInfo": {
        "copyId": 0,
        "maxPairsPerRPStore": 0,
        "archGroupId": 0,
        "flags": 0,
        "pairCount": 0,
        "commCellId": 0,
        "minSpacePerRPStoreGB": 0,
        "origRPStoreId": 0,
        "rpStoreId": 0,
        "subclient-01HostId": 0,
        "maxSpacePerRPStoreGB": 0,
        "intervalWindow": {}
      },
      "mountPathSummary": {
        "libraryName": "mount-path-01",
        "avgMediaConsumedPerDay": 0,
        "totalDeduplicationAppSize": 0,
        "totalUsableFreeSpace": -1,
        "avgDataWrittenPerDayMB": 0,
        "totalReserveSpaceMB": 0,
        "lastNumDays": 9,
        "libraryId": 0,
        "maxDataToWriteMB": 0,
        "totalSpace": -1,
        "totalValidData": 0,
        "estimatedSpaceRunoutDays": -1,
        "warningWaterMark": -1,
        "totalFreeSpace": -1,
        "avgMediaFreedPerDay": 0,
        "totalDataWritten": -1,
        "avgCapacityFreedMB": 0,
        "lowWaterMark": -1,
        "numberOfWriters": 0,
        "attribute": 0,
        "totalAppSize": 0,
        "totalEstMediaSize": 0,
        "totalDeduplicationDataWritten": -1
      },
      "deviceInfo": {
        "name": "",
        "id": 0
      },
      "metallicStorageInfo": {},
      "region": {
        "_type_": 102
      },
      "savedCredential": "<masked>"
    }
  }
  ```

  </details>

## `get_media_agent_for_library` - GET /MediaAgentForLibrary

> **SKIPPED** on this run: Commvault answered: 403

```python
cv.raw.storage.get_media_agent_for_library()
```

**On the wire**

- `GET /MediaAgentForLibrary` -> **403** (0.01 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

## `get_mount_path_content` - GET /V4/MountPath/Content

> **SKIPPED** on this run: not swept: starts work or returns a file

```python
cv.raw.storage.get_mount_path_content(...)
```

## `get_storage_policy_list_associated_to_media_agent`

GET /StoragePolicyListAssociatedToMediaAgent

> **SKIPPED** on this run: Commvault answered: 403

```python
cv.raw.storage.get_storage_policy_list_associated_to_media_agent()
```

**On the wire**

- `GET /StoragePolicyListAssociatedToMediaAgent` -> **403** (0.01 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

## `list_library` - GET /Library

```python
cv.raw.storage.list_library()
```

**On the wire**

- `GET /Library` -> **200** (0.12 s)

  <details><summary>Answer</summary>

  ```json
  {
    "response": [
      {
        "entityInfo": {
          "name": "storage-pool-01",
          "id": 1
        }
      }
    ]
  }
  ```

  </details>

## `list_media_agent` - GET /MediaAgent

```python
cv.raw.storage.list_media_agent()
```

**On the wire**

- `GET /MediaAgent` -> **200** (0.18 s)

  <details><summary>Answer</summary>

  ```json
  {
    "response": [
      {
        "entityInfo": {
          "name": "commserve-02",
          "id": 2
        }
      }
    ]
  }
  ```

  </details>

## `list_media_agents` - GET /v2/MediaAgents

```python
cv.raw.storage.list_media_agents()
```

**On the wire**

- `GET /v2/MediaAgents` -> **200** (0.21 s)

  <details><summary>Answer</summary>

  ```json
  {
    "mediaAgentList": [
      {
        "isDDBSupported": true,
        "offlineReason": 0,
        "description": "",
        "rolesBitMask": 527,
        "status": 1,
        "mediaAgentProps": {
          "pushMA": false,
          "isPreConfigured": false,
          "isUnlicensedMA": "<masked>",
          "isVirtualsClient": false
        },
        "osInfo": {
          "Type": "Windows",
          "osId": 210,
          "OsDisplayInfo": {
            "OSName": "Windows Server 2025 Datacenter"
          }
        },
        "versionInfo": {
          "UpdateStatus": 0,
          "GalaxyBuildNumber": "11",
          "ReleaseStatus": 0,
          "GalaxyRelease": {
            "ReleaseString": "11 SP46.30",
            "_type_": 58,
            "ReleaseID": 16
          }
        },
        "powerManagementInfo": {
          "powerStatus": 0,
          "isPowerMgmtAllowedCheck": true,
          "isPowerMgmtSupported": false,
          "isPowerManagementEnabled": false
        },
        "mediaAgent": {
          "displayName": "commserve-02",
          "mediaAgentId": 2,
          "_type_": 11,
          "mediaAgentName": "commserve-02",
          "netHostName": "commserve-02"
        },
        "region": {
          "displayName": "North America",
          "regionName": "North America",
          "_type_": 102,
          "regionId": 5
        }
      }
    ]
  }
  ```

  </details>

## `list_storage_policy` - GET /V2/StoragePolicy

```python
cv.raw.storage.list_storage_policy()
```

**On the wire**

- `GET /V2/StoragePolicy` -> **200** (0.17 s)

  <details><summary>Answer</summary>

  ```json
  {
    "policies": [
      {
        "numberOfStreams": 50,
        "storagePolicy": {
          "storagePolicyName": "plan-01",
          "storagePolicyId": 3
        }
      },
      {
        "numberOfStreams": 3,
        "storagePolicy": {
          "storagePolicyName": "storage-policy-01",
          "storagePolicyId": 4
        }
      }
    ]
  }
  ```

  </details>

## `list_storage_pool` - GET /StoragePool

```python
cv.raw.storage.list_storage_pool()
```

**On the wire**

- `GET /StoragePool` -> **200** (0.15 s)

  <details><summary>Answer</summary>

  ```json
  {
    "storagePoolList": [
      {
        "totalUsableFreeSpace": 1003792,
        "HSStoragePoolHealth": -1,
        "cloudStorageClassName": "",
        "numberOfNodes": 1,
        "poolRetentionPeriodDays": -1,
        "sizeOnDisk": 24144,
        "HSStoragePoolType": -1,
        "totalCapacity": 1048572,
        "wormStoragePoolFlag": 96,
        "reserved1": 1,
        "cloudStorageClassNumber": -1,
        "isArchiveStorage": 0,
        "libraryVendorType": 1,
        "totalFreeSpace": 1024272,
        "storagePoolType": 1,
        "storageSubType": 0,
        "storageType": 1,
        "status": "Online",
        "statusCode": 0,
        "dataRetentionLockDays": 0,
        "storageTags": {},
        "libraryList": [
          {
            "_type_": 9,
            "libraryId": 1
          }
        ],
        "storagePool": {
          "_type_": 28,
          "clientGroupId": 2,
          "clientGroupName": "storage-pool-01"
        },
        "storagePolicyEntity": {
          "_type_": 17,
          "storagePolicyName": "storage-pool-01",
          "storagePolicyId": 2
        },
        "storagePoolEntity": {
          "storagePoolName": "storage-pool-01",
          "_type_": 160,
          "storagePoolId": 2
        }
      }
    ]
  }
  ```

  </details>

## `get_ddb_information` - GET /DDBInformation/{storeID}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.storage.get_ddb_information(...)
```

## `get_library` - GET /Library/{LibraryId}

```python
cv.raw.storage.get_library('1')
```

**On the wire**

- `GET /Library/1` -> **200** (0.14 s)

  <details><summary>Answer</summary>

  ```json
  {
    "libraryInfo": {
      "lowWaterMarkPercentage": 0,
      "subclient-01MediaTypeId": 0,
      "description": "",
      "libraryUsedForLogCaching": false,
      "extendedAttributes": 262145,
      "manufacturer": "Disk",
      "storagePoolType": 1,
      "libraryVendorId": 0,
      "warningWaterMarkPercentage": 0,
      "database-03": "Disk",
      "libraryType": 3,
      "status": "",
      "libraryControllerList": [
        {
          "isSoftStateOn": true,
          "isEnabled": true,
          "SCSIId": "MAGNETIC",
          "isActive": true,
          "libControllerType": 4,
          "host": {
            "name": "commserve-02",
            "id": 2
          },
          "libraryController": {
            "name": "LmsLibrary1_1",
            "id": 1
          },
          "ndmpClient": {
            "_type_": 3
          }
        }
      ],
      "tapeLibSummary": {
        "numOfCleaningMedia": 0,
        "offlineReason": "",
        "numOfIESlots": 0,
        "lastDayThroughput": "",
        "isOnline": "",
        "numOfIESlotOccupied": 0,
        "lastRestoreTime": "",
        "overwriteRetentionTime": 0,
        "numOfActiveMedia": 0,
        "numOfSpareMedia": 0,
        "vendor": "",
        "numOfRegSlots": 0,
        "database-03": "",
        "numOfMedia": 0,
        "attribute": 0,
        "numOfDrivesOffline": 0,
        "firmwareRevision": "",
        "associatedMediaAgents": "",
        "controller": "",
        "bytesBackedupInLast24H": "",
        "serialNumber": "",
        "numOfAgedMedia": 0,
        "barcodePattern": "",
        "numOfAssignedMedia": 0,
        "numOfAppendableMedia": 0,
        "numOfRegSlotOccupied": 0,
        "backupReservations": 0,
        "numOfSlots": 0,
        "bytesBackedupInLast1H": "",
        "lastBackupTime": "",
        "lastHourThroughput": "",
        "numOfDrives": 0,
        "barcodeReader": "",
        "numOfMediaExporting": 0,
        "auxiliaryCopyWriteReservations": 0,
        "isEnabled": 0,
        "numOfFullMedia": 0,
        "numOfSpareMediaInLib": 0,
        "totalNumberOfWriteReservations": 0,
        "libraryAttribute": 0,
        "status": 0
      },
      "MountPathList": [
        {
          "mediaAgents": "",
          "mountPathUsedForLogCaching": false,
          "dataServerType": 0,
          "mountPathType": 4,
          "jobIds": "",
          "preventDataBlockReferences": false,
          "driveId": 0,
          "disabledForNewWrite": false,
          "libraryVendorId": 0,
          "mountPathId": 1,
          "mountPathName": "mount-path-02",
          "enabledMP": true,
          "status": "Ready",
          "rpStoreLibraryInfo": {
            "copyId": 0,
            "maxPairsPerRPStore": 0,
            "archGroupId": 0,
            "flags": 0,
            "pairCount": 0,
            "commCellId": 0,
            "minSpacePerRPStoreGB": 0,
            "origRPStoreId": 0,
            "rpStoreId": 0,
            "subclient-01HostId": 0,
            "maxSpacePerRPStoreGB": 0,
            "intervalWindow": {}
          },
          "mountPathSummary": {
            "libraryName": "storage-pool-01",
            "avgMediaConsumedPerDay": 0,
            "totalDeduplicationAppSize": 0,
            "totalUsableFreeSpace": 0,
            "avgDataWrittenPerDayMB": 0,
            "totalReserveSpaceMB": 0,
            "lastNumDays": 0,
            "libraryId": 1,
            "maxDataToWriteMB": 0,
            "totalSpace": 0,
            "totalValidData": 0,
            "estimatedSpaceRunoutDays": 0,
            "warningWaterMark": 0,
            "totalFreeSpace": 0,
            "avgMediaFreedPerDay": 0,
            "totalDataWritten": 0,
            "avgCapacityFreedMB": 0,
            "lowWaterMark": 0,
            "numberOfWriters": 0,
            "attribute": 0,
            "totalAppSize": 0,
            "totalEstMediaSize": 0,
            "totalDeduplicationDataWritten": 0
          },
          "deviceInfo": {
            "name": "Device_1",
            "id": 1
          },
          "metallicStorageInfo": {},
          "region": {
            "_type_": 102
          },
          "savedCredential": "<masked>"
        }
      ],
      "library": {
        "libraryName": "storage-pool-01",
        "_type_": 9,
        "libraryId": 1
      },
      "magLibSummary": {
        "associatedMediaAgents": " commserve-02",
        "bytesBackedupInLast24H": "1.30 GB",
        "lastDayThroughput": "1.35 GB/Hr",
        "isOnline": "Ready",
        "backupReservations": 0,
        "bytesBackedupInLast1H": "1.28 GB",
        "lastRestoreTime": "Nov  4 2026 11:05AM",
        "onlineMountPaths": "1 out of 1",
        "lastBackupTime": "Nov  5 2026 10:01AM",
        "totalAvailableSpace": "980.27 GB",
        "lastHourThroughput": "270.91 GB/Hr",
        "totalFreeSpace": "1000.27 GB",
        "totalCapacity": "1024.00 GB",
        "auxiliaryCopyWriteReservations": 0,
        "numOfMountPath": 1,
        "totalNumberOfWriteReservations": 0,
        "mountPathUsage": "Spill and Fill"
      }
    }
  }
  ```

  </details>

## `get_storage_associated_copies` - GET /V4/Storage/{storagePoolId}/associatedCopies

```python
cv.raw.storage.get_storage_associated_copies('2')
```

**On the wire**

- `GET /V4/Storage/2/associatedCopies` -> **200** (0.16 s)

  <details><summary>Answer</summary>

  ```json
  {
    "copies": [
      {
        "retentionPeriodDays": 15,
        "copyType": "storage-copy-01",
        "useExtendedRetentionRules": true,
        "extendedRetentionRules": {
          "firstExtendedRetentionRule": {
            "retentionPeriodDays": 90,
            "type": "WEEKLY_FULLS"
          },
          "secondExtendedRetentionRule": {
            "retentionPeriodDays": 180,
            "type": "MONTHLY_FULLS"
          }
        },
        "storagePolicy": {
          "name": "storage-policy-01",
          "id": 4
        },
        "copy": {
          "name": "storage-copy-01",
          "id": 3
        }
      },
      {
        "planType": "Server",
        "retentionPeriodDays": 30,
        "copyType": "storage-copy-01",
        "storagePolicy": {
          "name": "plan-01",
          "id": 3
        },
        "copy": {
          "name": "storage-copy-01",
          "id": 2
        },
        "plan": {
          "name": "plan-01",
          "id": 1
        }
      }
    ]
  }
  ```

  </details>

## `get_storage_policy` - GET /V2/StoragePolicy/{storagePolicyId}

```python
cv.raw.storage.get_storage_policy('3')
```

**On the wire**

- `GET /V2/StoragePolicy/3` -> **200** (0.20 s)

  <details><summary>Answer</summary>

  ```json
  {
    "policies": [
      {
        "copies": [
          {
            "copyType": 1,
            "issubclient-01": 1,
            "isSnapCopy": 0,
            "isMirrorCopy": 0,
            "StoragePolicyCopy": {
              "copyId": 2,
              "copyName": "storage-copy-01"
            }
          }
        ],
        "storagePolicy": {
          "storagePolicyName": "plan-01",
          "storagePolicyId": 3
        }
      }
    ],
    "error": {
      "errorMessage": "",
      "errorCode": 0
    }
  }
  ```

  </details>

## `get_storage_policy_search_engine_properties`

GET /V2/StoragePolicy/{storagePolicyId}/SearchEngineProperties

> **SKIPPED** on this run: Commvault answered: 403

```python
cv.raw.storage.get_storage_policy_search_engine_properties('3')
```

**On the wire**

- `GET /V2/StoragePolicy/3/SearchEngineProperties` -> **403** (0.01 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

## `get_storage_pool` - GET /StoragePool/{StoragePoolId}

```python
cv.raw.storage.get_storage_pool('2')
```

**On the wire**

- `GET /StoragePool/2` -> **200** (0.46 s)

  <details><summary>Answer</summary>

  ```json
  {
    "storagePoolDetails": {
      "isWormStorage": false,
      "earlyDeletionSize": 0,
      "HSStoragePoolType": -1,
      "isHSXReadOnly": false,
      "numOfSpareMedia": 0,
      "totalCapacity": 1048572,
      "devicePath": "",
      "isWormGovernanceMode": false,
      "reserved3": "",
      "reserved2": 0,
      "reserved1": 1,
      "redundancyFactor": 0,
      "reserved4": "",
      "maxStreams": 50,
      "resiliencyClass": 0,
      "nodesPerBlock": 0,
      "hasOverrideCopyRetention": true,
      "isArchiveStorage": -1,
      "disperseFactor": 0,
      "isHSXWriteOpExt": false,
      "libraryVendorId": 1,
      "storageOfferingType": 0,
      "isDatabaseDevTestStoragePool": false,
      "status": "Online",
      "statusCode": 0,
      "totalUsableFreeSpace": 1003792,
      "numOfCleaningMedia": 0,
      "lastDayThroughput": "0.00 GB/Hr",
      "sizeOnDisk": 24144,
      "cloudStorageVendorId": -1,
      "applicationSize": 0,
      "numOfMedia": 0,
      "retention": "",
      "usedSpacePerc": 0,
      "cloudStorageClassNumber": -1,
      "HSXUtilWarn": "",
      "totalFreeSpace": 1024272,
      "storageSubType": 0,
      "storagePoolType": 1,
      "isHSXWriteOpGraceAppl": false,
      "storageType": 1,
      "isS3StoragePool": false,
      "copyInfo": {
        "deviceType": 1,
        "isAzureVnetConfigEnabled": 0,
        "dataRetentionLockDays": 0,
        "wormStorageFlag": 96,
        "spareMediaGroup": {
          "spareMediaGroupId": 0,
          "spareMediaGroupName": "mount-path-01"
        },
        "retentionRules": {
          "retainBackupDataForCycles": -1,
          "jobs": 0,
          "retainArchiverDataForDays": -1,
          "retainBackupDataForDays": -1,
          "financialCalendarXML": {
            "calendarName": "Standard",
            "monthStartsOn": 1,
            "minutesSinceDayStarts": 0,
            "calendarId": 1,
            "startingMonthOfYear": 0,
            "weekStartsOn": 5
          },
          "retentionFlags": {
            "dirtyExtendedRetention": 1,
            "enableDataAging": 1
          }
        },
        "StoragePolicyCopy": {
          "storagePolicyName": "storage-pool-01",
          "storagePolicyId": 2,
          "copyId": 1,
          "copyName": "storage-copy-01"
        },
        "extendedFlags": {
          "isAirgapCopy": 0,
          "indelibleWormCopy": 0,
          "encryptOnDependentstorage-copy-01": 0
        },
        "drivePool": {
          "drivePoolId": 1,
          "drivePoolName": "DrivePool(commserve-02)1"
        },
        "copyFlags": {
          "wormCopy": 0,
          "encryptOnNetworkUsingSelectedCipher": 0,
          "preserveEncryptionModeAsInSource": 1,
          "auxCopyReencryptData": 0,
          "storePlainText": 0,
          "storeKeyOnMedia": 1
        },
        "dataEncryption": {
          "encryptionKeyLength": 0,
          "encryptionType": 0,
          "keyProvider": {
            "keyProviderId": 1,
            "keyProviderName": "Built-in"
          }
        },
        "driveType": {
          "name": "Magnetic",
          "id": 10001
        },
        "mediaAgent": {
          "mediaAgentId": 2,
          "mediaAgentName": "commserve-02"
        }
      },
      "distributedStorage": {
        "_type_": 195
      },
      "dedupDBDetailsList": [
        {
          "uniqueBlocksOfStore": 0,
          "commcellId": 2,
          "maxAllowedConnections": 0,
          "numberOfJobs": 0,
          "storeNameAlias": "",
          "dedupeFlags": 0,
          "baselineApplicationSize": 0,
          "fragmentedSpaceSize": 0,
          "baselineSize": 0,
          "totalDataSize": 614465536,
          "storeName": "storage-pool-01_Files_1",
          "ddbVersion": 0,
          "freeSpaceOnLibrary": 0,
          "totalAppSize": 3907138332,
          "storage-copy-01RecordsPercentage": 0,
          "prunePending": 0,
          "deDupSavingPercent": "84.27",
          "noOfPartitions": 2,
          "storeFlags": 0,
          "retentionCyclesForCopy": 0,
          "storeId": 1,
          "reserveField6": 1,
          "reserveField7": "2 of 2  partitions online",
          "reserveField8": "",
          "deDupSavingSize": 2025634830,
          "sizeOnMedia": 614465536,
          "sealedTime": 0,
          "maxAvgQITime": 0,
          "creationtime": 1791249029,
          "avgQITimeOfStore": 0,
          "reserveField1": 0,
          "extendedFlags": 0,
          "reserveField2": 0,
          "reserveField3": "",
          "reserveField4": 0,
          "retentionDaysForCopy": 0,
          "reserveField5": 0,
          "status": 0,
          "estMediaSize": 547364144,
          "enablePruningTime": {
            "EnableTimeZone": 0,
            "EnableTime": 0
          }
        },
        {
          "uniqueBlocksOfStore": 0,
          "commcellId": 2,
          "maxAllowedConnections": 0,
          "numberOfJobs": 0,
          "storeNameAlias": "",
          "dedupeFlags": 0,
          "baselineApplicationSize": 0,
          "fragmentedSpaceSize": 0,
          "baselineSize": 0,
          "totalDataSize": 1106247680,
          "storeName": "storage-pool-01_Databases_2",
          "ddbVersion": 0,
          "freeSpaceOnLibrary": 0,
          "totalAppSize": 9999563046,
          "storage-copy-01RecordsPercentage": 0,
          "prunePending": 0,
          "deDupSavingPercent": "88.94",
          "noOfPartitions": 2,
          "storeFlags": 0,
          "retentionCyclesForCopy": 0,
          "storeId": 2,
          "reserveField6": 1,
          "reserveField7": "2 of 2  partitions online",
          "reserveField8": "",
          "deDupSavingSize": 12010878,
          "sizeOnMedia": 1106247680,
          "sealedTime": 0,
          "maxAvgQITime": 0,
          "creationtime": 1791307993,
          "avgQITimeOfStore": 0,
          "reserveField1": 0,
          "extendedFlags": 0,
          "reserveField2": 0,
          "reserveField3": "",
          "reserveField4": 0,
          "retentionDaysForCopy": 0,
          "reserveField5": 0,
          "status": 0,
          "estMediaSize": 1023243920,
          "enablePruningTime": {
            "EnableTimeZone": 0,
            "EnableTime": 0
          }
        }
      ],
      "maxRetentionSharedLibraryStoragePool": {
        "retentionDays": 0,
        "retentionCycles": 0,
        "storagePolicy": {
          "_type_": 17
        }
      },
      "planList": [
        {
          "planName": "plan-01",
          "_type_": 158,
          "planId": 1
        }
      ],
      "region": {
        "_type_": 102
      },
      "sharePathInfo": {
        "isUnixRegularSharePathMissing": true,
        "isWinRegularSharePathMissing": true
      },
      "compressionSetting": {
        "isEditable": true,
        "compressionStatus": 1,
        "enabled": true
      },
      "libraryList": [
        {
          "lowWaterMarkPercentage": 15,
          "subclient-01MediaTypeId": 0,
          "description": "",
          "libraryUsedForLogCaching": false,
          "extendedAttributes": 0,
          "manufacturer": "Disk",
          "storagePoolType": 1,
          "libraryVendorId": 1,
          "warningWaterMarkPercentage": 30,
          "database-03": "Disk",
          "libraryType": 3,
          "status": "Ready",
          "tapeLibSummary": {
            "numOfCleaningMedia": 0,
            "offlineReason": "",
            "numOfIESlots": 0,
            "lastDayThroughput": "",
            "isOnline": "",
            "numOfIESlotOccupied": 0,
            "lastRestoreTime": "",
            "overwriteRetentionTime": 0,
            "numOfActiveMedia": 0,
            "numOfSpareMedia": 0,
            "vendor": "",
            "numOfRegSlots": 0,
            "database-03": "",
            "numOfMedia": 0,
            "attribute": 0,
            "numOfDrivesOffline": 0,
            "firmwareRevision": "",
            "associatedMediaAgents": "",
            "controller": "",
            "bytesBackedupInLast24H": "",
            "serialNumber": "",
            "numOfAgedMedia": 0,
            "barcodePattern": "",
            "numOfAssignedMedia": 0,
            "numOfAppendableMedia": 0,
            "numOfRegSlotOccupied": 0,
            "backupReservations": 0,
            "numOfSlots": 0,
            "bytesBackedupInLast1H": "",
            "lastBackupTime": "",
            "lastHourThroughput": "",
            "numOfDrives": 0,
            "barcodeReader": "",
            "numOfMediaExporting": 0,
            "auxiliaryCopyWriteReservations": 0,
            "isEnabled": 0,
            "numOfFullMedia": 0,
            "numOfSpareMediaInLib": 0,
            "totalNumberOfWriteReservations": 0,
            "libraryAttribute": 0,
            "status": 0
          },
          "MountPathList": [
            {
              "mediaAgents": "",
              "mountPathUsedForLogCaching": false,
              "dataServerType": 0,
              "mountPathType": 4,
              "jobIds": "",
              "preventDataBlockReferences": false,
              "driveId": 0,
              "disabledForNewWrite": false,
              "libraryVendorId": 0,
              "mountPathId": 1,
              "mountPathName": "mount-path-02",
              "enabledMP": true,
              "status": "Ready",
              "rpStoreLibraryInfo": {
                "copyId": 0,
                "maxPairsPerRPStore": 0,
                "archGroupId": 0,
                "flags": 0,
                "pairCount": 0,
                "commCellId": 0,
                "minSpacePerRPStoreGB": 0,
                "origRPStoreId": 0,
                "rpStoreId": 0,
                "subclient-01HostId": 0,
                "maxSpacePerRPStoreGB": 0,
                "intervalWindow": {}
              },
              "mountPathSummary": {
                "libraryName": "storage-pool-01",
                "avgMediaConsumedPerDay": 0,
                "totalDeduplicationAppSize": 0,
                "totalUsableFreeSpace": 1003792,
                "avgDataWrittenPerDayMB": 0,
                "totalReserveSpaceMB": 20480,
                "lastNumDays": 0,
                "libraryId": 1,
                "maxDataToWriteMB": 0,
                "totalSpace": 1048572,
                "totalValidData": 0,
                "estimatedSpaceRunoutDays": 0,
                "warningWaterMark": 0,
                "totalFreeSpace": 1024272,
                "avgMediaFreedPerDay": 0,
                "totalDataWritten": 0,
                "avgCapacityFreedMB": 0,
                "lowWaterMark": 0,
                "numberOfWriters": 0,
                "attribute": 0,
                "totalAppSize": 0,
                "totalEstMediaSize": 0,
                "totalDeduplicationDataWritten": 0
              },
              "deviceInfo": {
                "name": "Device_1",
                "id": 1
              },
              "metallicStorageInfo": {},
              "region": {
                "_type_": 102
              },
              "savedCredential": "<masked>"
            }
          ],
          "library": {
            "libraryName": "storage-pool-01",
            "_type_": 9,
            "libraryId": 1
          },
          "magLibSummary": {
            "associatedMediaAgents": "",
            "bytesBackedupInLast24H": "",
            "lastDayThroughput": "",
            "isOnline": "",
            "backupReservations": 0,
            "bytesBackedupInLast1H": "",
            "lastRestoreTime": "",
            "onlineMountPaths": "",
            "lastBackupTime": "",
            "totalAvailableSpace": "",
            "lastHourThroughput": "",
            "totalFreeSpace": "",
            "totalCapacity": "",
            "auxiliaryCopyWriteReservations": 0,
            "numOfMountPath": 0,
            "totalNumberOfWriteReservations": 0,
            "mountPathUsage": ""
          }
        }
      ],
      "mediaAgents": [
        {
          "bMetallicMA": true,
          "bStorageMA": true,
          "osType": "Windows",
          "bDDBRoleAllowed": true,
          "bDDBMA": true,
          "storageAccessType": 6,
          "status": 1,
          "mediaAgent": {
            "mediaAgentId": 2,
            "_type_": 11,
            "mediaAgentName": "commserve-02"
          },
          "clientGroup": {
            "_type_": 28
          }
        }
      ],
      "dedupDBDetails": {
        "uniqueBlocksOfStore": 0,
        "commcellId": 0,
        "maxAllowedConnections": 0,
        "numberOfJobs": 0,
        "storeNameAlias": "",
        "dedupeFlags": 0,
        "baselineApplicationSize": 0,
        "fragmentedSpaceSize": 0,
        "baselineSize": 0,
        "totalDataSize": 1720713216,
        "storeName": "",
        "ddbVersion": 0,
        "freeSpaceOnLibrary": 0,
        "totalAppSize": 13906701378,
        "storage-copy-01RecordsPercentage": 0,
        "prunePending": 0,
        "deDupSavingPercent": "87.63",
        "noOfPartitions": 0,
        "storeFlags": 0,
        "retentionCyclesForCopy": 0,
        "storeId": 0,
        "reserveField6": 0,
        "reserveField7": "",
        "reserveField8": "",
        "deDupSavingSize": 2037645708,
        "sizeOnMedia": 1720713216,
        "sealedTime": 0,
        "maxAvgQITime": 0,
        "creationtime": 0,
        "avgQITimeOfStore": 0,
        "reserveField1": 0,
        "extendedFlags": 0,
        "reserveField2": 0,
        "reserveField3": "",
        "reserveField4": 0,
        "retentionDaysForCopy": 0,
        "reserveField5": 0,
        "status": 0,
        "estMediaSize": 1570608064,
        "enablePruningTime": {
          "EnableTimeZone": 0,
          "EnableTime": 0
        }
      }
    }
  }
  ```

  </details>

## `get_storage_pool_media_agents` - GET /V4/StoragePool/{storagePoolId}/MediaAgents

> **SKIPPED** on this run: Commvault answered: 403

```python
cv.raw.storage.get_storage_pool_media_agents('2')
```

**On the wire**

- `GET /V4/StoragePool/2/MediaAgents` -> **403** (0.01 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

## `get_storage_pool_running_jobs` - GET /V4/StoragePool/{storagePoolId}/runningJobs

```python
cv.raw.storage.get_storage_pool_running_jobs('2')
```

**On the wire**

- `GET /V4/StoragePool/2/runningJobs` -> **200** (0.08 s)

  <details><summary>Answer</summary>

  ```json
  {
    "jobIds": [
      1434
    ]
  }
  ```

  </details>

## `get_media_agent_cloud_vm_power_management`

GET /MediaAgent/{mediaAgentId}/CloudVMPowerManagement/{operation}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.storage.get_media_agent_cloud_vm_power_management(...)
```

## `get_storage_policy_copy` - GET /V2/StoragePolicy/{storagePolicyId}/Copy/{copyId}

```python
cv.raw.storage.get_storage_policy_copy('3', '2')
```

**On the wire**

- `GET /V2/StoragePolicy/3/Copy/2` -> **200** (0.33 s)

  <details><summary>Answer</summary>

  ```json
  {
    "copy": {
      "copyType": 1,
      "deviceType": 1,
      "active": 1,
      "isAzureVnetConfigEnabled": 0,
      "issubclient-01": 1,
      "isSnapCopy": 0,
      "snapOperationsSupported": 0,
      "dataRetentionLockDays": 0,
      "isMirrorCopy": 0,
      "wormStorageFlag": 96,
      "poolRetentionPeriodDays": -1,
      "isSourceBackupCopy": 0,
      "throttleNetworkBandWidthMBHR": 0,
      "copyPrecedence": 1,
      "multiplexingFactor": 0,
      "storagePoolType": 1,
      "isSourceCatalog": 0,
      "storageType": 1,
      "spareMediaGroup": {
        "spareMediaGroupId": 0,
        "spareMediaGroupName": ""
      },
      "sourceCopy": {
        "copyId": 0,
        "copyName": ""
      },
      "dedupeFlags": {
        "enableDASHFull": 1,
        "pauseAndRecoverCurrentDDB": 1,
        "useGlobalDedupStore": 1,
        "automaticallyPauseAndRecoverDDB": 1,
        "enableDeduplication": 1,
        "enableClientSideDedup": 1
      },
      "storagePool": {
        "storagePoolName": "storage-pool-01",
        "storagePoolId": 2
      },
      "regionMap": [],
      "retentionRules": {
        "retainBackupDataForCycles": 1,
        "inheritJobRetentionOnExistingJobs": false,
        "jobs": 0,
        "retainArchiverDataForDays": -1,
        "retainBackupDataForDays": 30,
        "financialCalendarXML": {
          "calendarName": "Standard",
          "monthStartsOn": 1,
          "minutesSinceDayStarts": 0,
          "calendarId": 1,
          "startingMonthOfYear": 0,
          "weekStartsOn": 5
        },
        "retentionFlags": {
          "dirtyExtendedRetention": 1,
          "enableDataAging": 1
        }
      },
      "StoragePolicyCopy": {
        "copyId": 2,
        "copyName": "storage-copy-01"
      },
      "extendedFlags": {
        "overRideGACPRetention": 1
      },
      "associations": {
        "entities": [
          {
            "subclientId": 0,
            "clientId": 0,
            "instanceName": "",
            "clientGroupName": "",
            "appName": "subclient-01 Application Type Name",
            "clientGroupId": 0,
            "applicationId": 0,
            "clientName": "",
            "backupsetId": 0,
            "instanceId": 0,
            "subclientName": "",
            "backupsetName": "",
            "_type_": 2,
            "flags": {
              "include": true,
              "exclude": false,
              "disabled": false
            }
          },
          {
            "subclientId": 0,
            "clientId": 0,
            "instanceName": "",
            "clientGroupName": "",
            "appName": "subclient-01 Application Type Name",
            "clientGroupId": 0,
            "applicationId": 0,
            "clientName": "",
            "backupsetId": 0,
            "instanceId": 0,
            "subclientName": "",
            "backupsetName": "",
            "_type_": 27,
            "flags": {
              "include": true,
              "exclude": false,
              "disabled": false
            }
          }
        ]
      },
      "drivePool": {
        "drivePoolId": 1,
        "drivePoolName": "DrivePool(commserve-02)1"
      },
      "copyFlags": {
        "roundRobbinDataPath": 1,
        "preserveEncryptionModeAsInSource": 1,
        "storeKeyOnMedia": 1,
        "multiplexSourceStreams": 0,
        "autoAddDataPaths": 1,
        "noInlineCopyToSameLibrary": 0
      },
      "library": {
        "libraryName": "storage-pool-01",
        "libraryId": 1
      },
      "startTime": {
        "time": -1
      },
      "mediaAgent": {
        "mediaAgentId": 2,
        "mediaAgentName": "commserve-02"
      },
      "endTime": {
        "time": 2147483647
      }
    },
    "error": {
      "errorMessage": "",
      "errorCode": 0
    }
  }
  ```

  </details>

## `get_storage_policy_copy_size`

GET /V2/StoragePolicy/{storagePolicyId}/Copy/{copyId}/Size

```python
cv.raw.storage.get_storage_policy_copy_size('3', '2')
```

**On the wire**

- `GET /V2/StoragePolicy/3/Copy/2/Size` -> **200** (0.09 s)

  <details><summary>Answer</summary>

  ```json
  {
    "copyInfo": [
      {
        "dataSizeInGB": 12,
        "dataWrittenInGB": 1,
        "requiresBackupsOnOrAfterDate": false,
        "oldestJobStartTime": 1793897000,
        "spCopy": {
          "storagePolicyName": "plan-01",
          "storagePolicyId": 3,
          "copyId": 2,
          "copyName": "storage-copy-01"
        }
      }
    ]
  }
  ```

  </details>
