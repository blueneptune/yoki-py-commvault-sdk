# `cv.raw.role`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 16:43 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `list_role` - GET /Role

```python
cv.raw.role.list_role()
```

**On the wire**

- `GET /Role` -> **200** (0.15 s)

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
    "roleProperties": [
      {
        "role": {
          "roleId": 1,
          "GUID": "A5E556E9-C605-4857-BD0E-9FCA326CD227",
          "roleName": "user-group-01",
          "flags": {
            "disabled": false
          }
        }
      },
      {
        "role": {
          "roleId": 3,
          "GUID": "8EEF5B71-F339-4221-8B53-D3A046FFDF5F",
          "roleName": "View",
          "flags": {
            "disabled": false
          }
        }
      },
      {
        "role": {
          "roleId": 4,
          "GUID": "FE5AF7D4-CE62-4081-822F-58781DAF5B13",
          "roleName": "End Users",
          "flags": {
            "disabled": false
          }
        }
      },
      "... 30 more"
    ]
  }
  ```

  </details>

## `get_role` - GET /Role/{roleId}

```python
cv.raw.role.get_role('1')
```

**On the wire**

- `GET /Role/1` -> **200** (0.14 s)

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
    "roleProperties": [
      {
        "visibility": 0,
        "description": "System Created Role with all permissions",
        "role": {
          "roleId": 1,
          "GUID": "A5E556E9-C605-4857-BD0E-9FCA326CD227",
          "roleName": "user-group-01",
          "flags": {
            "disabled": false
          }
        },
        "categoryPermission": {
          "categoriesPermissionList": [
            {
              "_type_": 123
            }
          ]
        },
        "securityAssociations": {
          "ownerAssociations": {},
          "tagWithCompany": {
            "providerId": 0,
            "providerDomainName": "Commcell"
          }
        }
      }
    ]
  }
  ```

  </details>
