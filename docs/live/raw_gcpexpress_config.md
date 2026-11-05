# `cv.raw.gcpexpress_config`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 16:43 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_cloud_gcp_express_config_oauth_sign_in_details`

GET /v4/Cloud/GCP/ExpressConfig/OauthSignInDetails

> **SKIPPED** on this run: Commvault answered: 403

```python
cv.raw.gcpexpress_config.get_cloud_gcp_express_config_oauth_sign_in_details()
```

**On the wire**

- `GET /v4/Cloud/GCP/ExpressConfig/OauthSignInDetails` -> **403** (0.02 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

## `get_cloud_gcp_express_config_projects` - GET /v4/Cloud/GCP/ExpressConfig/Projects

> **SKIPPED** on this run: Commvault answered: 400 - Invalid credential id. Bad Request

```python
cv.raw.gcpexpress_config.get_cloud_gcp_express_config_projects()
```

**On the wire**

- `GET /v4/Cloud/GCP/ExpressConfig/Projects` -> **400** (0.07 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorMessage": "Invalid credential id. Bad Request",
    "errorCode": 1
  }
  ```

  </details>
