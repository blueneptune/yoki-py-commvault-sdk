# `cv.raw.storage_arrays`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:50 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_snaps` - GET /Snaps

```python
cv.raw.storage_arrays.get_snaps()
```

**On the wire**

- `GET /Snaps` -> **200** (0.12 s)

  <details><summary>Answer</summary>

  ```json
  {}
  ```

  </details>

## `get_storage_array_sv_ms` - GET /V4/StorageArrays/{arrayId}/SVMs

> **SKIPPED** on this run: Commvault answered: 403

```python
cv.raw.storage_arrays.get_storage_array_sv_ms('1')
```

**On the wire**

- `GET /V4/StorageArrays/1/SVMs` -> **403** (0.01 s)

  <details><summary>Answer</summary>

  (no body)

  </details>
