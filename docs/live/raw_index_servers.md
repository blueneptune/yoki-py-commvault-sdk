# `cv.raw.index_servers`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 16:43 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_index_servers` - GET /V4/IndexServers

```python
cv.raw.index_servers.get_index_servers()
```

**On the wire**

- `GET /V4/IndexServers` -> **200** (0.19 s)

  <details><summary>Answer</summary>

  ```json
  {
    "indexServers": [
      {
        "id": 3,
        "name": "host-01",
        "displayName": "host-01",
        "OS": "Windows",
        "cloudId": 1,
        "createdTime": 1791234811,
        "nodes": [
          {
            "name": "commserve-02",
            "id": 2
          }
        ]
      }
    ]
  }
  ```

  </details>
