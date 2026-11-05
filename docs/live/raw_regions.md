# `cv.raw.regions`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:50 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_entity_region` - GET /entity/region

> **SKIPPED** on this run: Commvault answered: 403

```python
cv.raw.regions.get_entity_region()
```

**On the wire**

- `GET /entity/region` -> **403** (0.01 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

## `list_regions` - GET /Regions

```python
cv.raw.regions.list_regions()
```

**On the wire**

- `GET /Regions` -> **200** (0.14 s)

  <details><summary>Answer</summary>

  ```json
  {
    "regions": [
      {
        "regionType": 0,
        "isInfraRegion": false,
        "regionEntity": {
          "displayName": "Africa",
          "regionName": "Africa",
          "regionId": 1,
          "entityInfo": {
            "companyId": 0,
            "companyName": "Commcell"
          }
        }
      },
      {
        "regionType": 0,
        "isInfraRegion": false,
        "regionEntity": {
          "displayName": "Asia",
          "regionName": "Asia",
          "regionId": 2,
          "entityInfo": {
            "companyId": 0,
            "companyName": "Commcell"
          }
        }
      },
      {
        "regionType": 0,
        "isInfraRegion": false,
        "regionEntity": {
          "displayName": "Australia",
          "regionName": "Australia",
          "regionId": 3,
          "entityInfo": {
            "companyId": 0,
            "companyName": "Commcell"
          }
        }
      },
      "... 196 more"
    ]
  }
  ```

  </details>

## `list_regions_v4` - GET /V4/Regions

```python
cv.raw.regions.list_regions_v4()
```

**On the wire**

- `GET /V4/Regions` -> **200** (0.48 s)

  <details><summary>Answer</summary>

  ```json
  {
    "regions": [
      {
        "id": 1,
        "name": "Africa",
        "displayName": "Africa",
        "regionType": "DEFAULT",
        "locations": [
          {
            "city": "",
            "state": "",
            "country": "Algeria"
          },
          {
            "city": "",
            "state": "",
            "country": "Angola"
          },
          {
            "city": "",
            "state": "",
            "country": "Benin"
          },
          "... 51 more"
        ],
        "associatedServers": 0,
        "associatedRegionBasedPlans": 0,
        "company": {
          "id": 0,
          "name": "Commcell"
        }
      },
      {
        "id": 2,
        "name": "Asia",
        "displayName": "Asia",
        "regionType": "DEFAULT",
        "locations": [
          {
            "city": "",
            "state": "",
            "country": "Afghanistan"
          },
          {
            "city": "",
            "state": "",
            "country": "Armenia"
          },
          {
            "city": "",
            "state": "",
            "country": "Bahrain"
          },
          "... 46 more"
        ],
        "associatedServers": 0,
        "associatedRegionBasedPlans": 0,
        "company": {
          "id": 0,
          "name": "Commcell"
        }
      },
      {
        "id": 3,
        "name": "Australia",
        "displayName": "Australia",
        "regionType": "DEFAULT",
        "locations": [
          {
            "city": "",
            "state": "",
            "country": "Australia"
          },
          {
            "city": "",
            "state": "",
            "country": "Fiji"
          },
          {
            "city": "",
            "state": "",
            "country": "Guam"
          },
          "... 16 more"
        ],
        "associatedServers": 0,
        "associatedRegionBasedPlans": 0,
        "company": {
          "id": 0,
          "name": "Commcell"
        }
      },
      "... 196 more"
    ]
  }
  ```

  </details>

## `get_region` - GET /Regions/{regionId}

```python
cv.raw.regions.get_region('1')
```

**On the wire**

- `GET /Regions/1` -> **200** (0.35 s)

  <details><summary>Answer</summary>

  ```json
  {
    "regions": [
      {
        "regionType": 0,
        "isInfraRegion": false,
        "regionEntity": {
          "displayName": "Africa",
          "regionName": "Africa",
          "regionId": 1,
          "entityInfo": {
            "companyId": 0,
            "companyName": "Commcell"
          }
        },
        "regionPlans": {
          "numOfPlans": 0
        },
        "regionClients": {
          "numOfClients": 0
        },
        "zones": {
          "zone": [
            {
              "continent": "Africa",
              "country": "Algeria",
              "city": "",
              "latitude": 28.0339,
              "state": "",
              "longitude": 1.65963,
              "zoneEntity": {
                "zoneId": 3,
                "zoneName": "Algeria"
              }
            },
            {
              "continent": "Africa",
              "country": "Angola",
              "city": "",
              "latitude": -11.2027,
              "state": "",
              "longitude": 17.8739,
              "zoneEntity": {
                "zoneId": 5,
                "zoneName": "Angola"
              }
            },
            {
              "continent": "Africa",
              "country": "Benin",
              "city": "",
              "latitude": 9.30769,
              "state": "",
              "longitude": 2.31583,
              "zoneEntity": {
                "zoneId": 20,
                "zoneName": "Benin"
              }
            },
            "... 51 more"
          ]
        }
      }
    ]
  }
  ```

  </details>

## `get_region_clients` - GET /Regions/{regionId}/clients

```python
cv.raw.regions.get_region_clients('1')
```

**On the wire**

- `GET /Regions/1/clients` -> **200** (0.34 s)

  <details><summary>Answer</summary>

  ```json
  {
    "regions": [
      {
        "regionType": 0,
        "isInfraRegion": false,
        "regionEntity": {
          "displayName": "Africa",
          "regionName": "Africa",
          "regionId": 1,
          "entityInfo": {
            "companyId": 0,
            "companyName": "Commcell"
          }
        },
        "regionPlans": {
          "numOfPlans": 0
        },
        "regionClients": {
          "numOfClients": 0
        },
        "zones": {
          "zone": [
            {
              "continent": "Africa",
              "country": "Algeria",
              "city": "",
              "latitude": 28.0339,
              "state": "",
              "longitude": 1.65963,
              "zoneEntity": {
                "zoneId": 3,
                "zoneName": "Algeria"
              }
            },
            {
              "continent": "Africa",
              "country": "Angola",
              "city": "",
              "latitude": -11.2027,
              "state": "",
              "longitude": 17.8739,
              "zoneEntity": {
                "zoneId": 5,
                "zoneName": "Angola"
              }
            },
            {
              "continent": "Africa",
              "country": "Benin",
              "city": "",
              "latitude": 9.30769,
              "state": "",
              "longitude": 2.31583,
              "zoneEntity": {
                "zoneId": 20,
                "zoneName": "Benin"
              }
            },
            "... 51 more"
          ]
        }
      }
    ]
  }
  ```

  </details>

## `get_region_v4` - GET /V4/Regions/{regionId}

```python
cv.raw.regions.get_region_v4('1')
```

**On the wire**

- `GET /V4/Regions/1` -> **200** (0.71 s)

  <details><summary>Answer</summary>

  ```json
  {
    "id": 1,
    "name": "Africa",
    "displayName": "Africa",
    "regionType": "DEFAULT",
    "locations": [
      {
        "continent": "Africa",
        "country": "Algeria",
        "city": "",
        "latitude": 28.0339,
        "state": "",
        "longitude": 1.65963,
        "zone": {
          "id": 3,
          "name": "Algeria"
        }
      },
      {
        "continent": "Africa",
        "country": "Angola",
        "city": "",
        "latitude": -11.2027,
        "state": "",
        "longitude": 17.8739,
        "zone": {
          "id": 5,
          "name": "Angola"
        }
      },
      {
        "continent": "Africa",
        "country": "Benin",
        "city": "",
        "latitude": 9.30769,
        "state": "",
        "longitude": 2.31583,
        "zone": {
          "id": 20,
          "name": "Benin"
        }
      },
      "... 51 more"
    ],
    "associatedServers": {
      "serversCount": 0,
      "servers": []
    },
    "associatedRegionBasedPlans": {
      "plansCount": 0,
      "plans": []
    }
  }
  ```

  </details>

## `get_entity_region_by_entity_type_entity_id` - GET /entity/{entityType}/{entityId}/region

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.regions.get_entity_region_by_entity_type_entity_id(...)
```
