# `cv.raw.email_server`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:50 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_email_server` - GET /V4/EmailServer

```python
cv.raw.email_server.get_email_server()
```

**On the wire**

- `GET /V4/EmailServer` -> **200** (0.15 s)

  <details><summary>Answer</summary>

  ```json
  {
    "SMTPServerName": "smtp.host-57",
    "SMTPPort": 465,
    "senderEmail": "user-05",
    "senderName": "cv toaster",
    "encryptionAlgorithm": "SSL",
    "useAuthentication": true,
    "username": "user-05"
  }
  ```

  </details>
