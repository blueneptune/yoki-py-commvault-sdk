# `cv.raw.alert`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:37 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_log_streaming_connector_templates` - GET /LogStreamingConnector/Templates

```python
cv.raw.alert.get_log_streaming_connector_templates()
```

**On the wire**

- `GET /LogStreamingConnector/Templates` -> **200** (0.07 s)

  <details><summary>Answer</summary>

  ```json
  {
    "templates": [
      {
        "name": "subclient-01",
        "policyTemplates": [
          {
            "template": "{\n    \"Alert Id\" : \"<ALERTID>\",\n    \"Alert name\" : \"<ALERTNAME>\",\n    \"Detected time\" : \"<ALERTTIME>\",\n    \"Severity\" : \"<ALERTSEVERITY>\",\n    \"Job Id\" : \"<JOBID>\",\n    \"Description\" : \"<ALERTDESCRIPTION>\",\n    \"Commcell name\" : \"<COMMCELLNAME>\",\n    \"Company name\" : \"<COMPANYNAME>\",\n    \"UTC Timestamp\" : \"<UTCTIMESTAMP>\"\n}",
            "dataType": 2,
            "syslogTemplate": "<<PRIVAL>>1 <FULL-DATE>T<FULL-TIME>Z <HOSTNAME> Commserver <PROCID> Alert [Alert@14604 AlertId=\"<ALERTID>\" AlertName=\"<ALERTNAME>\" DetectedTime=\"<ALERTTIME>\" JobId=\"<JOBID>\" CommcellName=\"<COMMCELLNAME>\" CompanyName=\"<COMPANYNAME>\" UTCTimestamp=\"<UTCTIMESTAMP>\"] <ALERTDESCRIPTION>"
          },
          {
            "template": "{\n    \"OpId\" : \"<OPID>\",\n    \"Audit Time\" : \"<AUDITTIME>\",\n    \"Severity\" : \"<SEVERITYLEVEL>\",\n    \"User\" : \"<USERNAME>\",\n    \"Operation\" : \"<OPERATION>\",\n    \"Details\" : \"<DETAILS>\",\n    \"Commcell name\" : \"<COMMCELLNAME>\",\n    \"Company name\" : \"<COMPANYNAME>\",\n    \"UTC Timestamp\" : \"<UTCTIMESTAMP>\"\n}",
            "dataType": 1,
            "syslogTemplate": "<<PRIVAL>>1 <FULL-DATE>T<FULL-TIME>Z <HOSTNAME> Commserver <PROCID> Audit [Audit@14604 OpId=\"<OPID>\" AuditTime=\"<AUDITTIME>\" User=\"<USERNAME>\" Operation=\"<OPERATION>\" CommcellName=\"<COMMCELLNAME>\" CompanyName=\"<COMPANYNAME>\" UTCTimestamp=\"<UTCTIMESTAMP>\"] <DETAILS>"
          },
          {
            "template": "{\n    \"Event Id\" : \"<EVENTID>\",\n    \"Occurrence Time\" : \"<OCCURRENCETIME>\",\n    \"Severity\" : \"<EVENTSEVERITY>\",\n    \"Computer\" : \"<COMPUTER>\",\n    \"Program\" : \"<PROGRAM>\",\n    \"Event Code\" : \"<EVENTCODE>\",\n    \"Description\" : \"<DESCRIPTION>\",\n    \"Commcell name\" : \"<COMMCELLNAME>\",\n    \"UTC Timestamp\" : \"<UTCTIMESTAMP>\"\n}",
            "dataType": 4,
            "syslogTemplate": "<<PRIVAL>>1 <FULL-DATE>T<FULL-TIME>Z <HOSTNAME> Commserver <PROCID> Event [Event@14604 EventId=\"<EVENTID>\" OccurrenceTime=\"<OCCURRENCETIME>\" Computer=\"<COMPUTER>\" Program=\"<PROGRAM>\" EventCode=\"<EVENTCODE>\" CommcellName=\"<COMMCELLNAME>\" UTCTimestamp=\"<UTCTIMESTAMP>\"] <DESCRIPTION>"
          }
        ]
      }
    ]
  }
  ```

  </details>

## `list_alert` - GET /Alert

```python
cv.raw.alert.list_alert()
```

**On the wire**

- `GET /Alert` -> **200** (0.10 s)

  <details><summary>Answer</summary>

  ```json
  {}
  ```

  </details>

## `list_alert_rule` - GET /AlertRule

```python
cv.raw.alert.list_alert_rule()
```

**On the wire**

- `GET /AlertRule` -> **200** (0.26 s)

  <details><summary>Answer</summary>

  ```json
  {
    "myReceiveTotal": 79,
    "filterQueryCount": 0,
    "myCreatedTotal": 0,
    "alertList": [
      {
        "notifType": 131073,
        "GUID": "",
        "description": "Air Gap Protect Alert when license about to expire",
        "commcellName": "",
        "escNotifType": 0,
        "organizationId": 0,
        "createdTime": 1787248182,
        "commcellGuid": "",
        "origCCId": 0,
        "status": 2064,
        "creator": {
          "name": "user-02",
          "id": 1
        },
        "alertType": {
          "name": "License",
          "id": 60
        },
        "globalConfigInfo": {},
        "alert": {
          "name": "Air Gap Protect",
          "id": 1
        },
        "organization": {
          "companyId": 0
        },
        "alertCategory": {
          "name": "Configuration",
          "id": 2
        }
      },
      {
        "notifType": 139265,
        "GUID": "",
        "description": "subclient-01 alert for no successful index backup in the last 30 days",
        "commcellName": "",
        "escNotifType": 0,
        "organizationId": 0,
        "createdTime": 1787248218,
        "commcellGuid": "",
        "origCCId": 0,
        "status": 2048,
        "creator": {
          "name": "user-02",
          "id": 1
        },
        "alertType": {
          "name": "Index backup status",
          "id": 6
        },
        "globalConfigInfo": {},
        "alert": {
          "name": "No Index Backup in last 30 days",
          "id": 2
        },
        "organization": {
          "companyId": 0
        },
        "alertCategory": {
          "name": "Custom Rules",
          "id": 9
        }
      },
      {
        "notifType": 139265,
        "GUID": "",
        "description": "subclient-01 alert for error status of index",
        "commcellName": "",
        "escNotifType": 0,
        "organizationId": 0,
        "createdTime": 1787248218,
        "commcellGuid": "",
        "origCCId": 0,
        "status": 2048,
        "creator": {
          "name": "user-02",
          "id": 1
        },
        "alertType": {
          "name": "Index State",
          "id": 7
        },
        "globalConfigInfo": {},
        "alert": {
          "name": "Index State",
          "id": 3
        },
        "organization": {
          "companyId": 0
        },
        "alertCategory": {
          "name": "Custom Rules",
          "id": 9
        }
      },
      "... 76 more"
    ]
  }
  ```

  </details>

## `list_log_streaming_connector` - GET /LogStreamingConnector

```python
cv.raw.alert.list_log_streaming_connector()
```

**On the wire**

- `GET /LogStreamingConnector` -> **200** (0.10 s)

  <details><summary>Answer</summary>

  ```json
  {}
  ```

  </details>

## `get_alert` - GET /Alert/{liveFeedId}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.alert.get_alert(...)
```

## `get_alert_rule` - GET /AlertRule/{alertId2}

```python
cv.raw.alert.get_alert_rule('1')
```

**On the wire**

- `GET /AlertRule/1` -> **200** (0.18 s)

  <details><summary>Answer</summary>

  ```json
  {
    "alertDetail": {
      "alertSeverity": 0,
      "queryId": 0,
      "escalationSeverity": 0,
      "subscriptionBased": false,
      "queryHasDynamicRecipients": false,
      "senderEmailId": "",
      "checkForEventParams": 0,
      "alertTokenRuleGroupXml": "<masked>",
      "sendIndividualNotificationForVM": false,
      "webhookGUID": "",
      "sendIndividualNotification": true,
      "eventCriteriaXML": "",
      "enabled": true,
      "senderDisplayName": "",
      "customQueryDetailsXml": "",
      "webhookId": 0,
      "queryReturnsHTMLFormattedOutput": false,
      "xmlEntityList": "<?xml version='1.0' encoding='utf-8' ?><CVGui_CommCellTreeNode><clients includeAll=\"0\"/><clientGroups includeAll=\"0\"/><libraries includeAll=\"0\"/><mediaAgents includeAll=\"0\"/><storagePolcies includeAll=\"0\"/><trackingPolicies includeAll=\"0\"/><trackingSchedules/><trackingJobs/><criterias includeAll=\"0\"/><workflows includeAll=\"0\"/><commcells includeAll=\"0\"/><replicationPairs includeAll=\"0\"/><blrPairs ... (441 characters)",
      "minJobCountForJobAnomaly": 0,
      "recipient": "",
      "periodicNotificationInterval": 0,
      "securityAssociations": {
        "ownerAssociations": {},
        "tagWithCompany": {
          "providerId": 0,
          "providerDomainName": "Commcell"
        }
      },
      "criteria": [
        {
          "reportId": 0,
          "criteriaId": 58,
          "esclationLevel": 1,
          "persistTimeSeconds": 0,
          "reportingOptions": 1,
          "selCriteriaId": 0,
          "criteriaSeverity": 0,
          "alertId": 0,
          "delayTimeSeconds": 0,
          "value": "Alert CommServe License Expires Within <7,15,30,0,-1> Days",
          "taskId": 0,
          "criteriaParams": [
            {
              "unit": 15,
              "type": 7,
              "value": 60,
              "paramIndex": 0
            }
          ]
        }
      ],
      "criteriasSelected": [
        58
      ],
      "regularNotifications": [
        1,
        131072
      ],
      "notifMsgs": [
        {
          "notifOptions": 0,
          "notifType": 1,
          "esclationLevel": 1,
          "notifMessage": "<SUBJECT BEGIN> Alert: <ALERT NAME> Type: <ALERT CATEGORY - ALERT TYPE> <IS ESCALATED?> <SUBJECT END> MsgNewLine_ Alert: <ALERT NAME> MsgNewLine_ Type: <ALERT CATEGORY - ALERT TYPE> MsgNewLine_MsgTab_ Detected Criteria: <DETECTED CRITERIA> MsgNewLine_MsgTab_ Detected Time: <TIME> MsgNewLine_MsgTab_ CommCell: <COMMCELL NAME> MsgNewLine_MsgTab_ User: <USER NAME> MsgNewLine_ MsgNewLine_ MsgTab_Commen... (569 characters)",
          "messageFormat": 1,
          "notifMessageHtml": "<SUBJECT BEGIN> Alert: <ALERT NAME> Type: <ALERT CATEGORY - ALERT TYPE> <IS ESCALATED?> <SUBJECT END><div id=\"contentTbl-table-scroll\">\n\n\t <table cellspacing=\"0\" cellpadding=\"0\" width=\"100%\" style=\"border-top-color: #2f4e66; border-top-style: solid; border-top-width: 1px; border-right-color: #2f4e66; border-right-style: solid; border-right-width: 1px; border-bottom-color: #2f4e66; border-bottom-st... (4684 characters)",
          "localeId": 0,
          "saveAlertToDisk": {
            "alertLocation": "",
            "cvpassword": "",
            "useNetworkShare": 0,
            "loginName": "",
            "impersonateUser": 0,
            "saveAlertCredentials": "<masked>"
          },
          "feeds": {
            "seperateIndex": false,
            "baseLocation": "",
            "selectedChannel": "",
            "rssFeedLocation": ""
          },
          "entity": {
            "_SubclType_": 0,
            "_type_": 0
          }
        },
        {
          "notifOptions": 0,
          "notifType": 131072,
          "esclationLevel": 1,
          "notifMessage": "<SUBJECT BEGIN> Alert: <ALERT NAME> Type: <ALERT CATEGORY - ALERT TYPE> <IS ESCALATED?> <SUBJECT END> MsgNewLine_ Alert: <ALERT NAME> MsgNewLine_ Type: <ALERT CATEGORY - ALERT TYPE> MsgNewLine_MsgTab_ Detected Criteria: <DETECTED CRITERIA> MsgNewLine_MsgTab_ Detected Time: <TIME> MsgNewLine_MsgTab_ CommCell: <COMMCELL NAME> MsgNewLine_MsgTab_ User: <USER NAME> MsgNewLine_ MsgNewLine_ MsgTab_Commen... (569 characters)",
          "messageFormat": 0,
          "notifMessageHtml": "<SUBJECT BEGIN> Alert: <ALERT NAME> Type: <ALERT CATEGORY - ALERT TYPE> <IS ESCALATED?> <SUBJECT END> MsgNewLine_ Alert: <ALERT NAME> MsgNewLine_ Type: <ALERT CATEGORY - ALERT TYPE> MsgNewLine_MsgTab_ Detected Criteria: <DETECTED CRITERIA> MsgNewLine_MsgTab_ Detected Time: <TIME> MsgNewLine_MsgTab_ CommCell: <COMMCELL NAME> MsgNewLine_MsgTab_ User: <USER NAME> MsgNewLine_ MsgNewLine_ MsgTab_Commen... (569 characters)",
          "localeId": 0,
          "saveAlertToDisk": {
            "alertLocation": "",
            "cvpassword": "",
            "useNetworkShare": 0,
            "loginName": "",
            "impersonateUser": 0,
            "saveAlertCredentials": "<masked>"
          },
          "feeds": {
            "seperateIndex": false,
            "baseLocation": "",
            "selectedChannel": "",
            "rssFeedLocation": ""
          },
          "entity": {
            "_SubclType_": 0,
            "_type_": 0
          }
        }
      ],
      "locale": {
        "localeName": "English",
        "localeID": 0
      },
      "alert": {
        "notifType": 131073,
        "GUID": "85FD9C27-CD62-4280-BE2D-B17E66E52763",
        "description": "",
        "commcellName": "",
        "escNotifType": 0,
        "organizationId": 0,
        "createdTime": 0,
        "commcellGuid": "",
        "origCCId": 2,
        "status": 2064,
        "creator": {
          "name": "",
          "id": 0
        },
        "alertType": {
          "name": "License",
          "id": 60
        },
        "globalConfigInfo": {},
        "alert": {
          "name": "Air Gap Protect",
          "id": 1
        },
        "organization": {
          "_type_": 189
        },
        "alertCategory": {
          "name": "Configuration",
          "id": 2
        }
      },
      "reportingParams": {
        "persistTimeSeconds": 0,
        "reportingOptions": 0,
        "delayTimeSeconds": 0
      },
      "appTypeFilters": {},
      "alertProperties": {
        "property": [
          {
            "propName": "Alert Token Rule Xml",
            "propValue": [
              "<?xml version=\"1.0\" encoding=\"UTF-8\"?><CVGui_AlertTokenRuleGroup groupOperator=\"0\"><rules groupOperator=\"0\"><rules groupOperator=\"2\"><alertTokenRule tokenMessage=\"COMMENT\" tokenId=\"1241514047\" tokenType=\"1\" tokenFormat=\"0\" value=\"Air Gap Protect\" tokenOperator=\"2\" /></rules></rules></CVGui_AlertTokenRuleGroup>"
            ]
          }
        ]
      }
    }
  }
  ```

  </details>

## `get_log_streaming_connector` - GET /LogStreamingConnector/{id}

> **SKIPPED** on this run: Commvault answered: 500

```python
cv.raw.alert.get_log_streaming_connector('2')
```

**On the wire**

- `GET /LogStreamingConnector/2` -> **500** (0.08 s)

  <details><summary>Answer</summary>

  (no body)

  </details>
