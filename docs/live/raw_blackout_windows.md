# `cv.raw.blackout_windows`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 16:43 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `list_blackout_window_v4` - GET /V4/BlackoutWindow

```python
cv.raw.blackout_windows.list_blackout_window_v4()
```

**On the wire**

- `GET /V4/BlackoutWindow` -> **200** (0.23 s)

  <details><summary>Answer</summary>

  ```json
  {
    "blackoutWindows": []
  }
  ```

  </details>

## `list_blackout_window_v5` - GET /V5/BlackoutWindow

```python
cv.raw.blackout_windows.list_blackout_window_v5()
```

**On the wire**

- `GET /V5/BlackoutWindow` -> **200** (0.22 s)

  <details><summary>Answer</summary>

  ```json
  {
    "blackoutWindows": []
  }
  ```

  </details>

## `get_blackout_window_v4` - GET /V4/BlackoutWindow/{blackoutWindowId}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.blackout_windows.get_blackout_window_v4(...)
```

## `get_blackout_window_v5` - GET /V5/BlackoutWindow/{blackoutWindowId}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.blackout_windows.get_blackout_window_v5(...)
```
