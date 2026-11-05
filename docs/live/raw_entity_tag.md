# `cv.raw.entity_tag`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:50 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_tags_associated_entities` - GET /V4/Tags/AssociatedEntities

```python
cv.raw.entity_tag.get_tags_associated_entities()
```

**On the wire**

- `GET /V4/Tags/AssociatedEntities` -> **200** (0.08 s)

  <details><summary>Answer</summary>

  ```json
  {
    "tagSetInfo": {
      "name": "Default Tagset",
      "id": 122
    }
  }
  ```

  </details>

## `get_tag_values` - GET /V4/Tags/{tagId}/Values

```python
cv.raw.entity_tag.get_tag_values('1')
```

**On the wire**

- `GET /V4/Tags/1/Values` -> **200** (0.07 s)

  <details><summary>Answer</summary>

  ```json
  {
    "tagId": 1
  }
  ```

  </details>
