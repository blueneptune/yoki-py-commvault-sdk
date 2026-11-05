# `cv.raw.user_group`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 16:43 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `list_user_group` - GET /UserGroup

```python
cv.raw.user_group.list_user_group()
```

**On the wire**

- `GET /UserGroup` -> **200** (0.14 s)

  <details><summary>Answer</summary>

  ```json
  {
    "userGroups": [
      {
        "userGroupEntity": {
          "userGroupId": 1,
          "userGroupName": "user-group-01",
          "GUID": "52F0152D-42C3-4CF1-8397-0B630F0E710E"
        }
      },
      {
        "userGroupEntity": {
          "userGroupId": 7,
          "userGroupName": "user-group-02",
          "GUID": "1257F0EC-7176-4B01-9CC8-57AC452B2800"
        }
      }
    ]
  }
  ```

  </details>

## `list_user_group_v4` - GET /V4/UserGroup

```python
cv.raw.user_group.list_user_group_v4()
```

**On the wire**

- `GET /V4/UserGroup` -> **200** (0.19 s)

  <details><summary>Answer</summary>

  ```json
  {
    "userGroups": [
      {
        "id": 1,
        "name": "user-group-01",
        "GUID": "52F0152D-42C3-4CF1-8397-0B630F0E710E",
        "serviceType": "UNKNOWN",
        "description": "Administrative Group",
        "provider": {
          "id": 0,
          "name": ""
        },
        "enabled": true,
        "allowMultipleCompanyMembers": false,
        "company": {
          "id": 0,
          "name": ""
        }
      },
      {
        "id": 7,
        "name": "user-group-02",
        "GUID": "1257F0EC-7176-4B01-9CC8-57AC452B2800",
        "serviceType": "UNKNOWN",
        "description": "",
        "provider": {
          "id": 0,
          "name": ""
        },
        "enabled": true,
        "allowMultipleCompanyMembers": false,
        "company": {
          "id": 0,
          "name": ""
        }
      }
    ]
  }
  ```

  </details>

## `get_user_group` - GET /UserGroup/{UserGroupId}

```python
cv.raw.user_group.get_user_group('1')
```

**On the wire**

- `GET /UserGroup/1` -> **200** (0.63 s)

  <details><summary>Answer</summary>

  ```json
  {
    "userGroups": [
      {
        "serviceType": 0,
        "enableTwoFactorAuthentication": 2,
        "enforceFSQuota": false,
        "agePasswordDays": "<masked>",
        "showAzureGuidOption": false,
        "enableLocalAuthentication": 2,
        "quotaLimitInGB": 100,
        "azureGUID": "",
        "description": "Administrative Group",
        "allAssociations": true,
        "allowMultiCompanyMembers": false,
        "enabled": true,
        "isCommCellUserGroup": true,
        "email": "",
        "edgeDriveQuotaLimitInGB": 100,
        "enforceEdgeDriveQuota": false,
        "preferenceMachineCentricClient": true,
        "allCapabilities": true,
        "isBlackListed": false,
        "pswdHistoryCount": 0,
        "securityAssociations": {
          "associations": [
            {
              "entities": {
                "entity": [
                  {
                    "clientGroupName": "client-group-05",
                    "clientGroupId": 5,
                    "_type_": 28
                  }
                ]
              },
              "properties": {
                "isOperatorAssociation": false,
                "isCreatorAssociation": false,
                "role": {
                  "_type_": 120,
                  "roleId": 1,
                  "roleName": "user-group-01",
                  "flags": {
                    "disabled": false
                  }
                }
              }
            },
            {
              "entities": {
                "entity": [
                  {
                    "clientGroupName": "client-group-06",
                    "clientGroupId": 6,
                    "_type_": 28
                  }
                ]
              },
              "properties": {
                "isOperatorAssociation": false,
                "isCreatorAssociation": false,
                "role": {
                  "_type_": 120,
                  "roleId": 1,
                  "roleName": "user-group-01",
                  "flags": {
                    "disabled": false
                  }
                }
              }
            },
            {
              "entities": {
                "entity": [
                  {
                    "commCellName": "commserve-02",
                    "commCellId": 2,
                    "_type_": 1
                  }
                ]
              },
              "properties": {
                "isOperatorAssociation": false,
                "isCreatorAssociation": false,
                "categoryPermission": {
                  "categoriesPermissionList": [
                    {
                      "permissionName": "Create Role",
                      "permissionId": 241,
                      "_type_": 122,
                      "categoryId": 135
                    },
                    {
                      "permissionName": "Edit Role",
                      "permissionId": 242,
                      "_type_": 122,
                      "categoryId": 135
                    },
                    {
                      "permissionName": "Delete Role",
                      "permissionId": 243,
                      "_type_": 122,
                      "categoryId": 135
                    }
                  ]
                }
              }
            }
          ]
        },
        "apiQuota": {},
        "plan": {},
        "users": [
          {
            "userName": "user-01",
            "userId": 2
          },
          {
            "userName": "user-03",
            "userId": 6
          },
          {
            "userName": "user-43",
            "userId": 7
          }
        ],
        "vcloudGroupProp": {
          "vCloudDirectorFlag": false
        },
        "groupSecurity": {
          "ownerAssociations": {},
          "tagWithCompany": {
            "providerId": 0,
            "providerDomainName": "Commcell"
          }
        },
        "legalHoldInfo": {
          "legalHold": 0
        },
        "provider": {
          "providerId": 0
        },
        "userGroupEntity": {
          "userGroupId": 1,
          "userGroupName": "user-group-01",
          "GUID": "52F0152D-42C3-4CF1-8397-0B630F0E710E"
        }
      }
    ]
  }
  ```

  </details>

## `get_user_group_by_name` - GET /UserGroup/byName(userGroupName='{UserGroupName}')

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.user_group.get_user_group_by_name(...)
```

## `get_user_group_v4` - GET /V4/UserGroup/{userGroupId}

```python
cv.raw.user_group.get_user_group_v4('1')
```

**On the wire**

- `GET /V4/UserGroup/1` -> **200** (0.76 s)

  <details><summary>Answer</summary>

  ```json
  {
    "id": 1,
    "name": "user-group-01",
    "GUID": "52F0152D-42C3-4CF1-8397-0B630F0E710E",
    "description": "Administrative Group",
    "enabled": true,
    "serviceType": "UNKNOWN",
    "email": "",
    "enableTwoFactorAuthentication": "DISABLED_AT_COMPANY",
    "enableLocalAuthentication": "DISABLED_AT_COMPANY",
    "laptopAdmins": false,
    "enforceFSQuota": false,
    "azureGUID": "",
    "eligibleToAllowMultipleCompanyMembers": true,
    "allowMultipleCompanyMembers": false,
    "company": {
      "id": 0,
      "name": ""
    },
    "users": [
      {
        "id": 2,
        "name": "user-01"
      },
      {
        "id": 6,
        "name": "user-03"
      },
      {
        "id": 7,
        "name": "user-43"
      }
    ]
  }
  ```

  </details>
