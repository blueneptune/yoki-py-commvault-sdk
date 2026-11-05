# `cv.raw.audits`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:50 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

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

- `GET /v4/Audits` -> **200** (0.16 s)

  <details><summary>Answer</summary>

  ```json
  {
    "audits": [
      {
        "auditId": "A1AD169BCF7341B9BC8A823EA536FF31462",
        "hasAuditId": true,
        "severity": "Critical",
        "user": {
          "userId": 2,
          "userName": "user-01",
          "hasUserName": true
        },
        "createdTimeUtc": 1793904547,
        "entities": [
          {
            "entityType": 28,
            "entityId": 13,
            "entityName": "mount-path-01",
            "hasEntityName": true
          }
        ],
        "operation": {
          "operationMessage": {
            "localizedMessages": [
              {
                "localeId": 0,
                "localeText": "Delete a Server group"
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
                  "localeText": "Server group: bltlive-11051848-servers "
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
        "auditId": "A1AD169BCF7341B9BC8A823EA536FF31461",
        "hasAuditId": true,
        "severity": "Medium",
        "user": {
          "userId": 2,
          "userName": "user-01",
          "hasUserName": true
        },
        "createdTimeUtc": 1793904544,
        "entities": [
          {
            "entityType": 28,
            "entityId": 13,
            "entityName": "mount-path-01",
            "hasEntityName": true
          }
        ],
        "operation": {
          "operationMessage": {
            "localizedMessages": [
              {
                "localeId": 0,
                "localeText": "Update Server group properties"
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
                  "localeText": "Server group: bltlive-11051848-servers <br>Description  Changed from [bltlive: made by the SDK's live tests] to [bltlive: changed by the SDK's live tests]"
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
        "auditId": "A1AD169BCF7341B9BC8A823EA536FF31460",
        "hasAuditId": true,
        "severity": "Medium",
        "user": {
          "userId": 2,
          "userName": "user-01",
          "hasUserName": true
        },
        "createdTimeUtc": 1793904541,
        "entities": [
          {
            "entityType": 28,
            "entityId": 13,
            "entityName": "mount-path-01",
            "hasEntityName": true
          }
        ],
        "operation": {
          "operationMessage": {
            "localizedMessages": [
              {
                "localeId": 0,
                "localeText": "Create New Server group"
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
                  "localeText": "Server group: bltlive-11051848-servers <br>Force Client Side Download  Set to [NO]<br>Description  Set to [bltlive: made by the SDK's live tests]<br>Edc Supported Instance Type  Set to [0]<br>For activity type [BACKUP], enable activity : Yes<br>For activity type [RESTORE], enable activity : Yes<br>For activity type [ARCHIVEPRUNE], enable activity : Yes<br>Current unlock method  Set to [Manual]<br>... (1278 characters)"
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
      "... 444 more"
    ],
    "filterMatchCount": 447,
    "hasFilterMatchCount": true
  }
  ```

  </details>
