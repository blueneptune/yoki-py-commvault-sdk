# `cv.raw.protection_group`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 16:43 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_protection_group_aws` - GET /V4/ProtectionGroup/AWS

```python
cv.raw.protection_group.get_protection_group_aws()
```

**On the wire**

- `GET /V4/ProtectionGroup/AWS` -> **200** (0.07 s)

  <details><summary>Answer</summary>

  ```json
  {
    "protectionGroups": []
  }
  ```

  </details>

## `get_protection_group_azure` - GET /V4/ProtectionGroup/Azure

```python
cv.raw.protection_group.get_protection_group_azure()
```

**On the wire**

- `GET /V4/ProtectionGroup/Azure` -> **200** (0.08 s)

  <details><summary>Answer</summary>

  ```json
  {
    "protectionGroups": []
  }
  ```

  </details>

## `get_protection_group_gcp` - GET /V4/ProtectionGroup/GCP

```python
cv.raw.protection_group.get_protection_group_gcp()
```

**On the wire**

- `GET /V4/ProtectionGroup/GCP` -> **200** (0.07 s)

  <details><summary>Answer</summary>

  ```json
  {
    "protectionGroups": []
  }
  ```

  </details>

## `get_protection_group` - GET /V4/ProtectionGroup/{protectionGroupId}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.protection_group.get_protection_group(...)
```

## `get_protection_group_entities` - GET /V4/ProtectionGroup/{protectionGroupId}/Entities

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.protection_group.get_protection_group_entities(...)
```
