# `cv.raw.cloud_configuration`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 16:43 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_cloud_cloud_config_client` - GET /v4/Cloud/CloudConfig/Client/{clientId}

> **SKIPPED** on this run: Commvault answered: 500 - Failed to get Cloud Config client details

```python
cv.raw.cloud_configuration.get_cloud_cloud_config_client('2')
```

**On the wire**

- `GET /v4/Cloud/CloudConfig/Client/2` -> **500** (0.09 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorMessage": "Failed to get Cloud Config client details",
    "errorCode": 500
  }
  ```

  </details>
