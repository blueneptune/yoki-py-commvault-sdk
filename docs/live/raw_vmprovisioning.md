# `cv.raw.vmprovisioning`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:50 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_virtual_lab_virtual_machines` - GET /V4/VirtualLab/VirtualMachines

> **SKIPPED** on this run: Commvault answered: 400 - Virtual lab id or name is required.

```python
cv.raw.vmprovisioning.get_virtual_lab_virtual_machines()
```

**On the wire**

- `GET /V4/VirtualLab/VirtualMachines` -> **400** (0.07 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorMessage": "Virtual lab id or name is required.",
    "errorCode": 1
  }
  ```

  </details>

## `get_virtual_labs` - GET /V4/VirtualLabs

```python
cv.raw.vmprovisioning.get_virtual_labs()
```

**On the wire**

- `GET /V4/VirtualLabs` -> **200** (1.11 s)

  <details><summary>Answer</summary>

  ```json
  {
    "labs": []
  }
  ```

  </details>

## `get_vm_provisioning_snapshots` - GET /V4/VMProvisioning/Snapshots

> **SKIPPED** on this run: Commvault answered: 400 - A valid VM GUID is required.

```python
cv.raw.vmprovisioning.get_vm_provisioning_snapshots()
```

**On the wire**

- `GET /V4/VMProvisioning/Snapshots` -> **400** (0.07 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorMessage": "A valid VM GUID is required.",
    "errorCode": 1
  }
  ```

  </details>

## `get_vm_provisioning_virtual_machines` - GET /V4/VMProvisioning/VirtualMachines

```python
cv.raw.vmprovisioning.get_vm_provisioning_virtual_machines()
```

**On the wire**

- `GET /V4/VMProvisioning/VirtualMachines` -> **200** (0.33 s)

  <details><summary>Answer</summary>

  ```json
  {
    "virtualMachines": []
  }
  ```

  </details>

## `get_vm_provisioning_policy` - GET /V4/VMProvisioning/Policy/{policyId}

```python
cv.raw.vmprovisioning.get_vm_provisioning_policy('40')
```

**On the wire**

- `GET /V4/VMProvisioning/Policy/40` -> **200** (0.28 s)

  <details><summary>Answer</summary>

  ```json
  {}
  ```

  </details>

## `get_vm_provisioning_virtual_machine` - GET /V4/VMProvisioning/VirtualMachine/{vmGUID}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.vmprovisioning.get_vm_provisioning_virtual_machine(...)
```

## `get_vm_provisioning_virtual_machine_volumes`

GET /V4/VMProvisioning/VirtualMachine/{vmGUID}/Volumes

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.vmprovisioning.get_vm_provisioning_virtual_machine_volumes(...)
```
