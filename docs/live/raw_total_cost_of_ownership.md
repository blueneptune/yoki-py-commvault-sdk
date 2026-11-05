# `cv.raw.total_cost_of_ownership`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:50 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_tco_assessment_details` - GET /V4/TCO/AssessmentDetails

```python
cv.raw.total_cost_of_ownership.get_tco_assessment_details()
```

**On the wire**

- `GET /V4/TCO/AssessmentDetails` -> **200** (0.07 s)

  <details><summary>Answer</summary>

  ```json
  {
    "Assessments": []
  }
  ```

  </details>

## `get_tco_assessment_discovery_criteria` - GET /V4/TCO/AssessmentDiscoveryCriteria

> **SKIPPED** on this run: Commvault answered: error CREDENTIAL_INVALID: Invalid credential. No details found

```python
cv.raw.total_cost_of_ownership.get_tco_assessment_discovery_criteria()
```

**On the wire**

- `GET /V4/TCO/AssessmentDiscoveryCriteria` -> **200** (0.07 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorMessage": "Invalid credential. No details found",
    "errorCode": "CREDENTIAL_INVALID"
  }
  ```

  </details>

## `get_tco_authenticated_users` - GET /V4/TCO/AuthenticatedUsers

```python
cv.raw.total_cost_of_ownership.get_tco_authenticated_users()
```

**On the wire**

- `GET /V4/TCO/AuthenticatedUsers` -> **200** (0.07 s)

  <details><summary>Answer</summary>

  ```json
  {}
  ```

  </details>
