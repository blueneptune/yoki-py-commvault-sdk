# `cv.raw.identity_servers`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:50 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_identity_servers` - GET /V4/IdentityServers

```python
cv.raw.identity_servers.get_identity_servers()
```

**On the wire**

- `GET /V4/IdentityServers` -> **200** (0.25 s)

  <details><summary>Answer</summary>

  ```json
  {
    "identityServers": []
  }
  ```

  </details>

## `get_ldap` - GET /V4/LDAP/{domainId}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.identity_servers.get_ldap(...)
```

## `get_open_id_connect` - GET /V4/OpenIdConnect/{name}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.identity_servers.get_open_id_connect(...)
```

## `get_saml` - GET /V4/SAML/{name}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.identity_servers.get_saml(...)
```

## `get_saml_metadata` - GET /V4/SAML/{name}/Metadata

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.identity_servers.get_saml_metadata(...)
```
