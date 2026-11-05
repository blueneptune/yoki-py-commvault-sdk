# `cv.raw.data_cube`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:50 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_dcube_get_analytics_engine` - GET /dcube/getAnalyticsEngine

```python
cv.raw.data_cube.get_dcube_get_analytics_engine()
```

**On the wire**

- `GET /dcube/getAnalyticsEngine` -> **200** (0.14 s)

  <details><summary>Answer</summary>

  ```json
  {}
  ```

  </details>

## `get_dcube_get_data_sources` - GET /dcube/GetDataSources

```python
cv.raw.data_cube.get_dcube_get_data_sources()
```

**On the wire**

- `GET /dcube/GetDataSources` -> **200** (0.16 s)

  <details><summary>Answer</summary>

  ```json
  {}
  ```

  </details>

## `get_dcube_getcommcellinfo` - GET /dcube/getcommcellinfo

> **SKIPPED** on this run: Commvault answered: 400

```python
cv.raw.data_cube.get_dcube_getcommcellinfo()
```

**On the wire**

- `GET /dcube/getcommcellinfo` -> **400** (0.06 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

## `get_e_discovery_clients_clients_4` - GET /V2/EDiscoveryClients/Clients/4

```python
cv.raw.data_cube.get_e_discovery_clients_clients_4()
```

**On the wire**

- `GET /V2/EDiscoveryClients/Clients/4` -> **200** (0.15 s)

  <details><summary>Answer</summary>

  ```json
  {
    "totalClientCount": 0,
    "totalDsCount": 0,
    "nodeList": []
  }
  ```

  </details>

## `get_dcube_export_status` - GET /dcube/export/{datasourceHandlerId}/status

> **SKIPPED** on this run: not swept: starts work or returns a file

```python
cv.raw.data_cube.get_dcube_export_status(...)
```

## `get_dcube_get_history` - GET /dcube/GetHistory/{DatasourceId}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.data_cube.get_dcube_get_history(...)
```

## `get_dcube_get_jdbc_driver` - GET /dcube/GetJDBCDrivers/{cloudId}

> **SKIPPED** on this run: Commvault answered: 403

```python
cv.raw.data_cube.get_dcube_get_jdbc_driver('1')
```

**On the wire**

- `GET /dcube/GetJDBCDrivers/1` -> **403** (0.02 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

## `get_dcube_get_status` - GET /dcube/GetStatus/{DatasourceId}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.data_cube.get_dcube_get_status(...)
```
