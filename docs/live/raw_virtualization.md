# `cv.raw.virtualization`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 16:43 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_client_vm_pseudo_client` - GET /Client/VMPseudoClient

```python
cv.raw.virtualization.get_client_vm_pseudo_client()
```

**On the wire**

- `GET /Client/VMPseudoClient` -> **200** (0.12 s)

  <details><summary>Answer</summary>

  ```json
  {}
  ```

  </details>

## `get_vm` - GET /VM

```python
cv.raw.virtualization.get_vm()
```

**On the wire**

- `GET /VM` -> **200** (0.08 s)

  <details><summary>Answer</summary>

  ```json
  {
    "totalRecords": 0,
    "pageNo": 0,
    "errorMessage": "",
    "errorCode": 0,
    "pageSize": 100
  }
  ```

  </details>

## `get_vm_browse` - GET /VMBrowse

> **SKIPPED** on this run: not swept: starts work or returns a file

```python
cv.raw.virtualization.get_vm_browse(...)
```

## `get_vs_aclientlist` - GET /VSAclientlist

```python
cv.raw.virtualization.get_vs_aclientlist()
```

**On the wire**

- `GET /VSAclientlist` -> **200** (0.08 s)

  <details><summary>Answer</summary>

  ```json
  {
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

## `list_vsa_vmgroups` - GET /v2/vsa/vmgroups

> **SKIPPED** on this run: Commvault answered: 400

```python
cv.raw.virtualization.list_vsa_vmgroups()
```

**On the wire**

- `GET /v2/vsa/vmgroups` -> **400** (0.06 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

## `get_client_credentials_verify` - GET /Client/{clientId}/credentials/verify

> **SKIPPED** on this run: Commvault answered: 400

```python
cv.raw.virtualization.get_client_credentials_verify('2')
```

**On the wire**

- `GET /Client/2/credentials/verify` -> **400** (0.06 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

## `get_vs_browse_inventory` - GET /VSBrowse/{vclientId}/INVENTORY

> **SKIPPED** on this run: not swept: starts work or returns a file

```python
cv.raw.virtualization.get_vs_browse_inventory(...)
```

## `get_vsa_hypervisor` - GET /v2/vsa/hypervisors/{clientId}

> **SKIPPED** on this run: Commvault answered: 403

```python
cv.raw.virtualization.get_vsa_hypervisor('2')
```

**On the wire**

- `GET /v2/vsa/hypervisors/2` -> **403** (0.02 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

## `get_vsa_hypervisor_refresh` - GET /v2/vsa/hypervisors/{clientId}/refresh

> **SKIPPED** on this run: not swept: starts work or returns a file

```python
cv.raw.virtualization.get_vsa_hypervisor_refresh(...)
```

## `get_vsa_vm_disks` - GET /v2/vsa/vm/{vmGuid}/disks

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.virtualization.get_vsa_vm_disks(...)
```

## `get_vsa_vm_jobs` - GET /v2/vsa/vm/{vmGuid}/Jobs

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.virtualization.get_vsa_vm_jobs(...)
```

## `get_vsa_vm_nics` - GET /v2/vsa/vm/{vmGuid}/nics

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.virtualization.get_vsa_vm_nics(...)
```

## `get_vsa_vmgroup` - GET /v2/vsa/vmgroups/{subclientId}

> **SKIPPED** on this run: Commvault answered: 403

```python
cv.raw.virtualization.get_vsa_vmgroup('44')
```

**On the wire**

- `GET /v2/vsa/vmgroups` -> **400** (0.06 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

- `GET /v2/vsa/vmgroups/44` -> **403** (0.02 s)

  <details><summary>Answer</summary>

  (no body)

  </details>
