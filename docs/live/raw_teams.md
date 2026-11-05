# `cv.raw.teams`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:50 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `list_office365_teams` - GET /V4/Office365/Teams

```python
cv.raw.teams.list_office365_teams()
```

**On the wire**

- `GET /V4/Office365/Teams` -> **200** (0.09 s)

  <details><summary>Answer</summary>

  ```json
  {
    "clients": []
  }
  ```

  </details>

## `list_office365_team_content` - GET /V4/Office365/Teams/{appId}/Content

> **SKIPPED** on this run: not swept: starts work or returns a file

```python
cv.raw.teams.list_office365_team_content(...)
```

## `list_office365_team_teams` - GET /V4/Office365/Teams/{appId}/Teams

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.teams.list_office365_team_teams(...)
```

## `list_office365_team_users` - GET /V4/Office365/Teams/{appId}/Users

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.teams.list_office365_team_users(...)
```
