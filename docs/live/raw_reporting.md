# `cv.raw.reporting`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:37 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_allreports` - GET /cr/reportsplusengine/reports

```python
cv.raw.reporting.get_allreports()
```

**On the wire**

- `GET /cr/reportsplusengine/reports?icludeDrafts=false&includeStoreVersions=false&includeMetricsReports=false` -> **200** (0.47 s)

  <details><summary>Answer</summary>

  ```json
  {
    "reports": [
      {
        "reportId": 60,
        "userReportId": "Commcell Split",
        "reportName": "Commcell Split",
        "description": "Commcell split summary report",
        "version": 1,
        "guid": "0e171b25-363d-4c67-bee4-b9dda333ada3",
        "revision": "$Revision: 192.0.2.9 $",
        "flags": 1152,
        "engineVersion": 1,
        "deployed": true,
        "deployedVersion": 1,
        "viewable": true,
        "editable": true,
        "icon": "vertical-bar.png",
        "translations": {},
        "remoteRevision": "",
        "whatsNew": "",
        "tags": "Commcell Split",
        "reportSource": 1,
        "customIcon": {},
        "packageId": 0,
        "isMetrics": 0
      },
      {
        "reportId": 107,
        "userReportId": "CorruptedJobsOnSourceCopy",
        "reportName": "Failed to be Copied jobs on Source copy",
        "description": "Failed to be copied jobs on source copy resulting in Fallen Behind auxiliary copies",
        "version": 1,
        "guid": "e7951127-e013-469f-9326-b26982fad80e",
        "revision": "$Revision: 192.0.2.3 $",
        "flags": 1152,
        "engineVersion": 1,
        "deployed": true,
        "deployedVersion": 1,
        "viewable": true,
        "editable": true,
        "icon": "data-table.png",
        "translations": {},
        "remoteRevision": "",
        "whatsNew": "",
        "tags": "",
        "reportSource": 1,
        "customIcon": {},
        "packageId": 0,
        "isMetrics": 0
      },
      {
        "reportId": 196,
        "userReportId": "client-group-01 Resource Utilization",
        "reportName": "client-group-01 Resource Utilization",
        "description": "Report gives a consolidated view of the load on Commvault client-group-01 entities (CommServer, MediaAgents, IndexServers, Access Nodes )",
        "version": 1,
        "guid": "87a51888-6859-4c00-9fc1-ea4d3ce7fbef",
        "revision": "$Revision: 192.0.2.17 $",
        "flags": 1152,
        "engineVersion": 1,
        "deployed": true,
        "deployedVersion": 1,
        "viewable": true,
        "editable": true,
        "icon": "data-table.png",
        "translations": {},
        "remoteRevision": "",
        "whatsNew": "",
        "tags": "Monitoring,Configuration",
        "reportSource": 1,
        "customIcon": {
          "type": "SVG",
          "content": "<svg\n\txmlns=\"http://host-89/2000/svg\" width=\"35\" height=\"35\" viewBox=\"0 0 35 35\">\n\t<defs>\n\t\t<style>.client-group-01-load-custom-icon-cls-1{fill:#394c5b;}.client-group-01-load-custom-icon-cls-2{fill:#2d2c2c;}.client-group-01-load-custom-icon-cls-3{fill:#2567a0;stroke:#2567a0;stroke-miterlimit:10;stroke-width:0.25px;}</style>\n\t</defs>\n\t<g id=\"IXv5lA.tif\">\n\t\t<path class=\"client-group-01-load-custom-i... (2117 characters)"
        },
        "packageId": 0,
        "isMetrics": 0
      },
      "... 20 more"
    ],
    "userHistory": []
  }
  ```

  </details>

## `get_cr_reportsplusengine_datasets` - GET /cr/reportsplusengine/datasets

```python
cv.raw.reporting.get_cr_reportsplusengine_datasets()
```

**On the wire**

- `GET /cr/reportsplusengine/datasets` -> **200** (0.20 s)

  <details><summary>Answer</summary>

  ```json
  {
    "dataSet": [
      {
        "dataSet": {
          "dataSetId": 2428,
          "dataSetName": "AuditTrailDataset",
          "dataSetGuid": "2b3e43c0-21fe-401d-ebf8-c485309262a7"
        },
        "endpoint": "DATABASE",
        "shared": true,
        "dataSources": [
          {
            "dataSource": {
              "dataSourceName": ""
            },
            "connectionType": "COMMCELL",
            "commCell": {
              "commCellName": "commcell-02"
            },
            "databaseName": ""
          }
        ],
        "allColumns": false,
        "fields": [
          {
            "name": "sys_rowid",
            "dataField": "$row_number$",
            "type": "String"
          },
          {
            "name": "Data Source",
            "dataField": "Data Source",
            "type": "String"
          },
          {
            "name": "ID",
            "dataField": "ID",
            "type": "Integer"
          },
          "... 6 more"
        ],
        "GetOperation": {
          "parameters": [
            {
              "name": "serachString",
              "dataType": "String",
              "values": [
                "=input.SearchString"
              ]
            },
            {
              "name": "playbackLevel",
              "dataType": "Integer",
              "values": [
                "4"
              ],
              "required": true
            },
            {
              "name": "TimeRange",
              "dataType": "DateRange",
              "isList": false,
              "values": [
                "=input.TimeRange"
              ]
            },
            "... 2 more"
          ],
          "sqlText": "--declare @sys_userid int =1\n--declare @sys_locale varchar(max) = 'en',@serachString varchar(max) = '' ,@playbackLevel int = 4,\n--@TimeRange_from datetime = getdate() -900 ,@TimeRange_to datetime = getdate()\n--declare @userlist table (userlist int)\n--declare @usergrouplist table (usergrouplist int)\n\nIF OBJECT_ID('tempdb.dbo.#TEGAM') IS NOT NULL DROP TABLE #TEGAM\n  CREATE TABLE #TEGAM ( opId INT )\n... (19073 characters)",
          "timeout": 5,
          "postQueryFilter": true,
          "rDataSetQuery": "",
          "rPlotQuery": ""
        },
        "description": "will show the audit details by honoring user security and selected filters",
        "databaseName": "CommServ",
        "deployed": true,
        "queryPlan": {
          "offline": false,
          "collectionType": "HTTP",
          "retentionDays": 1,
          "dynamicCollection": false,
          "frequency": 60,
          "direct": false
        },
        "version": 1,
        "guid": "2b3e43c0-21fe-401d-ebf8-c485309262a7",
        "hidden": false,
        "readOnly": false,
        "revision": "$Revision: 192.0.2.28 $",
        "visibleAll": true,
        "computedColumns": {
          "scriptName": "R",
          "script": ""
        },
        "visibleToTenantAdmins": true,
        "builtIn": true,
        "systemDataSet": false,
        "signature": "<masked>",
        "definition": "IyBTSEEtNTEyIFJTQSBFTVNBLVBLQ1MxLXYxXzUgU2lnbmF0dXJlDQojIGh0dHA6Ly93d3cuYXBwcy5pZXRmLm9yZy9yZmMvcmZjMzQ0Ny5odG1sI3NlYy05LjINCg0KNjBlZjYyNjEwMzJhYjAwYTNkMjMzMmMwNjc3YWUzOTc2OTI1ZjgwZGVkZTM4NTEyZDg2Y2Y5MWRhOWExDQoyNDQyMTNiNjI4MmU3Zjg2YzJlNmM3ZDQxNGViM2UxOWQ4MGY0MzI5ODNkZDUyN2M3YmNmMTA3MDQyOTcNCmU1NTMxYjY0YjJmYjZjZWM1MTBkZDUxMDVjYzFlZTFjMWIzNmM3NTJlZjI2YzZiOWQ3YTIwNWY5YjYyNQ0KYzQ3OThlNTRlYmMwNmM4NzBm... (1188 characters)"
      },
      {
        "dataSet": {
          "dataSetId": 2434,
          "dataSetName": "CommCellGroupsList",
          "dataSetGuid": "d2ef0b14-5997-4d58-a96a-3086a2e459be"
        },
        "endpoint": "DATABASE",
        "shared": true,
        "dataSources": [
          {
            "dataSource": {
              "dataSourceName": ""
            },
            "connectionType": "COMMCELL",
            "commCell": {
              "commCellName": "commcell-02"
            },
            "databaseName": ""
          }
        ],
        "allColumns": false,
        "fields": [
          {
            "name": "sys_rowid",
            "dataField": "$row_number$",
            "type": "String"
          },
          {
            "name": "Data Source",
            "dataField": "Data Source",
            "type": "String"
          },
          {
            "name": "CompanyId",
            "dataField": "CompanyId",
            "type": "Integer",
            "precision": 10,
            "scale": 0
          },
          "... 10 more"
        ],
        "GetOperation": {
          "sqlText": "--DECLARE @sys_userid INT = 1\nDECLARE @userId INT = @sys_userid\n\nDECLARE @SERVEY_CAPABILITY INT = 4\nDECLARE @CloudCapabilities INT = 0\n\nSET @CloudCapabilities = ISNULL((SELECT attrVal FROM UMUsersProp WITH (NOLOCK) WHERE componentNameId = @userId and modified = 0 and attrName='Cloud Capabilities'),0)\nSELECT @CloudCapabilities = (@CloudCapabilities |attrval) FROM UMUserGroup UG WITH (NOLOCK)\nINNER ... (15062 characters)",
          "timeout": 5,
          "postQueryFilter": true,
          "rDataSetQuery": "",
          "rPlotQuery": ""
        },
        "description": "Returns the list of CommCell Groups in Public Cloud.",
        "databaseName": "CommServ",
        "deployed": true,
        "queryPlan": {
          "offline": false,
          "collectionType": "HTTP",
          "retentionDays": 1,
          "versions": [
            "VERSION_11"
          ],
          "dynamicCollection": false,
          "frequency": 60,
          "direct": false
        },
        "version": 1,
        "guid": "d2ef0b14-5997-4d58-a96a-3086a2e459be",
        "hidden": false,
        "readOnly": false,
        "revision": "$Revision: 192.0.2.10 $",
        "visibleAll": true,
        "computedColumns": {
          "scriptName": "R",
          "script": ""
        },
        "visibleToTenantAdmins": true,
        "builtIn": true,
        "systemDataSet": false,
        "signature": "<masked>",
        "definition": "IyBTSEEtNTEyIFJTQSBFTVNBLVBLQ1MxLXYxXzUgU2lnbmF0dXJlDQojIGh0dHA6Ly93d3cuYXBwcy5pZXRmLm9yZy9yZmMvcmZjMzQ0Ny5odG1sI3NlYy05LjINCg0KNmZiZDEzZmVlNTI1M2IyNzk0ZjkyMWFhOGQwOGQ1YjJmMjMxYWZkNDRjMzA5ZWJiMTUyYmZhYjVlZTQxDQpjOGZlZDZkNWI3ZmE0N2U4ZmMzYzYzNjgzNmFlN2IxOWYxNTc5YjM0NmQwNmJiN2UxOGY4Y2I1YjM1MDMNCjRiMGY4MTg4ZTYxMDE3Y2IxNTNlMTdhNDFiMDFhZDVkYWVmMDYxZGJiZjI4MjY0NjE4NzFiMGVlNGUzMw0KZWJjZGQ2ZDlkODQxZGM0OTc4... (1188 characters)"
      },
      {
        "dataSet": {
          "dataSetId": 2456,
          "dataSetName": "GetCompaniesWithCSGUID",
          "dataSetGuid": "199e4087-9ac8-44c2-d3b5-57b2e8965df4"
        },
        "endpoint": "DATABASE",
        "shared": true,
        "dataSources": [
          {
            "dataSource": {
              "dataSourceName": ""
            },
            "connectionType": "COMMCELL",
            "endpoint": "DATABASE",
            "commCell": {
              "commCellName": "commcell-03"
            }
          }
        ],
        "allColumns": true,
        "fields": [
          {
            "name": "sys_rowid",
            "dataField": "$row_number$",
            "type": "String"
          },
          {
            "name": "Data Source",
            "dataField": "Data Source",
            "type": "String"
          },
          {
            "name": "CommcellTenantGUID",
            "dataField": "CommcellTenantGUID",
            "type": "String"
          },
          "... 1 more"
        ],
        "GetOperation": {
          "sqlText": "-- this dataset is to be used with script datasets to not reveal sensitive GUID information in browser\nSET NOCOUNT ON\nSET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED\n\nDECLARE @UserId   INT \nSELECT  @UserId = id FROM UMUsers WITH (NOLOCK) WHERE login = @sys_username\n\nDECLARE @ObjectType INT = 2572    -- SERVER_GROUP_NAME_ITEM\n\ncreate table  #UserObjects ( \n  [capabilities]  bigint  NOT null, \n  [f... (3555 characters)",
          "timeout": 5,
          "postQueryFilter": true,
          "rDataSetQuery": "",
          "rPlotQuery": ""
        },
        "description": "",
        "databaseName": "CommServ",
        "deployed": true,
        "queryPlan": {
          "offline": false,
          "collectionType": "HTTP",
          "retentionDays": 1,
          "versions": [
            "VERSION_11"
          ],
          "dynamicCollection": false,
          "frequency": 60,
          "direct": false
        },
        "version": 1,
        "guid": "199e4087-9ac8-44c2-d3b5-57b2e8965df4",
        "hidden": false,
        "readOnly": false,
        "revision": "$Revision: 192.0.2.8 $",
        "visibleAll": false,
        "computedColumns": {
          "scriptName": "R",
          "script": ""
        },
        "visibleToTenantAdmins": true,
        "builtIn": true,
        "systemDataSet": false,
        "signature": "",
        "definition": "IyBTSEEtNTEyIFJTQSBFTVNBLVBLQ1MxLXYxXzUgU2lnbmF0dXJlDQojIGh0dHA6Ly93d3cuYXBwcy5pZXRmLm9yZy9yZmMvcmZjMzQ0Ny5odG1sI3NlYy05LjINCg0KOTJhYWJkMmI0YmExNjI5NDdjN2ZmZWI2ZWY2YjVjMzZhNWJkY2RkNzNkNjM1MzQ1NmRjZTI5OGJlNzgyDQpjNGNmY2UxYmQzZjcxNmVmNTk5Yzg3MTJmNzc3NjRlMWE4OTgzODRlYWY0MDU3Mjc0YzMwN2QyOTg3ZDgNCmFjODE3YmE1MWUxYjQyNTZhNGI5MzY3NjUwZTYzM2QzNDc4NGZhNjJmNWJjMWUwNzhkNDk4OWM4ZTY0OQ0KN2UxM2VhMmIxNzQ5NWNjMjVk... (1188 characters)"
      },
      "... 5 more"
    ]
  }
  ```

  </details>

## `get_reports_subscriptions_list` - GET /Reports/SubscriptionsList

> **SKIPPED** on this run: Commvault answered: 403 - User not authorized to view report subscription

```python
cv.raw.reporting.get_reports_subscriptions_list()
```

**On the wire**

- `GET /Reports/SubscriptionsList` -> **403** (0.10 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorMessage": "User not authorized to view report subscription",
    "errorCode": -1
  }
  ```

  </details>

## `list_cr_reportsplusengine_datasets_5e7dfa05_07cd_4beb_be9c_181a1722c2e8_571a5443_fb35_435e_b013_ecd1a6dcfb65_data`

GET /cr/reportsplusengine/datasets/5e7dfa05-07cd-4beb-be9c-181a1722c2e8:571a5443-fb35-435e-b013-ecd1a6dcfb65/data

```python
cv.raw.reporting.list_cr_reportsplusengine_datasets_5e7dfa05_07cd_4beb_be9c_181a1722c2e8_571a5443_fb35_435e_b013_ecd1a6dcfb65_data()
```

**On the wire**

- `GET /cr/reportsplusengine/datasets/5e7dfa05-07cd-4beb-be9c-181a1722c2e8:571a5443-fb35-435e-b013-ecd1a6dcfb65/data` -> **200** (0.37 s)

  <details><summary>Answer</summary>

  ```json
  {
    "cacheId": "dbd9707d12b246c5a34c37b26a5a04cc",
    "offset": 0,
    "limit": 0,
    "totalRecordCount": 428,
    "columns": [
      {
        "name": "sys_rowid",
        "dataField": "sys_rowid",
        "displayName": "$row_number$",
        "type": "Long",
        "precision": 64,
        "scale": 0
      },
      {
        "name": "Data Source",
        "dataField": "Data Source",
        "displayName": "Data Source",
        "type": "String",
        "precision": 1000000000,
        "scale": 0
      },
      {
        "name": "ID",
        "dataField": "ID",
        "displayName": "ID",
        "type": "Integer",
        "precision": 32,
        "scale": 0
      },
      "... 7 more"
    ],
    "recordsCount": 428,
    "records": [
      [
        1,
        "commserve-02",
        430,
        "... 7 more"
      ],
      [
        2,
        "commserve-02",
        429,
        "... 7 more"
      ],
      [
        3,
        "commserve-02",
        428,
        "... 7 more"
      ],
      "... 425 more"
    ],
    "failures": {},
    "warnings": {}
  }
  ```

  </details>

## `list_cr_reportsplusengine_datasets_metrics_subclient-01_data`

GET /cr/reportsplusengine/datasets/METRICS_subclient-01/data

```python
cv.raw.reporting.list_cr_reportsplusengine_datasets_metrics_subclient-01_data()
```

**On the wire**

- `GET /cr/reportsplusengine/datasets/METRICS_subclient-01/data` -> **200** (0.19 s)

  <details><summary>Answer</summary>

  ```json
  {
    "offset": 0,
    "limit": 0,
    "totalRecordCount": 0,
    "columns": [],
    "recordsCount": 0,
    "records": [],
    "groupings": [],
    "failures": {
      "commserve-02": [
        "Bad Request. Please check the parameters."
      ]
    },
    "warnings": {}
  }
  ```

  </details>

## `get_cr_reportsplusengine_reports_name_report_name`

GET /cr/reportsplusengine/reports/name:{Report Name}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.reporting.get_cr_reportsplusengine_reports_name_report_name(...)
```

## `list_cr_reportsplusengine_dataset_data`

GET /cr/reportsplusengine/datasets/{dataSetId}/data

```python
cv.raw.reporting.list_cr_reportsplusengine_dataset_data('2b3e43c0-21fe-401d-ebf8-c485309262a7')
```

**On the wire**

- `GET /cr/reportsplusengine/datasets/2b3e43c0-21fe-401d-ebf8-c485309262a7/data` -> **200** (1.34 s)

  <details><summary>Answer</summary>

  ```json
  {
    "cacheId": "609aac067b0b4df49aa71ecec25ceb7e",
    "offset": 0,
    "limit": 0,
    "totalRecordCount": 425,
    "columns": [
      {
        "name": "sys_rowid",
        "dataField": "sys_rowid",
        "displayName": "$row_number$",
        "type": "Long",
        "precision": 64,
        "scale": 0
      },
      {
        "name": "Data Source",
        "dataField": "Data Source",
        "displayName": "Data Source",
        "type": "String",
        "precision": 1000000000,
        "scale": 0
      },
      {
        "name": "ID",
        "dataField": "ID",
        "displayName": "ID",
        "type": "Integer",
        "precision": 32,
        "scale": 0
      },
      "... 6 more"
    ],
    "recordsCount": 425,
    "records": [
      [
        1,
        "commserve-02",
        430,
        "... 6 more"
      ],
      [
        2,
        "commserve-02",
        429,
        "... 6 more"
      ],
      [
        3,
        "commserve-02",
        428,
        "... 6 more"
      ],
      "... 422 more"
    ],
    "failures": {},
    "warnings": {}
  }
  ```

  </details>
