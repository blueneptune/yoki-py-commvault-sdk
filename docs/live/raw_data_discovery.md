# `cv.raw.data_discovery`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 16:43 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_asset_discovery_configuration` - GET /Asset/Discovery/Configuration

```python
cv.raw.data_discovery.get_asset_discovery_configuration()
```

**On the wire**

- `GET /Asset/Discovery/Configuration` -> **200** (0.12 s)

  <details><summary>Answer</summary>

  ```json
  {
    "credentials": []
  }
  ```

  </details>

## `get_asset_discovery_status` - GET /Asset/Discovery/Status

```python
cv.raw.data_discovery.get_asset_discovery_status()
```

**On the wire**

- `GET /Asset/Discovery/Status` -> **200** (0.08 s)

  <details><summary>Answer</summary>

  ```json
  {
    "status": 10
  }
  ```

  </details>
