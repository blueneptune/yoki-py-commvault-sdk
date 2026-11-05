# `cv.raw.failover_groups`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:37 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_failover_groups_eligible_machines` - GET /V4/FailoverGroups/EligibleMachines

> **SKIPPED** on this run: Commvault answered: 400

```python
cv.raw.failover_groups.get_failover_groups_eligible_machines()
```

**On the wire**

- `GET /V4/FailoverGroups/EligibleMachines` -> **400** (0.06 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

## `list_failover_groups` - GET /V4/FailoverGroups

```python
cv.raw.failover_groups.list_failover_groups()
```

**On the wire**

- `GET /V4/FailoverGroups` -> **200** (0.09 s)

  <details><summary>Answer</summary>

  ```json
  {
    "failoverGroups": []
  }
  ```

  </details>

## `get_failover_group` - GET /V4/FailoverGroups/{failoverGroupId}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.failover_groups.get_failover_group(...)
```

## `get_failover_group_user-group-02_failover_machines`

GET /V4/FailoverGroups/{failoverGroupId}/TestFailoverMachines

> **SKIPPED** on this run: not swept: starts work or returns a file

```python
cv.raw.failover_groups.get_failover_group_user-group-02_failover_machines(...)
```

## `get_failover_group_virtual_machines`

GET /V4/FailoverGroup/{failoverGroupId}/VirtualMachines

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.failover_groups.get_failover_group_virtual_machines(...)
```
