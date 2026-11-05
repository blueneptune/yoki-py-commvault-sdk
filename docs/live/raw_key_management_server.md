# `cv.raw.key_management_server`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 16:43 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `list_key_management_servers` - GET /V4/KeyManagementServers

```python
cv.raw.key_management_server.list_key_management_servers()
```

**On the wire**

- `GET /V4/KeyManagementServers` -> **200** (0.17 s)

  <details><summary>Answer</summary>

  ```json
  {
    "KeyManagementServers": [
      {
        "id": 1,
        "name": "Built-in",
        "type": "COMMVAULT"
      }
    ]
  }
  ```

  </details>
