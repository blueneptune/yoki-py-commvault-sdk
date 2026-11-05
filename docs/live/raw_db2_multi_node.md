# `cv.raw.db2_multi_node`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 16:43 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_instance_db2_partitions` - GET /Instance/DB2Partitions

> **SKIPPED** on this run: Commvault answered: error 1: Failed to connect to remote client

```python
cv.raw.db2_multi_node.get_instance_db2_partitions()
```

**On the wire**

- `GET /Instance/DB2Partitions` -> **200** (0.11 s)

  <details><summary>Answer</summary>

  ```json
  {
    "error": {
      "errorMessage": "Failed to connect to remote client",
      "errorCode": 1
    }
  }
  ```

  </details>
