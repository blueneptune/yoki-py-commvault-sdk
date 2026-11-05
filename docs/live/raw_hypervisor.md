# `cv.raw.hypervisor`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:50 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_cloud_oci_quick_create_link_iamcft` - GET /v4/Cloud/OCI/QuickCreateLink/IAMCFT

```python
cv.raw.hypervisor.get_cloud_oci_quick_create_link_iamcft()
```

**On the wire**

- `GET /v4/Cloud/OCI/QuickCreateLink/IAMCFT` -> **200** (0.10 s)

  <details><summary>Answer</summary>

  ```json
  {
    "quickLinkUrl": "https://cloud.oracle.com/resourcemanager/stacks/create?zipUrl=https://host-120/n/ider8mzpzsf1/b/CommvaultCloudTemplates/o/IAM.zip"
  }
  ```

  </details>

## `get_vs_pseudo_clients_for_permission` - GET /VSPseudoClientsForPermission

> **SKIPPED** on this run: Commvault answered: 400

```python
cv.raw.hypervisor.get_vs_pseudo_clients_for_permission()
```

**On the wire**

- `GET /VSPseudoClientsForPermission` -> **400** (0.07 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

## `list_hypervisor` - GET /V4/Hypervisor

```python
cv.raw.hypervisor.list_hypervisor()
```

**On the wire**

- `GET /V4/Hypervisor` -> **200** (0.15 s)

  <details><summary>Answer</summary>

  ```json
  {
    "HypervisorCount": 0,
    "Hypervisors": []
  }
  ```

  </details>

## `get_hypervisor` - GET /V4/Hypervisor/{hypervisorId}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.hypervisor.get_hypervisor(...)
```

## `get_hypervisor_filter` - GET /v4/hypervisor/{hypervisorId}/filter

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.hypervisor.get_hypervisor_filter(...)
```

## `get_vs_browse` - GET /VSBrowse/{hypervisorId}

> **SKIPPED** on this run: not swept: starts work or returns a file

```python
cv.raw.hypervisor.get_vs_browse(...)
```

## `get_vsa_tenant_client_list` - GET /VSATenantClientList/{instanceId}

```python
cv.raw.hypervisor.get_vsa_tenant_client_list('1')
```

**On the wire**

- `GET /VSATenantClientList/1` -> **200** (0.07 s)

  <details><summary>Answer</summary>

  ```json
  {
    "clients": []
  }
  ```

  </details>

## `get_hypervisor_browse` - GET /V4/Hypervisor/{hypervisorId}/{InventoryEntityName}/Browse

> **SKIPPED** on this run: not swept: starts work or returns a file

```python
cv.raw.hypervisor.get_hypervisor_browse(...)
```
