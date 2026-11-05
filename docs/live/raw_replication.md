# `cv.raw.replication`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:37 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_replications_groups` - GET /Replications/Groups

```python
cv.raw.replication.get_replications_groups()
```

**On the wire**

- `GET /Replications/Groups` -> **200** (0.09 s)

  <details><summary>Answer</summary>

  ```json
  {}
  ```

  </details>

## `get_replications_monitors_streaming` - GET /V2/Replications/Monitors/streaming

```python
cv.raw.replication.get_replications_monitors_streaming()
```

**On the wire**

- `GET /V2/Replications/Monitors/streaming` -> **200** (0.14 s)

  <details><summary>Answer</summary>

  ```json
  {}
  ```

  </details>

## `list_replications_monitors_streaming` - GET /Replications/Monitors/streaming

```python
cv.raw.replication.list_replications_monitors_streaming()
```

**On the wire**

- `GET /Replications/Monitors/streaming` -> **200** (0.10 s)

  <details><summary>Answer</summary>

  ```json
  {}
  ```

  </details>

## `list_vm_allocation_policy` - GET /VMAllocationPolicy

```python
cv.raw.replication.list_vm_allocation_policy()
```

**On the wire**

- `GET /VMAllocationPolicy` -> **200** (0.12 s)

  <details><summary>Answer</summary>

  ```json
  {}
  ```

  </details>

## `get_task_details` - GET /Task/{taskId}/Details

```python
cv.raw.replication.get_task_details('40')
```

**On the wire**

- `GET /Task/40/Details` -> **200** (0.15 s)

  <details><summary>Answer</summary>

  ```json
  {
    "taskInfo": {
      "associations": [
        {
          "planName": "plan-01",
          "srmReportSet": 0,
          "srmTemplateId": 0,
          "subclientId": 0,
          "storagePolicyId": 0,
          "copyId": 0,
          "clientId": 0,
          "srmTemplateName": "",
          "planId": 1,
          "clientGroupId": 0,
          "applicationId": 0,
          "backupsetId": 0,
          "instanceId": 0,
          "sidbStoreId": 0,
          "agentlessPolicyId": 0,
          "mediaAgentId": 0,
          "workflowId": 0,
          "_type_": 158,
          "trackingPolicyId": 0,
          "flags": {
            "exclude": false
          }
        }
      ],
      "task": {
        "isDestinationHostedclient-group-01": false,
        "description": "Schedule policy created automatically for ''plan-01'' plan.",
        "isRecoveryGroupOwner": false,
        "ownerId": 1,
        "runUserId": 1,
        "taskType": 4,
        "ownerName": "user-38",
        "planId": 1,
        "alertId": 0,
        "GUID": "ba95131b-3662-455c-807a-b4ce344f03f1",
        "policyType": 0,
        "associatedObjects": 16,
        "taskName": "plan-01",
        "taskId": 40,
        "securityAssociations": {
          "ownerAssociations": {},
          "tagWithCompany": {
            "providerId": 0,
            "providerDomainName": "Commcell"
          }
        },
        "originalCC": {
          "commCellId": 2
        },
        "taskSecurity": {
          "associatedUserGroups": [
            {
              "userGroupId": 1,
              "_type_": 15,
              "userGroupName": "user-group-01"
            }
          ],
          "advancedPrivacySettings": {
            "authType": 1,
            "passkeySettings": {
              "enableAuthorizeForRestore": false,
              "expirationTime": {
                "time": 0
              }
            }
          },
          "ownerCapabilities": {}
        },
        "createAs": {
          "user": {
            "user": {
              "userName": "user-02",
              "userId": 1
            }
          }
        },
        "taskFlags": {
          "isEdgeDrive": false,
          "isEZOperation": false,
          "forDDB": false,
          "isPlanAssociated": true,
          "uninstalled": false,
          "isServerPlanAssociated": true,
          "isSystem": false,
          "isIndexBackup": false,
          "disabled": false,
          "isEdiscovery": false,
          "isGCMPolicy": false
        },
        "task": {
          "taskName": "plan-01",
          "taskId": 40
        }
      },
      "appGroup": {},
      "subTasks": [
        {
          "relativeTime": 30163,
          "nextScheduleTime": 1793934000,
          "subTask": {
            "subTaskOrder": 0,
            "subTaskName": "",
            "subTaskType": 2,
            "flags": 0,
            "operationType": 2,
            "subTaskId": 41,
            "subTask": {
              "subtaskId": 41,
              "subtaskName": ""
            }
          },
          "pattern": {
            "active_end_occurence": 0,
            "freq_subday_interval": 0,
            "freq_type": 4,
            "patternId": 27,
            "flags": 0,
            "description": "Every day at 9:00 PM Starting Jan  1 1970  ",
            "active_end_time": 0,
            "active_start_time_window": 0,
            "active_end_date": 0,
            "skipOccurence": 0,
            "skipDayNumber": 0,
            "active_start_time": 75600,
            "freq_restart_interval": 0,
            "active_start_date": 1791158400,
            "freq_interval": 1,
            "freq_relative_interval": 0,
            "name": "",
            "freq_recurrence_factor": 1,
            "calendar": {
              "calendarName": "Standard",
              "calendarId": 1
            },
            "timeZone": {
              "TimeZoneID": 1001,
              "TimeZoneName": "Client Time Zone"
            }
          },
          "options": {
            "backupOpts": {
              "bkpLatestVersion": true,
              "collectMetaInfo": false,
              "incrementalDataWithLogs": true,
              "backupLevel": 2,
              "incLevel": 1,
              "runIncrementalBackup": false,
              "doNotTruncateLog": false,
              "cdrOptions": {
                "incremental": true,
                "dataVerificationOnly": false,
                "full": false
              },
              "dataOpt": {
                "stopWinService": true,
                "stopDhcpService": true,
                "useCatalogServer": true,
                "optimizedBackup": true,
                "followMountPoints": true,
                "bkpFilesProctedByFS": true,
                "granularrecovery": true,
                "verifySynthFull": true
              },
              "vaultTrackerOpt": {
                "mediaStatus": {
                  "bad": true,
                  "overwriteProtected": true,
                  "full": true
                }
              },
              "mediaOpt": {
                "numberofDays": 30,
                "retentionJobType": 2,
                "waitForInlineBackupResources": true,
                "allowOtherSchedulesToUseMediaSet": true
              }
            },
            "commonOpts": {
              "useJobStartTimeForContinuousSchedule": true,
              "jobRetryOpts": {
                "runningTime": {
                  "totalRunningTime": 3600
                }
              }
            }
          }
        },
        {
          "subTask": {
            "subTaskOrder": 0,
            "subTaskName": "Synthetic Fulls",
            "subTaskType": 2,
            "flags": 0,
            "operationType": 2,
            "subTaskId": 42,
            "subTask": {
              "subtaskId": 42,
              "subtaskName": "Synthetic Fulls"
            }
          },
          "pattern": {
            "active_end_occurence": 0,
            "freq_subday_interval": 0,
            "freq_type": 1024,
            "patternId": 28,
            "flags": 0,
            "description": "Based on automatic schedule settings",
            "active_end_time": 0,
            "active_start_time_window": 0,
            "active_end_date": 0,
            "skipOccurence": 0,
            "skipDayNumber": 0,
            "active_start_time": 0,
            "freq_restart_interval": 0,
            "active_start_date": 1791158400,
            "freq_interval": 0,
            "freq_relative_interval": 0,
            "name": "",
            "freq_recurrence_factor": 0,
            "calendar": {
              "calendarName": "Standard",
              "calendarId": 1
            },
            "timeZone": {
              "TimeZoneID": 1000,
              "TimeZoneName": "CommServe Time Zone"
            }
          },
          "options": {
            "backupOpts": {
              "truncateLogsOnSource": false,
              "backupLevel": 4,
              "incLevel": 0,
              "runIncrementalBackup": false,
              "doNotTruncateLog": false,
              "vsaBackupOptions": {
                "backupFailedVMsOnly": false
              },
              "dataOpt": {
                "useCatalogServer": true,
                "followMountPoints": true,
                "useMultiStream": true,
                "useMaximumStreams": true,
                "enforceTransactionLogUsage": false,
                "skipConsistencyCheck": false,
                "maxNumberOfStreams": 1,
                "createNewIndex": true,
                "daysBetweenSyntheticBackup": 90,
                "autoCopy": true
              }
            },
            "commonOpts": {
              "automaticSchedulePattern": {
                "maxBackupInterval": 72,
                "minBackupIntervalMinutes": 15,
                "minSyncIntervalMinutes": 2,
                "newOrModifiedFile": {
                  "enabled": true
                }
              }
            }
          }
        }
      ]
    }
  }
  ```

  </details>
