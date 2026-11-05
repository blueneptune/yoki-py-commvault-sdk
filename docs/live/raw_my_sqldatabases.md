# `cv.raw.my_sqldatabases`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:37 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_client_instance_mysql_discover` - GET /Client/{clientId}/instance/mysql/discover

> **SKIPPED** on this run: Commvault answered: error 1: Discover Operation failed. Please check if services are running on the client.

```python
cv.raw.my_sqldatabases.get_client_instance_mysql_discover('2')
```

**On the wire**

- `GET /Client/2/instance/mysql/discover` -> **200** (0.11 s)

  <details><summary>Answer</summary>

  ```json
  {
    "error": {
      "errorString": "Discover Operation failed. Please check if services are running on the client.",
      "errorCode": 1
    }
  }
  ```

  </details>
