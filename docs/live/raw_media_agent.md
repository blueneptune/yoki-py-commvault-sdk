# `cv.raw.media_agent`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:50 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_ddb_media_agents` - GET /V4/DDB/MediaAgents

```python
cv.raw.media_agent.get_ddb_media_agents()
```

**On the wire**

- `GET /V4/DDB/MediaAgents` -> **200** (0.20 s)

  <details><summary>Answer</summary>

  ```json
  {
    "mediaAgents": [
      {
        "id": 2,
        "name": "commserve-02",
        "displayName": "commserve-02",
        "releaseId": 16,
        "SIMOSId": 210,
        "isDDBSubclientConfigured": true,
        "OSType": "Windows",
        "isConfigured": 1,
        "DDBDisks": [],
        "region": {
          "id": 5,
          "name": "North America",
          "displayName": "North America"
        }
      }
    ]
  }
  ```

  </details>

## `list_media_agent` - GET /V4/mediaAgent

```python
cv.raw.media_agent.list_media_agent()
```

**On the wire**

- `GET /V4/mediaAgent` -> **200** (0.38 s)

  <details><summary>Answer</summary>

  ```json
  {
    "mediaAgents": [
      {
        "id": 2,
        "name": "commserve-02",
        "displayName": "commserve-02",
        "netHostName": "commserve-02",
        "status": "ONLINE",
        "isUnlicensedMA": "<masked>",
        "isDDBSupported": true,
        "operatingSystem": {
          "id": 210,
          "name": "Windows Server 2025 Datacenter",
          "type": "Windows"
        },
        "powerManagementInfo": {
          "isPowerMgmtSupported": false
        },
        "version": "11 SP46.30",
        "releaseId": 16,
        "description": "",
        "company": {
          "id": 0,
          "name": ""
        },
        "region": {
          "id": 5,
          "name": "North America",
          "displayName": "North America"
        }
      }
    ]
  }
  ```

  </details>

## `get_media_agent` - GET /V4/mediaAgent/{mediaAgentId}

```python
cv.raw.media_agent.get_media_agent('2')
```

**On the wire**

- `GET /V4/mediaAgent/2` -> **200** (0.36 s)

  <details><summary>Answer</summary>

  ```json
  {
    "general": {
      "id": 2,
      "name": "commserve-02",
      "displayName": "commserve-02",
      "status": "ONLINE",
      "operatingSystem": "Windows Server 2025 Datacenter",
      "version": "11 SP46.30",
      "description": ""
    },
    "indexCache": {
      "path": "G:\\commvaultdata\\IndexCache",
      "logsCache": {
        "enabled": false,
        "path": "G:\\commvaultdata\\IndexCache"
      }
    },
    "control": {
      "enabled": true,
      "optimizeForConcurrentLANBackups": true,
      "maintenanceMode": false,
      "ransomwareProtection": true,
      "parallelDataTransferOperations": 100,
      "enableAfterDelay": false
    },
    "security": []
  }
  ```

  </details>

## `get_media_agent_associations` - GET /V4/mediaAgent/{mediaAgentId}/Associations

```python
cv.raw.media_agent.get_media_agent_associations('2')
```

**On the wire**

- `GET /V4/mediaAgent/2/Associations` -> **200** (0.14 s)

  <details><summary>Answer</summary>

  ```json
  {
    "associations": [
      {
        "entityType": "Storage",
        "name": "storage-pool-01",
        "id": 2,
        "storageInfo": {
          "storagePoolType": "DEDUPLICATION",
          "storageType": "DISK",
          "deviceType": {
            "name": "MAGNETIC",
            "id": 1
          }
        }
      }
    ]
  }
  ```

  </details>

## `get_media_agent_reconstruction_jobs` - GET /MediaAgent/{MediaAgent}/ReconstructionJobs

```python
cv.raw.media_agent.get_media_agent_reconstruction_jobs('2')
```

**On the wire**

- `GET /MediaAgent/2/ReconstructionJobs` -> **200** (0.09 s)

  <details><summary>Answer</summary>

  ```json
  {}
  ```

  </details>

## `get_media_agent_redistribution_jobs` - GET /MediaAgent/{MediaAgent}/RedistributionJobs

```python
cv.raw.media_agent.get_media_agent_redistribution_jobs('2')
```

**On the wire**

- `GET /MediaAgent/2/RedistributionJobs` -> **200** (0.09 s)

  <details><summary>Answer</summary>

  ```json
  {}
  ```

  </details>
