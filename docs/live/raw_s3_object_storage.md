# `cv.raw.s3_object_storage`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:50 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_cloud_apps_access_nodes` - GET /CloudApps/AccessNodes

```python
cv.raw.s3_object_storage.get_cloud_apps_access_nodes()
```

**On the wire**

- `GET /CloudApps/AccessNodes` -> **200** (0.09 s)

  <details><summary>Answer</summary>

  ```json
  {
    "accessNodes": [
      {
        "entity": {
          "clientId": 2,
          "clientName": "commserve-02",
          "_type_": 3
        }
      },
      {
        "entity": {
          "clientGroupName": "client-group-01",
          "clientGroupId": 1,
          "_type_": 28
        }
      },
      {
        "entity": {
          "clientGroupName": "client-group-03",
          "clientGroupId": 3,
          "_type_": 28
        }
      }
    ]
  }
  ```

  </details>
