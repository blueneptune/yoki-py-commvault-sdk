# `cv.raw.audit_plan`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 16:43 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_audit_plan` - GET /V4/AuditPlan/{planId}

> **SKIPPED** on this run: Commvault answered: 400 - Plan not found

```python
cv.raw.audit_plan.get_audit_plan('1')
```

**On the wire**

- `GET /V4/AuditPlan/1` -> **400** (0.07 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorMessage": "Plan not found",
    "errorCode": 2
  }
  ```

  </details>
