# `cv.raw.activate`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 16:43 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_analytics_servers` - GET /AnalyticsServers

```python
cv.raw.activate.get_analytics_servers()
```

**On the wire**

- `GET /AnalyticsServers` -> **200** (0.07 s)

  <details><summary>Answer</summary>

  ```json
  {
    "listOfCIServer": [
      {
        "hostName": "commserve-02",
        "internalCloudName": "CVTOASTERAnalyticsServer3",
        "clientName": "commserve-02",
        "cIServerURL": "http://commserve-02:20000",
        "type": 3,
        "basePort": 20000,
        "clientId": 2,
        "version": "DC 1.0",
        "cloudID": 1,
        "serverType": 1,
        "engineName": "host-01",
        "indexServerClientId": 3
      }
    ]
  }
  ```

  </details>

## `list_dcube_entity` - GET /dcube/entity

```python
cv.raw.activate.list_dcube_entity()
```

**On the wire**

- `GET /dcube/entity` -> **200** (0.11 s)

  <details><summary>Answer</summary>

  ```json
  {
    "entityDetails": [
      {
        "displayName": "Email",
        "flags": 1,
        "description": "Email address.",
        "categoryName": "Generic",
        "enabled": true,
        "entityName": "Email",
        "attribute": 2,
        "entityType": 2,
        "entityKey": "email",
        "entityId": 10,
        "entityXML": {
          "keywords": "",
          "userDefinedKeywords": "",
          "riskCategories": "PII_LINKABLE",
          "entityKey": "email",
          "isSystemDefinedEntity": true,
          "dsSensitivity": 3,
          "inheritBaseWords": false
        },
        "yaraRulesDetails": {
          "modifiedTime": 0,
          "createdTime": 0,
          "numYaraRules": 0
        }
      },
      {
        "displayName": "Finnish Driver License",
        "flags": 3,
        "description": "",
        "categoryName": "Finland",
        "enabled": true,
        "entityName": "Finnish Driver License",
        "createdTime": 1787248196,
        "attribute": 2,
        "entityType": 2,
        "entityKey": "finland_dl",
        "entityId": 100,
        "entityXML": {
          "keywords": "driverlic,driverlics,driverlicense,driverlicenses,driverlicence,driverlicences,driver lic,driver lics,driver license,driver licenses,driver licence,driver licences,driverslic,driverslics,driverslicence,driverslicences,driverslicense,ajokortti,permis de conduire,ajokortin numero,kuljettaja lic.,kÃ¶rkort,kÃ¶rkortnummer,fÃ¶rare lic.,ajokortit,ajokortin numerot",
          "userDefinedKeywords": "",
          "riskCategories": "PII",
          "entityKey": "finland_dl",
          "isSystemDefinedEntity": true,
          "dsSensitivity": 4,
          "inheritBaseWords": false
        },
        "yaraRulesDetails": {
          "modifiedTime": 0,
          "createdTime": 0,
          "numYaraRules": 0
        }
      },
      {
        "displayName": "French Driver License",
        "flags": 3,
        "description": "",
        "categoryName": "France",
        "enabled": true,
        "entityName": "French Driver License",
        "createdTime": 1787248196,
        "attribute": 2,
        "entityType": 2,
        "entityKey": "france_driver_id",
        "entityId": 101,
        "entityXML": {
          "keywords": "driverlic,driverlics,driverlicense,driverlicenses,driverlicence,driverlicences,driver lic,driver lics,driver license,driver licenses,driver licence,driver licences,driverslic,driverslics,driverslicence,driverslicences,driverslicense",
          "userDefinedKeywords": "",
          "riskCategories": "PII",
          "entityKey": "france_driver_id",
          "isSystemDefinedEntity": true,
          "dsSensitivity": 4,
          "inheritBaseWords": false
        },
        "yaraRulesDetails": {
          "modifiedTime": 0,
          "createdTime": 0,
          "numYaraRules": 0
        }
      },
      "... 189 more"
    ]
  }
  ```

  </details>

## `list_e_discovery_clients_inventories` - GET /EDiscoveryClients/Inventories

```python
cv.raw.activate.list_e_discovery_clients_inventories()
```

**On the wire**

- `GET /EDiscoveryClients/Inventories` -> **200** (0.11 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorResp": {}
  }
  ```

  </details>

## `list_e_discoveryclients` - GET /EDiscoveryclients

> **SKIPPED** on this run: Commvault answered: 500

```python
cv.raw.activate.list_e_discoveryclients()
```

**On the wire**

- `GET /EDiscoveryclients` -> **500** (0.07 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

## `get_analytics_servers_id` - GET /AnalyticsServers/id/{cloudId}

```python
cv.raw.activate.get_analytics_servers_id('1')
```

**On the wire**

- `GET /AnalyticsServers/id/1` -> **200** (0.07 s)

  <details><summary>Answer</summary>

  ```json
  {
    "listOfCIServer": [
      {
        "hostName": "commserve-02",
        "internalCloudName": "CVTOASTERAnalyticsServer3",
        "clientName": "commserve-02",
        "cIServerURL": "http://commserve-02:20000",
        "type": 3,
        "basePort": 20000,
        "clientId": 2,
        "version": "DC 1.0",
        "cloudID": 1,
        "serverType": 1,
        "engineName": "host-01",
        "indexServerClientId": 3
      }
    ]
  }
  ```

  </details>

## `get_dcube_getsubclient-01handler` - GET /dcube/getsubclient-01handler/{datasourceId}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.activate.get_dcube_getsubclient-01handler(...)
```

## `get_dcube_handler` - GET /dcube/handler/{datasourceHandlerId}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.activate.get_dcube_handler(...)
```

## `get_e_discovery_client` - GET /EDiscoveryClients/{projectId}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.activate.get_e_discovery_client(...)
```

**On the wire**

- `GET /EDiscoveryclients` -> **500** (0.06 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

## `get_e_discovery_clients_client_jobs` - GET /EDiscoveryClients/Clients/{projectId}/Jobs

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.activate.get_e_discovery_clients_client_jobs(...)
```

## `get_e_discovery_clients_inventory` - GET /EDiscoveryClients/Inventories/{inventoryId}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.activate.get_e_discovery_clients_inventory(...)
```

## `get_activate_entity_audit` - GET /V4/Activate/Entity/{entityType}/{entityId}/Audit

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.activate.get_activate_entity_audit(...)
```
