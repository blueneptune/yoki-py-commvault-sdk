# `cv.raw.archive_file_servers`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:50 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_archive_file_servers` - GET /V4/ArchiveFileServers

```python
cv.raw.archive_file_servers.get_archive_file_servers()
```

**On the wire**

- `GET /V4/ArchiveFileServers` -> **200** (0.34 s)

  <details><summary>Answer</summary>

  ```json
  {
    "fileServerCount": 0,
    "fileServers": []
  }
  ```

  </details>
