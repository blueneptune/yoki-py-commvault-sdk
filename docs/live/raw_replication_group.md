# `cv.raw.replication_group`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:37 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `list_replication_group` - GET /V4/ReplicationGroup

```python
cv.raw.replication_group.list_replication_group()
```

**On the wire**

- `GET /V4/ReplicationGroup` -> **200** (0.26 s)

  <details><summary>Answer</summary>

  ```json
  {
    "replicationGroups": []
  }
  ```

  </details>

## `get_replication_group` - GET /V4/ReplicationGroup/{replicationGroupId}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.replication_group.get_replication_group(...)
```

## `get_replication_group_virtual_machines`

GET /V4/ReplicationGroup/{replicationGroupTaskId}/VirtualMachines

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.replication_group.get_replication_group_virtual_machines(...)
```

## `get_replication_group_replication_task_mapping`

GET /V4/ReplicationGroup/{groupId}/ReplicationTask/{taskId}/Mapping

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.replication_group.get_replication_group_replication_task_mapping(...)
```
