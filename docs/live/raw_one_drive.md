# `cv.raw.one_drive`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:50 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `list_office365_one_drive` - GET /V4/Office365/OneDrive

```python
cv.raw.one_drive.list_office365_one_drive()
```

**On the wire**

- `GET /V4/Office365/OneDrive` -> **200** (0.08 s)

  <details><summary>Answer</summary>

  ```json
  {
    "clients": []
  }
  ```

  </details>

## `list_office365_one_drive_content` - GET /V4/Office365/OneDrive/{appId}/Content

> **SKIPPED** on this run: not swept: starts work or returns a file

```python
cv.raw.one_drive.list_office365_one_drive_content(...)
```

## `list_office365_onedrive_users` - GET /V4/Office365/Onedrive/{appId}/Users

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.one_drive.list_office365_onedrive_users(...)
```
