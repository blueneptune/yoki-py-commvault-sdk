# `cv.raw.hyper_scale_storage`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:50 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `list_storage_hyper_scale` - GET /V4/Storage/HyperScale

```python
cv.raw.hyper_scale_storage.list_storage_hyper_scale()
```

**On the wire**

- `GET /V4/Storage/HyperScale` -> **200** (0.23 s)

  <details><summary>Answer</summary>

  ```json
  {
    "hyperScaleStorage": []
  }
  ```

  </details>

## `get_storage_hyper_scale` - GET /V4/Storage/HyperScale/{hyperScaleStorageId}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.hyper_scale_storage.get_storage_hyper_scale(...)
```

## `get_storage_hyper_scale_node`

GET /V4/Storage/HyperScale/{hyperScaleStorageId}/Node/{nodeId}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.hyper_scale_storage.get_storage_hyper_scale_node(...)
```
