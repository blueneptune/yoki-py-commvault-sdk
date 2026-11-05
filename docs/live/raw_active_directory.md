# `cv.raw.active_directory`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:37 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_active_directory_apps` - GET /V4/ActiveDirectory/Apps

```python
cv.raw.active_directory.get_active_directory_apps()
```

**On the wire**

- `GET /V4/ActiveDirectory/Apps` -> **200** (0.10 s)

  <details><summary>Answer</summary>

  ```json
  {
    "totalADClients": 0
  }
  ```

  </details>

## `list_active_directory_azure_ad` - GET /v4/ActiveDirectory/AzureAD

> **SKIPPED** on this run: Commvault answered: 403

```python
cv.raw.active_directory.list_active_directory_azure_ad()
```

**On the wire**

- `GET /v4/ActiveDirectory/AzureAD` -> **403** (0.01 s)

  <details><summary>Answer</summary>

  (no body)

  </details>
