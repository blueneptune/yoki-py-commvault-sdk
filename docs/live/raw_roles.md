# `cv.raw.roles`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:37 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_permissions` - GET /V4/Permissions

```python
cv.raw.roles.get_permissions()
```

**On the wire**

- `GET /V4/Permissions` -> **200** (0.81 s)

  <details><summary>Answer</summary>

  ```json
  {
    "permissions": [
      {
        "category": {
          "id": 14,
          "name": "User Management"
        },
        "permissions": [
          {
            "id": 101,
            "name": "Add, delete and modify a user"
          },
          {
            "id": 102,
            "name": "Add, delete and modify a user group"
          },
          {
            "id": 249,
            "name": "Add Domain"
          },
          "... 4 more"
        ],
        "categoryList": [
          {
            "category": {
              "id": 135,
              "name": "Role"
            },
            "permissions": [
              {
                "id": 241,
                "name": "Create Role"
              },
              {
                "id": 242,
                "name": "Edit Role"
              },
              {
                "id": 243,
                "name": "Delete Role"
              }
            ]
          }
        ]
      },
      {
        "category": {
          "id": 101,
          "name": "Commcell"
        },
        "permissions": [
          {
            "id": 9,
            "name": "License Management"
          },
          {
            "id": 41,
            "name": "Download Center Management"
          },
          {
            "id": 65,
            "name": "Install Client"
          },
          "... 2 more"
        ]
      },
      {
        "category": {
          "id": 102,
          "name": "Client"
        },
        "permissions": [
          {
            "id": 2,
            "name": "Agent Management"
          },
          {
            "id": 3,
            "name": "Agent Scheduling"
          },
          {
            "id": 5,
            "name": "Upload"
          },
          "... 26 more"
        ]
      },
      "... 26 more"
    ]
  }
  ```

  </details>

## `list_role` - GET /V4/Role

```python
cv.raw.roles.list_role()
```

**On the wire**

- `GET /V4/Role` -> **200** (0.20 s)

  <details><summary>Answer</summary>

  ```json
  {
    "roles": [
      {
        "id": 1,
        "name": "user-group-01",
        "description": "System Created Role with all permissions",
        "status": "ENABLED",
        "company": {
          "id": 0,
          "name": ""
        }
      },
      {
        "id": 3,
        "name": "View",
        "description": "System Created Role for View permission",
        "status": "ENABLED",
        "company": {
          "id": 0,
          "name": ""
        }
      },
      {
        "id": 4,
        "name": "End Users",
        "description": "System created role for end users",
        "status": "ENABLED",
        "company": {
          "id": 0,
          "name": ""
        }
      },
      "... 30 more"
    ]
  }
  ```

  </details>

## `get_role` - GET /V4/Role/{roleId}

```python
cv.raw.roles.get_role('1')
```

**On the wire**

- `GET /V4/Role/1` -> **200** (0.29 s)

  <details><summary>Answer</summary>

  ```json
  {
    "id": 1,
    "name": "user-group-01",
    "description": "System Created Role with all permissions",
    "permissions": [
      {
        "type": "ALL_CATEGORIES"
      }
    ],
    "visibleToAll": false,
    "status": "ENABLED",
    "security": []
  }
  ```

  </details>
