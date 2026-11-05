# `cv.raw.snapshot`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:37 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_storage_array_snaps` - GET /V4/StorageArrays/{arrayId}/Snaps

```python
cv.raw.snapshot.get_storage_array_snaps('1')
```

**On the wire**

- `GET /V4/StorageArrays/1/Snaps` -> **200** (0.15 s)

  <details><summary>Answer</summary>

  ```json
  {
    "snaps": []
  }
  ```

  </details>

## `get_storage_arrays_job_snaps` - GET /V4/StorageArrays/Job/{jobId}/Snaps

```python
cv.raw.snapshot.get_storage_arrays_job_snaps('1498')
```

**On the wire**

- `GET /V4/StorageArrays/Job/1498/Snaps` -> **200** (0.16 s)

  <details><summary>Answer</summary>

  ```json
  {
    "snaps": []
  }
  ```

  </details>

## `get_snaps_snap_engine_plan_subclients`

GET /V4/Snaps/snapEngine/{snapEngineId}/Plan/{planId}/Subclients

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.snapshot.get_snaps_snap_engine_plan_subclients(...)
```
