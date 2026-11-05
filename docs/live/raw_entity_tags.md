# `cv.raw.entity_tags`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:37 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_ediscovery_tags` - GET /Ediscovery/Tags

```python
cv.raw.entity_tags.get_ediscovery_tags()
```

**On the wire**

- `GET /Ediscovery/Tags` -> **200** (0.32 s)

  <details><summary>Answer</summary>

  ```json
  {
    "listOftagSetList": [
      {
        "tagSetsAndItems": [
          {
            "container": {
              "capabilities": 4328650375167,
              "containerFullName": "CommonTags",
              "containerType": 9504,
              "containerName": "CommonTags",
              "deDuplicateFields": "",
              "containerOwnerType": 1,
              "comment": "System subclient-01 tag set",
              "attribute": 2,
              "containerId": 1,
              "containerGuid": "152AC4AC-ADDE-423C-8989-84C1EE223927",
              "ownerInfo": {
                "aliasName": "user-01",
                "userGuid": "70650349-DCD7-4363-9004-9562719F8130",
                "userName": "Administrator"
              }
            },
            "tags": [
              {
                "tagOwnerType": 1,
                "tagId": 1,
                "name": "Un-Reviewed",
                "flags": 2,
                "fullName": "user-07",
                "description": "System Tag",
                "id": "0D8BD683-993F-49A2-BEBF-919A45E49E07",
                "attribute": {
                  "system": true
                }
              },
              {
                "tagOwnerType": 1,
                "tagId": 2,
                "name": "Pending",
                "flags": 2,
                "fullName": "user-08",
                "description": "System Tag",
                "id": "64BB6877-A1E8-4367-AB52-136FCF258FD5",
                "attribute": {
                  "system": true
                }
              },
              {
                "tagOwnerType": 1,
                "tagId": 3,
                "name": "Responsive",
                "flags": 2,
                "fullName": "user-09",
                "description": "System Tag",
                "id": "2E2B92B3-A644-43F3-B344-494E105B6C8E",
                "attribute": {
                  "system": true
                }
              },
              "... 4 more"
            ]
          }
        ]
      },
      {
        "tagSetsAndItems": [
          {
            "container": {
              "capabilities": 4328650375167,
              "containerFullName": "DiscoveryEntity",
              "containerType": 9504,
              "containerName": "DiscoveryEntity",
              "deDuplicateFields": "",
              "containerOwnerType": 1,
              "comment": "Discovery Entity Tag Set",
              "attribute": 2,
              "containerId": 2,
              "containerGuid": "1151020F-FB4C-44C7-BAE4-D47FB2808BC0",
              "ownerInfo": {
                "aliasName": "user-01",
                "userGuid": "70650349-DCD7-4363-9004-9562719F8130",
                "userName": "Administrator"
              }
            },
            "tags": [
              {
                "tagOwnerType": 1,
                "tagId": 8,
                "name": "SSN",
                "flags": 2,
                "fullName": "user-14",
                "description": "Social Security Number",
                "id": "F76C8407-1B96-4205-ACB9-067F92C56B2E",
                "attribute": {
                  "system": true
                }
              },
              {
                "tagOwnerType": 1,
                "tagId": 9,
                "name": "American",
                "flags": 2,
                "fullName": "user-15",
                "description": "American Express",
                "id": "98D1F71D-DCD9-49E4-B322-B24CE87A3788",
                "attribute": {
                  "system": true
                }
              },
              {
                "tagOwnerType": 1,
                "tagId": 10,
                "name": "VISA",
                "flags": 2,
                "fullName": "user-16",
                "description": "VISA Card",
                "id": "C13CC358-B81A-46CC-8350-42A2C18CD02A",
                "attribute": {
                  "system": true
                }
              },
              "... 5 more"
            ]
          }
        ]
      },
      {
        "tagSetsAndItems": [
          {
            "container": {
              "capabilities": 4328650375167,
              "containerFullName": "HealthSafetyRecords",
              "containerType": 9504,
              "containerName": "HealthSafetyRecords",
              "deDuplicateFields": "",
              "containerOwnerType": 1,
              "comment": "Health & Safety Records Tag Set",
              "attribute": 2,
              "containerId": 4,
              "containerGuid": "084E495A-B687-4294-B330-AAB4373035D9",
              "ownerInfo": {
                "aliasName": "user-01",
                "userGuid": "70650349-DCD7-4363-9004-9562719F8130",
                "userName": "Administrator"
              }
            },
            "tags": [
              {
                "tagOwnerType": 1,
                "tagId": 25,
                "name": "Chemical Exposure",
                "flags": 2,
                "fullName": "user-22",
                "description": "Chemical Exposure",
                "id": "580DBAB0-C4B6-469B-B7AB-CCA4174B16BF",
                "attribute": {
                  "system": true
                }
              },
              {
                "tagOwnerType": 1,
                "tagId": 26,
                "name": "Occupational Injury",
                "flags": 2,
                "fullName": "user-23",
                "description": "Occupational Injury",
                "id": "DF703CDF-60C1-4EC4-8D9F-B57E04FA92A2",
                "attribute": {
                  "system": true
                }
              },
              {
                "tagOwnerType": 1,
                "tagId": 27,
                "name": "Hazardous Waste",
                "flags": 2,
                "fullName": "user-24",
                "description": "Hazardous Waste",
                "id": "8A319894-7B6E-4A0F-8898-3E41FCB17D39",
                "attribute": {
                  "system": true
                }
              },
              "... 2 more"
            ]
          }
        ]
      },
      "... 3 more"
    ]
  }
  ```

  </details>

## `get_tag` - GET /Tags/{entityType}/{entityId}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.entity_tags.get_tag(...)
```
