# `cv.raw.client_group`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:37 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `list_client_group` - GET /ClientGroup

```python
cv.raw.client_group.list_client_group()
```

**On the wire**

- `GET /ClientGroup` -> **200** (0.15 s)

  <details><summary>Answer</summary>

  ```json
  {
    "groups": [
      {
        "flag": 528384,
        "activity": 0,
        "isCommcellGroup": false,
        "groupAssocType": 1,
        "isSmartClientGroup": true,
        "isAddinClientGroup": false,
        "edcSupportedInstanceType": 0,
        "clientCount": 1,
        "isEDCInstanceDeleted": false,
        "isDiscoveredClientGroup": false,
        "revision": "",
        "isNetworkThrottleEnabled": false,
        "name": "client-group-01",
        "clientGroupUniqueId": 3,
        "Id": 1,
        "isCompanySmartClientGroup": false,
        "isEDCInstanceAssociated": false,
        "clientGroup": {
          "clientGroupId": 1,
          "clientGroupName": "client-group-01"
        },
        "discoverRulesInfo": {
          "syncStatus": 0
        }
      },
      {
        "flag": 1052672,
        "activity": 0,
        "isCommcellGroup": false,
        "groupAssocType": 1,
        "isSmartClientGroup": true,
        "isAddinClientGroup": false,
        "edcSupportedInstanceType": 0,
        "clientCount": 0,
        "isEDCInstanceDeleted": false,
        "isDiscoveredClientGroup": false,
        "revision": "",
        "isNetworkThrottleEnabled": false,
        "name": "client-group-02",
        "clientGroupUniqueId": 4,
        "Id": 2,
        "isCompanySmartClientGroup": false,
        "isEDCInstanceAssociated": false,
        "clientGroup": {
          "clientGroupId": 2,
          "clientGroupName": "client-group-02"
        },
        "discoverRulesInfo": {
          "syncStatus": 0
        }
      },
      {
        "flag": 4096,
        "activity": 0,
        "isCommcellGroup": false,
        "groupAssocType": 1,
        "isSmartClientGroup": true,
        "isAddinClientGroup": false,
        "edcSupportedInstanceType": 0,
        "clientCount": 1,
        "isEDCInstanceDeleted": false,
        "isDiscoveredClientGroup": false,
        "revision": "",
        "isNetworkThrottleEnabled": false,
        "name": "client-group-03",
        "clientGroupUniqueId": 1,
        "Id": 3,
        "isCompanySmartClientGroup": false,
        "isEDCInstanceAssociated": false,
        "clientGroup": {
          "clientGroupId": 3,
          "clientGroupName": "client-group-03"
        },
        "discoverRulesInfo": {
          "syncStatus": 0
        }
      },
      "... 4 more"
    ]
  }
  ```

  </details>

## `get_client_group` - GET /ClientGroup/{clientGroupId}

```python
cv.raw.client_group.get_client_group('3')
```

**On the wire**

- `GET /ClientGroup/3` -> **200** (0.61 s)

  <details><summary>Answer</summary>

  ```json
  {
    "clientGroupDetail": {
      "isHtmlDescription": false,
      "configurationGroupType": 0,
      "isAddinClientGroup": false,
      "slaInterval": 0,
      "isAssemblyOverriden": false,
      "showDLP": false,
      "isEDCInstanceDeleted": false,
      "claQuota": 0,
      "enableAutoDiscovery": false,
      "forceClientSideDownload": 0,
      "isNetworkThrottleEnabled": false,
      "enableClientSideCaching": false,
      "rtoMinutes": 0,
      "isCompanySmartClientGroup": false,
      "excludeSLAReason": "",
      "description": "Selects Clients which have client-group-03 installed",
      "isSmartClientGroup": true,
      "queueConflictingJobsEnabledForCG": false,
      "userHasAgentManagementPermission": 1,
      "edcSupportedInstanceType": 0,
      "rpoMinutes": 0,
      "allowJobsToRunPastOperationWindowEnabled": false,
      "autoDiscoverVMOwner": false,
      "isRGMigrated": false,
      "isCommCellGroup": false,
      "JobPriority": 0,
      "isDiscoveredClientGroup": false,
      "excludeFromSLA": false,
      "reEnableSLAInterval": 0,
      "slaCopyFallenBehindDays": 0,
      "useSystemsubclient-01SLA": false,
      "slaCopyRedundancy": 0,
      "isEDCInstanceAssociated": false,
      "networkThrottle": {
        "enableThrottle": false
      },
      "securityAssociations": {
        "associations": [
          {
            "company": {},
            "userOrGroup": [
              {
                "userGroupName": "user-group-01",
                "userGroupId": 1,
                "_type_": 15
              }
            ],
            "properties": {
              "isCreatorAssociation": true,
              "role": {
                "_type_": 120,
                "roleId": 1,
                "roleName": "user-group-01",
                "flags": {
                  "disabled": false
                }
              }
            }
          }
        ],
        "ownerAssociations": {},
        "tagWithCompany": {
          "providerId": 0,
          "providerDomainName": "Commcell"
        }
      },
      "dlpPropertise": {
        "dlpScanIntervalMins": 0,
        "dlpStolen": false,
        "dlpEnableAutomaticDecryption": false,
        "dlpUnlockMethod": 0,
        "enableDLP": false,
        "dlpEnableClientKeys": false,
        "dlpMinFileAgeMins": 0,
        "dlpRMProperties": {
          "enableRmDLP": false,
          "dlpRmNow": false,
          "dlpRmOfflineDays": 0
        }
      },
      "appMgrServiceLiteNode": {
        "hostName": "",
        "clientName": "",
        "clientId": 0
      },
      "scgRule": {
        "op": 0,
        "rules": [
          {
            "rule": {
              "filterID": 100,
              "secValue": "Media_Agent",
              "propID": 2,
              "propType": 4,
              "value": "5"
            }
          }
        ]
      },
      "overrideHigherLevelSettings": {
        "userAccount": {
          "userName": ""
        }
      },
      "httpProxy": {},
      "clientGroup": {
        "clientGroupId": 3,
        "GUID": "0F00E7AA-74A6-4B5E-8DF6-0FB54B6EC5BA",
        "clientGroupName": "client-group-03"
      },
      "firewallConfiguration": {
        "configureFirewallSettings": false,
        "isTrivialConfig": true,
        "fwTrivialConfig": {
          "firewallTrivialDetailsCS": {
            "networkType": 1,
            "connectionType": 1,
            "proxyEntity": {
              "_SubclType_": 0,
              "_type_": 0
            }
          },
          "firewallTrivialDetailsMA": {
            "networkType": 1,
            "connectionType": 1,
            "proxyEntity": {
              "_SubclType_": 0,
              "_type_": 0
            }
          }
        },
        "firewallOptions": {
          "isRoamingClient": false,
          "extendedProperties": "<App_FirewallExtendedProperties configureAutomatically=\"1\" subclient-01OutgoingProtocol=\"2\"/>",
          "tunnelconnectionPort": 8403,
          "foreceSSL": false,
          "tunnelInitSeconds": 30,
          "lockdown": false,
          "bindOpenPortsOnly": false,
          "isDMZ": false,
          "keepAliveSeconds": 180
        }
      },
      "jobThrottleSettings": {
        "isJobThrottleEnabled": 0,
        "dataThreshold": 0,
        "excludeImmidiateJobs": 0,
        "logThreshold": 0
      },
      "clientGroupSecurity": {
        "associatedUserGroups": [
          {
            "userGroupId": 1,
            "_type_": 15,
            "userGroupName": "user-group-01"
          }
        ],
        "advancedPrivacySettings": {
          "authType": 1,
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
      "associatedClients": [
        {
          "hostName": "commserve-02",
          "clientName": "commserve-02",
          "displayName": "commserve-02",
          "clientId": 2
        }
      ],
      "powerManagementInfo": {
        "isPowerMgmtAllowed": true,
        "isPowerMgmtSupported": true
      },
      "region": {},
      "clientGroupActivityControl": {
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
            "activityType": 16,
            "enableAfterADelay": false,
            "enableActivityType": true
          }
        ]
      },
      "globalFiltersInfo": {
        "globalFiltersInfoList": [
          {
            "operatingSystemType": 1,
            "globalFilters": {}
          },
          {
            "operatingSystemType": 2,
            "globalFilters": {}
          }
        ]
      },
      "scgScope": [
        {
          "entity": {
            "commCellName": "commserve-02",
            "commCellId": 2,
            "_type_": 1
          }
        }
      ],
      "createAs": {
        "userGroup": {
          "userGroupId": 1,
          "userGroupName": "user-group-01"
        }
      },
      "MSSQLCredentialinfo": "<masked>",
      "threatIndicatorConfig": {
        "minAlertSeverity": 2,
        "recipients": "",
        "isEnabled": false
      },
      "owner": {
        "userId": 0
      },
      "tiPlan": {
        "planName": "",
        "planId": 0
      },
      "dcPlan": {
        "planName": "",
        "planId": 0
      }
    }
  }
  ```

  </details>

## `get_client_group_by_name` - GET /ClientGroup/byName(clientGroupName='{clientGroupName}')

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.client_group.get_client_group_by_name(...)
```
