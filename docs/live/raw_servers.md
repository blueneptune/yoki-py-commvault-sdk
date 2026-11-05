# `cv.raw.servers`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 16:43 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_platform_upgrade_options` - GET /V4/PlatformUpgrade/Options

> **SKIPPED** on this run: not swept: starts work or returns a file

```python
cv.raw.servers.get_platform_upgrade_options(...)
```

## `get_servers` - GET /V4/Servers

```python
cv.raw.servers.get_servers()
```

**On the wire**

- `GET /V4/Servers` -> **200** (0.31 s)

  <details><summary>Answer</summary>

  ```json
  {
    "totalServers": 1,
    "servers": [
      {
        "id": 2,
        "name": "commserve-02",
        "displayName": "commserve-02",
        "hostName": "commserve-02",
        "installTime": 0,
        "clientDescription": "",
        "cloudVendor": "NOT_APPLICABLE",
        "lastBackup": {
          "jobId": 0,
          "status": "NEVER_BACKED_UP"
        },
        "agents": [
          {
            "id": 121,
            "name": "Metrics Reporting Server",
            "applicationSize": 0,
            "lastSuccessfulAGPBackup": 0,
            "lastSuccessfulBackup": 0
          },
          {
            "id": 106,
            "name": "Virtual Server",
            "applicationSize": 0,
            "lastSuccessfulAGPBackup": 0,
            "lastSuccessfulBackup": 0
          },
          {
            "id": 33,
            "name": "Windows File System",
            "applicationSize": 574504329,
            "lastSuccessfulAGPBackup": 0,
            "lastSuccessfulBackup": 1793847612
          }
        ],
        "serverGroups": [
          {
            "id": 1,
            "name": "client-group-01"
          },
          {
            "id": 3,
            "name": "client-group-03"
          }
        ],
        "configured": true,
        "version": "11.46.30",
        "OS": "Windows Server 2025 Datacenter",
        "updateStatus": "NEEDS_UPDATE",
        "releaseStatus": "UP_TO_DATE",
        "isclient-group-01": true,
        "isCommServer": true,
        "isMARoleSet": true,
        "isMAPackageInstalled": true,
        "networkReadiness": "ONLINE",
        "tags": [],
        "clientRoles": [
          {
            "name": "Index Server"
          },
          {
            "name": "Web Server"
          },
          {
            "name": "Command Center"
          },
          "... 4 more"
        ]
      }
    ]
  }
  ```

  </details>

## `get_servers_comm_serve_host_name` - GET /V4/Servers/CommServeHostName

```python
cv.raw.servers.get_servers_comm_serve_host_name()
```

**On the wire**

- `GET /V4/Servers/CommServeHostName` -> **200** (0.16 s)

  <details><summary>Answer</summary>

  ```json
  {
    "servers": [
      {
        "commServe": "commserve-02",
        "name": "host-02",
        "id": 4
      },
      {
        "commServe": "commserve-02",
        "name": "host-03",
        "id": 5
      },
      {
        "commServe": "commserve-02",
        "name": "host-04",
        "id": 6
      },
      "... 9 more"
    ]
  }
  ```

  </details>

## `get_servers_domain` - GET /V4/Servers/Domain

```python
cv.raw.servers.get_servers_domain()
```

**On the wire**

- `GET /V4/Servers/Domain` -> **200** (0.16 s)

  <details><summary>Answer</summary>

  ```json
  {
    "servers": [
      {
        "domain": "",
        "name": "host-02",
        "id": 4
      },
      {
        "domain": "",
        "name": "host-03",
        "id": 5
      },
      {
        "domain": "",
        "name": "host-04",
        "id": 6
      },
      "... 9 more"
    ]
  }
  ```

  </details>

## `get_server_is_vm` - GET /V4/Servers/{serverId}/isVM

```python
cv.raw.servers.get_server_is_vm('2')
```

**On the wire**

- `GET /V4/Servers/2/isVM` -> **200** (0.07 s)

  <details><summary>Answer</summary>

  ```json
  {
    "isVM": true
  }
  ```

  </details>
