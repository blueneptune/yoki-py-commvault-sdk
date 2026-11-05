# `cv.raw.hybrid_file_stores`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:37 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_hybrid_file_stores` - GET /V4/HybridFileStores

```python
cv.raw.hybrid_file_stores.get_hybrid_file_stores()
```

**On the wire**

- `GET /V4/HybridFileStores` -> **200** (0.19 s)

  <details><summary>Answer</summary>

  ```json
  {
    "hybridFileStores": []
  }
  ```

  </details>

## `get_hfs_share_status` - GET /v4/HFSShare/{HFSShareId}/Status

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.hybrid_file_stores.get_hfs_share_status(...)
```
