# `cv.raw.license`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:50 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_license` - GET /V4/License

```python
cv.raw.license.get_license()
```

**On the wire**

- `GET /V4/License` -> **200** (0.27 s)

  <details><summary>Answer</summary>

  ```json
  {
    "commCellId": -1,
    "commServeIPAddress": "192.0.2.15",
    "licenseIPAddress": "<masked>",
    "edition": "Commvault",
    "licenseMode": "<masked>",
    "serialNumber": "<masked>",
    "registrationCode": "3EA-536-FF31",
    "expiryDate": 1796431153
  }
  ```

  </details>

## `get_client_license` - GET /Client/{clientId}/License

```python
cv.raw.license.get_client_license('2')
```

**On the wire**

- `GET /Client/2/License` -> **200** (0.10 s)

  <details><summary>Answer</summary>

  ```json
  {
    "licensesInfo": "<masked>"
  }
  ```

  </details>
