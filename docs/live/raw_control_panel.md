# `cv.raw.control_panel`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:50 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_comm_cell_activity_control` - GET /CommCell/ActivityControl

```python
cv.raw.control_panel.get_comm_cell_activity_control()
```

**On the wire**

- `GET /CommCell/ActivityControl` -> **200** (0.08 s)

  <details><summary>Answer</summary>

  ```json
  {
    "acObjects": [
      {
        "reEnableTime": 0,
        "noSchedEnable": true,
        "reenableTimeZone": 0,
        "activityType": 128,
        "enabled": false
      },
      {
        "reEnableTime": 0,
        "noSchedEnable": true,
        "reenableTimeZone": 0,
        "activityType": 1,
        "enabled": false
      },
      {
        "reEnableTime": 0,
        "noSchedEnable": true,
        "reenableTimeZone": 0,
        "activityType": 2,
        "enabled": false
      },
      "... 7 more"
    ]
  }
  ```

  </details>

## `get_comm_serv` - GET /CommServ

```python
cv.raw.control_panel.get_comm_serv()
```

**On the wire**

- `GET /CommServ` -> **200** (0.09 s)

  <details><summary>Answer</summary>

  ```json
  {
    "revisionId": 1459,
    "hostName": "commserve-02",
    "releaseId": 16,
    "csVersionInfo": "11 SP46.30",
    "osType": "Windows",
    "timeZone": "1:360:(UTC-06:00) Central Time (US & Canada)",
    "currentSPVersion": 46,
    "installedSPVersion": 46,
    "csTimeZone": {
      "TimeZoneID": 23,
      "TimeZoneName": "Central Standard Time"
    },
    "commcell": {
      "commCellName": "commserve-02",
      "commCellId": 2,
      "csGUID": "A1AD169B-CF73-41B9-BC8A-823EA536FF31"
    }
  }
  ```

  </details>

## `get_comm_serv_add_remove_software_commserve_software_cache`

GET /CommServ/AddRemoveSoftware/CommserveSoftwareCache

```python
cv.raw.control_panel.get_comm_serv_add_remove_software_commserve_software_cache()
```

**On the wire**

- `GET /CommServ/AddRemoveSoftware/CommserveSoftwareCache` -> **200** (0.54 s)

  <details><summary>Answer</summary>

  ```json
  {
    "commserveSoftwareCache": {
      "storePatchlocation": "J:\\Program Files\\Commvault\\ContentStore\\SW",
      "FTP_FTPproxyport": 21,
      "autoPatchFlag": 0,
      "cacheCurrentSpace": 0,
      "cacheFreeSpace": 83562622976,
      "HTTPsiteLocation": "downloadcenter.commvault.com",
      "unixPatchusername": "",
      "downloadProtocol": "HTTPS",
      "FTPoperationType": 9,
      "FTP_HTTPproxyport": 8080,
      "FTP_HTTPproxyserver": "",
      "FTP_FTPproxyserver": "",
      "FTPsitelocation": "",
      "patchHttpuseToken": "<masked>",
      "patchHttpconfigURL": "https://downloadcenter.commvault.com/CVDownloadCenter/openfiles/nc",
      "FTP_FTPProxylocation": "",
      "cacheExpectedSpace": 0,
      "unixPatchlocation": "",
      "FTPsiteCredentials": "<masked>",
      "FTP_HTTPproxyCredentials": "<masked>",
      "storePatchCredentials": "<masked>",
      "client": {
        "clientName": "",
        "_type_": 3,
        "clientId": 0
      },
      "FTP_FTPproxyCredentials": "<masked>",
      "UaInfo": {
        "win32SP": "",
        "fbsdSP": "",
        "linuxSP": "",
        "deletePackageCache": false,
        "highestSP": "",
        "networkReadiness": 0,
        "uaPackageCacheStatus": 1,
        "osfSP": "",
        "inSyncWithCSLevelCache": 0,
        "uaCachePath": "",
        "irixSP": "",
        "hpSP": "",
        "deleteUpdateCache": false,
        "applianceType": 0,
        "unixTimeStampForUnix": 0,
        "swAgentOpType": 0,
        "dwnSP": "",
        "uaOpCode": 0,
        "aixSP": "",
        "uaUpdateCacheStatus": 1,
        "unixTimeStamp": 0,
        "unixTimeStampForWindows": 0,
        "defaultShareName": "",
        "winx64SP": "",
        "latestVersion": "",
        "solarisSP": "",
        "shareName": "",
        "patchUAContentConfigs": {},
        "uaImpersonate": {},
        "uaName": {
          "name": "",
          "id": 0
        },
        "client": {
          "_type_": 3
        },
        "cacheContents": [
          {
            "version": "11",
            "softwareCacheServicePackDetails": [
              {
                "servicePack": "11.46.30",
                "additionalUpdates": "WinX64_11.0.0B80-SP46-CU30_SP46-CU30-1133, WinX64_11.0.0B80-SP46-CU30_SP46-CU30-1134, WinX64_11.0.0B80-SP46-CU30_SP46-CU30-1135, WinX64_11.0.0B80-SP46-CU30_SP46-CU30-1144, WinX64_11.0.0B80-SP46-CU30_SP46-CU30-1157, WinX64_11.0.0B80-SP46-CU30_SP46-CU30-1160, WinX64_11.0.0B80-SP46-CU30_SP46-CU30-1161, WinX64_11.0.0B80-SP46-CU30_SP46-CU30-1162, WinX64_11.0.0B80-SP46-CU30_SP46-CU30-1182, WinX64_11.0.0... (10318 characters)",
                "packagesInCache": "",
                "osName": "WinX64"
              },
              {
                "servicePack": "11.46.30",
                "additionalUpdates": "linux-x8664_11.0.0B80-SP46-CU30_SP46-CU30-1132, linux-x8664_11.0.0B80-SP46-CU30_SP46-CU30-1134, linux-x8664_11.0.0B80-SP46-CU30_SP46-CU30-1135, linux-x8664_11.0.0B80-SP46-CU30_SP46-CU30-1160, linux-x8664_11.0.0B80-SP46-CU30_SP46-CU30-1161, linux-x8664_11.0.0B80-SP46-CU30_SP46-CU30-1162, linux-x8664_11.0.0B80-SP46-CU30_SP46-CU30-1182, linux-x8664_11.0.0B80-SP46-CU30_SP46-CU30-1183, linux-x8664_11.0... (11134 characters)",
                "packagesInCache": "",
                "osName": "linux-x8664"
              }
            ]
          },
          {
            "version": "10"
          }
        ]
      }
    },
    "error": {
      "errorMessage": "",
      "errorCode": 0
    }
  }
  ```

  </details>

## `get_comm_serv_add_remove_software_remote_software_cache`

GET /CommServ/AddRemoveSoftware/RemoteSoftwareCache

```python
cv.raw.control_panel.get_comm_serv_add_remove_software_remote_software_cache()
```

**On the wire**

- `GET /CommServ/AddRemoveSoftware/RemoteSoftwareCache` -> **200** (0.18 s)

  <details><summary>Answer</summary>

  ```json
  {
    "qualifiedClients": [
      {
        "defaultShare": "\\\\host-02\\SoftwareShare",
        "cachePath": "/opt/commvault/SW",
        "clientName": {
          "name": "host-02",
          "id": 4
        }
      },
      {
        "defaultShare": "\\\\host-03\\SoftwareShare",
        "cachePath": "/opt/commvault/SW",
        "clientName": {
          "name": "host-03",
          "id": 5
        }
      },
      {
        "defaultShare": "\\\\host-04\\SoftwareShare",
        "cachePath": "/opt/commvault/SW",
        "clientName": {
          "name": "host-04",
          "id": 6
        }
      },
      "... 9 more"
    ]
  }
  ```

  </details>

## `get_comm_serv_audit_trail` - GET /CommServ/AuditTrail

```python
cv.raw.control_panel.get_comm_serv_audit_trail()
```

**On the wire**

- `GET /CommServ/AuditTrail` -> **200** (0.16 s)

  <details><summary>Answer</summary>

  ```json
  {
    "auditTrailInfo": {
      "retentionForCritical": 365,
      "retentionForLow": 120,
      "retentionForMedium": 240,
      "retentionForHigh": 365
    }
  }
  ```

  </details>

## `get_comm_serv_custom_calendar` - GET /CommServ/CustomCalendar

```python
cv.raw.control_panel.get_comm_serv_custom_calendar()
```

**On the wire**

- `GET /CommServ/CustomCalendar` -> **200** (0.13 s)

  <details><summary>Answer</summary>

  ```json
  {
    "customCalendar": [
      {
        "beginDate": 0,
        "defineCustomMonths": false,
        "isDefault": true,
        "calendarType": 1,
        "numberOfYears": 0,
        "beginYear": 0,
        "beginMonth": 1,
        "customCalendarEntity": {
          "_type_": 171,
          "customCalendarId": 1,
          "customCalendarName": "Standard"
        },
        "company": {
          "_type_": 189,
          "companyId": 0,
          "companyName": "Commcell"
        }
      }
    ]
  }
  ```

  </details>

## `get_comm_serv_metrics_reporting` - GET /CommServ/MetricsReporting

```python
cv.raw.control_panel.get_comm_serv_metrics_reporting()
```

**On the wire**

- `GET /CommServ/MetricsReporting` -> **200** (0.20 s)

  <details><summary>Answer</summary>

  ```json
  {
    "config": {
      "uploadFrequency": 7,
      "metricsType": 0,
      "lastCollectionTime": 1793712083,
      "useProxyClient": false,
      "uploadNow": 0,
      "dataCollectionTime": 25200,
      "metricsReportPackageInstalled": false,
      "tieringActive": false,
      "randomization": 0,
      "commcellDiagUsage": true,
      "nextUploadTime": 1794315600,
      "scriptDownloadTime": 1792134464,
      "lastUploadTime": 1793712110,
      "clientGroupList": [
        {
          "_type_": 28,
          "clientGroupId": -1
        }
      ],
      "cloud": {
        "threatwisePreferredRegion": "",
        "uploadURL": "",
        "downloadURL": "",
        "useUploadUrlForLinks": false,
        "uploadSurveyResultsByDirectDIP": 0,
        "serviceList": [
          {
            "flags": 0,
            "description": "",
            "enabled": false,
            "service": {
              "name": "Health Check",
              "id": 1
            }
          },
          {
            "flags": 0,
            "description": "",
            "enabled": false,
            "service": {
              "name": "Activity",
              "id": 3
            }
          },
          {
            "flags": 0,
            "description": "",
            "enabled": false,
            "service": {
              "name": "Audit",
              "id": 5
            }
          },
          "... 5 more"
        ],
        "uploadUser": {}
      },
      "HttpServerInfo": {
        "RestrictQuery": {
          "QueryIds": ""
        },
        "ScrubCommCells": {
          "CCIDs": ""
        }
      }
    }
  }
  ```

  </details>

## `get_comm_serv_snmpv3_configuration` - GET /CommServ/SNMPV3Configuration

```python
cv.raw.control_panel.get_comm_serv_snmpv3_configuration()
```

**On the wire**

- `GET /CommServ/SNMPV3Configuration` -> **200** (0.16 s)

  <details><summary>Answer</summary>

  ```json
  {}
  ```

  </details>

## `get_commcell_internet_options_proxy` - GET /Commcell/InternetOptions/Proxy

```python
cv.raw.control_panel.get_commcell_internet_options_proxy()
```

**On the wire**

- `GET /Commcell/InternetOptions/Proxy` -> **200** (0.11 s)

  <details><summary>Answer</summary>

  ```json
  {
    "config": {
      "useInternetGatewayPublic": false,
      "ignoreHttpProxyForSendLog": false,
      "useIgDownloadSoftware": false,
      "useInternetGatewayForWebhook": false,
      "useHttpProxy": false,
      "useInternetGatewaySendLogFile": false,
      "softwareDownloadProtocolType": 3,
      "proxyServer": "",
      "proxyType": 1,
      "useInternetGatewayPrivate": false,
      "proxyPort": 0,
      "useProxyAuthentication": true,
      "usePassiveFTPConnection": true,
      "proxyBypassList": "",
      "proxyCredentials": {},
      "proxyClient": {
        "clientName": "",
        "_type_": 3,
        "clientId": 1
      }
    }
  }
  ```

  </details>

## `get_commcell_properties` - GET /commcell/properties

```python
cv.raw.control_panel.get_commcell_properties()
```

**On the wire**

- `GET /commcell/properties` -> **200** (0.14 s)

  <details><summary>Answer</summary>

  ```json
  {
    "commCellInfo": {
      "commCellEntity": {
        "_type_": 1,
        "commCellName": "commserve-02",
        "commCellId": 2
      },
      "generalInfo": {
        "hostName": "commserve-02",
        "enableLocalAuthentication": false,
        "enableSharedLaptopUsage": false,
        "enableTwoFactorAuthentication": false,
        "networkErrorRetryCount": 1,
        "useUPNForEmail": false,
        "flags": 0,
        "description": "",
        "networkErrorRetryFreq": 1,
        "autoClientOwnerAssignmentType": 1,
        "networkErrorRetryFlag": true,
        "allowUsersToEnablePasskey": false,
        "autoClientOwnerAssignmentValue": "EnumUserProfiles",
        "enablePrivacy": false,
        "twoFactorAuthenticationInfo": {
          "mode": 0,
          "webAuthn": {
            "allowPasswordlessLogin": "<masked>",
            "allowUsernamelessLogin": false
          }
        },
        "accountLockSettingsInfo": {
          "failedLoginAttemptsWithin": -1,
          "failedLoginAttemptLimit": 5,
          "accountLockDurationIncrements": -1,
          "accountLockDuration": 1800
        },
        "autoRetireDevices": {
          "retireDevicesAfterDays": -2,
          "forceDeleteDevicesAfterDays": -2
        }
      }
    }
  }
  ```

  </details>

## `get_email_server` - GET /EmailServer

```python
cv.raw.control_panel.get_email_server()
```

**On the wire**

- `GET /EmailServer` -> **200** (0.08 s)

  <details><summary>Answer</summary>

  ```json
  {
    "useModernAuth": false,
    "filterInvalidEmails": false,
    "startTLS": false,
    "smtpPort": 465,
    "providerType": 0,
    "timeout": 30000,
    "enableSSL": true,
    "smtpServer": "smtp.host-57",
    "useAuthentication": true,
    "useEncryptedMailServer": false,
    "maxMailServerSize": 3072,
    "userInfo": {
      "userName": "user-05",
      "savedCredential": "<masked>"
    },
    "senderInfo": {
      "senderName": "cv toaster",
      "senderAddress": "user-05"
    }
  }
  ```

  </details>

## `get_operation_window_op_window_list` - GET /OperationWindow/OpWindowList

```python
cv.raw.control_panel.get_operation_window_op_window_list()
```

**On the wire**

- `GET /OperationWindow/OpWindowList` -> **200** (0.16 s)

  <details><summary>Answer</summary>

  ```json
  {
    "error": {
      "errorCode": 0
    }
  }
  ```

  </details>

## `list_comm_cell_credentials` - GET /CommCell/Credentials

```python
cv.raw.control_panel.list_comm_cell_credentials()
```

**On the wire**

- `GET /CommCell/Credentials` -> **200** (0.17 s)

  <details><summary>Answer</summary>

  ```json
  {
    "credentialRecordInfo": "<masked>",
    "error": {
      "errorMessage": "",
      "errorCode": 0
    }
  }
  ```

  </details>

## `get_comm_cell_credential` - GET /CommCell/Credentials/{credentialName}

```python
cv.raw.control_panel.get_comm_cell_credential('blt-lab-sql-sa')
```

**On the wire**

- `GET /CommCell/Credentials/blt-lab-sql-sa` -> **200** (0.18 s)

  <details><summary>Answer</summary>

  ```json
  {
    "credentialRecordInfo": "<masked>",
    "error": {
      "errorMessage": "",
      "errorCode": 0
    }
  }
  ```

  </details>

## `get_operation_window` - GET /OperationWindow/{ruleId}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.control_panel.get_operation_window(...)
```
