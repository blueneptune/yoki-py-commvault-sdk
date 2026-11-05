# `cv.raw.commcell_group`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:37 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_commcell_group` - GET /CommcellGroup

> **SKIPPED** on this run: Commvault answered: 403

```python
cv.raw.commcell_group.get_commcell_group()
```

**On the wire**

- `GET /CommcellGroup` -> **403** (0.01 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

## `list_commcell_group` - GET /V4/CommcellGroup

```python
cv.raw.commcell_group.list_commcell_group()
```

**On the wire**

- `GET /V4/CommcellGroup` -> **200** (0.09 s)

  <details><summary>Answer</summary>

  ```json
  {
    "CommcellGroups": []
  }
  ```

  </details>

## `get_commcell_group_v4` - GET /V4/CommcellGroup/{commcellGroupId}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.commcell_group.get_commcell_group_v4(...)
```
