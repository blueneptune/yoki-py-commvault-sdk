# `cv.raw.company`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:37 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `list_company` - GET /V4/company

```python
cv.raw.company.list_company()
```

**On the wire**

- `GET /V4/company` -> **200** (0.16 s)

  <details><summary>Answer</summary>

  ```json
  {
    "companies": [],
    "companyCount": 0
  }
  ```

  </details>

## `get_company` - GET /V4/company/{companyId}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.company.get_company(...)
```

## `get_company_associations` - GET /V4/Company/{companyId}/associations

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.company.get_company_associations(...)
```

## `get_company_laptop_admins` - GET /V4/Company/{companyId}/LaptopAdmins

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.company.get_company_laptop_admins(...)
```

## `get_company_servers` - GET /V4/Company/{companyId}/Servers

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.company.get_company_servers(...)
```
