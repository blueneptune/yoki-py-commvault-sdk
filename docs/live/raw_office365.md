# `cv.raw.office365`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:50 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_office365_plans` - GET /V4/Office365/Plans

```python
cv.raw.office365.get_office365_plans()
```

**On the wire**

- `GET /V4/Office365/Plans` -> **200** (0.10 s)

  <details><summary>Answer</summary>

  ```json
  {
    "totalO365Plans": 0
  }
  ```

  </details>

## `list_office365` - GET /V4/Office365

```python
cv.raw.office365.list_office365()
```

**On the wire**

- `GET /V4/Office365` -> **200** (0.09 s)

  <details><summary>Answer</summary>

  ```json
  {
    "clients": []
  }
  ```

  </details>

## `get_office365_azure_app` - GET /V4/Office365/{appId}/AzureApp

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.office365.get_office365_azure_app(...)
```

## `get_office365_subclient_object_guid`

GET /Office365/Subclient/{subclientId}/ObjectGUID/{objectGUID}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.office365.get_office365_subclient_object_guid(...)
```
