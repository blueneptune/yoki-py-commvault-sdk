# `cv.raw.mssql_api`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:37 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_sql_instances` - GET /sql/instances

```python
cv.raw.mssql_api.get_sql_instances()
```

**On the wire**

- `GET /sql/instances` -> **200** (0.16 s)

  <details><summary>Answer</summary>

  ```json
  {
    "SqlInstance": [
      {
        "notReadyReason": "",
        "insName": "host-13",
        "sla": 0,
        "planName": "plan-01",
        "unprot": 0,
        "version": "16.0.4295.3",
        "attempt": 0,
        "insId": 6,
        "noDBs": 15,
        "cName": "host-13",
        "serverType": "DataBase Engine",
        "planId": 1,
        "protect": 15,
        "noSysDBs": 3,
        "cId": 15,
        "status": 1
      },
      {
        "notReadyReason": "Last backup job [1491] did not complete successfully for the instance with error: Another backup is running for client [host-14], iDataAgent [SQL Server], Instance [host-14], Subclient [subclient-01].<br/>Source: commserve-02, Process: JobManager",
        "insName": "host-14",
        "sla": 1,
        "planName": "plan-01",
        "unprot": 0,
        "version": "16.0.4295.3",
        "attempt": 0,
        "insId": 7,
        "noDBs": 13,
        "cName": "host-14",
        "serverType": "DataBase Engine",
        "planId": 1,
        "protect": 13,
        "noSysDBs": 3,
        "cId": 16,
        "status": 0
      }
    ],
    "response": {
      "total": 2,
      "errorMessage": "",
      "errorCode": 0,
      "end": 1
    }
  }
  ```

  </details>

## `get_client_sql_unconfigured_servers` - GET /Client/{clientId}/Sql/unconfiguredServers

> **SKIPPED** on this run: Commvault answered: 500 - Exception caught when job info retrieval with error [Exception of type 'CV.WebServer.Handlers.HandlerException' was thrown.].

```python
cv.raw.mssql_api.get_client_sql_unconfigured_servers('2')
```

**On the wire**

- `GET /Client/2/Sql/unconfiguredServers` -> **500** (0.22 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorMessage": "Exception caught when job info retrieval with error [Exception of type 'CV.WebServer.Handlers.HandlerException' was thrown.].",
    "errorCode": 0
  }
  ```

  </details>

## `get_client_sql_instance_unconfigured_databases`

GET /Client/{clientId}/Sql/Instance/{instanceId}/unconfiguredDatabases

> **SKIPPED** on this run: Commvault answered: 500

```python
cv.raw.mssql_api.get_client_sql_instance_unconfigured_databases('2', '1')
```

**On the wire**

- `GET /Client/2/Sql/Instance/1/unconfiguredDatabases` -> **500** (0.25 s)

  <details><summary>Answer</summary>

  ```json
  {
    "processinginstructioninfo": {
      "attributes": [
        {
          "name": "exitval",
          "value": "1"
        }
      ]
    },
    "genericerror": {
      "errorMessage": "Internal Error [150994988] in CVSession while communicating with remote host [Remote system [commserve-02*commserve-02*8400]. Communications Service returned error when executing remote library [sLNSQLClient61] function [sLPSQLMSG].].  [commserve-02]",
      "errorCode": 1
    }
  }
  ```

  </details>
