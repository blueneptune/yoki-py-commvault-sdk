# `cv.raw.node`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:50 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `list_nodes` - GET /V4/Nodes

```python
cv.raw.node.list_nodes()
```

**On the wire**

- `GET /V4/Nodes` -> **200** (0.30 s)

  <details><summary>Answer</summary>

  ```json
  {
    "nodeDetail": []
  }
  ```

  </details>

## `get_node` - GET /V4/Nodes/{nodeId}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.node.get_node(...)
```

## `get_node_ddb_disks` - GET /V4/Nodes/{nodeId}/DDB/Disks

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.node.get_node_ddb_disks(...)
```
