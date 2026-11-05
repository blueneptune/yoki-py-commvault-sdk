# `cv.raw.epic_servers`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:50 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_epic_servers` - GET /V4/EpicServers

```python
cv.raw.epic_servers.get_epic_servers()
```

**On the wire**

- `GET /V4/EpicServers` -> **200** (0.55 s)

  <details><summary>Answer</summary>

  ```json
  {
    "fileServerCount": 0,
    "fileServers": []
  }
  ```

  </details>
