# `cv.raw.cloud_storage`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:50 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `list_storage_cloud` - GET /V4/Storage/Cloud

```python
cv.raw.cloud_storage.list_storage_cloud()
```

**On the wire**

- `GET /V4/Storage/Cloud` -> **200** (0.20 s)

  <details><summary>Answer</summary>

  ```json
  {
    "cloudStorage": []
  }
  ```

  </details>

## `get_storage_cloud` - GET /V4/Storage/Cloud/{cloudStorageId}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.cloud_storage.get_storage_cloud(...)
```

## `get_storage_cloud_bucket` - GET /V4/Storage/Cloud/{cloudStorageId}/Bucket/{bucketId}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.cloud_storage.get_storage_cloud_bucket(...)
```

## `get_storage_cloud_bucket_access_path_media_agents`

GET /V4/Storage/Cloud/{cloudStorageId}/Bucket/{bucketId}/AccessPath/MediaAgents

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.cloud_storage.get_storage_cloud_bucket_access_path_media_agents(...)
```

## `get_storage_cloud_metadata_cache`

GET /V4/Storage/Cloud/{cloudStorageId}/MetadataCache/{metadataCacheId}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.cloud_storage.get_storage_cloud_metadata_cache(...)
```
