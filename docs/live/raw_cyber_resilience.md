# `cv.raw.cyber_resilience`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:37 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_cyber_resilience_credentials` - GET /V4/CyberResilience/Credentials

```python
cv.raw.cyber_resilience.get_cyber_resilience_credentials()
```

**On the wire**

- `GET /V4/CyberResilience/Credentials` -> **200** (0.14 s)

  <details><summary>Answer</summary>

  ```json
  {
    "credentials": []
  }
  ```

  </details>

## `get_cyber_resilience_credentials_sync_status`

GET /V4/CyberResilience/Credentials/Sync/Status

> **SKIPPED** on this run: not swept: starts work or returns a file

```python
cv.raw.cyber_resilience.get_cyber_resilience_credentials_sync_status(...)
```
