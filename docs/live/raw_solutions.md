# `cv.raw.solutions`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:37 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_solutions` - GET /V4/Solutions

```python
cv.raw.solutions.get_solutions()
```

**On the wire**

- `GET /V4/Solutions` -> **200** (0.13 s)

  <details><summary>Answer</summary>

  ```json
  {
    "id": [
      {
        "name": "File Servers",
        "id": 1,
        "commandCenterStateValue": 0,
        "commandCenterState": "fsServersList",
        "associatedWorkloads": [
          {
            "name": "NFS",
            "id": 5000
          },
          {
            "name": "CIFS",
            "id": 5001
          },
          {
            "name": "OpenVMS",
            "id": 5002
          },
          "... 30 more"
        ]
      },
      {
        "name": "Virtualization",
        "id": 2,
        "commandCenterStateValue": 1,
        "commandCenterState": "hypervisors,vmGroups,userVMs",
        "associatedWorkloads": [
          {
            "name": "ESX",
            "id": 10100
          },
          {
            "name": "VMware vCenter",
            "id": 10101
          },
          {
            "name": "Microsoft Hyper-V",
            "id": 10102
          },
          "... 27 more"
        ]
      },
      {
        "name": "Databases",
        "id": 3,
        "commandCenterStateValue": 3,
        "commandCenterState": "instances,dbDatabases,dbInstancesClone",
        "associatedWorkloads": [
          {
            "name": "AWS RDS SQL",
            "id": 5004
          },
          {
            "name": "Azure SQL Database",
            "id": 5005
          },
          {
            "name": "Azure SQL Managed Instance",
            "id": 5006
          },
          "... 51 more"
        ]
      },
      "... 1 more"
    ]
  }
  ```

  </details>
