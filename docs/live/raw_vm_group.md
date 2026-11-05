# `cv.raw.vm_group`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:37 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `list_vm_groups` - GET /V4/VMGroups

```python
cv.raw.vm_group.list_vm_groups()
```

**On the wire**

- `GET /V4/VMGroups` -> **200** (0.13 s)

  <details><summary>Answer</summary>

  ```json
  {
    "vmGroupCount": 0,
    "vmGroups": []
  }
  ```

  </details>

## `get_vm_group` - GET /V4/VmGroup/{VmGroupId}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.vm_group.get_vm_group(...)
```
