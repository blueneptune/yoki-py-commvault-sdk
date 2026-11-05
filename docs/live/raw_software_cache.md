# `cv.raw.software_cache`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 16:43 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_software_cache_qualified_servers` - GET /V4/SoftwareCache/QualifiedServers

```python
cv.raw.software_cache.get_software_cache_qualified_servers()
```

**On the wire**

- `GET /V4/SoftwareCache/QualifiedServers` -> **200** (0.10 s)

  <details><summary>Answer</summary>

  ```json
  {
    "softwareCacheDetailList": [
      {
        "cacheDirectory": "/opt/commvault/SW",
        "cache": {
          "name": "host-02",
          "id": 4
        }
      },
      {
        "cacheDirectory": "/opt/commvault/SW",
        "cache": {
          "name": "host-03",
          "id": 5
        }
      },
      {
        "cacheDirectory": "/opt/commvault/SW",
        "cache": {
          "name": "host-04",
          "id": 6
        }
      },
      "... 9 more"
    ]
  }
  ```

  </details>

## `list_software_cache` - GET /V4/SoftwareCache

```python
cv.raw.software_cache.list_software_cache()
```

**On the wire**

- `GET /V4/SoftwareCache` -> **200** (0.07 s)

  <details><summary>Answer</summary>

  ```json
  {
    "softwareCacheDetailList": [
      {
        "latestVersion": "11.46.30",
        "networkReadiness": 1,
        "cacheDirectory": "J:\\Program Files\\Commvault\\ContentStore\\SW",
        "enabled": true,
        "configurable": true,
        "status": 1,
        "cache": {
          "name": "commserve-02",
          "id": 2
        }
      }
    ]
  }
  ```

  </details>

## `get_software_cache` - GET /V4/SoftwareCache/{clientId}

```python
cv.raw.software_cache.get_software_cache('2')
```

**On the wire**

- `GET /V4/SoftwareCache/2` -> **200** (0.11 s)

  <details><summary>Answer</summary>

  ```json
  {
    "softwareCacheDetailList": [
      {
        "networkReadiness": 1,
        "cacheDirectory": "J:\\Program Files\\Commvault\\ContentStore\\SW",
        "enabled": true,
        "configurable": true,
        "status": 1,
        "cache": {
          "name": "commserve-02",
          "id": 2
        },
        "cacheContents": [
          {
            "additionalUpdates": "WinX64_11.0.0B80-SP46-CU30_SP46-CU30-1133, WinX64_11.0.0B80-SP46-CU30_SP46-CU30-1134, WinX64_11.0.0B80-SP46-CU30_SP46-CU30-1135, WinX64_11.0.0B80-SP46-CU30_SP46-CU30-1144, WinX64_11.0.0B80-SP46-CU30_SP46-CU30-1157, WinX64_11.0.0B80-SP46-CU30_SP46-CU30-1160, WinX64_11.0.0B80-SP46-CU30_SP46-CU30-1161, WinX64_11.0.0B80-SP46-CU30_SP46-CU30-1162, WinX64_11.0.0B80-SP46-CU30_SP46-CU30-1182, WinX64_11.0.0... (10318 characters)",
            "packagesInCache": "",
            "osName": "WinX64",
            "version": "11.46.30"
          },
          {
            "additionalUpdates": "linux-x8664_11.0.0B80-SP46-CU30_SP46-CU30-1132, linux-x8664_11.0.0B80-SP46-CU30_SP46-CU30-1134, linux-x8664_11.0.0B80-SP46-CU30_SP46-CU30-1135, linux-x8664_11.0.0B80-SP46-CU30_SP46-CU30-1160, linux-x8664_11.0.0B80-SP46-CU30_SP46-CU30-1161, linux-x8664_11.0.0B80-SP46-CU30_SP46-CU30-1162, linux-x8664_11.0.0B80-SP46-CU30_SP46-CU30-1182, linux-x8664_11.0.0B80-SP46-CU30_SP46-CU30-1183, linux-x8664_11.0... (11134 characters)",
            "packagesInCache": "",
            "osName": "linux-x8664",
            "version": "11.46.30"
          }
        ]
      }
    ]
  }
  ```

  </details>
