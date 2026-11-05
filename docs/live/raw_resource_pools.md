# `cv.raw.resource_pools`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:37 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_resource_pool` - GET /V4/ResourcePool

```python
cv.raw.resource_pools.get_resource_pool()
```

**On the wire**

- `GET /V4/ResourcePool` -> **200** (0.50 s)

  <details><summary>Answer</summary>

  ```json
  {
    "resourcePools": []
  }
  ```

  </details>

## `get_resource_pool_count` - GET /V4/ResourcePool/Count

> **SKIPPED** on this run: Commvault answered: 400

```python
cv.raw.resource_pools.get_resource_pool_count()
```

**On the wire**

- `GET /V4/ResourcePool/Count` -> **400** (0.06 s)

  <details><summary>Answer</summary>

  (no body)

  </details>
