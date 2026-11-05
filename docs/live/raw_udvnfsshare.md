# `cv.raw.udvnfsshare`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 16:43 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `list_udvnfs_shares` - GET /V4/UDVNFSShares

> **SKIPPED** on this run: Commvault answered: 404

```python
cv.raw.udvnfsshare.list_udvnfs_shares()
```

**On the wire**

- `GET /V4/UDVNFSShares` -> **404** (0.06 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

## `get_udvnfs_share` - GET /V4/UDVNFSShares/{id}

> **SKIPPED** on this run: Commvault answered: 403

```python
cv.raw.udvnfsshare.get_udvnfs_share('2')
```

**On the wire**

- `GET /V4/UDVNFSShares` -> **404** (0.07 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

- `GET /V4/UDVNFSShares/2` -> **403** (0.01 s)

  <details><summary>Answer</summary>

  (no body)

  </details>
