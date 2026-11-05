# `cv.raw.domain`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 16:43 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_identity_servers` - GET /IdentityServers

```python
cv.raw.domain.get_identity_servers()
```

**On the wire**

- `GET /IdentityServers` -> **200** (0.16 s)

  <details><summary>Answer</summary>

  ```json
  {}
  ```

  </details>

## `get_third_party_app` - GET /ThirdParty/App

```python
cv.raw.domain.get_third_party_app()
```

**On the wire**

- `GET /ThirdParty/App` -> **200** (0.10 s)

  <details><summary>Answer</summary>

  ```json
  {
    "error": {
      "errorString": "",
      "errorCode": 0
    }
  }
  ```

  </details>

## `list_comm_cell_domain_controller` - GET /CommCell/DomainController

```python
cv.raw.domain.list_comm_cell_domain_controller()
```

**On the wire**

- `GET /CommCell/DomainController` -> **200** (0.08 s)

  <details><summary>Answer</summary>

  ```json
  {}
  ```

  </details>
