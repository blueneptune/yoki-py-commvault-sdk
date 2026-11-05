# `cv.raw.plan_rules`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:50 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_plan_rule_entities` - GET /V4/Plan/Rule/Entities

```python
cv.raw.plan_rules.get_plan_rule_entities()
```

**On the wire**

- `GET /V4/Plan/Rule/Entities` -> **200** (0.12 s)

  <details><summary>Answer</summary>

  ```json
  {
    "entities": []
  }
  ```

  </details>

## `get_plan_rule_entities_exclude` - GET /V4/Plan/Rule/Entities/Exclude

```python
cv.raw.plan_rules.get_plan_rule_entities_exclude()
```

**On the wire**

- `GET /V4/Plan/Rule/Entities/Exclude` -> **200** (0.10 s)

  <details><summary>Answer</summary>

  ```json
  {}
  ```

  </details>

## `get_plan_rule_settings` - GET /V4/Plan/Rule/Settings

```python
cv.raw.plan_rules.get_plan_rule_settings()
```

**On the wire**

- `GET /V4/Plan/Rule/Settings` -> **200** (0.08 s)

  <details><summary>Answer</summary>

  ```json
  {
    "enableAlertNotification": true,
    "executionMode": 2,
    "executionInterval": 60
  }
  ```

  </details>

## `list_plan_rule` - GET /V4/Plan/Rule

```python
cv.raw.plan_rules.list_plan_rule()
```

**On the wire**

- `GET /V4/Plan/Rule` -> **200** (0.09 s)

  <details><summary>Answer</summary>

  ```json
  {}
  ```

  </details>

## `get_plan_rule` - GET /V4/Plan/Rule/{ruleId}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.plan_rules.get_plan_rule(...)
```
