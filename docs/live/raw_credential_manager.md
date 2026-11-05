# `cv.raw.credential_manager`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:50 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `list_credential` - GET /V4/Credential

```python
cv.raw.credential_manager.list_credential()
```

**On the wire**

- `GET /V4/Credential` -> **200** (0.24 s)

  <details><summary>Answer</summary>

  ```json
  {
    "credentialManager": "<masked>"
  }
  ```

  </details>

## `list_v6_credential` - GET /V6/Credential

```python
cv.raw.credential_manager.list_v6_credential()
```

**On the wire**

- `GET /V6/Credential` -> **200** (0.17 s)

  <details><summary>Answer</summary>

  ```json
  {
    "credentialManager": "<masked>"
  }
  ```

  </details>

## `get_credential_v4` - GET /V4/Credential/{credentialName}

```python
cv.raw.credential_manager.get_credential_v4('5')
```

**On the wire**

- `GET /V4/Credential/5` -> **200** (0.26 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorMessage": "",
    "errorCode": 0
  }
  ```

  </details>

## `get_credential_v5` - GET /V5/Credential/{credentialId}

```python
cv.raw.credential_manager.get_credential_v5('6')
```

**On the wire**

- `GET /V5/Credential/6` -> **200** (0.29 s)

  <details><summary>Answer</summary>

  ```json
  {
    "id": 6,
    "name": "gmail",
    "keyExpiryInterval": 90,
    "lastModifiedTime": "1792247882",
    "accountType": "WINDOWSACCOUNT",
    "userAccount": "user-05",
    "email": "user-05",
    "description": "",
    "security": {
      "owner": {},
      "associations": []
    }
  }
  ```

  </details>

## `get_v6_credential` - GET /V6/Credential/{credentialId}

```python
cv.raw.credential_manager.get_v6_credential('5')
```

**On the wire**

- `GET /V6/Credential/5` -> **200** (0.22 s)

  <details><summary>Answer</summary>

  ```json
  {
    "id": 5,
    "accountType": "WINDOWSACCOUNT",
    "userAccount": "sa",
    "name": "blt-lab-sql-sa",
    "description": "blt lab: sa on the lab SQL Server container"
  }
  ```

  </details>
