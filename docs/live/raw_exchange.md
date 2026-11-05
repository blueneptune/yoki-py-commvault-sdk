# `cv.raw.exchange`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 16:43 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `list_office365_exchange` - GET /V4/Office365/Exchange

```python
cv.raw.exchange.list_office365_exchange()
```

**On the wire**

- `GET /V4/Office365/Exchange` -> **200** (0.11 s)

  <details><summary>Answer</summary>

  ```json
  {
    "clients": []
  }
  ```

  </details>

## `list_office365_exchange_content` - GET /V4/Office365/Exchange/{appId}/Content

> **SKIPPED** on this run: not swept: starts work or returns a file

```python
cv.raw.exchange.list_office365_exchange_content(...)
```

## `list_office365_exchange_mailboxes` - GET /V4/Office365/Exchange/{appId}/Mailboxes

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.exchange.list_office365_exchange_mailboxes(...)
```
