# `cv.raw.commcell`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:50 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_comm_cell_password_encryption_config` - GET /CommCell/PasswordEncryptionConfig

```python
cv.raw.commcell.get_comm_cell_password_encryption_config()
```

**On the wire**

- `GET /CommCell/PasswordEncryptionConfig` -> **200** (0.10 s)

  <details><summary>Answer</summary>

  ```json
  {
    "keyProviderName": "Built-in"
  }
  ```

  </details>

## `get_commcell_package_downloader` - GET /V4/Commcell/PackageDownloader

> **SKIPPED** on this run: not swept: starts work or returns a file

```python
cv.raw.commcell.get_commcell_package_downloader(...)
```
