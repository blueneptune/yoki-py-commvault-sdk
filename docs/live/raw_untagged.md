# `cv.raw.untagged`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:50 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_workload_resource_pool` - GET /V4/Workload/ResourcePool

> **SKIPPED** on this run: Commvault answered: 400 - Invalid request received to get the resource pool for workload

```python
cv.raw.untagged.get_workload_resource_pool()
```

**On the wire**

- `GET /V4/Workload/ResourcePool` -> **400** (0.08 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorMessage": "Invalid request received to get the resource pool for workload",
    "errorCode": 12
  }
  ```

  </details>

## `list_asset_discovery_criteria` - GET /Asset/Discovery/Criteria

> **SKIPPED** on this run: Commvault answered: error 12: Failed to get asset discovery criteria : [Cloud Discovery Object Initialization Failed . Please check logs for details]

```python
cv.raw.untagged.list_asset_discovery_criteria()
```

**On the wire**

- `GET /Asset/Discovery/Criteria` -> **200** (0.08 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorMessage": "Failed to get asset discovery criteria : [Cloud Discovery Object Initialization Failed . Please check logs for details]",
    "errorCode": 12,
    "discoveryCriteria": {}
  }
  ```

  </details>

## `get_grid_filter` - GET /V4/GridFilters/{gridId}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.untagged.get_grid_filter(...)
```

## `get_storage_pool_backup_locations` - GET /V4/StoragePool/{storagePoolId}/BackupLocations

> **SKIPPED** on this run: Commvault answered: 403

```python
cv.raw.untagged.get_storage_pool_backup_locations('2')
```

**On the wire**

- `GET /V4/StoragePool/2/BackupLocations` -> **403** (0.01 s)

  <details><summary>Answer</summary>

  (no body)

  </details>
