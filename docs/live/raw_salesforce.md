# `cv.raw.salesforce`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:37 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `list_cr_reportsplusengine_datasets_4e639029_2764_4fb4_b7e3_0fc636cdd025_data`

GET /cr/reportsplusengine/datasets/4e639029-2764-4fb4-b7e3-0fc636cdd025/data

> **SKIPPED** on this run: Commvault answered: 500 - failed to retrieve Salesforce connection information from datasource [commserve-02]

```python
cv.raw.salesforce.list_cr_reportsplusengine_datasets_4e639029_2764_4fb4_b7e3_0fc636cdd025_data()
```

**On the wire**

- `GET /cr/reportsplusengine/datasets/4e639029-2764-4fb4-b7e3-0fc636cdd025/data` -> **500** (0.07 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorCode": 1,
    "errorMessage": "failed to retrieve Salesforce connection information from datasource [commserve-02]"
  }
  ```

  </details>

## `list_salesforce_organization` - GET /Salesforce/Organization

```python
cv.raw.salesforce.list_salesforce_organization()
```

**On the wire**

- `GET /Salesforce/Organization` -> **200** (0.10 s)

  <details><summary>Answer</summary>

  ```json
  {
    "filterQueryCount": 0,
    "account": []
  }
  ```

  </details>

## `get_masking_policy` - GET /MaskingPolicy/{InstanceId}

```python
cv.raw.salesforce.get_masking_policy('1')
```

**On the wire**

- `GET /MaskingPolicy/1` -> **200** (0.10 s)

  <details><summary>Answer</summary>

  ```json
  {
    "response": {
      "errorMessage": "",
      "errorCode": 0
    }
  }
  ```

  </details>

## `get_salesforce_gdpr_requests` - GET /Salesforce/{ClientId}/GDPR/Requests

```python
cv.raw.salesforce.get_salesforce_gdpr_requests('2')
```

**On the wire**

- `GET /Salesforce/2/GDPR/Requests` -> **200** (0.08 s)

  <details><summary>Answer</summary>

  ```json
  {}
  ```

  </details>

## `get_salesforce_organization` - GET /Salesforce/Organization/{ClientId}

> **SKIPPED** on this run: Commvault answered: 500

```python
cv.raw.salesforce.get_salesforce_organization('2')
```

**On the wire**

- `GET /Salesforce/Organization/2` -> **500** (0.09 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

## `get_salesforce_organization_user_permissions_refresh`

GET /Salesforce/Organization/{ClientId}/User/Permissions/Refresh

> **SKIPPED** on this run: not swept: starts work or returns a file

```python
cv.raw.salesforce.get_salesforce_organization_user_permissions_refresh(...)
```

## `list_salesforce_sandbox_seeding_templates`

GET /Salesforce/{ClientId}/Sandbox/Seeding/Templates

> **SKIPPED** on this run: Commvault answered: 500

```python
cv.raw.salesforce.list_salesforce_sandbox_seeding_templates('2')
```

**On the wire**

- `GET /Salesforce/2/Sandbox/Seeding/Templates` -> **500** (0.08 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

## `get_salesforce_archiving_archive_preview_objects`

GET /Salesforce/Archiving/{clientId}/Archive/preview/{jobId}/objects

> **SKIPPED** on this run: not swept: starts work or returns a file

```python
cv.raw.salesforce.get_salesforce_archiving_archive_preview_objects(...)
```

## `get_salesforce_restore_preview_objects`

GET /Salesforce/{clientId}/Restore/preview/{jobId}/objects

> **SKIPPED** on this run: not swept: starts work or returns a file

```python
cv.raw.salesforce.get_salesforce_restore_preview_objects(...)
```

## `get_salesforce_sandbox_seeding_template`

GET /Salesforce/{ClientId}/Sandbox/Seeding/Templates/{TemplateId}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.salesforce.get_salesforce_sandbox_seeding_template(...)
```

**On the wire**

- `GET /Salesforce/2/Sandbox/Seeding/Templates` -> **500** (0.07 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

## `get_salesforce_archiving_archive_preview_children`

GET /Salesforce/Archiving/{clientId}/Archive/preview/{jobId}/children/{parentEdgeId}

> **SKIPPED** on this run: not swept: starts work or returns a file

```python
cv.raw.salesforce.get_salesforce_archiving_archive_preview_children(...)
```

## `get_salesforce_restore_preview_children`

GET /Salesforce/{clientId}/Restore/preview/{jobId}/children/{parentEdgeId}

> **SKIPPED** on this run: not swept: starts work or returns a file

```python
cv.raw.salesforce.get_salesforce_restore_preview_children(...)
```
