# `cv.raw.recovery_target`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:50 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_recovery_targets` - GET /V4/RecoveryTargets

```python
cv.raw.recovery_target.get_recovery_targets()
```

**On the wire**

- `GET /V4/RecoveryTargets` -> **200** (0.21 s)

  <details><summary>Answer</summary>

  ```json
  {
    "recoveryTargets": []
  }
  ```

  </details>

## `get_recovery_target` - GET /V4/RecoveryTarget/{recoveryTargetId}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.recovery_target.get_recovery_target(...)
```

## `get_recovery_target_virtual_machines` - GET /V4/RecoveryTarget/{targetId}/VirtualMachines

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.recovery_target.get_recovery_target_virtual_machines(...)
```
