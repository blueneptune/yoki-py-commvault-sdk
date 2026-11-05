# `cv.raw.failover_group`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 16:43 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_dr_job_stats` - GET /DR/JobStats

```python
cv.raw.failover_group.get_dr_job_stats()
```

**On the wire**

- `GET /DR/JobStats` -> **200** (0.08 s)

  <details><summary>Answer</summary>

  ```json
  {}
  ```

  </details>

## `get_failover_groups_client_list` - GET /FailoverGroups/ClientList

> **SKIPPED** on this run: Commvault answered: 400

```python
cv.raw.failover_group.get_failover_groups_client_list()
```

**On the wire**

- `GET /FailoverGroups/ClientList` -> **400** (0.07 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

## `list_failover_groups` - GET /FailoverGroups

```python
cv.raw.failover_group.list_failover_groups()
```

**On the wire**

- `GET /FailoverGroups` -> **200** (0.09 s)

  <details><summary>Answer</summary>

  ```json
  {}
  ```

  </details>

## `get_failover_group` - GET /FailoverGroups/{FailoverGroupId}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.failover_group.get_failover_group(...)
```

## `get_failover_group_schedules` - GET /FailoverGroups/{failoverGroupId}/Schedules

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.failover_group.get_failover_group_schedules(...)
```
