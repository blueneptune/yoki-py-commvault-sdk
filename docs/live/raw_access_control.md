# `cv.raw.access_control`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:37 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_access_control` - GET /V4/AccessControl

```python
cv.raw.access_control.get_access_control()
```

**On the wire**

- `GET /V4/AccessControl` -> **200** (0.29 s)

  <details><summary>Answer</summary>

  ```json
  {
    "ownerPermissions": [],
    "automaticLaptopOwnershipAssignment": {
      "assignLaptopOwnerAutomatically": true,
      "laptopOwnerOption": "ALL_LOGGED_IN_AD_USERS"
    }
  }
  ```

  </details>
