# `cv.raw.client`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:50 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_client_distributed_apps` - GET /Client/DistributedApps

```python
cv.raw.client.get_client_distributed_apps()
```

**On the wire**

- `GET /Client/DistributedApps` -> **200** (0.14 s)

  <details><summary>Answer</summary>

  ```json
  {
    "response": {
      "errorMessage": "",
      "errorCode": 0
    }
  }
  ```

  </details>

## `get_clients_count` - GET /clients/count

> **SKIPPED** on this run: Commvault answered: 500 - An unexpected error occurred.

```python
cv.raw.client.get_clients_count()
```

**On the wire**

- `GET /clients/count` -> **500** (0.07 s)

  <details><summary>Answer</summary>

  ```json
  {
    "error": "An unexpected error occurred."
  }
  ```

  </details>

## `get_index_servers` - GET /IndexServers

```python
cv.raw.client.get_index_servers()
```

**On the wire**

- `GET /IndexServers` -> **200** (0.12 s)

  <details><summary>Answer</summary>

  ```json
  {
    "indexServers": [
      {
        "clusterType": 1,
        "cloudId": 1,
        "createdTime": 1791234811,
        "clients": {
          "clientName": "host-01",
          "displayName": "host-01",
          "clientId": 3
        },
        "osInfo": {
          "Type": "Windows",
          "SubType": "Server",
          "osId": 210
        },
        "nodes": [
          {
            "nodeClientEntity": {
              "displayName": "commserve-02",
              "clientId": 2
            }
          }
        ]
      }
    ]
  }
  ```

  </details>

## `list_client` - GET /Client

```python
cv.raw.client.list_client()
```

**On the wire**

- `GET /Client` -> **200** (0.10 s)

  <details><summary>Answer</summary>

  ```json
  {
    "clientProperties": [
      {
        "client": {
          "evmgrcPort": 0,
          "cvdPort": 8400,
          "clientEntity": {
            "hostName": "commserve-02",
            "clientName": "commserve-02",
            "displayName": "commserve-02",
            "_type_": 3,
            "clientId": 2,
            "clientGUID": "2DCFEA81-1B84-4E4D-ADB4-C317F96A112E"
          }
        },
        "clientProps": {
          "iSCSIPort": 3260,
          "clusterType": 0
        }
      },
      {
        "client": {
          "evmgrcPort": 0,
          "cvdPort": 0,
          "clientEntity": {
            "hostName": "host-01",
            "clientName": "host-01",
            "displayName": "host-01",
            "_type_": 3,
            "clientId": 3,
            "clientGUID": "F5AB5F53-80CD-4D54-8B89-D1CEB278387B"
          }
        },
        "clientProps": {
          "iSCSIPort": 3260,
          "clusterType": 15
        }
      },
      {
        "client": {
          "evmgrcPort": 8402,
          "cvdPort": 8400,
          "clientEntity": {
            "hostName": "host-02",
            "clientName": "host-02",
            "displayName": "host-02",
            "_type_": 3,
            "clientId": 4,
            "clientGUID": "99CA0BBB-F13D-4DEA-9778-08A913D3FEFA"
          }
        },
        "clientProps": {
          "iSCSIPort": 3260,
          "clusterType": 0
        }
      },
      "... 12 more"
    ]
  }
  ```

  </details>

## `get_client` - GET /client/{clientId}

```python
cv.raw.client.get_client('2')
```

**On the wire**

- `GET /client/2` -> **200** (1.31 s)

  <details><summary>Answer</summary>

  ```json
  {
    "processinginstructioninfo": {
      "attributes": [
        {
          "name": "exitval",
          "value": "0"
        }
      ]
    },
    "clientProperties": [
      {
        "client": {
          "displayName": "commserve-02",
          "ClockSkewInSeconds": 0,
          "clientDescription": "",
          "installDirectory": "C:\\Program Files\\Commvault\\ContentStore",
          "timezoneSetByUser": false,
          "evmgrcPort": 0,
          "cvdPort": 8400,
          "jobResulsDir": {
            "path": "H:\\commvaultdata\\JobResults",
            "userAccount": {
              "userName": "",
              "savedCredential": {}
            }
          },
          "origCommCell": {
            "commCellId": 0
          },
          "osInfo": {
            "Type": "Windows",
            "SubType": "Server",
            "osId": 210,
            "OsDisplayInfo": {
              "ProcessorType": "WinX64",
              "OSName": "Windows Server 2025 Datacenter"
            }
          },
          "idaList": [
            {
              "summary": {
                "slaStatus": 2,
                "slaCategoryDescription": "Backup job failed"
              },
              "idaEntity": {
                "_type_": 4,
                "appName": "File System",
                "applicationId": 33
              }
            },
            {
              "summary": {
                "slaStatus": 3,
                "slaCategoryDescription": "Deconfigured"
              },
              "idaEntity": {
                "_type_": 4,
                "appName": "Virtual Server",
                "applicationId": 106
              }
            },
            {
              "summary": {
                "slaStatus": 3,
                "slaCategoryDescription": "Deconfigured"
              },
              "idaEntity": {
                "_type_": 4,
                "appName": "Metrics Reporting Server",
                "applicationId": 121
              }
            }
          ],
          "clientEntity": {
            "hostName": "commserve-02",
            "clientName": "commserve-02",
            "displayName": "commserve-02",
            "workloadRegionId": 5,
            "commCellName": "commserve-02",
            "clientId": 2,
            "workloadRegionDisplayName": "North America",
            "clientGUID": "2DCFEA81-1B84-4E4D-ADB4-C317F96A112E"
          },
          "versionInfo": {
            "UpdateStatus": 2,
            "IsBaselineComparedToClient": 0,
            "version": "ServicePack:46.30,Additional Updates:,SP46-CU30-1134,SP46-CU30-1135,SP46-CU30-1144",
            "GalaxyRelease": {
              "ReleaseString": "11"
            },
            "PatchStatus": [
              {
                "BaselineUpdates": "CU30_SP46-CU30-1200, CU30_SP46-CU30-1219, CU30_SP46-CU30-1251, CU30_SP46-CU30-1298, CU30_SP46-CU30-1329, CU30_SP46-CU30-1355, CU30_SP46-CU30-1450, CU30_SP46-CU30-1457, CU30_SP46-CU30-1487, CU30_SP46-CU30-1515, CU30_SP46-CU30-1522, CU30_SP46-CU30-1545, CU3",
                "BaselineStatus": 2,
                "IsBaseLineDeltaSP": 0,
                "packageInfo": {
                  "packageId": 1,
                  "packageName": "File System Core"
                }
              },
              {
                "BaselineUpdates": "CU30_SP46-CU30-1161, CU30_SP46-CU30-1162, CU30_SP46-CU30-1211, CU30_SP46-CU30-1219, CU30_SP46-CU30-1271, CU30_SP46-CU30-1277, CU30_SP46-CU30-1291, CU30_SP46-CU30-1309, CU30_SP46-CU30-1315, CU30_SP46-CU30-1323, CU30_SP46-CU30-1325, CU30_SP46-CU30-1335, CU3",
                "BaselineStatus": 2,
                "IsBaseLineDeltaSP": 0,
                "packageInfo": {
                  "packageId": 20,
                  "packageName": "CommServe"
                }
              },
              {
                "BaselineUpdates": "CU30_SP46-CU30-1161, CU30_SP46-CU30-1355, CU30_SP46-CU30-1450, CU30_SP46-CU30-1522, CU30_SP46-CU30-1531, CU30_SP46-CU30-1545, CU30_SP46-CU30-1611, CU30_SP46-CU30-1628, CU30_SP46-CU30-1733",
                "BaselineStatus": 2,
                "IsBaseLineDeltaSP": 0,
                "packageInfo": {
                  "packageId": 23,
                  "packageName": "Workflow"
                }
              },
              "... 38 more"
            ]
          },
          "TimeZone": {
            "TimeZoneID": 23,
            "TimeZoneName": "(UTC-06:00) Central Time (US & Canada)"
          }
        },
        "ActivePhysicalNode": {
          "hostName": "commserve-02",
          "clientName": "commserve-02",
          "clientId": 2
        },
        "clusterClientProperties": {
          "configureClusterClient": false,
          "showAllAgents": false
        },
        "pseudoClientInfo": {
          "virtualServerClientProperties": {
            "managementVersion": "",
            "virtualServerInstanceInfo": {
              "vsInstanceType": 0,
              "virtualServerCredentialinfo": {},
              "azure": {
                "credentials": {}
              },
              "azureResourceManager": {
                "useManagedIdentity": false,
                "credentials": {}
              },
              "associatedClients": {
                "usePredefinedAccessNodes": false
              },
              "amazonInstanceInfo": {
                "useIamRole": false
              }
            },
            "vmBackupInfo": {}
          },
          "cloudClonnectorProperties": {
            "instance": {
              "cloudAppsInstance": {
                "generalCloudProperties": {
                  "credentials": {},
                  "accessNodes": {}
                }
              }
            }
          },
          "adForestPseudoClientProperties": {
            "auditEnabled": false,
            "auditAllowGPOConfiguration": false
          },
          "ibmiInstallOptions": {
            "jobProirity": 0,
            "jobQueue": "",
            "createJobQueue": false,
            "subsysDescription": "",
            "dataFolder": "",
            "runPriority": 0,
            "userProfile": {
              "userName": "",
              "savedCredential": {}
            }
          },
          "edgeDrivePseudoClientProperties": {
            "systemDriveType": 0,
            "impersonateUser": {},
            "outlookAddinStoreInfo": {}
          },
          "openVMSProperties": {
            "cvdPort": 8400,
            "baseInstallFolder": "",
            "proxyClients": {},
            "userAccount": {
              "userName": "",
              "savedCredential": {}
            }
          },
          "nasClientProperties": {
            "credentialEntity": {}
          },
          "dbThinClientProperties": {
            "proxyClients": {}
          },
          "indexServerProperties": {
            "cloudServerType": 1,
            "status": 1,
            "indexServerClients": [
              {
                "clientName": "host-01",
                "displayName": "host-01",
                "clientId": 3
              }
            ],
            "nodeMetaInfos": [
              {
                "name": "JVMMAXMEMORY",
                "value": "7643"
              },
              {
                "name": "INDEXLOCATION",
                "value": "G:\\commvaultdata\\IndexCache\\AnalyticsIndex"
              },
              {
                "name": "PORTNO",
                "value": "20000"
              }
            ]
          },
          "serviceMeshClientProperties": {},
          "idaInfo": {
            "sql61Prop": {
              "overrideHigherLevelSettings": {
                "userAccount": {}
              },
              "awsSqlInfo": {
                "sqlInstanceCredentials": {}
              },
              "azureInfo": {
                "useManagedIdentity": false,
                "azureSqlInstanceCredentials": {}
              },
              "MSSQLCredentialinfo": {}
            }
          }
        },
        "clientConfiguration": {
          "isMergedExchangePackageInstalled": false
        },
        "clientProps": {
          "isVirtualServerDiscoveredClient": false,
          "isClientBasePackageInstalled": true,
          "isMA": true,
          "slaStatus": 2,
          "CipherType": 2,
          "RetryFrequencyInSecOnNetworkError": 30,
          "isWebServerInstalled": true,
          "RestoreAccessFlag": 0,
          "isRemoteCacheEnabled": true,
          "SnapBackupMAInstalled": true,
          "clientSerialNumber": "<masked>",
          "PathToExchangeMiningTool": "",
          "RestoreAccessSynFull": false,
          "ClientInterface": "commserve-02",
          "OptimizeDataForSearch": false,
          "slaCategoryDescription": "Backup job failed",
          "retireClientPhase": 0,
          "ContentIndexEngineInstalled": false,
          "RetryCountOnNetworkError": 40,
          "devsnapServerType": "",
          "cloudFileShareWorkloadId": 0,
          "isPersonalWorkstation": false,
          "isIndexingV2NAS": false,
          "EnableSnapBackups": false,
          "isIndexingV2VSA": false,
          "StorePatchLocally": true,
          "isFastSearchSupported": false,
          "slaCategory": 2,
          "copyManagementLicense": "<masked>",
          "isDescriptionInHTMLFormat": false,
          "IsDeletedClient": false,
          "iswebSearchServerInstalled": true,
          "isUserCentricClient": false,
          "EnableRetryOnNetworkError": true,
          "queueJobsIfOtherConflictingJobsAreActive": false,
          "JobPriority": 6,
          "overrideGlobalDesktopGuiProperties": false,
          "isPseudoDBCluster": false,
          "CDRLogFileLocation": "",
          "isSecureInstallEnabled": false,
          "isFarmClient": false,
          "webSearchServiceUrl": "http://commserve-02:81/SearchSvc",
          "AutoUpdateLocation": "C:\\Program Files\\Commvault\\ContentStore",
          "JobResultsDiskCapThreshold": 90,
          "maxStreams": 0,
          "forceClientSideDownload": 2,
          "is1TouchClient": false,
          "isMARoleSet": true,
          "AltCachePartitionForQSnap": "",
          "cacheSource": 0,
          "isAdvancedFSPackageInstalled": true,
          "indexingV2EnabledMask": 1,
          "EncryptKeyLength": 128,
          "isIndexingV2": true,
          "IsQsnapUNIX": false,
          "dm2CacheDiskCapThreshold": 90,
          "devsnapTargetPort": 3260,
          "EnableContentIndexing": false,
          "recallService": "",
          "isclient-group-01": true,
          "CenteraResourceFilename": "",
          "isQsnapInstalled": 0,
          "CVS3BucketName": "",
          "specialClientFlags": 0,
          "pRDMVCenterClientId": 0,
          "dm2CacheRetentionDays": 7,
          "overrideGlobalEncryptionSettings": 3,
          "IsDCInstalled": false,
          "encryptionSettings": 0,
          "IsExchangeOnePassClient": false,
          "isExchangePseudoClient": false,
          "isPRDMMountEnabled": false,
          "DirectMediaAccessFlag": 0,
          "isMAPackageInstalled": true,
          "JobResultsThresholdMB": 500,
          "JobResultsRetentionDays": 7,
          "BlockLevelCacheDir": "",
          "vendorType": 1,
          "BinarySetID": 3,
          "IsCommServer": true,
          "EnableCollectDelegateInfo": true,
          "fileLevelAnalyticsLicense": "<masked>",
          "dm2CacheThresholdMB": 500,
          "IsVirtualClient": false,
          "devsnapInitiatorIQN": "iqn.1991-05.com.microsoft:commserve-02",
          "enableAccessControl": true,
          "EndUserUrl": "http://commserve-02/webconsole",
          "ClientNoPhysicalMachine": false,
          "byteOrder": "Little-endian",
          "RestoreAccessPubKey": false,
          "networkReadiness": {
            "status": 1,
            "lastOnlineTime": {
              "_type_": 55,
              "time": 1793903531
            },
            "lastUpdatedTime": {
              "_type_": 55,
              "time": 1793903531
            },
            "offlineTime": {
              "_type_": 55,
              "time": 0
            }
          },
          "dlpPropertise": {
            "dlpScanIntervalMins": 15,
            "dlpStolen": false,
            "dlpEnableAutomaticDecryption": false,
            "dlpUnlockMethod": 0,
            "enableDLP": false,
            "dlpEnableClientKeys": false,
            "dlpMinFileAgeMins": 5,
            "dlpRMProperties": {
              "enableRmDLP": false,
              "dlpRmNow": false,
              "dlpRmOfflineDays": 30
            }
          },
          "firewallConfiguration": {
            "configureFirewallSettings": false,
            "isTrivialConfig": false,
            "reachMeVia": {
              "reachMeViaSelected": false
            },
            "fwTrivialConfig": {
              "firewallTrivialDetailsCS": {
                "networkType": 1,
                "connectionType": 1,
                "proxyEntity": {
                  "displayName": "host-15",
                  "clientId": 1,
                  "clientName": "host-15"
                }
              },
              "firewallTrivialDetailsMA": {
                "networkType": 1,
                "connectionType": 1,
                "proxyEntity": {
                  "displayName": "host-15",
                  "clientId": 1,
                  "clientName": "host-15"
                }
              }
            },
            "firewallOptions": {
              "isRoamingClient": false,
              "extendedProperties": "<App_FirewallExtendedProperties configureAutomatically=\"1\" defaultOutgoingProtocol=\"2\" />",
              "tunnelconnectionPort": 8403,
              "foreceSSL": false,
              "tunnelInitSeconds": 30,
              "lockdown": false,
              "bindOpenPortsOnly": false,
              "isDMZ": false,
              "keepAliveSeconds": 180,
              "tppm": [
                {}
              ]
            }
          },
          "clientRegionInfo": {
            "geoLocation": {
              "latitude": "34.806000",
              "longitude": "-92.231000"
            }
          },
          "deDuplicationProperties": {
            "performClientSideDeduplication": true,
            "enableHighLatencyOptimization": false,
            "cacheBufferSize": 1024,
            "maxCacheDb": 4096,
            "clientSideDeduplication": 0,
            "enableVariableContentAlignment": false,
            "enableClientSideDiskCache": false
          },
          "spWebServerProperties": {
            "enableOnlineSearch": false,
            "spWebServerUserPassword": {}
          },
          "cvs3EndpointProp": {
            "offlineSince": 0,
            "s3Ports": "",
            "enabled": false
          },
          "dm2CacheDir": {
            "path": "H:\\commvaultdata\\DM2Cache",
            "userAccount": {
              "userName": ""
            }
          },
          "rightManagementServiceProperties": {
            "SMTPAddressOfTheRMSSuperUser": "",
            "decryptRMSDocumentDuringContentIndexing": false,
            "smtpAddressOfRMSSuperUser": "",
            "rmsCredentials": "<masked>"
          },
          "fsxStorageVirtualMachineProps": {
            "awsProperties": ""
          },
          "company": {
            "connectName": "",
            "shortName": {
              "domainName": "Commcell",
              "id": 0
            }
          },
          "networkThrottle": {
            "enableThrottle": false,
            "throttle": {}
          },
          "securityAssociations": {
            "ownerAssociations": {
              "inheritedOwners": [
                {
                  "permission": {
                    "permissionId": 1,
                    "_type_": 122,
                    "permissionName": "Administrative Management"
                  },
                  "parents": [
                    {
                      "commCellName": "commserve-02",
                      "commCellId": 2,
                      "_type_": 1
                    }
                  ]
                },
                {
                  "permission": {
                    "permissionId": 2,
                    "_type_": 122,
                    "permissionName": "Agent Management"
                  },
                  "parents": [
                    {
                      "commCellName": "commserve-02",
                      "commCellId": 2,
                      "_type_": 1
                    }
                  ]
                },
                {
                  "permission": {
                    "permissionId": 3,
                    "_type_": 122,
                    "permissionName": "Agent Scheduling"
                  },
                  "parents": [
                    {
                      "commCellName": "commserve-02",
                      "commCellId": 2,
                      "_type_": 1
                    }
                  ]
                },
                "... 127 more"
              ]
            },
            "tagWithCompany": {
              "providerId": 0,
              "providerDomainName": "Commcell"
            }
          },
          "clientSecurity": {
            "enableDataSecurity": false,
            "associatedUserGroups": [
              {
                "userGroupId": 1,
                "_type_": 15,
                "userGroupName": "master"
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
            "ownerCapabilities": {
              "inheritedCapabilities": [
                1,
                2,
                3,
                "... 24 more"
              ]
            }
          },
          "registryKeys": [
            {
              "relativepath": "CommServDB.GxGlobalParam",
              "keyName": "FailedLoginAttemptLimit",
              "type": "INTEGER",
              "enabled": 1,
              "isInheritedFromClientGroup": false,
              "comment": "",
              "value": "5",
              "sourceEntity": {}
            },
            {
              "relativepath": "CommServDB.AdminConsole",
              "keyName": "bDisableInfiniteRetention",
              "type": "BOOLEAN",
              "enabled": 1,
              "isInheritedFromClientGroup": false,
              "comment": "System created",
              "value": "true",
              "sourceEntity": {}
            },
            {
              "relativepath": "CommServDB.AdminConsole",
              "keyName": "bEnableOneWeekRetention",
              "type": "BOOLEAN",
              "enabled": 1,
              "isInheritedFromClientGroup": false,
              "comment": "System created",
              "value": "true",
              "sourceEntity": {}
            },
            "... 6 more"
          ],
          "activityControl": {
            "EnableDataRecovery": true,
            "EnableDataManagement": true,
            "EnableOnlineContentIndex": true
          },
          "advancedClientProperties": {
            "slaCopyFallenBehindDays": 0,
            "rpoMinutes": 0,
            "mailServerRole": 0,
            "rtoMinutes": 0,
            "slaCopyRedundancy": 0,
            "excludeFromSLA": false
          },
          "clientMacAddress": [
            "2001:db8::1"
          ],
          "clientActivityControl": {
            "activityControlOptions": [
              {
                "activityType": 1,
                "enableAfterADelay": false,
                "enableActivityType": true
              },
              {
                "activityType": 2,
                "enableAfterADelay": false,
                "enableActivityType": true
              },
              {
                "activityType": 512,
                "enableAfterADelay": false,
                "enableActivityType": true
              },
              "... 1 more"
            ]
          },
          "jobThrottleSettings": {
            "sweepThreshold": 1,
            "isJobThrottleEnabledAtCS": 0,
            "isJobThrottleEnabled": 0,
            "dataThreshold": 1,
            "excludeImmidiateJobs": 0,
            "logThreshold": 1
          },
          "webSearchServer": {
            "hostName": "commserve-02",
            "clientId": 2
          },
          "client-group-01MachineDetails": [
            {
              "client-group-01MachineType": 1024,
              "packageId": 20,
              "packageName": "CommServe"
            },
            {
              "client-group-01MachineType": 2048,
              "packageId": 51,
              "packageName": "MediaAgent"
            },
            {
              "client-group-01MachineType": 1,
              "packageId": 55,
              "packageName": "Index Store"
            },
            "... 7 more"
          ],
          "clientIpAddress": [
            "192.0.2.15"
          ],
          "emailWebAppProperties": {
            "enableEmailWebApp": false,
            "exchangeAdminSmtpAddress": "",
            "exchangeAdministratorAccount": {
              "userName": ""
            }
          }
        },
        "clientReadiness": {
          "DRStatus": "Ready.",
          "readinessStatus": "Ready.\n",
          "onlineTime": {
            "time": 1793903531
          },
          "ccrTime": {
            "time": 1793903531
          },
          "offlineTime": {
            "time": 0
          }
        },
        "clientGroups": [
          {
            "clientGroupId": 1,
            "clientGroupName": "client-group-01"
          },
          {
            "clientGroupId": 3,
            "clientGroupName": "client-group-03"
          }
        ],
        "AdvancedFeatures": [
          {
            "LicenseName": "<masked>",
            "LicenseId": "<masked>"
          },
          {
            "LicenseName": "<masked>",
            "LicenseId": "<masked>"
          },
          {
            "LicenseName": "<masked>",
            "LicenseId": "<masked>"
          },
          "... 25 more"
        ]
      }
    ]
  }
  ```

  </details>

## `get_client_additional_settings` - GET /Client/{clientId}/AdditionalSettings

```python
cv.raw.client.get_client_additional_settings('2')
```

**On the wire**

- `GET /Client/2/AdditionalSettings` -> **200** (0.12 s)

  <details><summary>Answer</summary>

  ```json
  {
    "returnValue": 0,
    "errorMsg": "",
    "regKeys": [
      {
        "displayLabel": "Account lockout threshold",
        "deleted": 0,
        "hidden": false,
        "relativepath": "CommServDB.GxGlobalParam",
        "keyName": "FailedLoginAttemptLimit",
        "comment": "",
        "type": "INTEGER",
        "value": "5",
        "enabled": 1,
        "isGlobalKey": false,
        "sourceEntity": {
          "_SubclType_": 0,
          "_type_": 0
        }
      },
      {
        "displayLabel": "bDisableInfiniteRetention",
        "deleted": 0,
        "hidden": false,
        "relativepath": "CommServDB.AdminConsole",
        "keyName": "bDisableInfiniteRetention",
        "comment": "System created",
        "type": "BOOLEAN",
        "value": "true",
        "enabled": 1,
        "isGlobalKey": false,
        "sourceEntity": {
          "_SubclType_": 0,
          "_type_": 0
        }
      },
      {
        "displayLabel": "bEnableOneWeekRetention",
        "deleted": 0,
        "hidden": false,
        "relativepath": "CommServDB.AdminConsole",
        "keyName": "bEnableOneWeekRetention",
        "comment": "System created",
        "type": "BOOLEAN",
        "value": "true",
        "enabled": 1,
        "isGlobalKey": false,
        "sourceEntity": {
          "_SubclType_": 0,
          "_type_": 0
        }
      },
      "... 6 more"
    ],
    "client": {
      "_type_": 3
    }
  }
  ```

  </details>

## `get_client_browse_fs` - GET /Client/{clientId}/browseFS

> **SKIPPED** on this run: not swept: starts work or returns a file

```python
cv.raw.client.get_client_browse_fs(...)
```

## `get_client_by_name` - GET /client/byName(clientName='{clientname}')

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.client.get_client_by_name(...)
```

## `get_client_checkreadiness` - GET /client/{clientId}/checkreadiness

> **SKIPPED** on this run: not swept: starts work or returns a file

```python
cv.raw.client.get_client_checkreadiness(...)
```

## `get_system_props_client` - GET /SystemProps/client/{clientId}

> **SKIPPED** on this run: Commvault answered: 500 - System state backup is not available. Please run system state backup to perform 1-Touch operation

```python
cv.raw.client.get_system_props_client('2')
```

**On the wire**

- `GET /SystemProps/client/2` -> **500** (1.66 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorMessage": "System state backup is not available. Please run system state backup to perform 1-Touch operation",
    "errorCode": 1
  }
  ```

  </details>

## `get_systemprops_client_by_name`

GET /systemprops/client/byName(clientName='{clientName}' )

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.client.get_systemprops_client_by_name(...)
```

## `get_systemprops_by_name`

GET /systemprops/byName(clientName='{clientName}' appName='{appName}' backupsetName='{backupsetName}' )

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.client.get_systemprops_by_name(...)
```
