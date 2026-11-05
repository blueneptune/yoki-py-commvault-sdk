# `cv.raw.tape_storage`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:37 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_storage_tape_locations` - GET /V4/Storage/Tape/Locations

```python
cv.raw.tape_storage.get_storage_tape_locations()
```

**On the wire**

- `GET /V4/Storage/Tape/Locations` -> **200** (0.27 s)

  <details><summary>Answer</summary>

  ```json
  {
    "locations": [
      {
        "id": 0,
        "name": "Not Available"
      }
    ]
  }
  ```

  </details>

## `get_vault_tracker_action` - GET /V4/VaultTrackerAction

```python
cv.raw.tape_storage.get_vault_tracker_action()
```

**On the wire**

- `GET /V4/VaultTrackerAction` -> **200** (0.29 s)

  <details><summary>Answer</summary>

  ```json
  {}
  ```

  </details>

## `get_vault_tracker_media` - GET /V4/VaultTracker/Media

> **SKIPPED** on this run: Commvault answered: 400 - Invalid Usage. User can list media either by actionId or by policyId or by containerId or by locationId.

```python
cv.raw.tape_storage.get_vault_tracker_media()
```

**On the wire**

- `GET /V4/VaultTracker/Media` -> **400** (0.07 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorMessage": "Invalid Usage. User can list media either by actionId or by policyId or by containerId or by locationId.",
    "errorCode": 1
  }
  ```

  </details>

## `get_vault_tracker_policies` - GET /V4/VaultTrackerPolicies

```python
cv.raw.tape_storage.get_vault_tracker_policies()
```

**On the wire**

- `GET /V4/VaultTrackerPolicies` -> **200** (0.17 s)

  <details><summary>Answer</summary>

  ```json
  {
    "error": {}
  }
  ```

  </details>

## `list_storage_tape` - GET /V4/Storage/Tape

```python
cv.raw.tape_storage.list_storage_tape()
```

**On the wire**

- `GET /V4/Storage/Tape` -> **200** (0.17 s)

  <details><summary>Answer</summary>

  ```json
  {
    "tapeStorage": []
  }
  ```

  </details>

## `get_library_media` - GET /V4/Library/{libraryId}/Media

> **SKIPPED** on this run: Commvault answered: 400

```python
cv.raw.tape_storage.get_library_media('1')
```

**On the wire**

- `GET /V4/Library/1/Media` -> **400** (0.06 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

## `get_library_slot` - GET /V4/Library/{libraryId}/Slot

> **SKIPPED** on this run: Commvault answered: 400

```python
cv.raw.tape_storage.get_library_slot('1')
```

**On the wire**

- `GET /V4/Library/1/Slot` -> **400** (0.07 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

## `get_storage_tape` - GET /V4/Storage/Tape/{libraryId}

```python
cv.raw.tape_storage.get_storage_tape('1')
```

**On the wire**

- `GET /V4/Storage/Tape/1` -> **200** (0.21 s)

  <details><summary>Answer</summary>

  ```json
  {
    "tapeLibSummary": {
      "id": 1,
      "name": "storage-pool-01",
      "manufacturer": "Disk",
      "database-03": "Disk",
      "firmwareRevision": "",
      "barcodeReader ": "",
      "serialNumber": ""
    },
    "status": {
      "enable": "false",
      "maintenanceMode": "false",
      "offlineReason": ""
    },
    "drives": [],
    "storagePoolList": [],
    "libraryType": 3
  }
  ```

  </details>

## `get_storage_tape_media` - GET /V4/Storage/Tape/{libraryId}/Media

```python
cv.raw.tape_storage.get_storage_tape_media('1')
```

**On the wire**

- `GET /V4/Storage/Tape/1/Media` -> **200** (0.21 s)

  <details><summary>Answer</summary>

  ```json
  {
    "tapeLibSummary": {
      "agedMedia": 0,
      "assignedMedia": 0,
      "cleaningMedia": 0,
      "totalMedia": 0,
      "spareMedia": 0
    },
    "vaultTrackerPolicies": []
  }
  ```

  </details>

## `get_storage_tape_media_type` - GET /V4/Storage/Tape/{libraryId}/MediaType

> **SKIPPED** on this run: Commvault answered: 500

```python
cv.raw.tape_storage.get_storage_tape_media_type('1')
```

**On the wire**

- `GET /V4/Storage/Tape/1/MediaType` -> **500** (0.64 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

## `get_storage_tape_spare_groups` - GET /V4/Storage/Tape/{libraryId}/SpareGroups

> **SKIPPED** on this run: Commvault answered: 400 - Invalid SpareGroupType

```python
cv.raw.tape_storage.get_storage_tape_spare_groups('1')
```

**On the wire**

- `GET /V4/Storage/Tape/1/SpareGroups` -> **400** (0.08 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorMessage": "Invalid SpareGroupType",
    "errorCode": 1
  }
  ```

  </details>

## `get_storage_tape_drive` - GET /V4/Storage/Tape/{libraryId}/Drive/{driveId}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.tape_storage.get_storage_tape_drive(...)
```

## `get_storage_tape_spare_group`

GET /V4/Storage/Tape/{libraryId}/SpareGroup/{spareGroupId}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.tape_storage.get_storage_tape_spare_group(...)
```
