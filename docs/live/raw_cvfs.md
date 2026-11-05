# `cv.raw.cvfs`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:37 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_user_s3_access_key` - GET /V4/User/S3AccessKey

> **SKIPPED** on this run: Commvault answered: 403 - Get User access key not allowed.

```python
cv.raw.cvfs.get_user_s3_access_key()
```

**On the wire**

- `GET /V4/User/S3AccessKey` -> **403** (0.08 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorMessage": "Get User access key not allowed.",
    "errorCode": 9
  }
  ```

  </details>

## `get_cvfs_s3_bucket` - GET /V4/CVFS/S3Bucket/{id}

> **SKIPPED** on this run: Commvault answered: 400 - Invalid Plan name provided. Verify plan exists with this name and retry.

```python
cv.raw.cvfs.get_cvfs_s3_bucket('2')
```

**On the wire**

- `GET /V4/CVFS/S3Bucket/2` -> **400** (0.23 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorMessage": "Invalid Plan name provided. Verify plan exists with this name and retry.",
    "errorCode": 1
  }
  ```

  </details>

## `get_user_s3_access_key_by_id` - GET /V4/User/{id}/S3AccessKey

> **SKIPPED** on this run: Commvault answered: 403 - Get User access key not allowed.

```python
cv.raw.cvfs.get_user_s3_access_key_by_id('2')
```

**On the wire**

- `GET /V4/User/2/S3AccessKey` -> **403** (0.09 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorMessage": "Get User access key not allowed.",
    "errorCode": 9
  }
  ```

  </details>

## `list_cvfs_s3_bucket_clone` - GET /V4/CVFS/S3Bucket/{id}/Clone

> **SKIPPED** on this run: Commvault answered: 404 - Unable to fetch the clone details

```python
cv.raw.cvfs.list_cvfs_s3_bucket_clone('2')
```

**On the wire**

- `GET /V4/CVFS/S3Bucket/2/Clone` -> **404** (0.31 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorMessage": "Unable to fetch the clone details",
    "errorCode": 10
  }
  ```

  </details>

## `get_cvfs_s3_bucket_clone` - GET /V4/CVFS/S3Bucket/{id}/Clone/{cloneId}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.cvfs.get_cvfs_s3_bucket_clone(...)
```

**On the wire**

- `GET /V4/CVFS/S3Bucket/2/Clone` -> **404** (0.25 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorMessage": "Unable to fetch the clone details",
    "errorCode": 10
  }
  ```

  </details>
