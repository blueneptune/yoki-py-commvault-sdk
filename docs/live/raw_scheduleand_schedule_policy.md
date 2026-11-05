# `cv.raw.scheduleand_schedule_policy`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:50 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `list_schedule_policy` - GET /SchedulePolicy

```python
cv.raw.scheduleand_schedule_policy.list_schedule_policy()
```

**On the wire**

- `GET /SchedulePolicy` -> **200** (0.69 s)

  <details><summary>Answer</summary>

  ```json
  {
    "taskDetail": [
      {
        "task": {
          "description": "System created schedule policy for All Agent Types",
          "ownerId": 2,
          "runUserId": 2,
          "taskType": 4,
          "ownerName": "user-01",
          "planId": 0,
          "alertId": 0,
          "GUID": "69173BC2-9642-4565-A875-B8D77DC11858",
          "policyType": 0,
          "associatedObjects": 0,
          "taskName": "System Created (All  Agent Types)",
          "taskId": 2,
          "originalCC": {
            "commCellId": 2
          },
          "taskFlags": {
            "isEdgeDrive": false,
            "isEZOperation": false,
            "forDDB": false,
            "isPlanAssociated": false,
            "uninstalled": false,
            "isServerPlanAssociated": false,
            "isSystem": true,
            "isIndexBackup": false,
            "disabled": false,
            "isEdiscovery": false
          },
          "task": {
            "taskName": "System Created (All  Agent Types)",
            "taskId": 2
          }
        },
        "appGroup": {}
      },
      {
        "task": {
          "description": "",
          "ownerId": 2,
          "runUserId": 2,
          "taskType": 4,
          "ownerName": "user-01",
          "planId": 0,
          "alertId": 0,
          "GUID": "1D75891D-695D-4DAA-AD8F-235477F8BD9E",
          "policyType": 1,
          "associatedObjects": 0,
          "taskName": "System Created Autocopy schedule",
          "taskId": 9,
          "originalCC": {
            "commCellId": 2
          },
          "taskFlags": {
            "isEdgeDrive": false,
            "isEZOperation": false,
            "forDDB": false,
            "isPlanAssociated": false,
            "uninstalled": false,
            "isServerPlanAssociated": false,
            "isSystem": true,
            "isIndexBackup": false,
            "disabled": false,
            "isEdiscovery": false
          },
          "task": {
            "taskName": "System Created Autocopy schedule",
            "taskId": 9
          }
        },
        "appGroup": {}
      },
      {
        "task": {
          "description": "System created schedule policy for DDB subclients",
          "ownerId": 2,
          "runUserId": 2,
          "taskType": 4,
          "ownerName": "user-01",
          "planId": 0,
          "alertId": 0,
          "GUID": "EFDD89C1-08F5-4F20-AD73-C0CC16E3B14F",
          "policyType": 0,
          "associatedObjects": 1,
          "taskName": "System Created for DDB subclients",
          "taskId": 10,
          "originalCC": {
            "commCellId": 2
          },
          "taskFlags": {
            "isEdgeDrive": false,
            "isEZOperation": false,
            "forDDB": true,
            "isPlanAssociated": false,
            "uninstalled": false,
            "isServerPlanAssociated": false,
            "isSystem": true,
            "isIndexBackup": false,
            "disabled": false,
            "isEdiscovery": false
          },
          "task": {
            "taskName": "System Created for DDB subclients",
            "taskId": 10
          }
        },
        "appGroup": {}
      },
      "... 13 more"
    ]
  }
  ```

  </details>

## `list_schedules` - GET /Schedules

```python
cv.raw.scheduleand_schedule_policy.list_schedules()
```

**On the wire**

- `GET /Schedules` -> **200** (1.39 s)

  <details><summary>Answer</summary>

  ```json
  {
    "taskDetail": [
      {
        "task": {
          "description": "System created schedule policy for All Agent Types",
          "ownerId": 2,
          "runUserId": 2,
          "taskType": 4,
          "ownerName": "user-01",
          "planId": 0,
          "alertId": 0,
          "GUID": "69173BC2-9642-4565-A875-B8D77DC11858",
          "policyType": 0,
          "taskName": "System Created (All  Agent Types)",
          "taskId": 2,
          "originalCC": {
            "commCellId": 2
          },
          "taskFlags": {
            "isEdgeDrive": false,
            "isEZOperation": false,
            "isPlanAssociated": false,
            "uninstalled": false,
            "isServerPlanAssociated": false,
            "isSystem": true,
            "isIndexBackup": false,
            "disabled": false,
            "isEdiscovery": false
          },
          "task": {
            "taskName": "System Created (All  Agent Types)",
            "taskId": 2
          }
        },
        "appGroup": {},
        "subTasks": [
          {
            "relativeTime": 18599,
            "nextScheduleTime": 1793923200,
            "subTask": {
              "subTaskOrder": 0,
              "subTaskName": "",
              "subTaskType": 2,
              "flags": 1,
              "operationType": 2,
              "subTaskId": 2
            },
            "pattern": {
              "active_end_occurence": 0,
              "freq_subday_interval": 0,
              "freq_type": 8,
              "patternId": 1,
              "flags": 0,
              "description": "",
              "active_end_time": 0,
              "active_start_time_window": 0,
              "active_end_date": 0,
              "skipOccurence": 0,
              "skipDayNumber": 0,
              "active_start_time": 64800,
              "freq_restart_interval": 0,
              "active_start_date": 1437091200,
              "freq_interval": 30,
              "freq_relative_interval": 0,
              "name": "",
              "freq_recurrence_factor": 1,
              "calendar": {
                "calendarId": 1
              },
              "timeZone": {
                "TimeZoneID": 1000,
                "TimeZoneName": "CommServe Time Zone"
              }
            },
            "options": {
              "backupOpts": {
                "sybaseSkipFullafterLogBkp": false,
                "bkpLatestVersion": false,
                "collectMetaInfo": true,
                "backupLevel": 2,
                "incLevel": 1,
                "runIncrementalBackup": true,
                "runSILOBackup": false,
                "doNotTruncateLog": false,
                "dataOpt": {
                  "followMountPoints": true,
                  "startLogBackupAfterSuccessfullBackup": false,
                  "createNewIndex": false
                },
                "oracleOptions": {
                  "level": 1,
                  "cumulative": false,
                  "deleteArchLogOptions": {
                    "backupArchiveLogCriteria": 0
                  },
                  "backupArchLogOptions": {
                    "backupArchiveLog": true,
                    "backupArchiveLogCriteria": 7,
                    "startLSN": 1,
                    "endLSN": 1
                  }
                }
              }
            }
          },
          {
            "relativeTime": 104999,
            "nextScheduleTime": 1794009600,
            "subTask": {
              "subTaskOrder": 0,
              "subTaskName": "",
              "subTaskType": 2,
              "flags": 2,
              "operationType": 2,
              "subTaskId": 3
            },
            "pattern": {
              "active_end_occurence": 0,
              "freq_subday_interval": 0,
              "freq_type": 8,
              "patternId": 2,
              "flags": 0,
              "description": "",
              "active_end_time": 0,
              "active_start_time_window": 0,
              "active_end_date": 0,
              "skipOccurence": 0,
              "skipDayNumber": 0,
              "active_start_time": 64800,
              "freq_restart_interval": 0,
              "active_start_date": 1437091200,
              "freq_interval": 32,
              "freq_relative_interval": 0,
              "name": "",
              "freq_recurrence_factor": 1,
              "calendar": {
                "calendarId": 1
              },
              "timeZone": {
                "TimeZoneID": 1000,
                "TimeZoneName": "CommServe Time Zone"
              }
            },
            "options": {
              "backupOpts": {
                "sybaseSkipFullafterLogBkp": false,
                "bkpLatestVersion": false,
                "collectMetaInfo": true,
                "backupLevel": 1,
                "incLevel": 1,
                "runIncrementalBackup": true,
                "runSILOBackup": false,
                "doNotTruncateLog": false,
                "dataOpt": {
                  "followMountPoints": true,
                  "startLogBackupAfterSuccessfullBackup": false,
                  "createNewIndex": true
                },
                "oracleOptions": {
                  "level": 1,
                  "cumulative": false,
                  "deleteArchLogOptions": {
                    "backupArchiveLogCriteria": 0
                  },
                  "backupArchLogOptions": {
                    "backupArchiveLog": true,
                    "backupArchiveLogCriteria": 7,
                    "startLSN": 1,
                    "endLSN": 1
                  }
                }
              }
            }
          }
        ]
      },
      {
        "associations": [
          {
            "srmReportSet": 0,
            "srmTemplateId": 0,
            "subclientId": 0,
            "storagePolicyId": 0,
            "copyId": 0,
            "clientId": 0,
            "srmTemplateName": "",
            "appName": "Default Application Type Name",
            "planId": 0,
            "clientGroupId": 0,
            "applicationId": 0,
            "backupsetId": 0,
            "instanceId": 0,
            "agentlessPolicyId": 0,
            "mediaAgentId": 0,
            "workflowId": 0,
            "_type_": 0,
            "flags": {
              "exclude": false
            }
          }
        ],
        "task": {
          "description": "",
          "ownerId": 2,
          "runUserId": 2,
          "taskType": 2,
          "ownerName": "user-01",
          "planId": 0,
          "alertId": 0,
          "GUID": "5145FEFB-82F7-4624-BA00-1B84EAB83D03",
          "policyType": 0,
          "taskName": "",
          "taskId": 3,
          "originalCC": {
            "commCellId": 2
          },
          "taskFlags": {
            "isEdgeDrive": false,
            "isEZOperation": false,
            "isPlanAssociated": false,
            "uninstalled": false,
            "isServerPlanAssociated": false,
            "isSystem": true,
            "isIndexBackup": false,
            "disabled": false,
            "isEdiscovery": false
          },
          "task": {
            "taskName": "",
            "taskId": 3
          }
        },
        "appGroup": {},
        "subTasks": [
          {
            "relativeTime": 76199,
            "nextScheduleTime": 1793980800,
            "subTask": {
              "subTaskOrder": 0,
              "subTaskName": "DR Backup Full",
              "subTaskType": 1,
              "flags": 4,
              "operationType": 4002,
              "subTaskId": 4
            },
            "pattern": {
              "active_end_occurence": 0,
              "freq_subday_interval": 0,
              "freq_type": 4,
              "patternId": 3,
              "flags": 0,
              "description": "",
              "active_end_time": 0,
              "active_start_time_window": 0,
              "active_end_date": 0,
              "skipOccurence": 0,
              "skipDayNumber": 0,
              "active_start_time": 36000,
              "freq_restart_interval": 0,
              "active_start_date": 1437091200,
              "freq_interval": 1,
              "freq_relative_interval": 0,
              "name": "",
              "freq_recurrence_factor": 1,
              "calendar": {
                "calendarId": 1
              },
              "timeZone": {
                "TimeZoneID": 1000,
                "TimeZoneName": "CommServe Time Zone"
              }
            },
            "options": {
              "adminOpts": {
                "drBackupOption": {
                  "drbackupType": 1,
                  "dbName": "commserv",
                  "shrinkDB": false,
                  "enableDatabasesBackupCompression": false
                }
              }
            }
          }
        ]
      },
      {
        "associations": [
          {
            "srmReportSet": 0,
            "srmTemplateId": 0,
            "subclientId": 0,
            "storagePolicyId": 0,
            "copyId": 0,
            "clientId": 0,
            "srmTemplateName": "",
            "appName": "Default Application Type Name",
            "planId": 0,
            "clientGroupId": 0,
            "applicationId": 0,
            "backupsetId": 0,
            "instanceId": 0,
            "agentlessPolicyId": 0,
            "mediaAgentId": 0,
            "workflowId": 0,
            "_type_": 0,
            "flags": {
              "exclude": false
            }
          }
        ],
        "task": {
          "description": "",
          "ownerId": 2,
          "runUserId": 2,
          "taskType": 2,
          "ownerName": "user-01",
          "planId": 0,
          "alertId": 0,
          "GUID": "14E1B121-9834-4C48-BC69-E77074335E04",
          "policyType": 0,
          "taskName": "",
          "taskId": 4,
          "originalCC": {
            "commCellId": 2
          },
          "taskFlags": {
            "isEdgeDrive": false,
            "isEZOperation": false,
            "isPlanAssociated": false,
            "uninstalled": false,
            "isServerPlanAssociated": false,
            "isSystem": true,
            "isIndexBackup": false,
            "disabled": false,
            "isEdiscovery": false
          },
          "task": {
            "taskName": "",
            "taskId": 4
          }
        },
        "appGroup": {},
        "subTasks": [
          {
            "relativeTime": 83399,
            "nextScheduleTime": 1793988000,
            "subTask": {
              "subTaskOrder": 0,
              "subTaskName": "Data Aging",
              "subTaskType": 1,
              "flags": 8,
              "operationType": 4018,
              "subTaskId": 5
            },
            "pattern": {
              "active_end_occurence": 0,
              "freq_subday_interval": 0,
              "freq_type": 4,
              "patternId": 4,
              "flags": 0,
              "description": "",
              "active_end_time": 0,
              "active_start_time_window": 0,
              "active_end_date": 0,
              "skipOccurence": 0,
              "skipDayNumber": 0,
              "active_start_time": 43200,
              "freq_restart_interval": 0,
              "active_start_date": 1437091200,
              "freq_interval": 1,
              "freq_relative_interval": 0,
              "name": "",
              "freq_recurrence_factor": 1,
              "calendar": {
                "calendarId": 1
              },
              "timeZone": {
                "TimeZoneID": 1000,
                "TimeZoneName": "CommServe Time Zone"
              }
            },
            "options": {
              "adminOpts": {
                "dataAgingOption": {
                  "selectCopies": false,
                  "includeAllClients": false,
                  "pruneSelectedCopies": false,
                  "isGranular": false
                }
              }
            }
          }
        ]
      },
      "... 19 more"
    ]
  }
  ```

  </details>

## `get_schedule` - GET /Schedules/{taskId}

```python
cv.raw.scheduleand_schedule_policy.get_schedule('2')
```

**On the wire**

- `GET /Schedules/2` -> **200** (0.26 s)

  <details><summary>Answer</summary>

  ```json
  {
    "taskInfo": {
      "task": {
        "isDestinationHostedclient-group-01": false,
        "description": "System created schedule policy for All Agent Types",
        "isRecoveryGroupOwner": false,
        "ownerId": 2,
        "runUserId": 2,
        "taskType": 4,
        "ownerName": "Administrator",
        "planId": 0,
        "alertId": 0,
        "GUID": "69173BC2-9642-4565-A875-B8D77DC11858",
        "policyType": 0,
        "associatedObjects": 0,
        "taskName": "System Created (All  Agent Types)",
        "taskId": 2,
        "securityAssociations": {
          "associations": [
            {
              "company": {},
              "userOrGroup": [
                {
                  "userId": 2,
                  "userName": "user-01",
                  "_type_": 13
                }
              ],
              "properties": {
                "isCreatorAssociation": true,
                "role": {
                  "_type_": 120,
                  "roleId": 9,
                  "roleName": "Schedule Policy Creator",
                  "flags": {
                    "disabled": false
                  }
                }
              }
            }
          ],
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
              "userGroupName": "master"
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
              "userName": "user-01",
              "userId": 2
            }
          }
        },
        "taskFlags": {
          "isEdgeDrive": false,
          "isEZOperation": false,
          "forDDB": false,
          "isPlanAssociated": false,
          "uninstalled": false,
          "isServerPlanAssociated": false,
          "isSystem": true,
          "isIndexBackup": false,
          "disabled": false,
          "isEdiscovery": false,
          "isGCMPolicy": false
        },
        "task": {
          "taskName": "System Created (All  Agent Types)",
          "taskId": 2
        }
      },
      "appGroup": {},
      "subTasks": [
        {
          "relativeTime": 18568,
          "nextScheduleTime": 1793923200,
          "subTask": {
            "subTaskOrder": 0,
            "subTaskName": "",
            "subTaskType": 2,
            "flags": 1,
            "operationType": 2,
            "subTaskId": 2,
            "subTask": {
              "subtaskId": 2,
              "subtaskName": ""
            }
          },
          "pattern": {
            "active_end_occurence": 0,
            "freq_subday_interval": 0,
            "freq_type": 8,
            "patternId": 1,
            "flags": 0,
            "description": "",
            "active_end_time": 0,
            "active_start_time_window": 0,
            "active_end_date": 0,
            "skipOccurence": 0,
            "skipDayNumber": 0,
            "active_start_time": 64800,
            "freq_restart_interval": 0,
            "active_start_date": 1437091200,
            "freq_interval": 30,
            "freq_relative_interval": 0,
            "name": "",
            "freq_recurrence_factor": 1,
            "daysToRun": {
              "week": 0,
              "Monday": true,
              "Thursday": true,
              "Wednesday": true,
              "Tuesday": true,
              "day": 0
            },
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
              "sybaseSkipFullafterLogBkp": false,
              "bkpLatestVersion": false,
              "collectMetaInfo": true,
              "backupLevel": 2,
              "incLevel": 1,
              "runIncrementalBackup": true,
              "runSILOBackup": false,
              "doNotTruncateLog": false,
              "dataOpt": {
                "followMountPoints": true,
                "startLogBackupAfterSuccessfullBackup": false,
                "createNewIndex": false
              },
              "oracleOptions": {
                "level": 1,
                "cumulative": false,
                "deleteArchLogOptions": {
                  "backupArchiveLogCriteria": 0
                },
                "backupArchLogOptions": {
                  "backupArchiveLog": true,
                  "backupArchiveLogCriteria": 7,
                  "startLSN": 1,
                  "endLSN": 1
                }
              }
            }
          }
        },
        {
          "relativeTime": 104968,
          "nextScheduleTime": 1794009600,
          "subTask": {
            "subTaskOrder": 0,
            "subTaskName": "",
            "subTaskType": 2,
            "flags": 2,
            "operationType": 2,
            "subTaskId": 3,
            "subTask": {
              "subtaskId": 3,
              "subtaskName": ""
            }
          },
          "pattern": {
            "active_end_occurence": 0,
            "freq_subday_interval": 0,
            "freq_type": 8,
            "patternId": 2,
            "flags": 0,
            "description": "",
            "active_end_time": 0,
            "active_start_time_window": 0,
            "active_end_date": 0,
            "skipOccurence": 0,
            "skipDayNumber": 0,
            "active_start_time": 64800,
            "freq_restart_interval": 0,
            "active_start_date": 1437091200,
            "freq_interval": 32,
            "freq_relative_interval": 0,
            "name": "",
            "freq_recurrence_factor": 1,
            "daysToRun": {
              "week": 0,
              "Friday": true,
              "day": 0
            },
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
              "sybaseSkipFullafterLogBkp": false,
              "bkpLatestVersion": false,
              "collectMetaInfo": true,
              "backupLevel": 1,
              "incLevel": 1,
              "runIncrementalBackup": true,
              "runSILOBackup": false,
              "doNotTruncateLog": false,
              "dataOpt": {
                "followMountPoints": true,
                "startLogBackupAfterSuccessfullBackup": false,
                "createNewIndex": true
              },
              "oracleOptions": {
                "level": 1,
                "cumulative": false,
                "deleteArchLogOptions": {
                  "backupArchiveLogCriteria": 0
                },
                "backupArchLogOptions": {
                  "backupArchiveLog": true,
                  "backupArchiveLogCriteria": 7,
                  "startLSN": 1,
                  "endLSN": 1
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

## `get_schedule_policy` - GET /SchedulePolicy/{taskId}

```python
cv.raw.scheduleand_schedule_policy.get_schedule_policy('2')
```

**On the wire**

- `GET /SchedulePolicy/2` -> **200** (0.22 s)

  <details><summary>Answer</summary>

  ```json
  {
    "taskInfo": {
      "task": {
        "isDestinationHostedclient-group-01": false,
        "description": "System created schedule policy for All Agent Types",
        "isRecoveryGroupOwner": false,
        "ownerId": 2,
        "runUserId": 2,
        "taskType": 4,
        "ownerName": "Administrator",
        "planId": 0,
        "alertId": 0,
        "GUID": "69173BC2-9642-4565-A875-B8D77DC11858",
        "policyType": 0,
        "associatedObjects": 0,
        "taskName": "System Created (All  Agent Types)",
        "taskId": 2,
        "securityAssociations": {
          "associations": [
            {
              "company": {},
              "userOrGroup": [
                {
                  "userId": 2,
                  "userName": "user-01",
                  "_type_": 13
                }
              ],
              "properties": {
                "isCreatorAssociation": true,
                "role": {
                  "_type_": 120,
                  "roleId": 9,
                  "roleName": "Schedule Policy Creator",
                  "flags": {
                    "disabled": false
                  }
                }
              }
            }
          ],
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
              "userGroupName": "master"
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
              "userName": "user-01",
              "userId": 2
            }
          }
        },
        "taskFlags": {
          "isEdgeDrive": false,
          "isEZOperation": false,
          "forDDB": false,
          "isPlanAssociated": false,
          "uninstalled": false,
          "isServerPlanAssociated": false,
          "isSystem": true,
          "isIndexBackup": false,
          "disabled": false,
          "isEdiscovery": false,
          "isGCMPolicy": false
        },
        "task": {
          "taskName": "System Created (All  Agent Types)",
          "taskId": 2
        }
      },
      "appGroup": {},
      "subTasks": [
        {
          "relativeTime": 18567,
          "nextScheduleTime": 1793923200,
          "subTask": {
            "subTaskOrder": 0,
            "subTaskName": "",
            "subTaskType": 2,
            "flags": 1,
            "operationType": 2,
            "subTaskId": 2,
            "subTask": {
              "subtaskId": 2,
              "subtaskName": ""
            }
          },
          "pattern": {
            "active_end_occurence": 0,
            "freq_subday_interval": 0,
            "freq_type": 8,
            "patternId": 1,
            "flags": 0,
            "description": "",
            "active_end_time": 0,
            "active_start_time_window": 0,
            "active_end_date": 0,
            "skipOccurence": 0,
            "skipDayNumber": 0,
            "active_start_time": 64800,
            "freq_restart_interval": 0,
            "active_start_date": 1437091200,
            "freq_interval": 30,
            "freq_relative_interval": 0,
            "name": "",
            "freq_recurrence_factor": 1,
            "daysToRun": {
              "week": 0,
              "Monday": true,
              "Thursday": true,
              "Wednesday": true,
              "Tuesday": true,
              "day": 0
            },
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
              "sybaseSkipFullafterLogBkp": false,
              "bkpLatestVersion": false,
              "collectMetaInfo": true,
              "backupLevel": 2,
              "incLevel": 1,
              "runIncrementalBackup": true,
              "runSILOBackup": false,
              "doNotTruncateLog": false,
              "dataOpt": {
                "followMountPoints": true,
                "startLogBackupAfterSuccessfullBackup": false,
                "createNewIndex": false
              },
              "oracleOptions": {
                "level": 1,
                "cumulative": false,
                "deleteArchLogOptions": {
                  "backupArchiveLogCriteria": 0
                },
                "backupArchLogOptions": {
                  "backupArchiveLog": true,
                  "backupArchiveLogCriteria": 7,
                  "startLSN": 1,
                  "endLSN": 1
                }
              }
            }
          }
        },
        {
          "relativeTime": 104967,
          "nextScheduleTime": 1794009600,
          "subTask": {
            "subTaskOrder": 0,
            "subTaskName": "",
            "subTaskType": 2,
            "flags": 2,
            "operationType": 2,
            "subTaskId": 3,
            "subTask": {
              "subtaskId": 3,
              "subtaskName": ""
            }
          },
          "pattern": {
            "active_end_occurence": 0,
            "freq_subday_interval": 0,
            "freq_type": 8,
            "patternId": 2,
            "flags": 0,
            "description": "",
            "active_end_time": 0,
            "active_start_time_window": 0,
            "active_end_date": 0,
            "skipOccurence": 0,
            "skipDayNumber": 0,
            "active_start_time": 64800,
            "freq_restart_interval": 0,
            "active_start_date": 1437091200,
            "freq_interval": 32,
            "freq_relative_interval": 0,
            "name": "",
            "freq_recurrence_factor": 1,
            "daysToRun": {
              "week": 0,
              "Friday": true,
              "day": 0
            },
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
              "sybaseSkipFullafterLogBkp": false,
              "bkpLatestVersion": false,
              "collectMetaInfo": true,
              "backupLevel": 1,
              "incLevel": 1,
              "runIncrementalBackup": true,
              "runSILOBackup": false,
              "doNotTruncateLog": false,
              "dataOpt": {
                "followMountPoints": true,
                "startLogBackupAfterSuccessfullBackup": false,
                "createNewIndex": true
              },
              "oracleOptions": {
                "level": 1,
                "cumulative": false,
                "deleteArchLogOptions": {
                  "backupArchiveLogCriteria": 0
                },
                "backupArchLogOptions": {
                  "backupArchiveLog": true,
                  "backupArchiveLogCriteria": 7,
                  "startLSN": 1,
                  "endLSN": 1
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
