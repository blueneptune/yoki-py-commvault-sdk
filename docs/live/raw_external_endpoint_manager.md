# `cv.raw.external_endpoint_manager`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:50 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `list_externalendpoint` - GET /v4/externalendpoint

> **SKIPPED** on this run: Commvault answered: 500 - No external endpoints are configured. Please add a new endpoint to proceed.

```python
cv.raw.external_endpoint_manager.list_externalendpoint()
```

**On the wire**

- `GET /v4/externalendpoint` -> **500** (0.10 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorMessage": "No external endpoints are configured. Please add a new endpoint to proceed.",
    "errorCode": 50000
  }
  ```

  </details>

## `get_externalendpoint` - GET /v4/externalendpoint/{externalEndpointId}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.external_endpoint_manager.get_externalendpoint(...)
```

**On the wire**

- `GET /v4/externalendpoint` -> **500** (0.09 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorMessage": "No external endpoints are configured. Please add a new endpoint to proceed.",
    "errorCode": 50000
  }
  ```

  </details>
