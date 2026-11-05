# `cv.raw.snapshot_configurations`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:50 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `list_storage_arrays_vendors` - GET /V4/StorageArrays/Vendors

```python
cv.raw.snapshot_configurations.list_storage_arrays_vendors()
```

**On the wire**

- `GET /V4/StorageArrays/Vendors` -> **200** (0.50 s)

  <details><summary>Answer</summary>

  ```json
  {
    "snapVendors": [
      {
        "snapVendor": {
          "id": 28,
          "name": "Amazon Web Services"
        },
        "capabilities": {
          "enableUserName": true,
          "enableControlHost": false,
          "enablePassword": "<masked>",
          "enableArrayDeviceGroup": false,
          "enableHostDeviceGroup": false,
          "enableArrayNameChange": false,
          "enableName": true,
          "enableArrayType": true,
          "enableNetAppCloudAccount": false
        },
        "labels": {
          "name": "",
          "controlHost": "",
          "userName": "",
          "password": ""
        }
      },
      {
        "snapVendor": {
          "id": 41,
          "name": "Cisco HyperFlex"
        },
        "capabilities": {
          "enableUserName": true,
          "enableControlHost": false,
          "enablePassword": "<masked>",
          "enableArrayDeviceGroup": false,
          "enableHostDeviceGroup": false,
          "enableArrayNameChange": false,
          "enableName": true,
          "enableArrayType": false,
          "enableNetAppCloudAccount": false
        },
        "labels": {
          "name": "",
          "controlHost": "",
          "userName": "",
          "password": ""
        }
      },
      {
        "snapVendor": {
          "id": 47,
          "name": "Commvault Distributed Storage"
        },
        "capabilities": {
          "enableUserName": true,
          "enableControlHost": true,
          "enablePassword": "<masked>",
          "enableArrayDeviceGroup": false,
          "enableHostDeviceGroup": false,
          "enableArrayNameChange": false,
          "enableName": true,
          "enableArrayType": false,
          "enableNetAppCloudAccount": false
        },
        "labels": {
          "name": "",
          "controlHost": "",
          "userName": "",
          "password": ""
        }
      },
      "... 42 more"
    ]
  }
  ```

  </details>

## `get_storage_arrays_vendor` - GET /V4/StorageArrays/Vendors/{vendorId}

```python
cv.raw.snapshot_configurations.get_storage_arrays_vendor('28')
```

**On the wire**

- `GET /V4/StorageArrays/Vendors/28` -> **200** (0.23 s)

  <details><summary>Answer</summary>

  ```json
  {
    "vendor": "Amazon Web Services",
    "configList": []
  }
  ```

  </details>

## `get_storage_array_client_snap_configs`

GET /V4/StorageArrays/{arrayId}/Client/{clientId}/Snap/Configs

```python
cv.raw.snapshot_configurations.get_storage_array_client_snap_configs('1', '2')
```

**On the wire**

- `GET /V4/StorageArrays/1/Client/2/Snap/Configs` -> **200** (0.24 s)

  <details><summary>Answer</summary>

  ```json
  {
    "copyId": 0,
    "subclientId": 0,
    "clientId": 0,
    "assocType": 8,
    "snapConfigurations": []
  }
  ```

  </details>

## `get_storage_array_subclient_snap_configs`

GET /V4/StorageArrays/{arrayId}/Subclient/{subclientId}/Snap/Configs

```python
cv.raw.snapshot_configurations.get_storage_array_subclient_snap_configs('1', '44')
```

**On the wire**

- `GET /V4/StorageArrays/1/Subclient/44/Snap/Configs` -> **200** (0.22 s)

  <details><summary>Answer</summary>

  ```json
  {
    "copyId": 0,
    "subclientId": 44,
    "clientId": 0,
    "assocType": 9,
    "snapConfigurations": []
  }
  ```

  </details>

## `get_storage_arrays_copy_array_snap_configs`

GET /V4/StorageArrays/Copy/{copyId}/Arrays/{arrayId}/Snap/Configs

```python
cv.raw.snapshot_configurations.get_storage_arrays_copy_array_snap_configs('2', '1')
```

**On the wire**

- `GET /V4/StorageArrays/Copy/2/Arrays/1/Snap/Configs` -> **200** (0.22 s)

  <details><summary>Answer</summary>

  ```json
  {
    "copyId": 2,
    "subclientId": 0,
    "clientId": 0,
    "assocType": 6,
    "snapConfigurations": []
  }
  ```

  </details>
