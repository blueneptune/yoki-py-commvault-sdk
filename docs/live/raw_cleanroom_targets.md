# `cv.raw.cleanroom_targets`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:37 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_cleanroom_target` - GET /V4/Cleanroom/Target/{id}

> **SKIPPED** on this run: Commvault answered: 404 - Impossible de trouver la politique requise.

```python
cv.raw.cleanroom_targets.get_cleanroom_target('2')
```

**On the wire**

- `GET /V4/Cleanroom/Target/2` -> **404** (0.20 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorMessage": "Impossible de trouver la politique requise.",
    "errorCode": 100
  }
  ```

  </details>
