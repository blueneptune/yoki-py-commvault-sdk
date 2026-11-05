# `cv.raw.hidden`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:37 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_client_retire_information` - GET /V4/Client/{clientId}/RetireInformation

> **SKIPPED** on this run: not swept: starts work or returns a file

```python
cv.raw.hidden.get_client_retire_information(...)
```

## `get_company_local_authentication` - GET /V4/Company/{companyId}/LocalAuthentication

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.hidden.get_company_local_authentication(...)
```

## `get_user_authentication_methods` - GET /V4/user/{userId}/authenticationMethods

```python
cv.raw.hidden.get_user_authentication_methods('2')
```

**On the wire**

- `GET /V4/user/2/authenticationMethods` -> **200** (0.09 s)

  <details><summary>Answer</summary>

  ```json
  {
    "authenticationMethod": "LOCAL",
    "authenticators": [
      {
        "authenticationMethod": "LOCAL",
        "name": "Local",
        "id": 0,
        "type": "LOCAL",
        "company": {
          "name": "Commcell",
          "id": 0
        }
      }
    ]
  }
  ```

  </details>
