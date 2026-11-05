# `cv.raw.audits`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 16:43 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_audits_entity` - GET /v4/Audits/Entity

> **SKIPPED** on this run: Commvault answered: 400 - invalid parameter [entityType]

```python
cv.raw.audits.get_audits_entity()
```

**On the wire**

- `GET /v4/Audits/Entity` -> **400** (0.07 s)

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

- `GET /v4/Audits` -> **200** (0.15 s)

  <details><summary>Answer</summary>

  ```json
  {
    "audits": [
      {
        "auditId": "A1AD169BCF7341B9BC8A823EA536FF31413",
        "hasAuditId": true,
        "severity": "High",
        "user": {
          "userId": 2,
          "userName": "user-01",
          "hasUserName": true
        },
        "createdTimeUtc": 1793894837,
        "entities": [
          {
            "entityType": 0,
            "entityId": 0,
            "entityName": "mount-path-01",
            "hasEntityName": true
          }
        ],
        "operation": {
          "operationMessage": {
            "localizedMessages": [
              {
                "localeId": 0,
                "localeText": "Renewed the REST Access Token."
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
                  "localeText": "Renewed the Access Token [blt] "
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
        "auditId": "A1AD169BCF7341B9BC8A823EA536FF31412",
        "hasAuditId": true,
        "severity": "High",
        "user": {
          "userId": 2,
          "userName": "user-01",
          "hasUserName": true
        },
        "createdTimeUtc": 1793894406,
        "entities": [
          {
            "entityType": 0,
            "entityId": 0,
            "entityName": "mount-path-01",
            "hasEntityName": true
          }
        ],
        "operation": {
          "operationMessage": {
            "localizedMessages": [
              {
                "localeId": 0,
                "localeText": "DR Backup"
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
                  "localeText": "DBCC CHECKDB was executed as part of DR backup Job ID: [1504]. "
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
        "auditId": "A1AD169BCF7341B9BC8A823EA536FF31411",
        "hasAuditId": true,
        "severity": "High",
        "user": {
          "userId": 2,
          "userName": "user-01",
          "hasUserName": true
        },
        "createdTimeUtc": 1793894326,
        "entities": [
          {
            "entityType": 0,
            "entityId": 0,
            "entityName": "mount-path-01",
            "hasEntityName": true
          }
        ],
        "operation": {
          "operationMessage": {
            "localizedMessages": [
              {
                "localeId": 0,
                "localeText": "Renewed the REST Access Token."
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
                  "localeText": "Renewed the Access Token [lab] "
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
      "... 395 more"
    ],
    "filterMatchCount": 398,
    "hasFilterMatchCount": true
  }
  ```

  </details>
