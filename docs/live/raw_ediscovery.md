# `cv.raw.ediscovery`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:50 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_ediscovery_package_access_nodes`

GET /V4/Ediscovery/Packages/{packageId}/AccessNodes

```python
cv.raw.ediscovery.get_ediscovery_package_access_nodes('20')
```

**On the wire**

- `GET /V4/Ediscovery/Packages/20/AccessNodes` -> **200** (0.08 s)

  <details><summary>Answer</summary>

  ```json
  {
    "accessNodes": [
      {
        "name": "commserve-02",
        "id": 2
      }
    ]
  }
  ```

  </details>
