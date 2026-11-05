# `cv.raw.global_exceptions`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 16:43 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_global_exceptions` - GET /V4/GlobalExceptions

```python
cv.raw.global_exceptions.get_global_exceptions()
```

**On the wire**

- `GET /V4/GlobalExceptions` -> **200** (0.22 s)

  <details><summary>Answer</summary>

  ```json
  {
    "useGlobalExceptionsOnAllSubclients": false
  }
  ```

  </details>
