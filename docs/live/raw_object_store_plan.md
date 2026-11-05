# `cv.raw.object_store_plan`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 16:43 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_object_store_plan` - GET /V4/ObjectStorePlan/{planId}

> **SKIPPED** on this run: Commvault answered: 400 - ObjectStore Plan not found

```python
cv.raw.object_store_plan.get_object_store_plan('1')
```

**On the wire**

- `GET /V4/ObjectStorePlan/1` -> **400** (0.07 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorMessage": "ObjectStore Plan not found",
    "errorCode": 2
  }
  ```

  </details>
