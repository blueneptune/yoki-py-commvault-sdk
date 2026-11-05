# `cv.raw.dashboard`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:50 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_airgapprotect_license`

GET /cr/reportsplusengine/datasets/d7faef75-cf66-40a2-98ce-a2d0cc2a144b:cc2e77ec-9315-4446-cd7e-44ef80a8860e/data/

```python
cv.raw.dashboard.get_airgapprotect_license()
```

**On the wire**

- `GET /cr/reportsplusengine/datasets/d7faef75-cf66-40a2-98ce-a2d0cc2a144b:cc2e77ec-9315-4446-cd7e-44ef80a8860e/data/?offset=0&fields=%5BLicUsageType%5D+AS+%5BLicense+ID%5D%2C%5BDial%5D+AS+%5BLicense%5D%2C%5BPurchased%5D+AS+%5BAvailable+Total+%28TB%29%5D%2C%5BPermTotal%5D+AS+%5BPermanent+Purchased+%28TB%29%5D%2C%5BEval%5D+AS+%5BTerm+Purchased+%28TB%29%5D%2C%5BUsage%5D+AS+%5BUsed+%28TB%29%5D%2C%5BEvalExpiryDate%5D+AS+%5BEvalExpiryDate%5D%2C%5BSummary%5D+AS+%5BSummary%5D&parameter.GUID=-1&limit=20` -> **200** (0.72 s)

  <details><summary>Answer</summary>

  ```json
  {
    "cacheId": "0ce402b8b2224cee967a97ee5e463204",
    "offset": 0,
    "limit": 20,
    "totalRecordCount": 0,
    "columns": [
      {
        "name": "License ID",
        "dataField": "License ID",
        "type": "Integer",
        "precision": 32,
        "scale": 0
      },
      {
        "name": "License",
        "dataField": "License",
        "type": "String",
        "precision": 1000000000,
        "scale": 0
      },
      {
        "name": "Available Total (TB)",
        "dataField": "Available Total (TB)",
        "type": "Integer",
        "precision": 32,
        "scale": 0
      },
      "... 5 more"
    ],
    "recordsCount": 0,
    "records": [],
    "failures": {
      "commserve-02": [
        "Bad Request. Please check the parameters."
      ]
    },
    "warnings": {
      "commserve-02": [
        "Warning: Null value is eliminated by an aggregate or other SET operation."
      ]
    }
  }
  ```

  </details>

## `get_anomalous_entities` - GET /CommServ/Anomaly/Entity/Count

```python
cv.raw.dashboard.get_anomalous_entities()
```

**On the wire**

- `GET /CommServ/Anomaly/Entity/Count?anomalousEntityType=14` -> **200** (0.19 s)

  <details><summary>Answer</summary>

  ```json
  {
    "CountOfAnomalousclient-group-01Servers": 0,
    "CountOfAnomalousServers": 1,
    "CountOfAnomalousJobs": 1
  }
  ```

  </details>

## `get_clientsclount` - GET /clients/count

```python
cv.raw.dashboard.get_clientsclount()
```

**On the wire**

- `GET /clients/count?type=fileserver%2Cvm%2Claptop` -> **200** (0.09 s)

  <details><summary>Answer</summary>

  ```json
  {
    "fileServerCount": 11,
    "laptopCount": 0,
    "vmCount": 0
  }
  ```

  </details>

## `get_commcellsladetails` - GET /cr/reportsplusengine/datasets/GetSLACounts/data

```python
cv.raw.dashboard.get_commcellsladetails()
```

**On the wire**

- `GET /cr/reportsplusengine/datasets/GetSLACounts/data?cache=true&parameter.i_DashboardType=commcell&datasource=2` -> **200** (0.30 s)

  <details><summary>Answer</summary>

  ```json
  {
    "cacheId": "99d7e867c0fe46e48d9f32dc18db3994",
    "offset": 0,
    "limit": 0,
    "totalRecordCount": 4,
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
        "name": "SLAStatus",
        "dataField": "SLAStatus",
        "displayName": "SLAStatus",
        "type": "String",
        "precision": 1000000000,
        "scale": 0
      },
      "... 2 more"
    ],
    "recordsCount": 4,
    "records": [
      [
        1,
        "commserve-02",
        "Met SLA",
        "... 2 more"
      ],
      [
        2,
        "commserve-02",
        "Missed SLA",
        "... 2 more"
      ],
      [
        3,
        "commserve-02",
        "Pending Application Investigation",
        "... 2 more"
      ],
      "... 1 more"
    ],
    "failures": {},
    "warnings": {}
  }
  ```

  </details>

## `get_cr_reportsplusengine_datasets_a0f077a5_2dfe_4010_a957_57a24cae89a8_data`

GET /cr/reportsplusengine/datasets/a0f077a5-2dfe-4010-a957-57a24cae89a8/data

```python
cv.raw.dashboard.get_cr_reportsplusengine_datasets_a0f077a5_2dfe_4010_a957_57a24cae89a8_data()
```

**On the wire**

- `GET /cr/reportsplusengine/datasets/a0f077a5-2dfe-4010-a957-57a24cae89a8/data` -> **200** (0.21 s)

  <details><summary>Answer</summary>

  ```json
  {
    "cacheId": "2625ab085d86430592a4a06fa237834c",
    "offset": 0,
    "limit": 0,
    "totalRecordCount": 1,
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
        "name": "CommCellID",
        "dataField": "CommCellID",
        "displayName": "CommCellID",
        "type": "Integer",
        "precision": 32,
        "scale": 0
      },
      "... 3 more"
    ],
    "recordsCount": 1,
    "records": [
      [
        1,
        "commserve-02",
        -1,
        "... 3 more"
      ]
    ],
    "failures": {},
    "warnings": {}
  }
  ```

  </details>

## `get_current_capacity`

GET /cr/reportsplusengine/datasets/d7faef75-cf66-40a2-98ce-a2d0cc2a144b:feabb5ca-b6b7-4572-b0cb-39352c7e1b67/data/

```python
cv.raw.dashboard.get_current_capacity()
```

**On the wire**

- `GET /cr/reportsplusengine/datasets/d7faef75-cf66-40a2-98ce-a2d0cc2a144b:feabb5ca-b6b7-4572-b0cb-39352c7e1b67/data/?cacheId=e76a6d07-2b1b-47b2-d97e-7a7f1a9793be&offset=0&fields=%5BDial%5D+AS+%5BDial%5D%2C%5BPurchased%5D+AS+%5BPurchased%5D%2C%5BPermTotal%5D+AS+%5BPermTotal%5D%2C%5BEval%5D+AS+%5BEval%5D%2C%5BUsage%5D+AS+%5BUsage%5D%2C%5BTermDate%5D+AS+%5BTermDate%5D%2C%5BEvalExpiryDate%5D+AS+%5BEvalExpiryDate%5D&isExport=false&componentName=Capacity+Licenses&parameter.GUID=-1&limit=5&rawData=false` -> **200** (0.21 s)

  <details><summary>Answer</summary>

  ```json
  {
    "cacheId": "e76a6d07-2b1b-47b2-d97e-7a7f1a9793be",
    "offset": 0,
    "limit": 5,
    "totalRecordCount": 0,
    "columns": [
      {
        "name": "Dial",
        "dataField": "Dial",
        "displayName": "Dial",
        "type": "String",
        "precision": 1000000000,
        "scale": 0
      },
      {
        "name": "Purchased",
        "dataField": "Purchased",
        "displayName": "Purchased",
        "type": "Integer",
        "precision": 32,
        "scale": 0
      },
      {
        "name": "PermTotal",
        "dataField": "PermTotal",
        "displayName": "PermTotal",
        "type": "Integer",
        "precision": 32,
        "scale": 0
      },
      "... 4 more"
    ],
    "recordsCount": 0,
    "records": [],
    "failures": {
      "commserve-02": [
        "Bad Request. Please check the parameters."
      ]
    },
    "warnings": {}
  }
  ```

  </details>

## `get_data_insights_license`

GET /cr/reportsplusengine/datasets/d7faef75-cf66-40a2-98ce-a2d0cc2a144b:f7c6b473-f99d-44b4-ff5e-466b55656500/data/

```python
cv.raw.dashboard.get_data_insights_license()
```

**On the wire**

- `GET /cr/reportsplusengine/datasets/d7faef75-cf66-40a2-98ce-a2d0cc2a144b:f7c6b473-f99d-44b4-ff5e-466b55656500/data/?offset=0&fields=%5BLicUsageType%5D+AS+%5BLicense+ID%5D%2C%5BDial%5D+AS+%5BLicense%5D%2C%5BPurchased%5D+AS+%5BAvailable+Total%5D%2C%5BPermTotal%5D+AS+%5BPermanent+Purchased%5D%2C%5BEval%5D+AS+%5BTerm+Purchased%5D%2C%5BUsage%5D+AS+%5BUsed%5D%2C%5BEvalExpiryDate%5D+AS+%5BEvalExpiryDate%5D%2C%5BSummary%5D+AS+%5BSummary%5D&parameter.GUID=-1&limit=20` -> **200** (0.20 s)

  <details><summary>Answer</summary>

  ```json
  {
    "cacheId": "19f664b656e24221a51ee7fe7b5bc479",
    "offset": 0,
    "limit": 20,
    "totalRecordCount": 0,
    "columns": [
      {
        "name": "License ID",
        "dataField": "License ID",
        "type": "Integer",
        "precision": 32,
        "scale": 0
      },
      {
        "name": "License",
        "dataField": "License",
        "type": "String",
        "precision": 1000000000,
        "scale": 0
      },
      {
        "name": "Available Total",
        "dataField": "Available Total",
        "type": "Long",
        "precision": 64,
        "scale": 0
      },
      "... 5 more"
    ],
    "recordsCount": 0,
    "records": [],
    "failures": {
      "commserve-02": [
        "Bad Request. Please check the parameters."
      ]
    },
    "warnings": {
      "commserve-02": [
        "Warning: Null value is eliminated by an aggregate or other SET operation."
      ]
    }
  }
  ```

  </details>

## `get_environment_details`

GET /cr/reportsplusengine/datasets/d0a73c45-b06d-4358-8d7e-d55d428ba75c/data

```python
cv.raw.dashboard.get_environment_details()
```

**On the wire**

- `GET /cr/reportsplusengine/datasets/d0a73c45-b06d-4358-8d7e-d55d428ba75c/data?cache=true&parameter.i_DashboardType=commcell&datasource=2` -> **200** (0.31 s)

  <details><summary>Answer</summary>

  ```json
  {
    "cacheId": "4d6595e8682a410eac31f437f7e5b019",
    "offset": 0,
    "limit": 0,
    "totalRecordCount": 4,
    "columns": [
      {
        "name": "Data Source",
        "dataField": "Data Source",
        "type": "String",
        "precision": 1000000000,
        "scale": 0
      },
      {
        "name": "PropertyType",
        "dataField": "PropertyType",
        "type": "String",
        "precision": 1000000000,
        "scale": 0
      },
      {
        "name": "PropertyCount",
        "dataField": "PropertyCount",
        "type": "Integer",
        "precision": 32,
        "scale": 0
      }
    ],
    "recordsCount": 4,
    "records": [
      [
        "commserve-02",
        "SERVERS",
        13
      ],
      [
        "commserve-02",
        "VMS",
        0
      ],
      [
        "commserve-02",
        "LAPTOPS",
        0
      ],
      "... 1 more"
    ],
    "failures": {},
    "warnings": {}
  }
  ```

  </details>

## `get_health_overview`

GET /cr/reportsplusengine/datasets/b50b20ed-5fc4-4b4c-f7c4-fc6b84eb35cc/data

```python
cv.raw.dashboard.get_health_overview()
```

**On the wire**

- `GET /cr/reportsplusengine/datasets/b50b20ed-5fc4-4b4c-f7c4-fc6b84eb35cc/data?cache=true` -> **200** (0.20 s)

  <details><summary>Answer</summary>

  ```json
  {
    "cacheId": "a974fed9c12e44d4b153f20eefe7bdee",
    "offset": 0,
    "limit": 0,
    "totalRecordCount": 4,
    "columns": [
      {
        "name": "Data Source",
        "dataField": "Data Source",
        "type": "String",
        "precision": 1000000000,
        "scale": 0
      },
      {
        "name": "Status",
        "dataField": "Status",
        "type": "String",
        "precision": 1000000000,
        "scale": 0
      },
      {
        "name": "Count",
        "dataField": "Count",
        "type": "Integer",
        "precision": 32,
        "scale": 0
      }
    ],
    "recordsCount": 4,
    "records": [
      [
        "commserve-02",
        "1_Good",
        0
      ],
      [
        "commserve-02",
        "2_Info",
        0
      ],
      [
        "commserve-02",
        "3_Warning",
        0
      ],
      "... 1 more"
    ],
    "failures": {},
    "warnings": {}
  }
  ```

  </details>

## `get_hypescalelicensereport`

GET /cr/reportsplusengine/datasets/d7faef75-cf66-40a2-98ce-a2d0cc2a144b:2654b01f-9bb0-481e-b273-4b4fddc585b1/data/

```python
cv.raw.dashboard.get_hypescalelicensereport()
```

**On the wire**

- `GET /cr/reportsplusengine/datasets/d7faef75-cf66-40a2-98ce-a2d0cc2a144b:2654b01f-9bb0-481e-b273-4b4fddc585b1/data/?offset=0&fields=%5BLicUsageType%5D+AS+%5BLicense+ID%5D%2C%5BDial%5D+AS+%5BLicense%5D%2C%5BPurchased%5D+AS+%5BAvailable+Total+%28TB%29%5D%2C%5BPermTotal%5D+AS+%5BPermanent+Purchased+%28TB%29%5D%2C%5BEval%5D+AS+%5BTerm+Purchased+%28TB%29%5D%2C%5BUsage%5D+AS+%5BUsed+%28TB%29%5D%2C%5BEvalExpiryDate%5D+AS+%5BEvalExpiryDate%5D%2C%5BSummary%5D+AS+%5BSummary%5D&parameter.GUID=-1&limit=10` -> **200** (0.21 s)

  <details><summary>Answer</summary>

  ```json
  {
    "cacheId": "a2fbbdda05c34f26a905c421153ff199",
    "offset": 0,
    "limit": 10,
    "totalRecordCount": 0,
    "columns": [
      {
        "name": "License ID",
        "dataField": "License ID",
        "type": "Integer",
        "precision": 32,
        "scale": 0
      },
      {
        "name": "License",
        "dataField": "License",
        "type": "String",
        "precision": 1000000000,
        "scale": 0
      },
      {
        "name": "Available Total (TB)",
        "dataField": "Available Total (TB)",
        "type": "Long",
        "precision": 64,
        "scale": 0
      },
      "... 5 more"
    ],
    "recordsCount": 0,
    "records": [],
    "failures": {
      "commserve-02": [
        "Bad Request. Please check the parameters."
      ]
    },
    "warnings": {
      "commserve-02": [
        "Warning: Null value is eliminated by an aggregate or other SET operation."
      ]
    }
  }
  ```

  </details>

## `get_jobsin_24hours`

GET /cr/reportsplusengine/datasets/075e703a-b29f-46d6-ad29-7c1a60f7e4f3/data

```python
cv.raw.dashboard.get_jobsin_24hours()
```

**On the wire**

- `GET /cr/reportsplusengine/datasets/075e703a-b29f-46d6-ad29-7c1a60f7e4f3/data?cache=true&parameter.i_DashboardType=commcell&datasource=2` -> **200** (0.37 s)

  <details><summary>Answer</summary>

  ```json
  {
    "cacheId": "683834909f044c6d8e54396143981845",
    "offset": 0,
    "limit": 0,
    "totalRecordCount": 7,
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
        "name": "Name",
        "dataField": "Name",
        "displayName": "Name",
        "type": "String",
        "precision": 1000000000,
        "scale": 0
      },
      "... 3 more"
    ],
    "recordsCount": 7,
    "records": [
      [
        1,
        "commserve-02",
        "Completed",
        "... 3 more"
      ],
      [
        2,
        "commserve-02",
        "Failed",
        "... 3 more"
      ],
      [
        3,
        "commserve-02",
        "Killed",
        "... 3 more"
      ],
      "... 4 more"
    ],
    "failures": {},
    "warnings": {}
  }
  ```

  </details>

## `get_local_cs_unique_id` - GET /LocalCSUniqueId

> **SKIPPED** on this run: Commvault answered: 500 - GetLocalCommServUniqueID :: StoredProcedure returned ErrorCode : 2

```python
cv.raw.dashboard.get_local_cs_unique_id()
```

**On the wire**

- `GET /LocalCSUniqueId` -> **500** (0.08 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorMessage": "GetLocalCommServUniqueID :: StoredProcedure returned ErrorCode : 2",
    "errorCode": 2
  }
  ```

  </details>

## `get_operatinginstanceslicense`

GET /cr/reportsplusengine/datasets/d7faef75-cf66-40a2-98ce-a2d0cc2a144b:cd38c52a-e099-4252-d36f-3e2c54540f6f/data/

```python
cv.raw.dashboard.get_operatinginstanceslicense()
```

**On the wire**

- `GET /cr/reportsplusengine/datasets/d7faef75-cf66-40a2-98ce-a2d0cc2a144b:cd38c52a-e099-4252-d36f-3e2c54540f6f/data/?offset=0&fields=%5BLicUsageType%5D+AS+%5BLicense+ID%5D%2C%5BDial%5D+AS+%5BLicense%5D%2C%5BPurchased%5D+AS+%5BAvailable+Total+%28instances%29%5D%2C%5BPermTotal%5D+AS+%5BPermanent+Purchased+%28instances%29%5D%2C%5BEval%5D+AS+%5BTerm+Purchased+%28instances%29%5D%2C%5BUsage%5D+AS+%5BUsed+%28instances%29%5D%2C%5BEvalExpiryDate%5D+AS+%5BEvalExpiryDate%5D%2C%5BSummary%5D+AS+%5BSummary%5D&parameter.GUID=-1&limit=5` -> **200** (0.22 s)

  <details><summary>Answer</summary>

  ```json
  {
    "cacheId": "55eaf313e84644ca9c7dc27d610700f2",
    "offset": 0,
    "limit": 5,
    "totalRecordCount": 0,
    "columns": [
      {
        "name": "License ID",
        "dataField": "License ID",
        "type": "Integer",
        "precision": 32,
        "scale": 0
      },
      {
        "name": "License",
        "dataField": "License",
        "type": "String",
        "precision": 1000000000,
        "scale": 0
      },
      {
        "name": "Available Total (instances)",
        "dataField": "Available Total (instances)",
        "type": "Long",
        "precision": 64,
        "scale": 0
      },
      "... 5 more"
    ],
    "recordsCount": 0,
    "records": [],
    "failures": {
      "commserve-02": [
        "Bad Request. Please check the parameters."
      ]
    },
    "warnings": {
      "commserve-02": [
        "Warning: Null value is eliminated by an aggregate or other SET operation."
      ]
    }
  }
  ```

  </details>

## `get_security_dashboard` - GET /Security/Dashboard

```python
cv.raw.dashboard.get_security_dashboard()
```

**On the wire**

- `GET /Security/Dashboard` -> **200** (0.50 s)

  <details><summary>Answer</summary>

  ```json
  {
    "companyId": 0,
    "securityCategories": [
      {
        "category": 0,
        "parameter": [
          {
            "active": "Active",
            "recommendation": "5 or fewer failed log-ins",
            "paramName": "Failed login lockout count",
            "currentSetting": "5 failed logins",
            "paramId": 3,
            "remarks": "This setting is not following recommendations in accordance to AC-7 NIST 800-53 publication.<br><a href=#/commCell target=\"_blank\">Click here</a> to configure by going to <b>settings</b> section on the page.",
            "status": 0
          },
          {
            "active": "Active",
            "recommendation": "30 minutes or more",
            "paramName": "Account lockout duration",
            "currentSetting": "30 minutes",
            "paramId": 4,
            "remarks": "This setting is not following recommendations in accordance to AC-7 NIST 800-53 publication.<br><a href=#/commCell target=\"_blank\">Click here</a> to configure by going to <b>settings</b> section on the page.",
            "status": 0
          },
          {
            "active": "Active",
            "recommendation": "It is recommended to enable this feature so delete requests require additional authorization for approval.",
            "paramName": "Delete authorization",
            "currentSetting": "Enabled",
            "paramId": 5,
            "remarks": "When this setting is enabled, deletion requests will require approval from another administrator, protecting against accidental and malicious destructive tasks. This cannot be disabled once it is enabled.",
            "status": 1
          },
          "... 6 more"
        ]
      },
      {
        "category": 3,
        "parameter": [
          {
            "active": "Active",
            "recommendation": "Enable this option to allow restrictions for browse and restores only for company tenants",
            "paramName": "Privacy feature",
            "currentSetting": "Disabled",
            "paramId": 18,
            "remarks": "<a href=#/commCell target=\"_blank\">Click here</a> to configure by going to <b>privacy</b> section on the page.",
            "status": 1
          },
          {
            "active": "Active",
            "recommendation": "Enable this option to allow password-protected restores only for company tenants",
            "paramName": "Passkey for restore feature",
            "currentSetting": "host-15 computer owners have enabled the passkey for restore operations",
            "paramId": 19,
            "remarks": "<a href=#/commCell target=\"_blank\">Click here</a> to configure by going to <b>passkey</b> section on the page.",
            "status": 1
          },
          {
            "active": "Active",
            "recommendation": "",
            "paramName": "Requires user authentication for installing agents",
            "currentSetting": "Authentication is required",
            "paramId": 23,
            "remarks": "",
            "status": 0
          }
        ]
      },
      {
        "category": 1,
        "parameter": [
          {
            "active": "Not Applicable",
            "recommendation": "Retention for Critical audit trail: 1 year\nRetention for High audit trail: 1 year\nRetention for Medium audit trail: 8 months\nRetention for Low audit trail: 4 months",
            "paramName": "Audit trail",
            "currentSetting": "Retention for Critical audit trail: 1 year<br>Retention for High audit trail: 1 year<br>Retention for Medium audit trail: 8 months<br>Retention for Low audit trail: 4 months",
            "paramId": 7,
            "remarks": "<a href=#/reportDetails?reportId=AuditTrailReport target=\"_blank\">View full audit trail report</a> for export options",
            "status": 0
          },
          {
            "active": "Active",
            "recommendation": "Review and remove unused CommCell management entities",
            "paramName": "Cleanup of unused entities",
            "currentSetting": "0 user groups without users<br>0 users without security associations<br>0 users not logged-in in 30 days",
            "paramId": 16,
            "remarks": "Review user security configurations to identify and mitigate potential user access risks.<br><a href=#/reportDetails?reportName=Cleanup%20Report target=\"_blank\">Click here</a> to view.",
            "status": 1
          },
          {
            "active": "Active",
            "recommendation": "Review and remove privileged access accounts that are no longer needed",
            "paramName": "User and user group permissions",
            "currentSetting": "View users in master group",
            "paramId": 17,
            "remarks": "",
            "status": 1
          }
        ]
      },
      "... 2 more"
    ],
    "error": {
      "errorCode": 0
    }
  }
  ```

  </details>

## `get_storage_pool_hyper_scale_dashboard` - GET /StoragePool/HyperScale/Dashboard

> **SKIPPED** on this run: Commvault answered: error -1: Failed to get HyperScale dashboard information

```python
cv.raw.dashboard.get_storage_pool_hyper_scale_dashboard()
```

**On the wire**

- `GET /StoragePool/HyperScale/Dashboard` -> **200** (0.07 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorMessage": "Failed to get HyperScale dashboard information",
    "errorCode": -1,
    "aggregatedHyperScaleStoragePoolHealth": {}
  }
  ```

  </details>

## `get_storagespaceusage`

GET /cr/reportsplusengine/datasets/2b366703-52e1-4775-8047-1f4cfa13d2db/data

```python
cv.raw.dashboard.get_storagespaceusage()
```

**On the wire**

- `GET /cr/reportsplusengine/datasets/2b366703-52e1-4775-8047-1f4cfa13d2db/data?cache=true&parameter.i_DashboardType=commcell&orderby=%22Date+to+be+Full%22&datasource=2` -> **200** (0.21 s)

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

## `get_topfiveservers`

GET /cr/reportsplusengine/datasets/841800ea-53c4-4249-91fa-76ea0d60f6a4/data

```python
cv.raw.dashboard.get_topfiveservers()
```

**On the wire**

- `GET /cr/reportsplusengine/datasets/841800ea-53c4-4249-91fa-76ea0d60f6a4/data?cache=true&parameter.i_dashboardType=commcell&datasource=2` -> **200** (0.22 s)

  <details><summary>Answer</summary>

  ```json
  {
    "cacheId": "88235d46164c4db099b360b6f694b173",
    "offset": 0,
    "limit": 0,
    "totalRecordCount": 3,
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
        "name": "Client ID",
        "dataField": "Client ID",
        "displayName": "Client ID",
        "type": "Integer",
        "precision": 32,
        "scale": 0
      },
      "... 3 more"
    ],
    "recordsCount": 3,
    "records": [
      [
        1,
        "commserve-02",
        2,
        "... 3 more"
      ],
      [
        2,
        "commserve-02",
        15,
        "... 3 more"
      ],
      [
        3,
        "commserve-02",
        16,
        "... 3 more"
      ]
    ],
    "failures": {},
    "warnings": {}
  }
  ```

  </details>

## `get_userlicenses`

GET /cr/reportsplusengine/datasets/d7faef75-cf66-40a2-98ce-a2d0cc2a144b:44cd7de8-ecb2-4ec8-8b2b-162491172eef/data/

```python
cv.raw.dashboard.get_userlicenses()
```

**On the wire**

- `GET /cr/reportsplusengine/datasets/d7faef75-cf66-40a2-98ce-a2d0cc2a144b:44cd7de8-ecb2-4ec8-8b2b-162491172eef/data/?offset=0&fields=%5BLicUsageType%5D+AS+%5BLicense+ID%5D%2C%5BDial%5D+AS+%5BLicense%5D%2C%5BPurchased%5D+AS+%5BAvailable+Total+%28users%29%5D%2C%5BPermTotal%5D+AS+%5BPermanent+Purchased+%28users%29%5D%2C%5BEval%5D+AS+%5BTerm+Purchased+%28users%29%5D%2C%5BUsage%5D+AS+%5BUsed+%28users%29%5D%2C%5BEvalExpiryDate%5D+AS+%5BEvalExpiryDate%5D%2C%5BSummary%5D+AS+%5BSummary%5D&parameter.GUID=-1&limit=5` -> **200** (0.20 s)

  <details><summary>Answer</summary>

  ```json
  {
    "cacheId": "33bb28e370e24d0aa6897f8b4feb85c1",
    "offset": 0,
    "limit": 5,
    "totalRecordCount": 0,
    "columns": [
      {
        "name": "License ID",
        "dataField": "License ID",
        "type": "Integer",
        "precision": 32,
        "scale": 0
      },
      {
        "name": "License",
        "dataField": "License",
        "type": "String",
        "precision": 1000000000,
        "scale": 0
      },
      {
        "name": "Available Total (users)",
        "dataField": "Available Total (users)",
        "type": "Long",
        "precision": 64,
        "scale": 0
      },
      "... 5 more"
    ],
    "recordsCount": 0,
    "records": [],
    "failures": {
      "commserve-02": [
        "Bad Request. Please check the parameters."
      ]
    },
    "warnings": {
      "commserve-02": [
        "Warning: Null value is eliminated by an aggregate or other SET operation."
      ]
    }
  }
  ```

  </details>
