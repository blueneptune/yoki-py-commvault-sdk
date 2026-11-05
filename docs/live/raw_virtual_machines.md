# `cv.raw.virtual_machines`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:50 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_access_nodes` - GET /V4/AccessNodes

```python
cv.raw.virtual_machines.get_access_nodes()
```

**On the wire**

- `GET /V4/AccessNodes` -> **200** (0.15 s)

  <details><summary>Answer</summary>

  ```json
  {
    "accessNodes": [
      {
        "id": 2,
        "displayName": "commserve-02",
        "hostName": "commserve-02",
        "name": "commserve-02"
      }
    ]
  }
  ```

  </details>

## `get_kubernetes_application_groups` - GET /V4/Kubernetes/ApplicationGroups

```python
cv.raw.virtual_machines.get_kubernetes_application_groups()
```

**On the wire**

- `GET /V4/Kubernetes/ApplicationGroups` -> **200** (0.16 s)

  <details><summary>Answer</summary>

  ```json
  {
    "applicationGroupCount": 0,
    "applicationGroups": []
  }
  ```

  </details>

## `get_kubernetes_applications` - GET /V4/Kubernetes/Applications

```python
cv.raw.virtual_machines.get_kubernetes_applications()
```

**On the wire**

- `GET /V4/Kubernetes/Applications` -> **200** (0.24 s)

  <details><summary>Answer</summary>

  ```json
  {
    "applicationCount": 0,
    "applications": []
  }
  ```

  </details>

## `get_kubernetes_cluster` - GET /V4/Kubernetes/cluster

```python
cv.raw.virtual_machines.get_kubernetes_cluster()
```

**On the wire**

- `GET /V4/Kubernetes/cluster` -> **200** (0.20 s)

  <details><summary>Answer</summary>

  ```json
  {
    "clusters": []
  }
  ```

  </details>

## `list_virtual_machines` - GET /V4/VirtualMachines

```python
cv.raw.virtual_machines.list_virtual_machines()
```

**On the wire**

- `GET /V4/VirtualMachines` -> **200** (0.15 s)

  <details><summary>Answer</summary>

  ```json
  {
    "virtualMachinesCount": 0,
    "virtualMachines": []
  }
  ```

  </details>

## `get_virtual_machine` - GET /V4/VirtualMachines/{vmUUID}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.virtual_machines.get_virtual_machine(...)
```
