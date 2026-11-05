# `cv.raw.kubernetes`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 16:43 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `list_kubernetes_application` - GET /V5/Kubernetes/Application

```python
cv.raw.kubernetes.list_kubernetes_application()
```

**On the wire**

- `GET /V5/Kubernetes/Application` -> **200** (0.13 s)

  <details><summary>Answer</summary>

  ```json
  {
    "applicationCount": 0,
    "applications": []
  }
  ```

  </details>

## `list_kubernetes_application_group` - GET /V5/Kubernetes/ApplicationGroup

```python
cv.raw.kubernetes.list_kubernetes_application_group()
```

**On the wire**

- `GET /V5/Kubernetes/ApplicationGroup` -> **200** (0.16 s)

  <details><summary>Answer</summary>

  ```json
  {
    "applicationGroupCount": 0,
    "applicationGroups": []
  }
  ```

  </details>

## `list_kubernetes_cluster` - GET /V5/Kubernetes/Cluster

```python
cv.raw.kubernetes.list_kubernetes_cluster()
```

**On the wire**

- `GET /V5/Kubernetes/Cluster` -> **200** (0.13 s)

  <details><summary>Answer</summary>

  ```json
  {
    "clusterCount": 0,
    "clusters": []
  }
  ```

  </details>

## `get_kubernetes_application` - GET /V5/Kubernetes/Application/{appGUID}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.kubernetes.get_kubernetes_application(...)
```

## `get_kubernetes_application_group`

GET /V5/Kubernetes/ApplicationGroup/{applicationGroupId}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.kubernetes.get_kubernetes_application_group(...)
```

## `get_kubernetes_cluster` - GET /V5/Kubernetes/Cluster/{clusterId}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.kubernetes.get_kubernetes_cluster(...)
```

## `get_kubernetes_cluster_content_namespace`

GET /V5/Kubernetes/Cluster/{clusterId}/Content/Namespace

> **SKIPPED** on this run: not swept: starts work or returns a file

```python
cv.raw.kubernetes.get_kubernetes_cluster_content_namespace(...)
```

## `get_kubernetes_cluster_content_storage_class`

GET /V5/Kubernetes/Cluster/{clusterId}/Content/StorageClass

> **SKIPPED** on this run: not swept: starts work or returns a file

```python
cv.raw.kubernetes.get_kubernetes_cluster_content_storage_class(...)
```

## `list_kubernete_modifier` - GET /V4/Kubernetes/{clusterId}/Modifier

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.kubernetes.list_kubernete_modifier(...)
```

## `list_kubernetes_application_group_browse_application`

GET /V5/Kubernetes/ApplicationGroup/{applicationGroupId}/Browse/Application

> **SKIPPED** on this run: not swept: starts work or returns a file

```python
cv.raw.kubernetes.list_kubernetes_application_group_browse_application(...)
```

## `list_kubernetes_application_group_browse_namespace`

GET /V5/Kubernetes/ApplicationGroup/{applicationGroupId}/Browse/Namespace

> **SKIPPED** on this run: not swept: starts work or returns a file

```python
cv.raw.kubernetes.list_kubernetes_application_group_browse_namespace(...)
```

## `get_kubernete_modifier` - GET /V4/Kubernetes/{clusterId}/Modifier/{ModifierName}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.kubernetes.get_kubernete_modifier(...)
```

## `get_kubernetes_cluster_content_namespace_applications`

GET /V5/Kubernetes/Cluster/{clusterId}/Content/Namespace/{nameSpace}/Applications

> **SKIPPED** on this run: not swept: starts work or returns a file

```python
cv.raw.kubernetes.get_kubernetes_cluster_content_namespace_applications(...)
```

## `get_kubernetes_cluster_content_namespace_labels`

GET /V5/Kubernetes/Cluster/{clusterId}/Content/Namespace/{nameSpace}/Labels

> **SKIPPED** on this run: not swept: starts work or returns a file

```python
cv.raw.kubernetes.get_kubernetes_cluster_content_namespace_labels(...)
```

## `get_kubernetes_cluster_content_namespace_volumes`

GET /V5/Kubernetes/Cluster/{clusterId}/Content/Namespace/{nameSpace}/Volumes

> **SKIPPED** on this run: not swept: starts work or returns a file

```python
cv.raw.kubernetes.get_kubernetes_cluster_content_namespace_volumes(...)
```
