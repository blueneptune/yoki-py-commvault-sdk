# `cv.raw.cloud_apps`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:50 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_client_proxy_cloud_apps` - GET /Client/proxy/CloudApps

```python
cv.raw.cloud_apps.get_client_proxy_cloud_apps()
```

**On the wire**

- `GET /Client/proxy/CloudApps` -> **200** (0.31 s)

  <details><summary>Answer</summary>

  ```json
  {
    "vendor": 0,
    "clients": [
      {
        "hostName": "commserve-02",
        "clientName": "commserve-02",
        "displayName": "commserve-02",
        "_type_": 3,
        "csGUID": "2DCFEA81-1B84-4E4D-ADB4-C317F96A112E",
        "clientId": 2
      }
    ]
  }
  ```

  </details>

## `get_crd_cloud_accounts` - GET /V4/CRD/CloudAccounts

> **SKIPPED** on this run: Commvault answered: error 1: Unsupported vendor

```python
cv.raw.cloud_apps.get_crd_cloud_accounts()
```

**On the wire**

- `GET /V4/CRD/CloudAccounts` -> **200** (0.10 s)

  <details><summary>Answer</summary>

  ```json
  {
    "cloudAccounts": [],
    "error": {
      "errorMessage": "Unsupported vendor",
      "errorCode": 1
    }
  }
  ```

  </details>
