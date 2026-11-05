# `cv.raw.array_management`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:50 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `list_storage_arrays` - GET /StorageArrays

```python
cv.raw.array_management.list_storage_arrays()
```

**On the wire**

- `GET /StorageArrays` -> **200** (0.20 s)

  <details><summary>Answer</summary>

  ```json
  {
    "copyId": 0,
    "appId": 0,
    "array": {
      "name": "",
      "id": 0
    },
    "vendor": {
      "name": "",
      "id": 0
    },
    "arrayList": [
      {
        "offlineReason": "",
        "flags": 4,
        "description": "",
        "ctrlHostName": "",
        "arrayTypeFlags": 0,
        "arrayType": 0,
        "VSVendor": 0,
        "isEnabled": true,
        "arrayInfoType": 0,
        "arrayName": {
          "name": "AWS-DefaultUseIAMRoleArray",
          "id": 1
        },
        "vendor": {
          "name": "Amazon Web Services",
          "id": 0
        },
        "userPswd": {
          "userName": ""
        }
      },
      {
        "offlineReason": "",
        "flags": 4,
        "description": "",
        "ctrlHostName": "",
        "arrayTypeFlags": 0,
        "arrayType": 0,
        "VSVendor": 0,
        "isEnabled": true,
        "arrayInfoType": 0,
        "arrayName": {
          "name": "GCP-Default-IAM",
          "id": 3
        },
        "vendor": {
          "name": "Google Cloud Platform",
          "id": 0
        },
        "userPswd": {
          "userName": ""
        }
      },
      {
        "offlineReason": "",
        "flags": 4,
        "description": "",
        "ctrlHostName": "",
        "arrayTypeFlags": 0,
        "arrayType": 0,
        "VSVendor": 0,
        "isEnabled": true,
        "arrayInfoType": 0,
        "arrayName": {
          "name": "Azure-Default-MSI",
          "id": 2
        },
        "vendor": {
          "name": "Microsoft Azure",
          "id": 0
        },
        "userPswd": {
          "userName": ""
        }
      },
      "... 2 more"
    ]
  }
  ```

  </details>

## `list_storage_arrays_v4` - GET /V4/StorageArrays

```python
cv.raw.array_management.list_storage_arrays_v4()
```

**On the wire**

- `GET /V4/StorageArrays` -> **200** (0.16 s)

  <details><summary>Answer</summary>

  ```json
  {
    "arrays": [
      {
        "assocFlag": false,
        "flags": 4,
        "VSVendor": 0,
        "description": "",
        "arrayTypeFlags": 0,
        "userName": "",
        "type": 0,
        "vendor": "Amazon Web Services",
        "name": "AWS-DefaultUseIAMRoleArray",
        "controlHost": "",
        "id": 1,
        "company": {
          "name": "Commcell",
          "id": 0
        }
      },
      {
        "assocFlag": false,
        "flags": 4,
        "VSVendor": 0,
        "description": "",
        "arrayTypeFlags": 0,
        "userName": "",
        "type": 0,
        "vendor": "Google Cloud Platform",
        "name": "GCP-Default-IAM",
        "controlHost": "",
        "id": 3,
        "company": {
          "name": "Commcell",
          "id": 0
        }
      },
      {
        "assocFlag": false,
        "flags": 4,
        "VSVendor": 0,
        "description": "",
        "arrayTypeFlags": 0,
        "userName": "",
        "type": 0,
        "vendor": "Microsoft Azure",
        "name": "Azure-Default-MSI",
        "controlHost": "",
        "id": 2,
        "company": {
          "name": "Commcell",
          "id": 0
        }
      },
      "... 2 more"
    ]
  }
  ```

  </details>

## `get_storage_array` - GET /StorageArrays/{storagearrayId}

```python
cv.raw.array_management.get_storage_array('1')
```

**On the wire**

- `GET /StorageArrays/1` -> **200** (0.23 s)

  <details><summary>Answer</summary>

  ```json
  {
    "clientId": 0,
    "flags": 0,
    "assocType": 3,
    "arrayPasswordLabel": "",
    "copyId": 0,
    "arrayNameLabel": "",
    "appId": 0,
    "arrayControlHostLabel": "",
    "capabilitiesFlag": 275233268125,
    "arrayUserNameLabel": "",
    "availableMAs": [
      {
        "displayName": "commserve-02",
        "arrayControllerId": 0,
        "mediaAgent": {
          "name": "commserve-02",
          "id": 2
        }
      }
    ],
    "hostDG": {
      "doNotMoveDevices": true,
      "isOverridden": false,
      "hostDGName": "",
      "useOnlySpouseDevices": false,
      "flags": 0,
      "deviceGroupOption": 0
    },
    "capabilities": {
      "enableControlHost": false,
      "enableUserName": true,
      "enablePassword": "<masked>",
      "enableArrayDG": false,
      "enableHostDG": false,
      "enableArrayNameChange": false,
      "enableName": true,
      "enableArrayType": true,
      "enableNetAppCloudAccount": false
    },
    "arrayDG": {
      "isOverridden": false,
      "arrayDGName": "",
      "flags": 0,
      "disableDG": false,
      "useDevicesFromThisDG": false
    },
    "configList": {},
    "error": {
      "errorString": "",
      "errorCode": 0
    },
    "array": {
      "name": "AWS-DefaultUseIAMRoleArray",
      "id": 1
    },
    "vendor": {
      "name": "Amazon Web Services",
      "id": 28
    },
    "info": {
      "passwordEdit": "<masked>",
      "offlineReason": "",
      "flags": 4,
      "description": "",
      "ctrlHostName": "",
      "arrayTypeFlags": 0,
      "enableNetAppCloudAccount": false,
      "uniqueIdentifier": "",
      "arrayType": 0,
      "VSVendor": 0,
      "cloudVendorId": 2,
      "offlineCode": 0,
      "isEnabled": true,
      "credentialRecordType": "<masked>",
      "arrayInfoType": 0,
      "securityAssociations": {
        "ownerAssociations": {},
        "tagWithCompany": {
          "providerId": 0,
          "providerDomainName": "Commcell"
        }
      },
      "arraySecurity": {
        "associatedUserGroups": [
          {
            "userGroupId": 1,
            "userGroupName": "master"
          }
        ]
      },
      "physicalArray": {
        "name": "",
        "id": 0
      },
      "arrayName": {
        "name": "AWS-DefaultUseIAMRoleArray",
        "id": 1
      },
      "vendor": {
        "name": "Amazon Web Services",
        "id": 0
      },
      "client": {
        "name": "",
        "id": 0
      },
      "userPswd": {
        "userName": ""
      },
      "entityInfo": {},
      "region": {
        "regionName": "",
        "regionId": 0
      },
      "savedCredential": "<masked>"
    },
    "serverGroupList": {
      "groups": [
        {
          "mediaAgentCount": 1,
          "name": "client-group-01",
          "id": 1
        },
        {
          "mediaAgentCount": 1,
          "name": "client-group-03",
          "id": 3
        }
      ]
    }
  }
  ```

  </details>

## `get_storage_array_v4` - GET /V4/StorageArrays/{arrayId}

```python
cv.raw.array_management.get_storage_array_v4('1')
```

**On the wire**

- `GET /V4/StorageArrays/1` -> **200** (0.38 s)

  <details><summary>Answer</summary>

  ```json
  {
    "labels": {
      "name": "",
      "controlHost": "",
      "userName": "",
      "password": ""
    },
    "general": {
      "snapVendor": {
        "id": 28,
        "name": "Amazon Web Services"
      },
      "array": {
        "id": 1,
        "name": "AWS-DefaultUseIAMRoleArray"
      },
      "physicalArray": {
        "id": 0,
        "name": ""
      },
      "controlHost": "",
      "assocType": 3,
      "credential": "",
      "region": {
        "id": 0,
        "name": ""
      },
      "flags": 4,
      "arrayType": 0,
      "arrayTypeFlags": 0,
      "enableNetAppCloudAccount": false,
      "cloudVendorId": 2,
      "uniqueIdentifier": "",
      "description": "",
      "company": {
        "id": 0,
        "name": "Commcell"
      }
    },
    "security": [],
    "accessNodes": [],
    "availableAccessNodes": [
      {
        "id": 2,
        "name": "commserve-02",
        "displayName": "commserve-02"
      }
    ],
    "snapConfigurations": [],
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
    "serverGroups": [
      {
        "id": 1,
        "name": "client-group-01",
        "mediaAgentCount": 1
      },
      {
        "id": 3,
        "name": "client-group-03",
        "mediaAgentCount": 1
      }
    ]
  }
  ```

  </details>

## `get_storage_arrays_client_arrays` - GET /V4/StorageArrays/Client/{clientId}/Arrays

```python
cv.raw.array_management.get_storage_arrays_client_arrays('2')
```

**On the wire**

- `GET /V4/StorageArrays/Client/2/Arrays` -> **200** (0.16 s)

  <details><summary>Answer</summary>

  ```json
  {
    "arrays": [
      {
        "assocFlag": false,
        "flags": 4,
        "VSVendor": 0,
        "description": "",
        "arrayTypeFlags": 0,
        "userName": "",
        "type": 0,
        "vendor": "Amazon Web Services",
        "name": "AWS-DefaultUseIAMRoleArray",
        "controlHost": "",
        "id": 1,
        "company": {
          "name": "Commcell",
          "id": 0
        }
      },
      {
        "assocFlag": false,
        "flags": 4,
        "VSVendor": 0,
        "description": "",
        "arrayTypeFlags": 0,
        "userName": "",
        "type": 0,
        "vendor": "Google Cloud Platform",
        "name": "GCP-Default-IAM",
        "controlHost": "",
        "id": 3,
        "company": {
          "name": "Commcell",
          "id": 0
        }
      },
      {
        "assocFlag": false,
        "flags": 4,
        "VSVendor": 0,
        "description": "",
        "arrayTypeFlags": 0,
        "userName": "",
        "type": 0,
        "vendor": "Microsoft Azure",
        "name": "Azure-Default-MSI",
        "controlHost": "",
        "id": 2,
        "company": {
          "name": "Commcell",
          "id": 0
        }
      },
      "... 2 more"
    ]
  }
  ```

  </details>

## `get_storage_arrays_copy_arrays` - GET /V4/StorageArrays/Copy/{copyId}/Arrays

```python
cv.raw.array_management.get_storage_arrays_copy_arrays('2')
```

**On the wire**

- `GET /V4/StorageArrays/Copy/2/Arrays` -> **200** (0.17 s)

  <details><summary>Answer</summary>

  ```json
  {
    "arrays": [
      {
        "assocFlag": false,
        "flags": 4,
        "VSVendor": 0,
        "description": "",
        "arrayTypeFlags": 0,
        "userName": "",
        "type": 0,
        "vendor": "Amazon Web Services",
        "name": "AWS-DefaultUseIAMRoleArray",
        "controlHost": "",
        "id": 1,
        "company": {
          "name": "Commcell",
          "id": 0
        }
      },
      {
        "assocFlag": false,
        "flags": 4,
        "VSVendor": 0,
        "description": "",
        "arrayTypeFlags": 0,
        "userName": "",
        "type": 0,
        "vendor": "Google Cloud Platform",
        "name": "GCP-Default-IAM",
        "controlHost": "",
        "id": 3,
        "company": {
          "name": "Commcell",
          "id": 0
        }
      },
      {
        "assocFlag": false,
        "flags": 4,
        "VSVendor": 0,
        "description": "",
        "arrayTypeFlags": 0,
        "userName": "",
        "type": 0,
        "vendor": "Microsoft Azure",
        "name": "Azure-Default-MSI",
        "controlHost": "",
        "id": 2,
        "company": {
          "name": "Commcell",
          "id": 0
        }
      },
      "... 2 more"
    ]
  }
  ```

  </details>

## `get_storage_arrays_client_subclient_arrays`

GET /V4/StorageArrays/Client/{clientId}/Subclient/{subclientId}/Arrays

```python
cv.raw.array_management.get_storage_arrays_client_subclient_arrays('2', '44')
```

**On the wire**

- `GET /V4/StorageArrays/Client/2/Subclient/44/Arrays` -> **200** (0.18 s)

  <details><summary>Answer</summary>

  ```json
  {
    "arrays": [
      {
        "assocFlag": false,
        "flags": 4,
        "VSVendor": 0,
        "description": "",
        "arrayTypeFlags": 0,
        "userName": "",
        "type": 0,
        "vendor": "Amazon Web Services",
        "name": "AWS-DefaultUseIAMRoleArray",
        "controlHost": "",
        "id": 1,
        "company": {
          "name": "Commcell",
          "id": 0
        }
      },
      {
        "assocFlag": false,
        "flags": 4,
        "VSVendor": 0,
        "description": "",
        "arrayTypeFlags": 0,
        "userName": "",
        "type": 0,
        "vendor": "Google Cloud Platform",
        "name": "GCP-Default-IAM",
        "controlHost": "",
        "id": 3,
        "company": {
          "name": "Commcell",
          "id": 0
        }
      },
      {
        "assocFlag": false,
        "flags": 4,
        "VSVendor": 0,
        "description": "",
        "arrayTypeFlags": 0,
        "userName": "",
        "type": 0,
        "vendor": "Microsoft Azure",
        "name": "Azure-Default-MSI",
        "controlHost": "",
        "id": 2,
        "company": {
          "name": "Commcell",
          "id": 0
        }
      },
      "... 2 more"
    ]
  }
  ```

  </details>
