# `cv.raw.oracle_db`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 16:43 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_client_instance_oracle_discover` - GET /client/{clientId}/instance/oracle/discover

> **SKIPPED** on this run: Commvault answered: 403

```python
cv.raw.oracle_db.get_client_instance_oracle_discover('2')
```

**On the wire**

- `GET /client/2/instance/oracle/discover` -> **403** (0.02 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

## `get_job_rman_logs` - GET /Job/{JobId}/RMANLogs

> **SKIPPED** on this run: Commvault answered: error 1: View RMAN logs operation failed.

```python
cv.raw.oracle_db.get_job_rman_logs('1')
```

**On the wire**

- `GET /Job/1/RMANLogs` -> **200** (0.12 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorString": "View RMAN logs operation failed.",
    "errorCode": 1,
    "hasMoreRestoredItemEntries": false
  }
  ```

  </details>

## `get_oracle_instance_backup_pieces` - GET /oracle/instance/{instanceId}/backupPieces

> **SKIPPED** on this run: Commvault answered: 500 - Exception caught when job info retrieval with error [Subquery returned more than 1 value. This is not permitted when the subquery follows =, !=, <, <= , >, >= or when the subquery is used as an expression.].

```python
cv.raw.oracle_db.get_oracle_instance_backup_pieces('1')
```

**On the wire**

- `GET /oracle/instance/1/backupPieces` -> **500** (0.08 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorMessage": "Exception caught when job info retrieval with error [Subquery returned more than 1 value. This is not permitted when the subquery follows =, !=, <, <= , >, >= or when the subquery is used as an expression.].",
    "errorCode": 0
  }
  ```

  </details>
