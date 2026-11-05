# `cv.raw.organization`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:37 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_navigation_settings` - GET /NavigationSettings

```python
cv.raw.organization.get_navigation_settings()
```

**On the wire**

- `GET /NavigationSettings` -> **200** (0.09 s)

  <details><summary>Answer</summary>

  ```json
  {
    "navSettings": {
      "globalSettings": [
        {
          "deniedNavItems": "servers,powerPlatformApps,saasAppsListPage,cloudStorageApp,distributedSystem,bigDataApps,notesDatabase,serviceCatalog,activeDirectory,autotaskPSA,connectwisePSA,haloPSA,modalitiesConfig,billing,vnaConfig,genApps,gitAppsAccounts,cloudConfiguration,salesforceOrganizations,dynamics365,company,epicServersList,servicenowInstances,sharepoint,serviceNowPSA,gsuiteApps,oktaApp",
          "userRole": 0
        },
        {
          "deniedNavItems": "snmp,modalitiesConfig,lifeCyclePolicy,webconsoleMonitoring,webconsoleAnalytics,cvlivesync,encryption,mongoDBHealthDashboard,commCell,webconsoleStore,webconsoleDownloadCenter,globalExceptions,epicServersList,replicationSettings,maintenance,troubleshooting,rpStores,metricsReporting,certificate,cloudStorageApp,storageHyperscale,servers,storageCloud,genApps,dataOptions,storageTape,storageMetallic,fail... (1205 characters)",
          "userRole": 1
        },
        {
          "deniedNavItems": "identityServers,snmp,rpStores,plugin,vsaOrganizations,cloudConfiguration,accessControl,operationWindow,developerSettings,haloPSA,reactVsaReplicationMonitor,commcellGroups,troubleshooting,triggeredAlerts,applications,mongoDBHealthDashboard,tables,reportsManager,blrReplicationGroups,environment,users,networkStore,serviceNowPSA,logStreaming,genApps,epicServersList,events,userGroups,globalConfigManage... (2164 characters)",
          "userRole": 2
        },
        "... 2 more"
      ]
    },
    "error": {
      "errorMessage": "",
      "errorCode": 0
    }
  }
  ```

  </details>

## `list_email_templates` - GET /EmailTemplates

```python
cv.raw.organization.list_email_templates()
```

**On the wire**

- `GET /EmailTemplates` -> **200** (0.16 s)

  <details><summary>Answer</summary>

  ```json
  {
    "emailTemplatesList": [
      {
        "modifiedTime": 1791247233,
        "description": "Email sent to the user when a access token is deleted",
        "localizedTypeName": "Access Token deleted",
        "issubclient-01": true,
        "emailTemplateTypeId": 24,
        "name": "Access Token deleted",
        "emailTemplateId": 24,
        "ownerCompany": {
          "providerId": 0,
          "providerDomainName": "Commcell"
        },
        "locale": {
          "displayString": "English-UnitedStates",
          "localeId": 0
        },
        "from": {}
      },
      {
        "modifiedTime": 1791247233,
        "description": "Email sent to user when their Access tokens are about to expire or become non-renewable.",
        "localizedTypeName": "Access token is about to become inoperable.",
        "issubclient-01": true,
        "emailTemplateTypeId": 27,
        "name": "Access token is about to become inoperable.",
        "emailTemplateId": 27,
        "ownerCompany": {
          "providerId": 0,
          "providerDomainName": "Commcell"
        },
        "locale": {
          "displayString": "English-UnitedStates",
          "localeId": 0
        },
        "from": {}
      },
      {
        "modifiedTime": 1791247233,
        "description": "Email sent to the user when a access token is modified",
        "localizedTypeName": "Access Token modified",
        "issubclient-01": true,
        "emailTemplateTypeId": 25,
        "name": "Access Token modified",
        "emailTemplateId": 25,
        "ownerCompany": {
          "providerId": 0,
          "providerDomainName": "Commcell"
        },
        "locale": {
          "displayString": "English-UnitedStates",
          "localeId": 0
        },
        "from": {}
      },
      "... 38 more"
    ]
  }
  ```

  </details>

## `list_organization` - GET /Organization

```python
cv.raw.organization.list_organization()
```

**On the wire**

- `GET /Organization` -> **200** (0.15 s)

  <details><summary>Answer</summary>

  ```json
  {}
  ```

  </details>

## `get_organization` - GET /Organization/{OrganizationId}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.organization.get_organization(...)
```

## `get_organization_auth_token` - GET /Organization/{OrganizationId}/AuthToken

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.organization.get_organization_auth_token(...)
```

## `get_organization_customization` - GET /Organization/{organizationId}/Customization

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.organization.get_organization_customization(...)
```

## `get_organization_subclient-01plan` - GET /Organization/{OrganizationId}/subclient-01plan

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.organization.get_organization_subclient-01plan(...)
```

## `get_organization_email_customization`

GET /Organization/{OrganizationId}/EmailCustomization

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.organization.get_organization_email_customization(...)
```
