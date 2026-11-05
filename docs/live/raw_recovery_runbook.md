# `cv.raw.recovery_runbook`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:37 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_recovery_runbook_eligible_resources` - GET /V4/RecoveryRunbook/EligibleResources

> **SKIPPED** on this run: Commvault answered: 403

```python
cv.raw.recovery_runbook.get_recovery_runbook_eligible_resources()
```

**On the wire**

- `GET /V4/RecoveryRunbook/EligibleResources` -> **403** (0.01 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

## `list_recovery_runbook` - GET /V4/RecoveryRunbook

```python
cv.raw.recovery_runbook.list_recovery_runbook()
```

**On the wire**

- `GET /V4/RecoveryRunbook` -> **200** (0.09 s)

  <details><summary>Answer</summary>

  ```json
  {
    "runbooks": []
  }
  ```

  </details>

## `get_recovery_runbook_kpi` - GET /V4/RecoveryRunbook/{runbookId}/KPI

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.recovery_runbook.get_recovery_runbook_kpi(...)
```

## `get_recovery_runbook_site_validation`

GET /V4/RecoveryRunbook/{runbookId}/Site/Validation

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.recovery_runbook.get_recovery_runbook_site_validation(...)
```

## `list_recovery_runbook_resources` - GET /V4/RecoveryRunbook/{runbookId}/Resources

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.recovery_runbook.list_recovery_runbook_resources(...)
```

## `get_recovery_runbook_resource`

GET /V4/RecoveryRunbook/{runbookId}/Resources/{resourceId}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.recovery_runbook.get_recovery_runbook_resource(...)
```
