# `cv.raw.alerts`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:50 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_alert_type` - GET /V4/AlertType

```python
cv.raw.alerts.get_alert_type()
```

**On the wire**

- `GET /V4/AlertType` -> **200** (0.77 s)

  <details><summary>Answer</summary>

  ```json
  {
    "alertTypes": [
      {
        "notificationOptionsAllowed": 1,
        "actionsAllowed": 39,
        "processDiscoveredVMs": false,
        "categoryType": {
          "id": 1
        },
        "criteria": {
          "name": "Job Succeeded",
          "id": 1
        },
        "category": {
          "id": 1
        }
      },
      {
        "notificationOptionsAllowed": 1,
        "actionsAllowed": 39,
        "processDiscoveredVMs": false,
        "categoryType": {
          "id": 1
        },
        "criteria": {
          "name": "Job Succeeded",
          "id": 1
        },
        "category": {
          "id": 2
        }
      },
      {
        "notificationOptionsAllowed": 177,
        "actionsAllowed": 183,
        "processDiscoveredVMs": false,
        "categoryType": {
          "id": 1
        },
        "criteria": {
          "name": "Job Succeeded",
          "id": 1
        },
        "category": {
          "id": 3
        }
      },
      "... 271 more"
    ]
  }
  ```

  </details>

## `list_alert_custom_rule` - GET /Alert/CustomRule

```python
cv.raw.alerts.list_alert_custom_rule()
```

**On the wire**

- `GET /Alert/CustomRule` -> **200** (0.89 s)

  <details><summary>Answer</summary>

  ```json
  {
    "queryEntities": [
      {
        "isQueryModifyEnabled": true,
        "visibility": 0,
        "sqlQuery": "SET NOCOUNT ON\n\n\t\t\t--------- Insert your SQL statements here \n\n\t\t\tSET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED\n\n\t\t\t-- This query is to find the Clients that are not protected in last 30 days.\n\n\t\t\t-- This is used for SLA report in health check.\n\n\t\t\tDECLARE @nProtected     INT = 0\n\n\t\t\tDECLARE @nNotProtected  INT = 0\n\n\t\t\tDECLARE @nExcluded      INT = 0\n\n\t\t\tDECLARE @clients        XML\n\n\t\t\tDECLARE ... (9493 characters)",
        "doesQuerySupportOutputFilter": true,
        "customAlertType": 3,
        "queryDescription": "Custom query to alert when SLA requirement is not met",
        "frequency": 86400,
        "isOverwriteAssociationAtAlertAllowed": true,
        "isSystemCreated": true,
        "queryCriteriaName": "Alert when CommCell SLA for last <LastNDays,1> days is less than <slaPercent,1> Percent",
        "isPrimaryKeyPresent": false,
        "isDisabled": false,
        "creator": {
          "userName": "user-01",
          "userId": 2
        },
        "securityAssociations": {
          "ownerAssociations": {},
          "tagWithCompany": {
            "providerId": 0,
            "providerDomainName": "Commcell"
          }
        },
        "commcellAssociation": {},
        "queryEntity": {
          "queryId": 2,
          "queryName": "SLA Health check"
        },
        "queryParamsList": {
          "queryParamsList": [
            {
              "defaultValue": "",
              "displayName": "",
              "className": "java.lang.Double",
              "type": "{http://host-89/2001/XMLSchema}double",
              "listType": false,
              "required": false,
              "inputName": "slaPercent",
              "minimumValue": "",
              "typeOptions": false,
              "inputType": "java.lang.Double",
              "documentation": "",
              "readOnly": false,
              "controlType": 0,
              "name": "slaPercent",
              "maximumValue": "",
              "defaultValues": [
                ""
              ]
            },
            {
              "defaultValue": "",
              "displayName": "",
              "className": "java.lang.Integer",
              "type": "{http://host-89/2001/XMLSchema}integer",
              "listType": false,
              "required": true,
              "inputName": "LastNDays",
              "minimumValue": "",
              "typeOptions": false,
              "inputType": "java.lang.Integer",
              "documentation": "",
              "readOnly": false,
              "controlType": 2,
              "name": "LastNDays",
              "maximumValue": "",
              "options": [
                "1",
                "2",
                "3",
                "... 5 more"
              ],
              "defaultValues": [
                ""
              ]
            }
          ]
        },
        "queryOutputColumns": [
          {
            "isColumnFilterable": false,
            "lmDataType": 0,
            "isPrimaryKey": false,
            "columnFriendlyName": "SLA Percent",
            "columnName": "SLAPercent",
            "columnAdditionalDetails": {},
            "supportedOpTypes": [
              0,
              1,
              4,
              "... 3 more"
            ]
          }
        ]
      },
      {
        "isQueryModifyEnabled": true,
        "visibility": 0,
        "sqlQuery": "SET NOCOUNT ON\r\n\r\n--------- Insert your SQL statements here \r\n\r\nSET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED\r\n\r\nSELECT jobID, UserName , clientId, appTypeId, instance, backupSet, applicationId, CONVERT (nvarchar(max), ROUND((CONVERT (float,uncompBytes)/POWER(2,30)),2))+' GB' as 'BackedupSize'\r\n\r\nFROM RunningBackups  \r\n\r\nWHERE CONVERT (float,uncompBytes) / POWER(2,30) >= @maxSize AND (userId=@u... (523 characters)",
        "doesQuerySupportOutputFilter": true,
        "customAlertType": 3,
        "queryDescription": "Custom query for sending alert when size of data being backed up exceeds X GB",
        "frequency": 86400,
        "isOverwriteAssociationAtAlertAllowed": true,
        "isSystemCreated": true,
        "queryCriteriaName": "Threshold size of data in GB<maxSize,1>",
        "isPrimaryKeyPresent": true,
        "isDisabled": false,
        "creator": {
          "userName": "user-01",
          "userId": 2
        },
        "securityAssociations": {
          "ownerAssociations": {},
          "tagWithCompany": {
            "providerId": 0,
            "providerDomainName": "Commcell"
          }
        },
        "commcellAssociation": {},
        "queryEntity": {
          "queryId": 3,
          "queryName": "Backup exceeds X GB"
        },
        "queryParamsList": {
          "queryParamsList": [
            {
              "defaultValue": "5",
              "displayName": "Threshold Size (GB)",
              "className": "java.lang.Float",
              "type": "{http://host-89/2001/XMLSchema}float",
              "listType": false,
              "required": true,
              "inputName": "maxSize",
              "minimumValue": "1",
              "typeOptions": false,
              "inputType": "java.lang.Float",
              "documentation": "",
              "readOnly": false,
              "controlType": 0,
              "name": "maxSize",
              "maximumValue": "",
              "defaultValues": [
                ""
              ]
            }
          ]
        },
        "queryOutputColumns": [
          {
            "isColumnFilterable": true,
            "lmDataType": 0,
            "isPrimaryKey": true,
            "columnFriendlyName": "JobID",
            "columnName": "jobID",
            "columnAdditionalDetails": {},
            "supportedOpTypes": [
              0,
              1,
              4,
              "... 3 more"
            ]
          },
          {
            "isColumnFilterable": true,
            "lmDataType": 1,
            "isPrimaryKey": false,
            "columnFriendlyName": "User",
            "columnName": "UserName",
            "columnAdditionalDetails": {},
            "supportedOpTypes": [
              2,
              3,
              0,
              "... 1 more"
            ]
          },
          {
            "isColumnFilterable": true,
            "lmDataType": 14,
            "isPrimaryKey": false,
            "columnFriendlyName": "Client",
            "columnName": "clientId",
            "columnAdditionalDetails": {},
            "supportedOpTypes": [
              9
            ]
          },
          "... 5 more"
        ]
      },
      {
        "isQueryModifyEnabled": true,
        "visibility": 1,
        "sqlQuery": "\n\n\tIF object_id('tempdb.dbo.#AppsExcluded') IS NOT NULL DROP TABLE #AppsExcluded\n\n\tIF object_id('tempdb.dbo.#tmpDetails') is not null DROP TABLE #tmpDetails\n\n\tIF object_id('tempdb.dbo.#tempValidApps') is not null DROP TABLE #tempValidApps\n\n\tIF object_id('tempdb.dbo.#tempSCIndexBS') is not null DROP TABLE #tempSCIndexBS\n\n\tDECLARE @curTime BIGINT = dbo.GetUnixTime(GETUTCDATE())\n\n\t--DECLARE @userId I... (8730 characters)",
        "isRuleAssociatedWithAlert": true,
        "doesQuerySupportOutputFilter": true,
        "customAlertType": 3,
        "queryDescription": "",
        "frequency": 86400,
        "isOverwriteAssociationAtAlertAllowed": true,
        "isSystemCreated": false,
        "queryCriteriaName": "Index backup status",
        "isPrimaryKeyPresent": false,
        "isDisabled": false,
        "creator": {
          "userName": "user-02",
          "userId": 1
        },
        "securityAssociations": {
          "ownerAssociations": {},
          "tagWithCompany": {
            "providerId": 0,
            "providerDomainName": "Commcell"
          }
        },
        "commcellAssociation": {},
        "additionalQueryDetails": {
          "querySeverity": 1,
          "alertType": 0,
          "isHealthParam": false,
          "alertCriteria": 0,
          "defaultTextTemplate": "",
          "defaultHtmlTemplate": "",
          "externalQueryEntity": {
            "_type_": 125
          },
          "scriptDescription": {
            "reportName": "Index backup status",
            "description": "",
            "revision": "",
            "guid": "13762C34-F869-4C08-B60C-16AAB2E1B567"
          }
        },
        "security": {
          "associatedUserGroups": [
            {
              "userGroupId": 1,
              "userGroupName": "master"
            }
          ]
        },
        "queryEntity": {
          "queryId": 6,
          "queryName": "Index backup status"
        },
        "queryOutputColumns": [
          {
            "isColumnFilterable": false,
            "lmDataType": 1,
            "isPrimaryKey": false,
            "columnFriendlyName": "ClientName",
            "columnName": "ClientName",
            "columnAdditionalDetails": {
              "includeInAlertOutput": true
            },
            "supportedOpTypes": [
              2,
              3,
              0,
              "... 1 more"
            ]
          },
          {
            "isColumnFilterable": false,
            "lmDataType": 1,
            "isPrimaryKey": false,
            "columnFriendlyName": "Agent",
            "columnName": "Agent",
            "columnAdditionalDetails": {
              "includeInAlertOutput": true
            },
            "supportedOpTypes": [
              2,
              3,
              0,
              "... 1 more"
            ]
          },
          {
            "isColumnFilterable": false,
            "lmDataType": 1,
            "isPrimaryKey": false,
            "columnFriendlyName": "BackupsetName",
            "columnName": "BackupsetName",
            "columnAdditionalDetails": {
              "includeInAlertOutput": true
            },
            "supportedOpTypes": [
              2,
              3,
              0,
              "... 1 more"
            ]
          },
          "... 5 more"
        ]
      },
      "... 24 more"
    ]
  }
  ```

  </details>

## `list_alert_definitions` - GET /V4/AlertDefinitions

```python
cv.raw.alerts.list_alert_definitions()
```

**On the wire**

- `GET /V4/AlertDefinitions` -> **200** (0.25 s)

  <details><summary>Answer</summary>

  ```json
  {
    "alertDefinitions": [
      {
        "name": "Air Gap Protect",
        "id": 1,
        "type": "License",
        "category": "Configuration",
        "enabled": true,
        "company": {
          "name": "",
          "id": 0
        }
      },
      {
        "name": "No Index Backup in last 30 days",
        "id": 2,
        "type": "Index backup status",
        "category": "Custom Rules",
        "enabled": true,
        "company": {
          "name": "",
          "id": 0
        }
      },
      {
        "name": "Index State",
        "id": 3,
        "type": "Index State",
        "category": "Custom Rules",
        "enabled": true,
        "company": {
          "name": "",
          "id": 0
        }
      },
      "... 76 more"
    ]
  }
  ```

  </details>

## `list_triggered_alerts` - GET /V4/TriggeredAlerts

```python
cv.raw.alerts.list_triggered_alerts()
```

**On the wire**

- `GET /V4/TriggeredAlerts` -> **200** (0.08 s)

  <details><summary>Answer</summary>

  ```json
  {
    "unreadCount": 0,
    "totalCount": 0,
    "alertsTriggered": []
  }
  ```

  </details>

## `get_alert_custom_rule` - GET /Alert/CustomRule/{alertRuleId}

```python
cv.raw.alerts.get_alert_custom_rule('2')
```

**On the wire**

- `GET /Alert/CustomRule/2` -> **200** (0.18 s)

  <details><summary>Answer</summary>

  ```json
  {
    "queryEntities": [
      {
        "isQueryModifyEnabled": true,
        "visibility": 0,
        "sqlQuery": "SET NOCOUNT ON\n\n\t\t\t--------- Insert your SQL statements here \n\n\t\t\tSET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED\n\n\t\t\t-- This query is to find the Clients that are not protected in last 30 days.\n\n\t\t\t-- This is used for SLA report in health check.\n\n\t\t\tDECLARE @nProtected     INT = 0\n\n\t\t\tDECLARE @nNotProtected  INT = 0\n\n\t\t\tDECLARE @nExcluded      INT = 0\n\n\t\t\tDECLARE @clients        XML\n\n\t\t\tDECLARE ... (9493 characters)",
        "doesQuerySupportOutputFilter": true,
        "customAlertType": 3,
        "queryDescription": "Custom query to alert when SLA requirement is not met",
        "frequency": 86400,
        "isOverwriteAssociationAtAlertAllowed": true,
        "isSystemCreated": true,
        "queryCriteriaName": "Alert when CommCell SLA for last <LastNDays,1> days is less than <slaPercent,1> Percent",
        "isPrimaryKeyPresent": false,
        "isDisabled": false,
        "creator": {
          "userName": "user-01",
          "userId": 2
        },
        "securityAssociations": {
          "ownerAssociations": {},
          "tagWithCompany": {
            "providerId": 0,
            "providerDomainName": "Commcell"
          }
        },
        "commcellAssociation": {},
        "queryEntity": {
          "queryId": 2,
          "queryName": "SLA Health check"
        },
        "queryParamsList": {
          "queryParamsList": [
            {
              "defaultValue": "",
              "displayName": "",
              "className": "java.lang.Double",
              "type": "{http://host-89/2001/XMLSchema}double",
              "listType": false,
              "required": false,
              "inputName": "slaPercent",
              "minimumValue": "",
              "typeOptions": false,
              "inputType": "java.lang.Double",
              "documentation": "",
              "readOnly": false,
              "controlType": 0,
              "name": "slaPercent",
              "maximumValue": "",
              "defaultValues": [
                ""
              ]
            },
            {
              "defaultValue": "",
              "displayName": "",
              "className": "java.lang.Integer",
              "type": "{http://host-89/2001/XMLSchema}integer",
              "listType": false,
              "required": true,
              "inputName": "LastNDays",
              "minimumValue": "",
              "typeOptions": false,
              "inputType": "java.lang.Integer",
              "documentation": "",
              "readOnly": false,
              "controlType": 2,
              "name": "LastNDays",
              "maximumValue": "",
              "options": [
                "1",
                "2",
                "3",
                "... 5 more"
              ],
              "defaultValues": [
                ""
              ]
            }
          ]
        },
        "queryOutputColumns": [
          {
            "isColumnFilterable": false,
            "lmDataType": 0,
            "isPrimaryKey": false,
            "columnFriendlyName": "SLA Percent",
            "columnName": "SLAPercent",
            "columnAdditionalDetails": {},
            "supportedOpTypes": [
              0,
              1,
              4,
              "... 3 more"
            ]
          }
        ]
      }
    ]
  }
  ```

  </details>

## `get_alert_definition` - GET /V4/AlertDefinitions/{id}

```python
cv.raw.alerts.get_alert_definition('1')
```

**On the wire**

- `GET /V4/AlertDefinitions/1` -> **200** (0.17 s)

  <details><summary>Answer</summary>

  ```json
  {
    "alertSeverity": 0,
    "sendIndividualNotifications": true,
    "subscriptionBasedAlert": false,
    "name": "Air Gap Protect",
    "id": 1,
    "processDiscoveredVMs": false,
    "templates": {
      "messages": [
        {
          "format": "HTML",
          "textContent": "<SUBJECT BEGIN> Alert: <ALERT NAME> Type: <ALERT CATEGORY - ALERT TYPE> <IS ESCALATED?> <SUBJECT END> MsgNewLine_ Alert: <ALERT NAME> MsgNewLine_ Type: <ALERT CATEGORY - ALERT TYPE> MsgNewLine_MsgTab_ Detected Criteria: <DETECTED CRITERIA> MsgNewLine_MsgTab_ Detected Time: <TIME> MsgNewLine_MsgTab_ CommCell: <COMMCELL NAME> MsgNewLine_MsgTab_ User: <USER NAME> MsgNewLine_ MsgNewLine_ MsgTab_Commen... (569 characters)",
          "type": "EMAIL",
          "htmlContent": "<SUBJECT BEGIN> Alert: <ALERT NAME> Type: <ALERT CATEGORY - ALERT TYPE> <IS ESCALATED?> <SUBJECT END><div id=\"contentTbl-table-scroll\">\n\n\t <table cellspacing=\"0\" cellpadding=\"0\" width=\"100%\" style=\"border-top-color: #2f4e66; border-top-style: solid; border-top-width: 1px; border-right-color: #2f4e66; border-right-style: solid; border-right-width: 1px; border-bottom-color: #2f4e66; border-bottom-st... (4684 characters)"
        }
      ],
      "locale": {
        "name": "English",
        "id": 0
      }
    },
    "alertSummary": {
      "type": {
        "name": "License",
        "id": 60
      },
      "category": {
        "name": "Configuration",
        "id": 2
      },
      "criteriaList": [
        {
          "name": "Alert CommServe License Expires Within <7,15,30,0,-1> Days",
          "id": 58,
          "notificationCriteria": {
            "delayTime": 0,
            "value": 1,
            "persistTime": 0
          },
          "paramsList": [
            {
              "unit": 15,
              "type": 7,
              "value": 60,
              "paramIndex": 0
            }
          ]
        }
      ]
    },
    "alertTarget": {
      "recipients": {
        "webHookGUID": "",
        "webHookId": 0,
        "cc": [],
        "bcc": [],
        "to": []
      },
      "sendAlertTo": [
        "EMAIL",
        "CONTENT_INDEX"
      ]
    },
    "tokens": "<masked>",
    "company": {
      "name": "",
      "id": 0
    }
  }
  ```

  </details>

## `get_triggered_alert` - GET /V4/TriggeredAlerts/{id}

> **SKIPPED** on this run: Commvault answered: 403 - You do not have permission to access this triggered alert.

```python
cv.raw.alerts.get_triggered_alert('2')
```

**On the wire**

- `GET /V4/TriggeredAlerts/2` -> **403** (0.13 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorMessage": "You do not have permission to access this triggered alert.",
    "errorCode": 587204969
  }
  ```

  </details>
