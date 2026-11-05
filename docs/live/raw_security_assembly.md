# `cv.raw.security_assembly`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 16:43 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_security_assembly` - GET /Security/Assembly

```python
cv.raw.security_assembly.get_security_assembly()
```

**On the wire**

- `GET /Security/Assembly` -> **200** (0.11 s)

  <details><summary>Answer</summary>

  ```json
  {}
  ```

  </details>

## `get_security_assembly_eligible_resources` - GET /Security/Assembly/EligibleResources

> **SKIPPED** on this run: Commvault answered: 500 - Failed to fetch assembly eligible resources. Invalid assemblyId parameter

```python
cv.raw.security_assembly.get_security_assembly_eligible_resources()
```

**On the wire**

- `GET /Security/Assembly/EligibleResources` -> **500** (0.07 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorMessage": "Failed to fetch assembly eligible resources. Invalid assemblyId parameter",
    "errorCode": 1
  }
  ```

  </details>
