# `cv.raw.additional_settings`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:37 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_added_entity_settings` - GET /V4/AddedEntitySettings

```python
cv.raw.additional_settings.get_added_entity_settings()
```

**On the wire**

- `GET /V4/AddedEntitySettings` -> **200** (0.11 s)

  <details><summary>Answer</summary>

  ```json
  {
    "entitySettings": [
      {
        "displayLabel": "Geo Location Based Restores",
        "type": "Boolean",
        "enabled": 1,
        "name": "bConsiderGeoLocationForRestores",
        "category": "CommServDB.Console",
        "values": [
          {
            "comment": "",
            "value": "true",
            "entity": {
              "sourceEntityType": 0,
              "name": "commserve-02",
              "id": 2,
              "type": "Server"
            }
          },
          {
            "comment": "",
            "value": "true",
            "entity": {
              "sourceEntityType": 0,
              "name": "commserve-02",
              "id": 2,
              "type": "Server"
            }
          }
        ]
      },
      {
        "displayLabel": "bDisableInfiniteRetention",
        "type": "Boolean",
        "enabled": 1,
        "name": "bDisableInfiniteRetention",
        "category": "CommServDB.AdminConsole",
        "values": [
          {
            "comment": "System created",
            "value": "true",
            "entity": {
              "sourceEntityType": 0,
              "name": "commserve-02",
              "id": 2,
              "type": "Server"
            }
          }
        ]
      },
      {
        "displayLabel": "bEnableOneWeekRetention",
        "type": "Boolean",
        "enabled": 1,
        "name": "bEnableOneWeekRetention",
        "category": "CommServDB.AdminConsole",
        "values": [
          {
            "comment": "System created",
            "value": "true",
            "entity": {
              "sourceEntityType": 0,
              "name": "commserve-02",
              "id": 2,
              "type": "Server"
            }
          }
        ]
      },
      "... 5 more"
    ]
  }
  ```

  </details>

## `get_added_global_settings` - GET /V4/AddedGlobalSettings

```python
cv.raw.additional_settings.get_added_global_settings()
```

**On the wire**

- `GET /V4/AddedGlobalSettings` -> **200** (0.17 s)

  <details><summary>Answer</summary>

  ```json
  {
    "globalSettings": [
      {
        "name": "FailedLoginAttemptLimit",
        "displayLabel": "Account lockout threshold",
        "value": "5",
        "comment": "",
        "type": "Integer",
        "category": "CommServDB.GxGlobalParam",
        "enabled": 1
      },
      {
        "name": "bDisableInfiniteRetention",
        "displayLabel": "bDisableInfiniteRetention",
        "value": "true",
        "comment": "System created",
        "type": "Boolean",
        "category": "CommServDB.AdminConsole",
        "enabled": 1
      },
      {
        "name": "bEnableOneWeekRetention",
        "displayLabel": "bEnableOneWeekRetention",
        "value": "true",
        "comment": "System created",
        "type": "Boolean",
        "category": "CommServDB.AdminConsole",
        "enabled": 1
      },
      "... 6 more"
    ]
  }
  ```

  </details>

## `get_global_settings` - GET /V4/GlobalSettings

```python
cv.raw.additional_settings.get_global_settings()
```

**On the wire**

- `GET /V4/GlobalSettings` -> **200** (1.92 s)

  <details><summary>Answer</summary>

  ```json
  {
    "globalSettings": [
      {
        "name": "<AppName>_FDSETSZ",
        "description": "Controls size of select mask for the application ",
        "subclient-01Value": " ",
        "type": "Integer",
        "isRestartRequired": false,
        "minValue": 0,
        "maxValue": -2147483648,
        "category": "Session"
      },
      {
        "name": "<ArrayManagementName>_DataIPORHostNameForMount",
        "description": "The IP address or hostname specified in the <ArrayManagementName>_DataIPORHostNameForMount is used to mount the cloned volume during the mount operation. If the array management entry has Remote Snap MediaAgent configured, then this additional setting should be present on the Remote Snap MediaAgent.",
        "acceptableValues": [
          "IP address"
        ],
        "subclient-01Value": "IP address",
        "type": "String",
        "isRestartRequired": false,
        "category": "iDataAgent"
      },
      {
        "name": "<cluster_name>StageFolder",
        "description": "Additional setting to set a path to the stage folder for transaction log backups in a clustered environment. The stage folder provided should be a shared path accessible by all the cluster computers.  If cluster name is \"abcsql\", then the key name becomes \"abcsqlStageFolder\". And its value should be a folder shared by all nodes in the cluster, like O:\\stageFolder.  Note that for each cluster, key ... (465 characters)",
        "acceptableValues": [
          "Path to a shared stage folder",
          "like O:\\StageFolder"
        ],
        "subclient-01Value": "",
        "type": "String",
        "isRestartRequired": true,
        "category": "MSSQLAgent"
      },
      "... 8424 more"
    ]
  }
  ```

  </details>

## `get_lookup_settings` - GET /V4/LookupSettings

```python
cv.raw.additional_settings.get_lookup_settings()
```

**On the wire**

- `GET /V4/LookupSettings` -> **200** (1.10 s)

  <details><summary>Answer</summary>

  ```json
  {
    "additionalSettings": [
      {
        "name": "<AppName>_FDSETSZ",
        "displayLabel": "<AppName>_FDSETSZ",
        "description": "Controls size of select mask for the application ",
        "subclient-01Value": " ",
        "type": "Integer",
        "isRestartRequired": false,
        "minValue": 0,
        "maxValue": -2147483648,
        "category": "Session"
      },
      {
        "name": "<ArrayManagementName>_DataIPORHostNameForMount",
        "displayLabel": "<ArrayManagementName>_DataIPORHostNameForMount",
        "description": "The IP address or hostname specified in the <ArrayManagementName>_DataIPORHostNameForMount is used to mount the cloned volume during the mount operation. If the array management entry has Remote Snap MediaAgent configured, then this additional setting should be present on the Remote Snap MediaAgent.",
        "acceptableValues": [
          "IP address"
        ],
        "subclient-01Value": "IP address",
        "type": "String",
        "isRestartRequired": false,
        "category": "iDataAgent"
      },
      {
        "name": "<cluster_name>StageFolder",
        "displayLabel": "<cluster_name>StageFolder",
        "description": "Additional setting to set a path to the stage folder for transaction log backups in a clustered environment. The stage folder provided should be a shared path accessible by all the cluster computers.  If cluster name is \"abcsql\", then the key name becomes \"abcsqlStageFolder\". And its value should be a folder shared by all nodes in the cluster, like O:\\stageFolder.  Note that for each cluster, key ... (465 characters)",
        "acceptableValues": [
          "Path to a shared stage folder",
          "like O:\\StageFolder"
        ],
        "subclient-01Value": "",
        "type": "String",
        "isRestartRequired": true,
        "category": "MSSQLAgent"
      },
      "... 8424 more"
    ]
  }
  ```

  </details>
