# `cv.raw.replication_monitor`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:50 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_array_replication_monitor` - GET /V4/ArrayReplicationMonitor

```python
cv.raw.replication_monitor.get_array_replication_monitor()
```

**On the wire**

- `GET /V4/ArrayReplicationMonitor` -> **200** (0.11 s)

  <details><summary>Answer</summary>

  ```json
  {
    "arrayReplicationMonitorInfo": []
  }
  ```

  </details>

## `get_replication_monitor` - GET /V4/ReplicationMonitor/{pairId}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.replication_monitor.get_replication_monitor(...)
```

## `get_replication_monitor_user-group-01_failover_machines`

GET /V4/ReplicationMonitor/{replicationPairId}/testFailoverMachines

> **SKIPPED** on this run: not swept: starts work or returns a file

```python
cv.raw.replication_monitor.get_replication_monitor_user-group-01_failover_machines(...)
```

## `get_replication_monitor_virtual_machines`

GET /V4/ReplicationMonitor/{pairId}/VirtualMachines

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.replication_monitor.get_replication_monitor_virtual_machines(...)
```

## `get_vm_provisioning_virtual_machine_active_mounts`

GET /V4/VMProvisioning/VirtualMachine/{vmGUID}/ActiveMounts

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.replication_monitor.get_vm_provisioning_virtual_machine_active_mounts(...)
```
