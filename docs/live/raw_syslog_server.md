# `cv.raw.syslog_server`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:50 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_syslog_server` - GET /V4/syslogServer

```python
cv.raw.syslog_server.get_syslog_server()
```

**On the wire**

- `GET /V4/syslogServer` -> **200** (0.13 s)

  <details><summary>Answer</summary>

  ```json
  {
    "hostname": "",
    "port": 514,
    "secureMessaging": false,
    "enabled": false,
    "tppmClientId": 0,
    "forwardToSyslog": {
      "alerts": false,
      "audit": false,
      "events": false
    }
  }
  ```

  </details>
