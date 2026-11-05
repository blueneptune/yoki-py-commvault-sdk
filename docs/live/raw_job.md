# `cv.raw.job`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 16:43 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_jobs_active` - GET /Jobs/active

```python
cv.raw.job.get_jobs_active()
```

**On the wire**

- `GET /Jobs/active` -> **200** (0.08 s)

  <details><summary>Answer</summary>

  ```json
  {
    "totalRecordsWithoutPaging": 1,
    "jobs": [
      {
        "jobDetail": {
          "generalInfo": {
            "systemState": "No"
          },
          "progressInfo": {
            "estimatedCompletionTime": 0
          }
        },
        "jobSummary": {
          "sizeOfApplication": 0,
          "vsaParentJobID": 0,
          "backupSetName": "backupset-01",
          "opType": 4,
          "isAnomalous": true,
          "totalFailedFolders": 0,
          "totalFailedFiles": 0,
          "numStreamsAllocated": 0,
          "jobAttributes": 2594073385365405696,
          "currentPhase": 3,
          "failureReason": "508,",
          "restartInterval": 1200,
          "redactedPendingReason": "Unable to reach Client/Access Node [host-14]. Please check Client and Access node configuration, confirm Access Node and Client are up and running then check network connectivity between Commserve and Access Node, and Access Node and Client.<br/>Source: commserve-02, Process: JobManager",
          "status": "Pending",
          "percentSavings": 0,
          "localizedOperationName": "Backup",
          "jobCategory": 1,
          "backupLevel": 4,
          "jobElapsedTime": 0,
          "jobStartTime": 1793653211,
          "currentPhaseName": "Differential Backup",
          "isPreemptable": 1,
          "retention": 1,
          "attemptStartTime": -1,
          "maxNumberOfStreams": 2,
          "appTypeName": "SQL Server",
          "sidbStoreName": "storage-pool-01_Databases_2",
          "displayState": 2,
          "operationNameLocaleMsgId": 0,
          "failureKBArticle": "cliver=0\rserver=16\rida=0\ropType=4\rphaseNum=0\rmessageId=318768235\rcustomMessageId=318768235;",
          "currentThroughput": 0,
          "subclientName": "subclient-01",
          "destClientName": "host-14",
          "commcellId": 2,
          "thresholdTime": 2280,
          "phasePercentagesList": "0,0,0,81,18,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
          "combinedPriority": 166,
          "alertColorLevel": 16,
          "currentPhaseType": 5632,
          "jobAttributesEx": 0,
          "workloadName": "SQL Server",
          "isVisible": true,
          "localizedStatus": "Pending",
          "totalNumOfFiles": 0,
          "transferSize": 0,
          "jobId": 1434,
          "retainedBy": 0,
          "lastUpdateTime": 0,
          "maxRestarts": 10,
          "statusColor": "redspan",
          "pendingReason": "Unable to reach Client/Access Node [host-14]. Please check Client and Access node configuration, confirm Access Node and Client are up and running then check network connectivity between Commserve and Access Node, and Access Node and Client.<br/>Source: commserve-02, Process: JobManager",
          "lastStateChangeTime": 3851982502927270314,
          "jobType": "Backup",
          "backupLevelName": "Differential",
          "totItemsToProcess": 0,
          "percentComplete": 0,
          "phaseTimingsList": "0,0,206,34,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
          "averageThroughput": 0,
          "localizedBackupLevelName": "Differential",
          "plan": {
            "planName": "plan-01",
            "_type_": 158,
            "planId": 1
          },
          "subTaskEntity": {
            "subtaskId": 41,
            "_type_": 68,
            "subtaskName": ""
          },
          "taskEntity": {
            "_type_": 69,
            "taskName": "plan-01",
            "taskId": 40
          },
          "destinationClient": {
            "clientName": "host-14",
            "displayName": "host-14",
            "_type_": 3,
            "clientId": 16
          },
          "mediaAgent": {
            "mediaAgentId": 2,
            "_type_": 11,
            "mediaAgentName": "commserve-02"
          },
          "alert": {
            "_type_": 64,
            "alertName": "",
            "alertId": 0
          },
          "subclient": {
            "clientName": "host-14",
            "instanceName": "host-14",
            "displayName": "host-14",
            "backupsetId": 30,
            "_type_": 7,
            "instanceId": 7,
            "workloadId": 12010,
            "subclientId": 44,
            "clientId": 16,
            "appName": "SQL Server",
            "_SubclType_": 0,
            "backupsetName": "backupset-01",
            "applicationId": 81,
            "subclientName": "subclient-01"
          },
          "company": {
            "_type_": 189,
            "companyId": 0,
            "companyName": "",
            "GUID": "95189D4E-4A7F-4CB3-969F-80D5871AC13F"
          },
          "storagePolicy": {
            "_type_": 17,
            "storagePolicyName": "plan-01",
            "storagePolicyId": 3
          },
          "userName": {
            "userName": "user-02",
            "userId": 1,
            "_type_": 13
          }
        }
      }
    ]
  }
  ```

  </details>

## `list_events` - GET /Events

```python
cv.raw.job.list_events()
```

**On the wire**

- `GET /Events` -> **200** (0.11 s)

  <details><summary>Answer</summary>

  ```json
  {
    "commservEvents": [
      {
        "severity": 0,
        "eventCode": "318767783",
        "jobId": 1504,
        "acknowledge": 0,
        "eventCodeString": "19:679",
        "subsystem": "JobManager",
        "description": "Disaster Recovery operation has completed. Media Used [mount-path-02].",
        "id": 2545,
        "timeSource": 1793894492,
        "type": 0,
        "clientEntity": {
          "clientName": "commserve-02",
          "displayName": "commserve-02",
          "clientId": 2
        }
      },
      {
        "severity": 0,
        "eventCode": "570425430",
        "jobId": 1504,
        "acknowledge": 0,
        "eventCodeString": "34:86",
        "subsystem": "storage-policy-01",
        "description": "storage-policy-01: Skipping upload to Commvault Cloud as CommCell is on evaluation license.",
        "id": 2544,
        "timeSource": 1793894432,
        "type": 0,
        "clientEntity": {
          "clientName": "commserve-02",
          "displayName": "commserve-02",
          "clientId": 2
        }
      },
      {
        "severity": 0,
        "eventCode": "570425346",
        "jobId": 1504,
        "acknowledge": 0,
        "eventCodeString": "34:2",
        "subsystem": "storage-policy-01",
        "description": "storage-policy-01: Full backup started for set [48].",
        "id": 2543,
        "timeSource": 1793894406,
        "type": 0,
        "clientEntity": {
          "clientName": "commserve-02",
          "displayName": "commserve-02",
          "clientId": 2
        }
      },
      "... 97 more"
    ]
  }
  ```

  </details>

## `list_job` - GET /Job

```python
cv.raw.job.list_job()
```

**On the wire**

- `GET /Job` -> **200** (1.06 s)

  <details><summary>Answer</summary>

  ```json
  {
    "totalRecordsWithoutPaging": 1090,
    "jobs": [
      {
        "jobSummary": {
          "sizeOfApplication": 23586357421,
          "vsaParentJobID": 0,
          "backupSetName": "",
          "opType": 36,
          "totalFailedFolders": 0,
          "distributedAppsClusterType": 0,
          "totalFailedFiles": 0,
          "isAged": false,
          "jobSubmitErrorCode": 0,
          "sizeOfMediaOnDisk": 0,
          "currentPhase": 0,
          "status": "Completed",
          "percentSavings": 0,
          "localizedOperationName": "Download Software",
          "estMediaSize": 0,
          "backupLevel": 0,
          "jobElapsedTime": -5445,
          "jobStartTime": 1791252215,
          "currentPhaseName": "",
          "isPreemptable": 0,
          "attemptStartTime": 0,
          "appTypeName": "",
          "currentThroughput": 0,
          "subclientName": "",
          "destClientName": "",
          "jobEndTime": 1791246770,
          "commcellId": 2,
          "alertColorLevel": 0,
          "isVisible": true,
          "localizedStatus": "Completed",
          "totalNumOfFiles": 7948,
          "jobId": 1,
          "lastUpdateTime": 1791246770,
          "statusColor": "black",
          "pendingReason": "",
          "errorType": 0,
          "description": "",
          "jobType": "Patch Download",
          "backupLevelName": "",
          "pendingReasonErrorCode": "",
          "percentComplete": 100,
          "averageThroughput": 0,
          "localizedBackupLevelName": "",
          "destinationDisplayClient": {
            "clientId": 0
          },
          "plan": {
            "planId": 0
          },
          "logStoragePolicy": {
            "storagePolicyId": 0
          },
          "destinationClient": {
            "clientName": "",
            "displayName": "",
            "clientId": 0
          },
          "dataSource": {
            "dataSourceId": 0
          },
          "subclient": {
            "clientName": "",
            "instanceName": "",
            "backupsetId": 0,
            "commCellName": "commserve-02",
            "instanceId": 0,
            "workloadId": 0,
            "subclientId": 0,
            "clientId": 0,
            "appName": "",
            "backupsetName": "",
            "applicationId": 0,
            "subclientName": ""
          },
          "company": {
            "companyId": 0,
            "companyName": ""
          },
          "storagePolicy": {
            "storagePolicyName": "",
            "storagePolicyId": 0
          },
          "userName": {
            "userName": "user-01",
            "userId": 2
          }
        }
      },
      {
        "jobSummary": {
          "sizeOfApplication": 0,
          "vsaParentJobID": 0,
          "backupSetName": "",
          "opType": 210,
          "totalFailedFolders": 0,
          "distributedAppsClusterType": 0,
          "totalFailedFiles": 0,
          "isAged": false,
          "jobSubmitErrorCode": 0,
          "sizeOfMediaOnDisk": 0,
          "currentPhase": 0,
          "status": "Completed",
          "percentSavings": 0,
          "localizedOperationName": "Software Sync",
          "estMediaSize": 0,
          "backupLevel": 0,
          "jobElapsedTime": 6,
          "jobStartTime": 1791246771,
          "currentPhaseName": "",
          "isPreemptable": 0,
          "attemptStartTime": 0,
          "appTypeName": "",
          "currentThroughput": 0,
          "subclientName": "",
          "destClientName": "",
          "jobEndTime": 1791246777,
          "commcellId": 2,
          "alertColorLevel": 0,
          "isVisible": true,
          "localizedStatus": "Completed",
          "totalNumOfFiles": 0,
          "jobId": 2,
          "lastUpdateTime": 1791246777,
          "statusColor": "black",
          "pendingReason": "",
          "errorType": 0,
          "description": "",
          "jobType": "Software Sync",
          "backupLevelName": "",
          "pendingReasonErrorCode": "",
          "percentComplete": 100,
          "averageThroughput": 0,
          "localizedBackupLevelName": "",
          "destinationDisplayClient": {
            "clientId": 0
          },
          "plan": {
            "planId": 0
          },
          "logStoragePolicy": {
            "storagePolicyId": 0
          },
          "destinationClient": {
            "clientName": "",
            "displayName": "",
            "clientId": 0
          },
          "dataSource": {
            "dataSourceId": 0
          },
          "subclient": {
            "clientName": "",
            "instanceName": "",
            "backupsetId": 0,
            "commCellName": "commserve-02",
            "instanceId": 0,
            "workloadId": 0,
            "subclientId": 0,
            "clientId": 0,
            "appName": "",
            "backupsetName": "",
            "applicationId": 0,
            "subclientName": ""
          },
          "company": {
            "companyId": 0,
            "companyName": ""
          },
          "storagePolicy": {
            "storagePolicyName": "",
            "storagePolicyId": 0
          },
          "userName": {
            "userName": "user-01",
            "userId": 2
          }
        }
      },
      {
        "jobSummary": {
          "sizeOfApplication": 27125,
          "vsaParentJobID": 0,
          "backupSetName": "backupset-01",
          "opType": 4,
          "totalFailedFolders": 0,
          "distributedAppsClusterType": 12022,
          "totalFailedFiles": 0,
          "workflowInputsXml": "",
          "jobAttributes": 1441151880758558720,
          "isAged": false,
          "jobSubmitErrorCode": 0,
          "sizeOfMediaOnDisk": 57453,
          "currentPhase": 0,
          "status": "Completed",
          "percentSavings": -111.808,
          "localizedOperationName": "Backup",
          "estMediaSize": 57453,
          "extRetentionFlags": 0,
          "backupLevel": 1,
          "jobElapsedTime": 90,
          "jobStartTime": 1791256740,
          "currentPhaseName": "",
          "isPreemptable": 0,
          "attemptStartTime": 0,
          "appTypeName": "Windows File System",
          "retainUntil": 1793848740,
          "currentThroughput": 0,
          "subclientName": "subclient-02",
          "destClientName": "commserve-02",
          "jobEndTime": 1791256840,
          "commcellId": 2,
          "alertColorLevel": 0,
          "jobAttributesEx": 0,
          "isVisible": true,
          "localizedStatus": "Completed",
          "totalNumOfFiles": 5,
          "jobId": 3,
          "lastUpdateTime": 1791256840,
          "statusColor": "black",
          "pendingReason": "",
          "errorType": 0,
          "description": "",
          "jobType": "Backup",
          "backupLevelName": "Full",
          "pendingReasonErrorCode": "",
          "percentComplete": 100,
          "averageThroughput": 0,
          "localizedBackupLevelName": "Full",
          "destinationDisplayClient": {
            "clientId": 0
          },
          "plan": {
            "planName": "plan-01",
            "planId": 1
          },
          "logStoragePolicy": {
            "storagePolicyName": "",
            "storagePolicyId": 0
          },
          "destinationClient": {
            "clientName": "commserve-02",
            "displayName": "commserve-02",
            "clientId": 2
          },
          "clientGroups": [
            {
              "_type_": 28,
              "clientGroupId": 1,
              "clientGroupName": "client-group-01"
            },
            {
              "_type_": 28,
              "clientGroupId": 3,
              "clientGroupName": "client-group-03"
            }
          ],
          "dataSource": {
            "dataSourceId": 0
          },
          "subclient": {
            "clientName": "commserve-02",
            "instanceName": "asset-01",
            "backupsetId": 3,
            "commCellName": "commserve-02",
            "instanceId": 1,
            "workloadId": 12022,
            "subclientId": 7,
            "clientId": 2,
            "appName": "Windows File System",
            "backupsetName": "backupset-01",
            "applicationId": 33,
            "subclientName": "subclient-02"
          },
          "company": {
            "companyId": 0,
            "companyName": ""
          },
          "storagePolicy": {
            "storagePolicyName": "plan-01",
            "storagePolicyId": 3
          },
          "userName": {
            "userName": "user-01",
            "userId": 2
          }
        }
      },
      "... 97 more"
    ]
  }
  ```

  </details>

## `list_jobs_history` - GET /Jobs/History

```python
cv.raw.job.list_jobs_history()
```

**On the wire**

- `GET /Jobs/History` -> **200** (0.08 s)

  <details><summary>Answer</summary>

  ```json
  {
    "totalRecordsWithoutPaging": 29,
    "hasNextPage": false,
    "jobs": [
      {
        "jobSummary": {
          "sizeOfApplication": 0,
          "vsaParentJobID": 0,
          "backupSetName": "",
          "opType": 106,
          "totalFailedFolders": 0,
          "distributedAppsClusterType": 0,
          "totalFailedFiles": 0,
          "totalSkippedObjects": 0,
          "isAged": false,
          "snapBkpCopyJobID": 0,
          "statusId": 1,
          "sizeOfMediaOnDisk": 0,
          "contentIndexed": false,
          "status": "Completed",
          "percentSavings": 0,
          "localizedOperationName": "DDB Verification",
          "estMediaSize": 0,
          "isReconcileBackup": false,
          "jobCategory": 3,
          "backupLevel": 6,
          "jobElapsedTime": 328,
          "jobStartTime": 1793811613,
          "retention": 0,
          "appTypeName": "",
          "extendedJobType": 0,
          "totalWriteTime": 0,
          "subclientName": "",
          "totalDataWriten": 0,
          "jobEndTime": 1793811941,
          "commcellId": 2,
          "compressionType": 0,
          "pruningStatus": 0,
          "isLaptop": false,
          "workloadName": "",
          "localizedStatus": "Completed",
          "totalNumOfFiles": 0,
          "jobId": 1475,
          "isAgedOrSoftDeleted": false,
          "pendingReason": "",
          "description": "",
          "isAdminJob": true,
          "isSystemState": false,
          "jobType": "DDB Verification",
          "backupLevelName": "",
          "isThreatAnalysisJob": false,
          "pendingReasonErrorCode": "",
          "percentComplete": 100,
          "averageThroughput": 0,
          "isSoftDeletedJob": false,
          "localizedBackupLevelName": "",
          "securityAssemblyEntity": {
            "clientGroupId": 0
          },
          "plan": {
            "planId": 0
          },
          "subTaskEntity": {
            "subtaskId": 18,
            "subtaskName": ""
          },
          "logStoragePolicy": {
            "storagePolicyId": 0
          },
          "taskEntity": {
            "taskName": "System Created DDB Verification schedule policy",
            "taskId": 17
          },
          "destinationClient": {
            "clientName": "",
            "displayName": "",
            "clientId": 0
          },
          "mediaAgent": {
            "mediaAgentId": 0
          },
          "replicationGroupEntity": {
            "replicationGroupId": 0
          },
          "runbookTemplate": {
            "runbookId": 0
          },
          "dataSource": {
            "dataSourceId": 0
          },
          "subclient": {
            "clientName": "",
            "instanceName": "",
            "displayName": "",
            "backupsetId": 0,
            "commCellName": "commserve-02",
            "instanceId": 0,
            "workloadId": 0,
            "subclientId": 0,
            "clientId": 0,
            "appName": "",
            "backupsetName": "",
            "applicationId": 0,
            "subclientName": ""
          },
          "company": {
            "companyId": 0,
            "companyName": "Commcell",
            "GUID": "95189D4E-4A7F-4CB3-969F-80D5871AC13F"
          },
          "storagePolicy": {
            "storagePolicyName": "storage-pool-01",
            "storagePolicyId": 2
          },
          "userName": {
            "userName": "user-group-01",
            "userId": 3
          }
        }
      },
      {
        "jobSummary": {
          "sizeOfApplication": 0,
          "vsaParentJobID": 0,
          "backupSetName": "",
          "opType": 106,
          "totalFailedFolders": 0,
          "distributedAppsClusterType": 0,
          "totalFailedFiles": 0,
          "totalSkippedObjects": 0,
          "isAged": false,
          "snapBkpCopyJobID": 0,
          "statusId": 1,
          "sizeOfMediaOnDisk": 0,
          "contentIndexed": false,
          "status": "Completed",
          "percentSavings": 0,
          "localizedOperationName": "DDB Verification",
          "estMediaSize": 0,
          "isReconcileBackup": false,
          "jobCategory": 3,
          "backupLevel": 6,
          "jobElapsedTime": 202,
          "jobStartTime": 1793811612,
          "retention": 0,
          "appTypeName": "",
          "extendedJobType": 0,
          "totalWriteTime": 0,
          "subclientName": "",
          "totalDataWriten": 0,
          "jobEndTime": 1793811814,
          "commcellId": 2,
          "compressionType": 0,
          "pruningStatus": 0,
          "isLaptop": false,
          "workloadName": "",
          "localizedStatus": "Completed",
          "totalNumOfFiles": 0,
          "jobId": 1476,
          "isAgedOrSoftDeleted": false,
          "pendingReason": "",
          "description": "",
          "isAdminJob": true,
          "isSystemState": false,
          "jobType": "DDB Verification",
          "backupLevelName": "",
          "isThreatAnalysisJob": false,
          "pendingReasonErrorCode": "",
          "percentComplete": 100,
          "averageThroughput": 0,
          "isSoftDeletedJob": false,
          "localizedBackupLevelName": "",
          "securityAssemblyEntity": {
            "clientGroupId": 0
          },
          "plan": {
            "planId": 0
          },
          "subTaskEntity": {
            "subtaskId": 18,
            "subtaskName": ""
          },
          "logStoragePolicy": {
            "storagePolicyId": 0
          },
          "taskEntity": {
            "taskName": "System Created DDB Verification schedule policy",
            "taskId": 17
          },
          "destinationClient": {
            "clientName": "",
            "displayName": "",
            "clientId": 0
          },
          "mediaAgent": {
            "mediaAgentId": 0
          },
          "replicationGroupEntity": {
            "replicationGroupId": 0
          },
          "runbookTemplate": {
            "runbookId": 0
          },
          "dataSource": {
            "dataSourceId": 0
          },
          "subclient": {
            "clientName": "",
            "instanceName": "",
            "displayName": "",
            "backupsetId": 0,
            "commCellName": "commserve-02",
            "instanceId": 0,
            "workloadId": 0,
            "subclientId": 0,
            "clientId": 0,
            "appName": "",
            "backupsetName": "",
            "applicationId": 0,
            "subclientName": ""
          },
          "company": {
            "companyId": 0,
            "companyName": "Commcell",
            "GUID": "95189D4E-4A7F-4CB3-969F-80D5871AC13F"
          },
          "storagePolicy": {
            "storagePolicyName": "storage-pool-01",
            "storagePolicyId": 2
          },
          "userName": {
            "userName": "user-group-01",
            "userId": 3
          }
        }
      },
      {
        "jobSummary": {
          "sizeOfApplication": 0,
          "vsaParentJobID": 0,
          "backupSetName": "",
          "opType": 10,
          "totalFailedFolders": 0,
          "distributedAppsClusterType": 0,
          "totalFailedFiles": 0,
          "totalSkippedObjects": 0,
          "isAged": false,
          "snapBkpCopyJobID": 0,
          "statusId": 1,
          "sizeOfMediaOnDisk": 0,
          "contentIndexed": false,
          "status": "Completed",
          "percentSavings": 0,
          "localizedOperationName": "Data Aging",
          "estMediaSize": 0,
          "isReconcileBackup": false,
          "jobCategory": 3,
          "backupLevel": 0,
          "jobElapsedTime": 36,
          "jobStartTime": 1793815205,
          "retention": 0,
          "appTypeName": "",
          "extendedJobType": 0,
          "totalWriteTime": 0,
          "subclientName": "",
          "totalDataWriten": 0,
          "jobEndTime": 1793815241,
          "commcellId": 2,
          "compressionType": 0,
          "pruningStatus": 0,
          "isLaptop": false,
          "workloadName": "",
          "localizedStatus": "Completed",
          "totalNumOfFiles": 0,
          "jobId": 1477,
          "isAgedOrSoftDeleted": false,
          "pendingReason": "",
          "description": "",
          "isAdminJob": true,
          "isSystemState": false,
          "jobType": "Prune",
          "backupLevelName": "",
          "isThreatAnalysisJob": false,
          "pendingReasonErrorCode": "",
          "percentComplete": 100,
          "averageThroughput": 0,
          "isSoftDeletedJob": false,
          "localizedBackupLevelName": "",
          "securityAssemblyEntity": {
            "clientGroupId": 0
          },
          "plan": {
            "planId": 0
          },
          "subTaskEntity": {
            "subtaskId": 5,
            "subtaskName": "Data Aging"
          },
          "logStoragePolicy": {
            "storagePolicyId": 0
          },
          "taskEntity": {
            "taskName": "",
            "taskId": 4
          },
          "destinationClient": {
            "clientName": "",
            "displayName": "",
            "clientId": 0
          },
          "mediaAgent": {
            "mediaAgentId": 0
          },
          "replicationGroupEntity": {
            "replicationGroupId": 0
          },
          "runbookTemplate": {
            "runbookId": 0
          },
          "dataSource": {
            "dataSourceId": 0
          },
          "subclient": {
            "clientName": "",
            "instanceName": "",
            "displayName": "",
            "backupsetId": 0,
            "commCellName": "commserve-02",
            "instanceId": 0,
            "workloadId": 0,
            "subclientId": 0,
            "clientId": 0,
            "appName": "",
            "backupsetName": "",
            "applicationId": 0,
            "subclientName": ""
          },
          "company": {
            "companyId": 0,
            "companyName": "Commcell",
            "GUID": "95189D4E-4A7F-4CB3-969F-80D5871AC13F"
          },
          "storagePolicy": {
            "storagePolicyName": "",
            "storagePolicyId": 1
          },
          "userName": {
            "userName": "user-01",
            "userId": 2
          }
        }
      },
      "... 26 more"
    ]
  }
  ```

  </details>

## `get_event` - GET /Events/{eventId}

```python
cv.raw.job.get_event('1504')
```

**On the wire**

- `GET /Events/1504` -> **200** (0.07 s)

  <details><summary>Answer</summary>

  ```json
  {
    "commservEvents": [
      {
        "severity": 0,
        "eventCode": "1409287036",
        "jobId": 0,
        "acknowledge": 0,
        "eventCodeString": "84:892",
        "subsystem": "GuiAudit",
        "description": "DR Backup",
        "id": 1504,
        "timeSource": 1792422014,
        "type": 2,
        "clientEntity": {
          "clientName": "",
          "displayName": "",
          "clientId": 0
        }
      }
    ]
  }
  ```

  </details>

## `get_job` - GET /Job/{jobId}

```python
cv.raw.job.get_job('1')
```

**On the wire**

- `GET /Job/1` -> **200** (0.07 s)

  <details><summary>Answer</summary>

  ```json
  {
    "totalRecordsWithoutPaging": 1,
    "hasNextPage": false,
    "jobs": [
      {
        "jobSummary": {
          "sizeOfApplication": 23586357421,
          "vsaParentJobID": 0,
          "backupSetName": "",
          "opType": 36,
          "totalFailedFolders": 0,
          "distributedAppsClusterType": 0,
          "totalFailedFiles": 0,
          "totalSkippedObjects": 0,
          "isAged": false,
          "snapBkpCopyJobID": 0,
          "statusId": 1,
          "sizeOfMediaOnDisk": 0,
          "contentIndexed": false,
          "status": "Completed",
          "percentSavings": 0,
          "localizedOperationName": "Download Software",
          "estMediaSize": 0,
          "isReconcileBackup": false,
          "jobCategory": 3,
          "backupLevel": 0,
          "jobElapsedTime": -5445,
          "jobStartTime": 1791252215,
          "retention": 0,
          "appTypeName": "",
          "extendedJobType": 0,
          "totalWriteTime": 0,
          "subclientName": "",
          "totalDataWriten": 0,
          "jobEndTime": 1791246770,
          "commcellId": 2,
          "compressionType": 0,
          "pruningStatus": 0,
          "isLaptop": false,
          "workloadName": "",
          "localizedStatus": "Completed",
          "totalNumOfFiles": 7948,
          "jobId": 1,
          "isAgedOrSoftDeleted": false,
          "pendingReason": "",
          "description": "",
          "isAdminJob": true,
          "isSystemState": false,
          "jobType": "Patch Download",
          "backupLevelName": "",
          "isThreatAnalysisJob": false,
          "pendingReasonErrorCode": "",
          "percentComplete": 100,
          "averageThroughput": 0,
          "isSoftDeletedJob": false,
          "localizedBackupLevelName": "",
          "securityAssemblyEntity": {
            "clientGroupId": 0
          },
          "plan": {
            "planId": 0
          },
          "subTaskEntity": {
            "subtaskId": 43
          },
          "logStoragePolicy": {
            "storagePolicyId": 0
          },
          "taskEntity": {},
          "destinationClient": {
            "clientName": "",
            "displayName": "",
            "clientId": 0
          },
          "mediaAgent": {
            "mediaAgentId": 0
          },
          "replicationGroupEntity": {
            "replicationGroupId": 0
          },
          "runbookTemplate": {
            "runbookId": 0
          },
          "dataSource": {
            "dataSourceId": 0
          },
          "subclient": {
            "clientName": "",
            "instanceName": "",
            "displayName": "",
            "backupsetId": 0,
            "commCellName": "commserve-02",
            "instanceId": 0,
            "workloadId": 0,
            "subclientId": 0,
            "clientId": 0,
            "appName": "",
            "backupsetName": "",
            "applicationId": 0,
            "subclientName": ""
          },
          "company": {
            "companyId": 0,
            "companyName": "Commcell",
            "GUID": "95189D4E-4A7F-4CB3-969F-80D5871AC13F"
          },
          "storagePolicy": {
            "storagePolicyName": "",
            "storagePolicyId": 0
          },
          "userName": {
            "userName": "user-01",
            "userId": 2
          }
        }
      }
    ]
  }
  ```

  </details>

## `get_job_advanced_details` - GET /Job/{jobId}/AdvancedDetails

> **SKIPPED** on this run: Commvault answered: 400

```python
cv.raw.job.get_job_advanced_details('1')
```

**On the wire**

- `GET /Job/1/AdvancedDetails` -> **400** (0.06 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

## `get_job_failed_items` - GET /Job/{jobId}/FailedItems

> **SKIPPED** on this run: Commvault answered: 500 - View failed items operation failed.

```python
cv.raw.job.get_job_failed_items('1')
```

**On the wire**

- `GET /Job/1/FailedItems` -> **500** (0.14 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorMessage": "View failed items operation failed.",
    "errorCode": 1
  }
  ```

  </details>

## `get_job_task_details` - GET /Job/{jobId}/TaskDetails

> **SKIPPED** on this run: Commvault answered: error 587204882: Unable to resubmit job as job is older than [7] days.

```python
cv.raw.job.get_job_task_details('1')
```

**On the wire**

- `GET /Job/1/TaskDetails` -> **200** (0.37 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorMessage": "Unable to resubmit job as job is older than [7] days.",
    "errorCode": 587204882
  }
  ```

  </details>

## `get_stream_job_logs` - GET /Stream/Job/{jobId}/Logs

> **SKIPPED** on this run: not swept: starts work or returns a file

```python
cv.raw.job.get_stream_job_logs(...)
```
