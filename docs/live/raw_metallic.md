# `cv.raw.metallic`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 16:43 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_azuredb_backupgateway` - GET /V4/azuredb/backupgateway

```python
cv.raw.metallic.get_azuredb_backupgateway()
```

**On the wire**

- `GET /V4/azuredb/backupgateway` -> **200** (0.15 s)

  <details><summary>Answer</summary>

  ```json
  {
    "backupGateways": []
  }
  ```

  </details>

## `get_azuredb_cloudaccount` - GET /V4/azuredb/cloudaccount

```python
cv.raw.metallic.get_azuredb_cloudaccount()
```

**On the wire**

- `GET /V4/azuredb/cloudaccount` -> **200** (0.13 s)

  <details><summary>Answer</summary>

  ```json
  {
    "cloudAccounts": []
  }
  ```

  </details>

## `get_azuredb_maria_instance` - GET /V4/azuredb/maria/instance

> **SKIPPED** on this run: Commvault answered: 500 - Failed to browse RDS inventory

```python
cv.raw.metallic.get_azuredb_maria_instance()
```

**On the wire**

- `GET /V4/azuredb/maria/instance` -> **500** (0.18 s)

  <details><summary>Answer</summary>

  ```json
  {
    "failedStage": "GetDiscoveredInstances",
    "errorCode": -1,
    "errorMessage": {
      "type": "https://host-119/html/rfc9110#section-15.6.1",
      "title": "An error occurred while processing your request.",
      "status": "500",
      "detail": "Failed to browse RDS inventory",
      "traceId": "00-41eb41e023156532bd96819c0d06a9cb-083cd52b8c9c0573-01"
    }
  }
  ```

  </details>

## `get_azuredb_mssql_credentials` - GET /V4/azuredb/mssql/credentials

```python
cv.raw.metallic.get_azuredb_mssql_credentials()
```

**On the wire**

- `GET /V4/azuredb/mssql/credentials` -> **200** (0.23 s)

  <details><summary>Answer</summary>

  ```json
  {
    "credentialManager": []
  }
  ```

  </details>

## `get_azuredb_mssql_instance` - GET /V4/azuredb/mssql/instance

> **SKIPPED** on this run: Commvault answered: 404

```python
cv.raw.metallic.get_azuredb_mssql_instance()
```

**On the wire**

- `GET /V4/azuredb/mssql/instance` -> **404** (0.12 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

## `get_azuredb_mysql_instance` - GET /V4/azuredb/mysql/instance

> **SKIPPED** on this run: Commvault answered: 500 - Failed to browse RDS inventory

```python
cv.raw.metallic.get_azuredb_mysql_instance()
```

**On the wire**

- `GET /V4/azuredb/mysql/instance` -> **500** (0.13 s)

  <details><summary>Answer</summary>

  ```json
  {
    "type": "https://host-119/html/rfc9110#section-15.6.1",
    "title": "An error occurred while processing your request.",
    "status": 500,
    "detail": "Failed to browse RDS inventory",
    "traceId": "00-560653fa5c893b13fc85633eb9ce070e-45069efa5b77fdc1-01"
  }
  ```

  </details>

## `get_azuredb_postgresql_instance` - GET /V4/azuredb/postgresql/instance

> **SKIPPED** on this run: Commvault answered: 500 - Failed to browse RDS inventory

```python
cv.raw.metallic.get_azuredb_postgresql_instance()
```

**On the wire**

- `GET /V4/azuredb/postgresql/instance` -> **500** (0.14 s)

  <details><summary>Answer</summary>

  ```json
  {
    "type": "https://host-119/html/rfc9110#section-15.6.1",
    "title": "An error occurred while processing your request.",
    "status": 500,
    "detail": "Failed to browse RDS inventory",
    "traceId": "00-34cc69d5d6b6d93e2939373b582fdcd2-88a78b364dc57555-01"
  }
  ```

  </details>

## `get_credentials_azure_cloud_account` - GET /V4/credentials/azure/cloudAccount

```python
cv.raw.metallic.get_credentials_azure_cloud_account()
```

**On the wire**

- `GET /V4/credentials/azure/cloudAccount` -> **200** (0.52 s)

  <details><summary>Answer</summary>

  ```json
  {
    "credentialManager": []
  }
  ```

  </details>

## `get_credentials_azure_storage` - GET /V4/credentials/azure/storage

```python
cv.raw.metallic.get_credentials_azure_storage()
```

**On the wire**

- `GET /V4/credentials/azure/storage` -> **200** (0.22 s)

  <details><summary>Answer</summary>

  ```json
  {
    "credentialManager": []
  }
  ```

  </details>

## `get_hypervisors_azure` - GET /V4/Hypervisors/azure

```python
cv.raw.metallic.get_hypervisors_azure()
```

**On the wire**

- `GET /V4/Hypervisors/azure` -> **200** (0.16 s)

  <details><summary>Answer</summary>

  ```json
  {
    "Hypervisors": []
  }
  ```

  </details>

## `get_metallic_supported_regions` - GET /V4/Metallic/supported-regions

> **SKIPPED** on this run: Commvault answered: 404

```python
cv.raw.metallic.get_metallic_supported_regions()
```

**On the wire**

- `GET /V4/Metallic/supported-regions` -> **404** (0.14 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

## `get_objectstorage_instance` - GET /V4/objectstorage/instance

```python
cv.raw.metallic.get_objectstorage_instance()
```

**On the wire**

- `GET /V4/objectstorage/instance` -> **200** (0.64 s)

  <details><summary>Answer</summary>

  ```json
  {
    "instances": []
  }
  ```

  </details>

## `get_office365_serverplan` - GET /V4/office365/serverplan

> **SKIPPED** on this run: Commvault answered: 404

```python
cv.raw.metallic.get_office365_serverplan()
```

**On the wire**

- `GET /V4/office365/serverplan` -> **404** (0.07 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

## `get_office365plan` - GET /V4/office365plan

> **SKIPPED** on this run: Commvault answered: 404

```python
cv.raw.metallic.get_office365plan()
```

**On the wire**

- `GET /V4/office365plan` -> **404** (0.07 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

## `get_storage_cloud_azure` - GET /V4/storage/cloud/azure

```python
cv.raw.metallic.get_storage_cloud_azure()
```

**On the wire**

- `GET /V4/storage/cloud/azure` -> **200** (0.23 s)

  <details><summary>Answer</summary>

  ```json
  {
    "cloudStorage": []
  }
  ```

  </details>

## `get_tenant_usage_details` - GET /api/v1/tenant/usage/details

> **SKIPPED** on this run: Commvault answered: 403

```python
cv.raw.metallic.get_tenant_usage_details()
```

**On the wire**

- `GET /api/v1/tenant/usage/details` -> **403** (0.02 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

## `get_tenant_usage_summary` - GET /api/v1/tenant/usage/summary

> **SKIPPED** on this run: Commvault answered: 403

```python
cv.raw.metallic.get_tenant_usage_summary()
```

**On the wire**

- `GET /api/v1/tenant/usage/summary` -> **403** (0.02 s)

  <details><summary>Answer</summary>

  (no body)

  </details>
