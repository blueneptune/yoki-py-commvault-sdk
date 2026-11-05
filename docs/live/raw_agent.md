# `cv.raw.agent`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 16:43 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_agent` - GET /Agent

> **SKIPPED** on this run: Commvault answered: 400

```python
cv.raw.agent.get_agent()
```

**On the wire**

- `GET /Agent` -> **400** (0.07 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

## `get_comm_cell_agents` - GET /V4/CommCell/Agents

```python
cv.raw.agent.get_comm_cell_agents()
```

**On the wire**

- `GET /V4/CommCell/Agents` -> **200** (0.08 s)

  <details><summary>Answer</summary>

  ```json
  {
    "agentDetails": [
      {
        "appTypeId": 5,
        "appTypeName": "Sybase"
      },
      {
        "appTypeId": 29,
        "appTypeName": "File System"
      },
      {
        "appTypeId": 33,
        "appTypeName": "File System"
      },
      "... 4 more"
    ]
  }
  ```

  </details>

## `get_get_id` - GET /GetId

> **SKIPPED** on this run: Commvault answered: 403 - Access denied: unsupported entity type for permission validation.

```python
cv.raw.agent.get_get_id()
```

**On the wire**

- `GET /GetId` -> **403** (0.10 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorMessage": "Access denied: unsupported entity type for permission validation.",
    "errorCode": -1
  }
  ```

  </details>
