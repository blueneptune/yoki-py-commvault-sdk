# `cv.raw.recovery_point_stores`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 16:43 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_recovery_point_stores` - GET /V4/RecoveryPointStores

```python
cv.raw.recovery_point_stores.get_recovery_point_stores()
```

**On the wire**

- `GET /V4/RecoveryPointStores` -> **200** (0.17 s)

  <details><summary>Answer</summary>

  ```json
  {
    "stores": []
  }
  ```

  </details>

## `get_recovery_point_store` - GET /V4/RecoveryPointStore/{rpsId}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.recovery_point_stores.get_recovery_point_store(...)
```
