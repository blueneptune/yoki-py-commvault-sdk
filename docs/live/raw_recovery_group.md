# `cv.raw.recovery_group`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 16:43 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_license_usage` - GET /LicenseUsage

> **SKIPPED** on this run: Commvault answered: 400

```python
cv.raw.recovery_group.get_license_usage()
```

**On the wire**

- `GET /LicenseUsage` -> **400** (0.07 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

## `get_recovery_groups` - GET /RecoveryGroups

```python
cv.raw.recovery_group.get_recovery_groups()
```

**On the wire**

- `GET /RecoveryGroups` -> **200** (0.13 s)

  <details><summary>Answer</summary>

  ```json
  {
    "recoveryGroups": []
  }
  ```

  </details>

## `get_recovery_group` - GET /RecoveryGroup/{recoveryGroupId}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.recovery_group.get_recovery_group(...)
```

## `get_recovery_group_kpi` - GET /RecoveryGroup/{recoverygroupid}/KPI

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.recovery_group.get_recovery_group_kpi(...)
```

## `get_recovery_group_entity` - GET /RecoveryGroup/{recoveryGroupId}/Entity/{entityId}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.recovery_group.get_recovery_group_entity(...)
```
