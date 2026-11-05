# `cv.raw.user`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 16:43 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_sessions` - GET /Sessions

> **SKIPPED** on this run: Commvault answered: 403

```python
cv.raw.user.get_sessions()
```

**On the wire**

- `GET /Sessions` -> **403** (0.01 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

## `get_users_and_groups` - GET /UsersAndGroups

```python
cv.raw.user.get_users_and_groups()
```

**On the wire**

- `GET /UsersAndGroups` -> **200** (0.20 s)

  <details><summary>Answer</summary>

  ```json
  {
    "userGroups": [
      {
        "fullName": "",
        "description": "Administrative Group",
        "email": "",
        "associatedUserOrUserGroup": {
          "GUID": "52F0152D-42C3-4CF1-8397-0B630F0E710E",
          "userGroupName": "user-group-01",
          "userGroupId": 1,
          "_type_": 15
        }
      },
      {
        "fullName": "",
        "description": "",
        "email": "",
        "associatedUserOrUserGroup": {
          "GUID": "1257F0EC-7176-4B01-9CC8-57AC452B2800",
          "userGroupName": "user-group-02",
          "userGroupId": 7,
          "_type_": 15
        }
      }
    ],
    "users": [
      {
        "fullName": "user-07",
        "description": "user-07",
        "email": "user-05",
        "associatedUserOrUserGroup": {
          "userId": 2,
          "userGUID": "70650349-DCD7-4363-9004-9562719F8130",
          "userName": "user-01",
          "_type_": 13
        }
      },
      {
        "fullName": "",
        "description": "",
        "email": "",
        "associatedUserOrUserGroup": {
          "userId": 7,
          "userGUID": "27CCE1D2-3A98-4517-8AB7-9B7912461EA5",
          "userName": "user-43",
          "_type_": 13
        }
      },
      {
        "fullName": "user-44",
        "description": "",
        "email": "user-03",
        "associatedUserOrUserGroup": {
          "userId": 6,
          "userGUID": "BC7AA2DD-10B4-4E28-AA84-137AB63F8B61",
          "userName": "user-03",
          "_type_": 13
        }
      }
    ]
  }
  ```

  </details>

## `list_user` - GET /User

```python
cv.raw.user.list_user()
```

**On the wire**

- `GET /User` -> **200** (0.16 s)

  <details><summary>Answer</summary>

  ```json
  {
    "processinginstructioninfo": {
      "attributes": [
        {
          "name": "exitval",
          "value": "0"
        }
      ]
    },
    "users": [
      {
        "loggedInMode": 0,
        "idleTime": 0,
        "userEntity": {
          "userGUID": "70650349-DCD7-4363-9004-9562719F8130",
          "userName": "user-01",
          "userId": 2
        }
      },
      {
        "loggedInMode": 0,
        "idleTime": 0,
        "userEntity": {
          "userGUID": "BC7AA2DD-10B4-4E28-AA84-137AB63F8B61",
          "userName": "user-03",
          "userId": 6
        }
      },
      {
        "loggedInMode": 0,
        "idleTime": 0,
        "userEntity": {
          "userGUID": "27CCE1D2-3A98-4517-8AB7-9B7912461EA5",
          "userName": "user-43",
          "userId": 7
        }
      }
    ]
  }
  ```

  </details>

## `list_user_v4` - GET /V4/user

```python
cv.raw.user.list_user_v4()
```

**On the wire**

- `GET /V4/user` -> **200** (0.14 s)

  <details><summary>Answer</summary>

  ```json
  {
    "numberOfUsers": 3,
    "users": [
      {
        "id": 2,
        "name": "user-01",
        "GUID": "70650349-DCD7-4363-9004-9562719F8130",
        "email": "user-05",
        "fullName": "user-07",
        "userPrincipalName": "",
        "lastLoggedIn": 1793717986,
        "enabled": true,
        "description": "user-07",
        "lockInfo": {
          "isLocked": false
        },
        "numberOfLaptops": 0,
        "company": {
          "id": 0,
          "name": ""
        }
      },
      {
        "id": 6,
        "name": "user-03",
        "GUID": "BC7AA2DD-10B4-4E28-AA84-137AB63F8B61",
        "email": "user-03",
        "fullName": "user-44",
        "userPrincipalName": "user-03",
        "lastLoggedIn": 1792511627,
        "enabled": true,
        "description": "",
        "lockInfo": {
          "isLocked": false
        },
        "numberOfLaptops": 0,
        "company": {
          "id": 0,
          "name": ""
        }
      },
      {
        "id": 7,
        "name": "user-43",
        "GUID": "27CCE1D2-3A98-4517-8AB7-9B7912461EA5",
        "email": "",
        "fullName": "",
        "userPrincipalName": "",
        "lastLoggedIn": 0,
        "enabled": true,
        "description": "",
        "lockInfo": {
          "isLocked": false
        },
        "numberOfLaptops": 0,
        "company": {
          "id": 0,
          "name": ""
        }
      }
    ]
  }
  ```

  </details>

## `get_user` - GET /User/{UserId}

```python
cv.raw.user.get_user('2')
```

**On the wire**

- `GET /User/2` -> **200** (0.12 s)

  <details><summary>Answer</summary>

  ```json
  {
    "processinginstructioninfo": {
      "attributes": [
        {
          "name": "exitval",
          "value": "0"
        }
      ]
    },
    "users": [
      {
        "istfaEnabled": false,
        "companyName": "Commcell",
        "UPN": "",
        "quotaLimitInGB": 100,
        "loggedInMode": 0,
        "enableUser": true,
        "email": "user-05",
        "edgeDriveQuotaLimitInGB": 100,
        "isServiceAccount": false,
        "enforceFSQuota": false,
        "idleTime": 0,
        "agePasswordDays": "<masked>",
        "authenticationMethod": "LOCAL",
        "isAccountLocked": false,
        "description": "user-07",
        "inheritGroupEdgeDriveQuotaSettings": true,
        "lastLogIntime": 1793717986,
        "enforceEdgeDriveQuota": false,
        "fullName": "user-07",
        "inheritGroupQuotaSettings": true,
        "userEntity": {
          "userGUID": "70650349-DCD7-4363-9004-9562719F8130",
          "userName": "user-01",
          "userId": 2
        },
        "currentAuthenticator": {
          "IdentityServerId": 0,
          "IdentityServerName": "Commcell",
          "ownerCompany": {
            "domainName": "Commcell",
            "id": 0
          }
        },
        "apiQuota": {
          "APILimit": 0,
          "APItimeFrame": 0
        },
        "LinkedCommvaultUser": {},
        "legalHoldInfo": {
          "legalHold": 0,
          "sourceEntity": {
            "entityType": 0,
            "entityId": 0
          }
        }
      }
    ]
  }
  ```

  </details>

## `get_user_by_name` - GET /User/byName(userName='{UserName}')

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.user.get_user_by_name(...)
```

## `get_user_v4` - GET /V4/user/{userId}

```python
cv.raw.user.get_user_v4('2')
```

**On the wire**

- `GET /V4/user/2` -> **200** (0.17 s)

  <details><summary>Answer</summary>

  ```json
  {
    "id": 2,
    "name": "user-01",
    "GUID": "70650349-DCD7-4363-9004-9562719F8130",
    "fullName": "user-07",
    "email": "user-05",
    "userPrincipalName": "",
    "enabled": true,
    "lockInfo": {
      "isLocked": false
    },
    "description": "user-07",
    "serviceType": "UNKNOWN",
    "lastLoggedIn": 1793717986,
    "company": {
      "id": 0,
      "name": ""
    },
    "authenticationMethod": "LOCAL",
    "authenticationMethodServer": {
      "id": 0,
      "name": "Commcell",
      "appKey": "",
      "company": {
        "id": 0,
        "name": "Commcell"
      }
    },
    "associatedUserGroups": [
      {
        "id": 1,
        "name": "user-group-01"
      }
    ],
    "legalHoldInfo": {
      "legalHold": "NOT_SET",
      "sourceEntity": {
        "entityType": 0,
        "entityId": 0
      }
    }
  }
  ```

  </details>
