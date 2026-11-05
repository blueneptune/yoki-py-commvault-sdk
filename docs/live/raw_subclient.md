# `cv.raw.subclient`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 16:43 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_subclient_email_policy_association`

GET /Subclient/{subclientId}/EmailPolicyAssociation

```python
cv.raw.subclient.get_subclient_email_policy_association('44')
```

**On the wire**

- `GET /Subclient/44/EmailPolicyAssociation` -> **200** (0.13 s)

  <details><summary>Answer</summary>

  ```json
  {
    "stats": {
      "indexCreationTime": 0,
      "ciCount": 0,
      "numberOfItems": 0,
      "lastCiJobRanTime": 0,
      "lastArchiveJobRanTime": 0,
      "appArchiveSize": 0,
      "emailCount": 0
    }
  }
  ```

  </details>

## `get_subclient_by_name`

GET /Subclient/byName(clientName='{clientname}',appName='{appname}',backupsetName='{backupsetname}',subclientName='{subclientname}')

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.subclient.get_subclient_by_name(...)
```
