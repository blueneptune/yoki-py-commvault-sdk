# `cv.raw.cslive_sync`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:37 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_comm_serv_failover` - GET /CommServ/Failover

> **SKIPPED** on this run: Commvault answered: 500

```python
cv.raw.cslive_sync.get_comm_serv_failover()
```

**On the wire**

- `GET /CommServ/Failover` -> **500** (0.08 s)

  <details><summary>Answer</summary>

  ```json
  {
    "genericResp": {
      "errorString": "CommServe LiveSync needs at least one standby node and CommServe failover package should be installed on both active and standby nodes. Please check and install the required packages.",
      "errorCode": 587207528
    }
  }
  ```

  </details>
