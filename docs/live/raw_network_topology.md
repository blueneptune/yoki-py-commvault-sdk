# `cv.raw.network_topology`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:37 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_comm_serv_data_interface_pairs` - GET /CommServ/DataInterfacePairs

```python
cv.raw.network_topology.get_comm_serv_data_interface_pairs()
```

**On the wire**

- `GET /CommServ/DataInterfacePairs` -> **200** (0.12 s)

  <details><summary>Answer</summary>

  ```json
  {}
  ```

  </details>

## `get_comm_serv_data_interface_pairs_host_interfaces`

GET /CommServ/DataInterfacePairs/HostInterfaces

> **SKIPPED** on this run: Commvault answered: 400

```python
cv.raw.network_topology.get_comm_serv_data_interface_pairs_host_interfaces()
```

**On the wire**

- `GET /CommServ/DataInterfacePairs/HostInterfaces` -> **400** (0.06 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

## `get_commserv_data_interface_pairs` - GET /v2/Commserv/DataInterfacePairs

> **SKIPPED** on this run: Commvault answered: 400 - Please provide either source ClientId or ClientGroupId

```python
cv.raw.network_topology.get_commserv_data_interface_pairs()
```

**On the wire**

- `GET /v2/Commserv/DataInterfacePairs` -> **400** (0.08 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorMessage": "Please provide either source ClientId or ClientGroupId",
    "errorCode": 87
  }
  ```

  </details>

## `list_firewall_topology` - GET /FirewallTopology

```python
cv.raw.network_topology.list_firewall_topology()
```

**On the wire**

- `GET /FirewallTopology` -> **200** (0.25 s)

  <details><summary>Answer</summary>

  ```json
  {
    "error": {
      "errorCode": 0
    }
  }
  ```

  </details>

## `get_firewall_summary` - GET /FirewallSummary/{clientId}

```python
cv.raw.network_topology.get_firewall_summary('2')
```

**On the wire**

- `GET /FirewallSummary/2` -> **200** (0.82 s)

  <details><summary>Answer</summary>

  ```
  No Network Configuration Found
  ```

  </details>

## `get_firewall_topology` - GET /FirewallTopology/{topologyId}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.network_topology.get_firewall_topology(...)
```

## `get_network_topology` - GET /V4/NetworkTopology/{topologyId}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.network_topology.get_network_topology(...)
```
