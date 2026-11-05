# `cv.raw.awsexport_db`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 16:43 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_instance_rds_discover_0` - GET /Instance/RDSDiscover/0

> **SKIPPED** on this run: Commvault answered: 500 - Failed to browse RDS inventory

```python
cv.raw.awsexport_db.get_instance_rds_discover_0()
```

**On the wire**

- `GET /Instance/RDSDiscover/0` -> **500** (0.09 s)

  <details><summary>Answer</summary>

  ```json
  {
    "type": "https://host-119/html/rfc9110#section-15.6.1",
    "title": "An error occurred while processing your request.",
    "status": 500,
    "detail": "Failed to browse RDS inventory",
    "traceId": "00-5e625bd6377e848d2e6878e9f123f65c-f0f0fb5e2f7e29e1-01"
  }
  ```

  </details>

## `list_instance` - GET /Instance

> **SKIPPED** on this run: Commvault answered: 400

```python
cv.raw.awsexport_db.list_instance()
```

**On the wire**

- `GET /Instance` -> **400** (0.07 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

## `get_backupset` - GET /backupset/{backupsetId}

```python
cv.raw.awsexport_db.get_backupset('7')
```

**On the wire**

- `GET /Backupset` -> **400** (0.06 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

- `GET /backupset/7` -> **200** (0.42 s)

  <details><summary>Answer</summary>

  ```json
  {
    "backupsetProperties": [
      {
        "modifiedTime": 1791258096,
        "applicationSize": 262481,
        "totalBackupSize": 2112985,
        "lastBackupTime": 1793826011,
        "firstBackupTime": 1791259361,
        "scIdxEnabled": 1,
        "sizeOnMedia": 1116350,
        "dedupeRatio": 47.1672,
        "securityAssociations": {
          "ownerAssociations": {},
          "tagWithCompany": {
            "providerId": 0,
            "providerDomainName": "Commcell"
          }
        },
        "content": [
          {
            "path": "/"
          },
          {
            "path": "/data"
          }
        ],
        "backupsetSecurity": {
          "associatedUserGroups": [
            {
              "userGroupId": 1,
              "_type_": 15,
              "userGroupName": "user-group-01"
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
          "ownerCapabilities": {}
        },
        "fsBackupSet": {
          "hasOneTouchSubclient": true,
          "hasBackupSystemStateSubclient": true,
          "isIndexingV2": true,
          "isUseBlockLevelBackup": false,
          "preserveFileAccessTimes": false,
          "useDCserviceForScan": true
        },
        "credentialEntity": "<masked>",
        "planEntity": {},
        "commonBackupSet": {
          "newBackupSetName": "backupset-01",
          "slaStatus": 2,
          "isDeleted": false,
          "isFanInBackupSet": false,
          "isLegalHoldBackupset": false,
          "isArchivingEnabled": false,
          "isMyBackupSet": false,
          "isbackupset-01": true,
          "isHidden": false,
          "isMining": false,
          "isSnapEnabled": false
        },
        "backupSetEntity": {
          "clientName": "host-02",
          "instanceName": "asset-01",
          "displayName": "host-02",
          "backupsetId": 7,
          "_type_": 6,
          "instanceId": 1,
          "backupsetGUID": "D8313A81-59C2-485A-ABBA-3AD0CA6645E4",
          "clientId": 4,
          "appName": "File System",
          "backupsetName": "backupset-01",
          "applicationId": 29,
          "entityInfo": {
            "companyId": 0,
            "companyName": "Commcell"
          }
        }
      }
    ]
  }
  ```

  </details>
