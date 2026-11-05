# `cv.raw.laptop_devices`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 16:43 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `list_device` - GET /Device

```python
cv.raw.laptop_devices.list_device()
```

**On the wire**

- `GET /Device` -> **200** (0.10 s)

  <details><summary>Answer</summary>

  ```json
  {
    "error": {
      "errorMessage": "",
      "errorCode": 0
    }
  }
  ```

  </details>

## `get_device` - GET /Device/{deviceId}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.laptop_devices.get_device(...)
```
