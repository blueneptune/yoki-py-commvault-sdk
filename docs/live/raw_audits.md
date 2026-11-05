# `cv.raw.audits`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:37 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_audits_entity` - GET /v4/Audits/Entity

> **SKIPPED** on this run: Commvault answered: 400 - invalid parameter [entityType]

```python
cv.raw.audits.get_audits_entity()
```

**On the wire**

- `GET /v4/Audits/Entity` -> **400** (0.06 s)

  <details><summary>Answer</summary>

  ```
  invalid parameter [entityType]
  ```

  </details>

## `list_audits` - GET /v4/Audits

```python
cv.raw.audits.list_audits()
```

**On the wire**

- `GET /v4/Audits` -> **200** (0.17 s)

  <details><summary>Answer</summary>

  ```json
  {
    "audits": [
      {
        "auditId": "A1AD169BCF7341B9BC8A823EA536FF31453",
        "hasAuditId": true,
        "severity": "Critical",
        "user": {
          "userId": 2,
          "userName": "user-01",
          "hasUserName": true
        },
        "createdTimeUtc": 1793903594,
        "entities": [
          {
            "entityType": 15,
            "entityId": 10,
            "entityName": "mount-path-01",
            "hasEntityName": true
          }
        ],
        "operation": {
          "operationMessage": {
            "localizedMessages": [
              {
                "localeId": 0,
                "localeText": "Delete User group"
              }
            ]
          }
        },
        "details": {
          "detailsMessage": [
            {
              "localizedMessages": [
                {
                  "localeId": 0,
                  "localeText": "User Group: bltlive-11051833-users <br>Service Type  [UNKNOWN] (Removed)<br>Two Factor Authentication  [DISABLED_AT_COMPANY] (Removed)<br>Quota Limit In GB  [100] (Removed)<br>Description  [bltlive: changed by the SDK's live tests] (Removed)<br>Enabled  Changed from [true] to []<br>Edge Drive Quota Limit In GB  [100] (Removed)<br>Preference Machine Centric Client  Changed from [true] to []<br>&ems... (563 characters)"
                }
              ],
              "messageLevel": 0
            }
          ]
        },
        "commcell": {
          "commcellId": 2,
          "hasCommcellId": true,
          "commcellName": "commserve-02",
          "hasCommcellName": true,
          "commcellGuid": "A1AD169B-CF73-41B9-BC8A-823EA536FF31",
          "hasCommcellGuid": true
        },
        "company": {
          "companyId": 0,
          "hasCompanyId": true,
          "companyName": "Commcell",
          "hasCompanyName": true,
          "companyGuid": "",
          "hasCompanyGuid": true
        },
        "auditNotesCount": 0
      },
      {
        "auditId": "A1AD169BCF7341B9BC8A823EA536FF31452",
        "hasAuditId": true,
        "severity": "High",
        "user": {
          "userId": 2,
          "userName": "user-01",
          "hasUserName": true
        },
        "createdTimeUtc": 1793903593,
        "entities": [
          {
            "entityType": 15,
            "entityId": 10,
            "entityName": "mount-path-01",
            "hasEntityName": true
          }
        ],
        "operation": {
          "operationMessage": {
            "localizedMessages": [
              {
                "localeId": 0,
                "localeText": "Update User Group properties"
              }
            ]
          }
        },
        "details": {
          "detailsMessage": [
            {
              "localizedMessages": [
                {
                  "localeId": 0,
                  "localeText": "User Group: bltlive-11051833-users <br>Description  Changed from [bltlive: made by the SDK's live tests] to [bltlive: changed by the SDK's live tests]"
                }
              ],
              "messageLevel": 0
            }
          ]
        },
        "commcell": {
          "commcellId": 2,
          "hasCommcellId": true,
          "commcellName": "commserve-02",
          "hasCommcellName": true,
          "commcellGuid": "A1AD169B-CF73-41B9-BC8A-823EA536FF31",
          "hasCommcellGuid": true
        },
        "company": {
          "companyId": 0,
          "hasCompanyId": true,
          "companyName": "Commcell",
          "hasCompanyName": true,
          "companyGuid": "",
          "hasCompanyGuid": true
        },
        "auditNotesCount": 0
      },
      {
        "auditId": "A1AD169BCF7341B9BC8A823EA536FF31451",
        "hasAuditId": true,
        "severity": "High",
        "user": {
          "userId": 2,
          "userName": "user-01",
          "hasUserName": true
        },
        "createdTimeUtc": 1793903590,
        "entities": [
          {
            "entityType": 15,
            "entityId": 10,
            "entityName": "mount-path-01",
            "hasEntityName": true
          }
        ],
        "operation": {
          "operationMessage": {
            "localizedMessages": [
              {
                "localeId": 0,
                "localeText": "Add New User Group"
              }
            ]
          }
        },
        "details": {
          "detailsMessage": [
            {
              "localizedMessages": [
                {
                  "localeId": 0,
                  "localeText": "User Group: bltlive-11051833-users <br>Service Type  Set to [UNKNOWN]<br>Two Factor Authentication  Set to [DISABLED_AT_COMPANY]<br>Quota Limit In GB  Set to [100]<br>Description  Set to [bltlive: made by the SDK's live tests]<br>Enabled : Yes<br>Edge Drive Quota Limit In GB  Set to [100]<br>Preference Machine Centric Client : Yes<br>&emsp;Company <br>&emsp;&emsp;Provider Domain Name  Set to [Comm... (497 characters)"
                }
              ],
              "messageLevel": 0
            }
          ]
        },
        "commcell": {
          "commcellId": 2,
          "hasCommcellId": true,
          "commcellName": "commserve-02",
          "hasCommcellName": true,
          "commcellGuid": "A1AD169B-CF73-41B9-BC8A-823EA536FF31",
          "hasCommcellGuid": true
        },
        "company": {
          "companyId": 0,
          "hasCompanyId": true,
          "companyName": "Commcell",
          "hasCompanyName": true,
          "companyGuid": "",
          "hasCompanyGuid": true
        },
        "auditNotesCount": 0
      },
      "... 435 more"
    ],
    "filterMatchCount": 438,
    "hasFilterMatchCount": true
  }
  ```

  </details>
