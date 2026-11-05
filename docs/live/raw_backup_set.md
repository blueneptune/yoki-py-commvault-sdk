# `cv.raw.backup_set`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:37 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `list_backupset` - GET /Backupset

> **SKIPPED** on this run: Commvault answered: 400

```python
cv.raw.backup_set.list_backupset()
```

**On the wire**

- `GET /Backupset` -> **400** (0.07 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

## `get_backupset_by_name`

GET /Backupset/byName(clientName='{ClientName}',appName='{AppName}',backupsetName='{BackupsetName}')

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.backup_set.get_backupset_by_name(...)
```
