# The CommServe: version, identity, what it runs

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:37 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `cv.commcell.info()` - the CommServe's version, Service Pack and operating system

What the live pages are stamped with.

```python
record.result({k: commserve.get(k) for k in ("csVersionInfo", "currentSPVersion", "osType")})
assert commserve.get("currentSPVersion")
```

**What the SDK gave back**

```json
{
  "csVersionInfo": "11 SP46.30",
  "currentSPVersion": 46,
  "osType": "Windows"
}
```

## `cv.commcell.packages()` - the software packages it can push to a client

```python
packages = cv.commcell.packages()
record.result(packages[:5])
assert packages
```

**On the wire**

- `GET /V4/commcell/available-packages` -> **200** (0.23 s)

  <details><summary>Answer</summary>

  ```json
  {
    "pkgList": [
      {
        "fileName": "WindowsFileServer64.exe",
        "showInPackageDownloader": 1,
        "fileSize": "528 MB",
        "releaseDate": "Jun16, 2026, 2:18 PM",
        "checksum": "8ce62a3c5740490e0037b7d47309dae1b0d411e7726f828c318b8271583eb16f",
        "downloadURL": "https://downloadcenter.commvault.com/CVDownloadCenter/openfiles/cc/11/46/software/WindowsFileServer64.exe",
        "platform": "WindowsFileServer64"
      },
      {
        "fileName": "ActiveDirectory64.exe",
        "showInPackageDownloader": 1,
        "fileSize": "286 MB",
        "releaseDate": "Jun16, 2026, 1:35 PM",
        "checksum": "3df547b437c03edd140b3d88e8a2a50ffbf3508ee54f05fc2728cb8be94bf2d2",
        "downloadURL": "https://downloadcenter.commvault.com/CVDownloadCenter/openfiles/cc/11/46/software/ActiveDirectory64.exe",
        "platform": "ActiveDirectory64"
      },
      {
        "fileName": "ADForestAccessNode64.exe",
        "showInPackageDownloader": 1,
        "fileSize": "716 MB",
        "releaseDate": "Jun16, 2026, 1:48 PM",
        "checksum": "87e27d43d5cfae381ccf900d22c699254878a97cddc3eca4bbf3648fd8efed7c",
        "downloadURL": "https://downloadcenter.commvault.com/CVDownloadCenter/openfiles/cc/11/46/software/ADForestAccessNode64.exe",
        "platform": "ADForestAccessNode64"
      },
      "... 134 more"
    ]
  }
  ```

  </details>

**What the SDK gave back**

```json
[
  {
    "fileName": "WindowsFileServer64.exe",
    "showInPackageDownloader": 1,
    "fileSize": "528 MB",
    "releaseDate": "Jun16, 2026, 2:18 PM",
    "checksum": "8ce62a3c5740490e0037b7d47309dae1b0d411e7726f828c318b8271583eb16f",
    "downloadURL": "https://downloadcenter.commvault.com/CVDownloadCenter/openfiles/cc/11/46/software/WindowsFileServer64.exe",
    "platform": "WindowsFileServer64"
  },
  {
    "fileName": "ActiveDirectory64.exe",
    "showInPackageDownloader": 1,
    "fileSize": "286 MB",
    "releaseDate": "Jun16, 2026, 1:35 PM",
    "checksum": "3df547b437c03edd140b3d88e8a2a50ffbf3508ee54f05fc2728cb8be94bf2d2",
    "downloadURL": "https://downloadcenter.commvault.com/CVDownloadCenter/openfiles/cc/11/46/software/ActiveDirectory64.exe",
    "platform": "ActiveDirectory64"
  },
  {
    "fileName": "ADForestAccessNode64.exe",
    "showInPackageDownloader": 1,
    "fileSize": "716 MB",
    "releaseDate": "Jun16, 2026, 1:48 PM",
    "checksum": "87e27d43d5cfae381ccf900d22c699254878a97cddc3eca4bbf3648fd8efed7c",
    "downloadURL": "https://downloadcenter.commvault.com/CVDownloadCenter/openfiles/cc/11/46/software/ADForestAccessNode64.exe",
    "platform": "ADForestAccessNode64"
  },
  "... 2 more"
]
```

## `cv.clients.list()` - every client: servers, MediaAgents, the CommServe itself

```python
clients = cv.clients.list()
record.result(clients[:3])
assert clients
```

**On the wire**

- `GET /Client` -> **200** (0.11 s)

  <details><summary>Answer</summary>

  ```json
  {
    "clientProperties": [
      {
        "client": {
          "evmgrcPort": 0,
          "cvdPort": 8400,
          "clientEntity": {
            "hostName": "commserve-02",
            "clientName": "commserve-02",
            "displayName": "commserve-02",
            "_type_": 3,
            "clientId": 2,
            "clientGUID": "2DCFEA81-1B84-4E4D-ADB4-C317F96A112E"
          }
        },
        "clientProps": {
          "iSCSIPort": 3260,
          "clusterType": 0
        }
      },
      {
        "client": {
          "evmgrcPort": 0,
          "cvdPort": 0,
          "clientEntity": {
            "hostName": "host-01",
            "clientName": "host-01",
            "displayName": "host-01",
            "_type_": 3,
            "clientId": 3,
            "clientGUID": "F5AB5F53-80CD-4D54-8B89-D1CEB278387B"
          }
        },
        "clientProps": {
          "iSCSIPort": 3260,
          "clusterType": 15
        }
      },
      {
        "client": {
          "evmgrcPort": 8402,
          "cvdPort": 8400,
          "clientEntity": {
            "hostName": "host-02",
            "clientName": "host-02",
            "displayName": "host-02",
            "_type_": 3,
            "clientId": 4,
            "clientGUID": "99CA0BBB-F13D-4DEA-9778-08A913D3FEFA"
          }
        },
        "clientProps": {
          "iSCSIPort": 3260,
          "clusterType": 0
        }
      },
      "... 12 more"
    ]
  }
  ```

  </details>

**What the SDK gave back**

```json
[
  {
    "hostName": "commserve-02",
    "clientName": "commserve-02",
    "displayName": "commserve-02",
    "_type_": 3,
    "clientId": 2,
    "clientGUID": "2DCFEA81-1B84-4E4D-ADB4-C317F96A112E"
  },
  {
    "hostName": "host-01",
    "clientName": "host-01",
    "displayName": "host-01",
    "_type_": 3,
    "clientId": 3,
    "clientGUID": "F5AB5F53-80CD-4D54-8B89-D1CEB278387B"
  },
  {
    "hostName": "host-02",
    "clientName": "host-02",
    "displayName": "host-02",
    "_type_": 3,
    "clientId": 4,
    "clientGUID": "99CA0BBB-F13D-4DEA-9778-08A913D3FEFA"
  }
]
```

## `cv.storage.disk()` - disk storage pools, with capacity and use

What blt's storage monitoring will read.

```python
record.result(cv.storage.disk()[:3])
```

**On the wire**

- `GET /V4/Storage/Disk` -> **200** (0.24 s)

  <details><summary>Answer</summary>

  ```json
  {
    "diskStorage": [
      {
        "id": 2,
        "name": "storage-pool-01",
        "storagePoolType": "DEDUPLICATION",
        "status": "Online",
        "capacity": 1048572,
        "freeSpace": 1025530,
        "usableFreeSpace": 1005050,
        "company": {
          "id": 0,
          "name": ""
        },
        "tags": []
      }
    ]
  }
  ```

  </details>

**What the SDK gave back**

```json
[
  {
    "id": 2,
    "name": "storage-pool-01",
    "storagePoolType": "DEDUPLICATION",
    "status": "Online",
    "capacity": 1048572,
    "freeSpace": 1025530,
    "usableFreeSpace": 1005050,
    "company": {
      "id": 0,
      "name": ""
    },
    "tags": []
  }
]
```

## `cv.plans.list()` - the plans: what protects what

```python
record.result(cv.plans.list()[:3])
```

**On the wire**

- `GET /V4/Plan/Summary` -> **200** (0.25 s)

  <details><summary>Answer</summary>

  ```json
  {
    "plansCount": 2,
    "plans": [
      {
        "planType": "Server",
        "searchType": "METADATA",
        "derivable": false,
        "description": "plan-01",
        "RPO": 0,
        "associatedEntities": 16,
        "numberOfCopies": 1,
        "status": "ENABLED",
        "plan": {
          "name": "plan-01",
          "id": 1
        }
      },
      {
        "planType": "Server",
        "searchType": "METADATA",
        "derivable": false,
        "description": "bltlive-11051831-plan",
        "RPO": 0,
        "associatedEntities": 0,
        "numberOfCopies": 1,
        "status": "ENABLED",
        "plan": {
          "name": "bltlive-11051831-plan-2",
          "id": 3
        }
      }
    ]
  }
  ```

  </details>

**What the SDK gave back**

```json
[
  {
    "planType": "Server",
    "searchType": "METADATA",
    "derivable": false,
    "description": "plan-01",
    "RPO": 0,
    "associatedEntities": 16,
    "numberOfCopies": 1,
    "status": "ENABLED",
    "plan": {
      "name": "plan-01",
      "id": 1
    }
  },
  {
    "planType": "Server",
    "searchType": "METADATA",
    "derivable": false,
    "description": "bltlive-11051831-plan",
    "RPO": 0,
    "associatedEntities": 0,
    "numberOfCopies": 1,
    "status": "ENABLED",
    "plan": {
      "name": "bltlive-11051831-plan-2",
      "id": 3
    }
  }
]
```
