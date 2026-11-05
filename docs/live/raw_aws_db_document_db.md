# `cv.raw.aws_db_document_db`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:37 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_instance` - GET /Instance/{instanceid}

```python
cv.raw.aws_db_document_db.get_instance('1')
```

**On the wire**

- `GET /Instance` -> **400** (0.07 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

- `GET /Instance/1` -> **200** (0.08 s)

  <details><summary>Answer</summary>

  ```json
  {
    "instanceProperties": [
      {
        "instance": {
          "instanceName": "asset-01",
          "instanceId": 1
        }
      }
    ]
  }
  ```

  </details>

## `get_subclient` - GET /subclient/{subclientid}

```python
cv.raw.aws_db_document_db.get_subclient('44')
```

**On the wire**

- `GET /Subclient` -> **400** (0.06 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

- `GET /subclient/44` -> **200** (0.11 s)

  <details><summary>Answer</summary>

  ```json
  {
    "filterQueryCount": 1,
    "subClientProperties": [
      {
        "status": 8,
        "automaticStreamConfig": true,
        "useLocalContent": false,
        "protectionGroupDeleteOption": 0,
        "isProtectionGroupGenerated": false,
        "isFailoverSubclient": 0,
        "useLocalArchivalRules": true,
        "canChangeEncryptionSetting": false,
        "planEntity": {
          "planType": 2,
          "planName": "plan-01",
          "planSubtype": 33554437,
          "planId": 1
        },
        "cassandraProps": {},
        "awsEFSProperties": {},
        "planParentEntity": {
          "displayName": "host-14",
          "clientId": 16,
          "instanceName": "host-14",
          "instanceId": 7,
          "_type_": 5
        },
        "taPlanEntity": {},
        "splunkProps": {},
        "bigDataProps": {},
        "proxyClient": {},
        "dcPlanEntity": {},
        "subClientEntity": {
          "clientName": "host-14",
          "instanceName": "host-14",
          "displayName": "host-14",
          "backupsetId": 30,
          "_type_": 7,
          "commCellName": "commserve-02",
          "instanceId": 7,
          "csGUID": "A1AD169B-CF73-41B9-BC8A-823EA536FF31",
          "subclientGUID": "82244B9D-1133-41AE-B123-199BBCFB9603",
          "subclientId": 44,
          "clientId": 16,
          "appName": "SQL Server",
          "backupsetName": "backupset-01",
          "applicationId": 81,
          "subclientName": "subclient-01",
          "entityInfo": {
            "companyId": 0,
            "multiCommcellGuid": "2DCFEA81-1B84-4E4D-ADB4-C317F96A112E",
            "multiCommcellName": "commserve-02",
            "companyName": "Commcell"
          }
        },
        "dfsSubclientProp": {},
        "databricksSubclientProps": {},
        "region": {},
        "mssqlSubClientProp": {
          "numberOfBackupStreams": 2,
          "backupStagingDir": "",
          "useBlockLevelBackupWithOptimizedRecovery": false,
          "blockLevelSPOSBackup": 0,
          "numberOfTransactionLogStreams": 2,
          "backupRules": 3,
          "blockLevelBackup": 0,
          "thresholdLogFreeSpaceInPercent": 0,
          "sqlSubclientType": 1,
          "isRebootNowPermitted": 0,
          "bufferCount": 20,
          "thresholdLogFileSizeInMB": 0,
          "dumpSweepCache": "",
          "maxTransferSize": 2097152,
          "mssqlAzureBackupProp": {
            "vCoresForDBCopy": 0,
            "subTierForStandardTierDBCopy": "",
            "subTierForPremiumTierDBCopy": ""
          }
        },
        "content": [
          {
            "mssqlDbContent": {
              "discoverType": 1,
              "databaseName": "user-group-01",
              "databaseId": 1
            }
          },
          {
            "mssqlDbContent": {
              "discoverType": 1,
              "databaseName": "database-03",
              "databaseId": 3
            }
          },
          {
            "mssqlDbContent": {
              "discoverType": 1,
              "databaseName": "database-04",
              "databaseId": 4
            }
          },
          "... 10 more"
        ],
        "commonProperties": {
          "nextBackupTime": 1793934000,
          "slaStatus": 1,
          "isAdAppAwareSubclient": false,
          "disableArchivingTurboRule": false,
          "isSnapshotV2": false,
          "firstBackupTime": 1791406807,
          "lastBackupTime": 1793644988,
          "indexingBackupSubClient": false,
          "allowVssForSnapbackup": false,
          "isActivityDisabledFromPolicy": false,
          "isETCDSubclient": false,
          "enableBackupAfterDelay": false,
          "runAs": 0,
          "slaCategoryDescription": "Protected",
          "onBoardCompanyId": 0,
          "sizeOnMedia": 417894240,
          "enableBackup": true,
          "encryptionFlag": 2,
          "numberOfBackupStreams": 1,
          "idaType": 0,
          "runTrueUpJobAfterDays": 30,
          "totalBackupSize": 4008809970,
          "issubclient-01Subclient": true,
          "dedupeRatio": 89.5756,
          "isTrueUpOptionEnabled": false,
          "slaCategory": 1,
          "subClientPropertiesFlag": 0,
          "lastBackupSize": 50005310,
          "hasScaleProfileAccessNode": false,
          "readBuffersize": 2048,
          "securityAssociations": {
            "ownerAssociations": {},
            "tagWithCompany": {
              "providerId": 0,
              "providerDomainName": "Commcell"
            }
          },
          "associatedSnapShotSCId": {
            "_type_": 7
          },
          "snapCopyInfo": {
            "IsOracleSposDriverEnabled": false,
            "isRMANEnableForTapeMovement": false,
            "useProxyForSQLIntegrity": {},
            "sybaseUser": {},
            "snapToTapeSelectedEngine": {
              "_type_": 110
            },
            "sqlUser": {},
            "vmApplicationUser": {},
            "snapToTapeProxyToUse": {
              "_type_": 3
            },
            "quiesceImpersonateUser": {},
            "separateProxyForSnapToTape": {
              "_type_": 3
            },
            "sshKey": {},
            "configuredSybaseInstance": {
              "_type_": 5
            }
          },
          "subclientPolicy": {
            "_type_": 65,
            "subclientPolicyName": ""
          },
          "applicationCredentialinfo": "<masked>",
          "lastBackupJobInfo": {
            "jobID": 1491,
            "failureReasonIds": "515,",
            "commCellID": 2,
            "failureReasonMessageEnglish": "Another backup is running for client [host-14], iDataAgent [SQL Server], Instance [host-14], Subclient [subclient-01].<br/>Source: commserve-02, Process: JobManager",
            "status": 9,
            "startTime": {
              "time": 1793826011
            },
            "endTime": {
              "time": 1793826011
            }
          },
          "impersonateUserCredentialinfo": "<masked>",
          "enableBackupAtDateTime": {
            "TimeZoneID": 0,
            "time": 0
          },
          "turboNASClient": {
            "_type_": 3
          },
          "dbDumpConfig": {
            "exportRDSLocalMode": false
          },
          "prepostProcess": {
            "runPostScan": 0,
            "runPostBackup": 0,
            "runAs": 1,
            "runPostLog": 0,
            "prepostUserName": {}
          },
          "security": {
            "associatedUserGroups": [
              {
                "userGroupId": 1,
                "_type_": 15,
                "userGroupName": "user-group-01"
              }
            ],
            "advancedPrivacySettings": {
              "isPasskeyFeatureEnabled": false,
              "authType": 1,
              "isPrivacyFeatureEnabled": false,
              "passkeySettings": {
                "enableAuthorizeForRestore": false,
                "expirationTime": {
                  "time": 0
                }
              }
            },
            "ownerCapabilities": {}
          },
          "storageDevice": {
            "networkAgents": 2,
            "applicableReadSize": 2048,
            "softwareCompression": 0,
            "overrideDataPath": false,
            "throttleNetworkBandwidth": -1,
            "dataBackupStoragePolicy": {
              "_type_": 17,
              "storagePolicyName": "plan-01",
              "storagePolicyId": 3
            },
            "deDuplicationOptions": {
              "enableDeduplication": true,
              "generateSignature": "<masked>"
            },
            "logBackupStoragePolicy": {
              "_type_": 17,
              "storagePolicyName": "plan-01",
              "storagePolicyId": 3
            },
            "performanceMode": {
              "perfSPName": "plan-01",
              "multiplexingValid": false,
              "enableMultiplexing": false,
              "perfCopyName": "Primary",
              "perfClientName": "host-14",
              "streamsOverMux": false,
              "pipelineBufferSize": 64,
              "numOfPipelineBuffers": 180,
              "muxFactor": 0,
              "lookAheadReaderSlots": 4,
              "perfCRCDetails": [
                {
                  "crcOverMedia": true,
                  "perfMaId": 2,
                  "crcOverNetwork": true,
                  "perfMa": "commserve-02"
                }
              ]
            }
          },
          "UNCScriptCredentialinfo": "<masked>",
          "vmBackupValidationSettings": {
            "isAppValidationEnabled": false,
            "backupValidationThreadCount": 0,
            "subTaskId": 0,
            "isCustomAppEnabled": false,
            "runAsDevTestGroup": false,
            "taskId": 0,
            "useSourceVMEsxToMount": false,
            "uncScriptImpersonateUser": {
              "userName": "0"
            }
          },
          "prepostCredentialinfo": "<masked>",
          "associatedPolicy": {
            "subclientPolicyId": 0
          },
          "guestCredentialinfo": "<masked>"
        },
        "auditPlanEntity": {},
        "analyticsSubclientProp": {}
      }
    ]
  }
  ```

  </details>
