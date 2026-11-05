# `cv.raw.threat_indicators`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:50 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_client_anomaly` - GET /Client/Anomaly

```python
cv.raw.threat_indicators.get_client_anomaly()
```

**On the wire**

- `GET /Client/Anomaly` -> **200** (0.10 s)

  <details><summary>Answer</summary>

  ```json
  {}
  ```

  </details>

## `list_client_anomaly_record` - GET /Client/AnomalyRecord

> **SKIPPED** on this run: Commvault answered: error 1: Invalid parameter, missing client list or job id or subclient id

```python
cv.raw.threat_indicators.list_client_anomaly_record()
```

**On the wire**

- `GET /Client/AnomalyRecord` -> **200** (0.07 s)

  <details><summary>Answer</summary>

  ```json
  {
    "error": {
      "errorMessage": "Invalid parameter, missing client list or job id or subclient id",
      "errorCode": 1
    }
  }
  ```

  </details>
