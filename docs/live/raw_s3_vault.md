# `cv.raw.s3_vault`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:37 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_cvs3_endpoint_state` - GET /V4/CVS3Endpoint/{ClientID}/state

```python
cv.raw.s3_vault.get_cvs3_endpoint_state('2')
```

**On the wire**

- `GET /V4/CVS3Endpoint/2/state` -> **200** (1.55 s)

  <details><summary>Answer</summary>

  ```json
  {
    "clientProperties": [
      {
        "clientProps": {
          "cvs3EndpointProp": {
            "offlineSince": 0,
            "s3Ports": "",
            "enabled": false
          }
        }
      }
    ]
  }
  ```

  </details>

## `get_cvs3_store` - GET /V4/CVS3Store/{storeId}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.s3_vault.get_cvs3_store(...)
```
