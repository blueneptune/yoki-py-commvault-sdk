# `cv.raw.dataroom`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:37 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `list_dataroom` - GET /Dataroom

```python
cv.raw.dataroom.list_dataroom()
```

**On the wire**

- `GET /Dataroom` -> **200** (0.12 s)

  <details><summary>Answer</summary>

  ```json
  {
    "error": {},
    "datarooms": []
  }
  ```

  </details>

## `get_dataroom` - GET /Dataroom/{id}

> **SKIPPED** on this run: Commvault answered: 404 - Dataroom 2 not found

```python
cv.raw.dataroom.get_dataroom('2')
```

**On the wire**

- `GET /Dataroom/2` -> **404** (0.21 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorMessage": "Dataroom 2 not found",
    "errorCode": 1002
  }
  ```

  </details>
