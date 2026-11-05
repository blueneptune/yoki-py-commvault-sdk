# Coverage, proven live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:37 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

**327 of 1487** operations in the server's own API description were called by the live tests and answered without an error. (Commvault publishes it at
api.commvault.com; scripts/spec.py reads it from there.)

| Area | Proven | Operations |
|---|---|---|
| plan | 12 | 47 |
| storage | 13 | 44 |
| hidden | 1 | 34 |
| metallic | 8 | 34 |
| activate | 4 | 33 |
| control_panel | 14 | 32 |
| kubernetes | 3 | 32 |
| partner_apis | 0 | 32 |
| organization | 3 | 28 |
| salesforce | 3 | 28 |
| server_plan | 4 | 28 |
| commcell | 1 | 24 |
| alerts | 6 | 22 |
| client | 6 | 21 |
| virtualization | 3 | 21 |
| user | 5 | 20 |
| cloud_storage | 1 | 18 |
| dashboard | 16 | 18 |
| hypervisor | 3 | 18 |
| server_group | 6 | 17 |
| servers | 4 | 17 |
| tape_storage | 6 | 17 |
| alert | 5 | 16 |
| job | 7 | 16 |
| network_topology | 3 | 16 |
| archive_plan | 1 | 15 |
| data_cube | 3 | 15 |
| laptop_plan | 1 | 15 |
| untagged | 1 | 15 |
| identity_servers | 1 | 14 |
| plan_rules | 4 | 14 |
| regions | 5 | 14 |
| snapshot | 2 | 14 |
| user_group | 7 | 14 |
| virtual_machines | 5 | 14 |
| array_management | 7 | 13 |
| credential_manager | 5 | 13 |
| cvfs | 0 | 13 |
| disk_storage | 2 | 13 |
| local_storage | 1 | 13 |
| recovery_runbook | 1 | 13 |
| scheduleand_schedule_policy | 4 | 12 |
| workflow | 3 | 12 |
| aws_db_document_db | 2 | 11 |
| failover_groups | 1 | 11 |
| media_agent | 6 | 11 |
| recovery_group | 1 | 11 |
| replication | 5 | 11 |
| reporting | 5 | 11 |
| teams | 1 | 11 |
| company | 1 | 10 |
| protection_group | 3 | 10 |
| udvnfsshare | 0 | 10 |
| vmprovisioning | 3 | 10 |
| agent | 1 | 9 |
| blackout_windows | 2 | 9 |
| client_group | 2 | 9 |
| drbackup | 4 | 9 |
| exchange | 1 | 9 |
| failover_group | 2 | 9 |
| hyper_scale_storage | 1 | 9 |
| one_drive | 1 | 9 |
| replication_group | 1 | 9 |
| sharepoint | 1 | 9 |
| snapshot_configurations | 5 | 9 |
| subclient | 1 | 9 |
| azure_blob | 0 | 8 |
| azure_data_lake_storage_gen2 | 0 | 8 |
| backup_set | 0 | 8 |
| cloud_connection | 1 | 8 |
| compliance | 1 | 8 |
| data_discovery | 2 | 8 |
| domain | 3 | 8 |
| instances | 1 | 8 |
| total_cost_of_ownership | 3 | 8 |
| vm_group | 1 | 8 |
| s3_vault | 1 | 7 |
| awsexport_db | 1 | 6 |
| cyber_resilience | 1 | 6 |
| office365 | 2 | 6 |
| replication_monitor | 1 | 6 |
| roles | 3 | 6 |
| software_cache | 3 | 6 |
| access_tokens | 1 | 5 |
| additional_settings | 4 | 5 |
| azure_file | 0 | 5 |
| commcell_group | 1 | 5 |
| entity_tag | 2 | 5 |
| entity_tags | 1 | 5 |
| external_endpoint_manager | 0 | 5 |
| license | 2 | 5 |
| node | 1 | 5 |
| recovery_group_entities | 0 | 5 |
| role | 2 | 5 |
| active_directory | 1 | 4 |
| cloud_apps | 2 | 4 |
| dataroom | 1 | 4 |
| dcplan | 0 | 4 |
| disaster_recovery_backup | 2 | 4 |
| email_server | 1 | 4 |
| mssql_api | 1 | 4 |
| net_app_ransomware_resilience | 0 | 4 |
| object_store_plan | 0 | 4 |
| recovery_target | 1 | 4 |
| remediation_policy | 0 | 4 |
| storage_arrays | 1 | 4 |
| array_ransomware_resilience | 0 | 3 |
| authentication | 0 | 3 |
| bigdata | 0 | 3 |
| cleanroom_runbook | 0 | 3 |
| cleanroom_targets | 0 | 3 |
| data_security | 0 | 3 |
| event_filter | 0 | 3 |
| file | 0 | 3 |
| file_server | 1 | 3 |
| gcpexpress_config | 0 | 3 |
| gcpspanner | 0 | 3 |
| instance | 1 | 3 |
| ip_library | 0 | 3 |
| nas | 0 | 3 |
| oracle_db | 1 | 3 |
| recovery_point_stores | 1 | 3 |
| restore | 1 | 3 |
| runbook_resources | 1 | 3 |
| s3_object_storage | 1 | 3 |
| schedule | 0 | 3 |
| smart_protect | 0 | 3 |
| syslog_server | 1 | 3 |
| access_control | 1 | 2 |
| activity_control | 0 | 2 |
| audit_plan | 0 | 2 |
| audits | 1 | 2 |
| awsdynamodb | 0 | 2 |
| backup | 0 | 2 |
| comm_serv | 0 | 2 |
| cslive_sync | 0 | 2 |
| db2_database | 2 | 2 |
| db2_multi_node | 1 | 2 |
| dynamics365 | 0 | 2 |
| filtersfor_searchor_list | 0 | 2 |
| global_exceptions | 1 | 2 |
| global_parameters | 0 | 2 |
| hybrid_file_stores | 1 | 2 |
| key_management_server | 1 | 2 |
| laptop | 1 | 2 |
| laptop_devices | 1 | 2 |
| microsoft_azure_object_storage | 1 | 2 |
| my_sqldatabases | 1 | 2 |
| partner_integrations | 0 | 2 |
| qcommands | 0 | 2 |
| rdssnap | 0 | 2 |
| resource_pools | 1 | 2 |
| scrub_logs | 0 | 2 |
| security | 0 | 2 |
| security_assembly | 1 | 2 |
| threat_indicators | 2 | 2 |
| alibaba_objectstorage | 0 | 1 |
| anomalous_conditions | 1 | 1 |
| archive_file_servers | 1 | 1 |
| azure_ad | 0 | 1 |
| cdmplan | 0 | 1 |
| cloud_configuration | 0 | 1 |
| cloud_object_storage | 1 | 1 |
| cockroach_db | 0 | 1 |
| commcell_level_encryption_settings | 0 | 1 |
| convert_xmlto_json | 0 | 1 |
| couchbase | 0 | 1 |
| databases | 1 | 1 |
| ediscovery | 1 | 1 |
| epic_servers | 1 | 1 |
| file_operationsforshares | 0 | 1 |
| file_servers | 1 | 1 |
| global_search | 0 | 1 |
| global_server_plan | 0 | 1 |
| google_workspace | 1 | 1 |
| hbase | 0 | 1 |
| index_servers | 1 | 1 |
| instant_clones | 1 | 1 |
| mount_path | 0 | 1 |
| multi_comm_cell | 1 | 1 |
| recovery_groups | 1 | 1 |
| recovery_readiness | 0 | 1 |
| satori | 0 | 1 |
| service_commcells | 1 | 1 |
| snapshot_management | 0 | 1 |
| snmp | 1 | 1 |
| solutions | 1 | 1 |
| splunk | 0 | 1 |
| storage_policy | 0 | 1 |
| sybase_db | 0 | 1 |
| yugabytedb | 0 | 1 |

## Proven

### access_control

- `GET /V4/AccessControl`

### access_tokens

- `GET /V4/AccessToken`

### activate

- `GET /AnalyticsServers`
- `GET /AnalyticsServers/id/{cloudId}`
- `GET /EDiscoveryClients/Inventories`
- `GET /dcube/entity`

### active_directory

- `GET /V4/ActiveDirectory/Apps`

### additional_settings

- `GET /V4/AddedEntitySettings`
- `GET /V4/AddedGlobalSettings`
- `GET /V4/GlobalSettings`
- `GET /V4/LookupSettings`

### agent

- `GET /V4/CommCell/Agents`

### alert

- `GET /Alert`
- `GET /AlertRule`
- `GET /AlertRule/{alertId2}`
- `GET /LogStreamingConnector`
- `GET /LogStreamingConnector/Templates`

### alerts

- `GET /Alert/CustomRule`
- `GET /Alert/CustomRule/{alertRuleId}`
- `GET /V4/AlertDefinitions`
- `GET /V4/AlertDefinitions/{id}`
- `GET /V4/AlertType`
- `GET /V4/TriggeredAlerts`

### anomalous_conditions

- `GET /V4/AnomalousAudits`

### archive_file_servers

- `GET /V4/ArchiveFileServers`

### archive_plan

- `GET /V4/ArchivePlan/{planId}/BackupDestinations`

### array_management

- `GET /StorageArrays`
- `GET /StorageArrays/{storagearrayId}`
- `GET /V4/StorageArrays`
- `GET /V4/StorageArrays/Client/{clientId}/Arrays`
- `GET /V4/StorageArrays/Client/{clientId}/Subclient/{subclientId}/Arrays`
- `GET /V4/StorageArrays/Copy/{copyId}/Arrays`
- `GET /V4/StorageArrays/{arrayId}`

### audits

- `GET /v4/Audits`

### aws_db_document_db

- `GET /Instance/{instanceid}`
- `GET /subclient/{subclientid}`

### awsexport_db

- `GET /backupset/{backupsetId}`

### blackout_windows

- `GET /V4/BlackoutWindow`
- `GET /V5/BlackoutWindow`

### client

- `GET /Client`
- `GET /Client/DistributedApps`
- `GET /Client/{clientId}/AdditionalSettings`
- `GET /IndexServers`
- `GET /client/{clientId}`
- `GET /clients/count`

### client_group

- `GET /ClientGroup`
- `GET /ClientGroup/{clientGroupId}`

### cloud_apps

- `GET /Client/proxy/CloudApps`
- `GET /V4/CRD/CloudAccounts`

### cloud_connection

- `GET /V4/Cloud/CloudConnection`

### cloud_object_storage

- `GET /Instance/CloudStorage`

### cloud_storage

- `GET /V4/Storage/Cloud`

### commcell

- `GET /CommCell/PasswordEncryptionConfig`

### commcell_group

- `GET /V4/CommcellGroup`

### company

- `GET /V4/company`

### compliance

- `GET /getCIServerList`

### control_panel

- `GET /CommCell/ActivityControl`
- `GET /CommCell/Credentials`
- `GET /CommCell/Credentials/{credentialName}`
- `GET /CommServ`
- `GET /CommServ/AddRemoveSoftware/CommserveSoftwareCache`
- `GET /CommServ/AddRemoveSoftware/RemoteSoftwareCache`
- `GET /CommServ/AuditTrail`
- `GET /CommServ/CustomCalendar`
- `GET /CommServ/MetricsReporting`
- `GET /CommServ/SNMPV3Configuration`
- `GET /Commcell/InternetOptions/Proxy`
- `GET /EmailServer`
- `GET /OperationWindow/OpWindowList`
- `GET /commcell/properties`

### credential_manager

- `GET /V4/Credential`
- `GET /V4/Credential/{credentialName}`
- `GET /V5/Credential/{credentialId}`
- `GET /V6/Credential`
- `GET /V6/Credential/{credentialId}`

### cyber_resilience

- `GET /V4/CyberResilience/Credentials`

### dashboard

- `GET /CommServ/Anomaly/Entity/Count?anomalousEntityType=14`
- `GET /Security/Dashboard`
- `GET /StoragePool/HyperScale/Dashboard`
- `GET /cr/reportsplusengine/datasets/075e703a-b29f-46d6-ad29-7c1a60f7e4f3/data?cache=true&parameter.i_DashboardType=commcell&datasource=2`
- `GET /cr/reportsplusengine/datasets/2b366703-52e1-4775-8047-1f4cfa13d2db/data?cache=true&parameter.i_DashboardType=commcell&orderby="Date to be Full"&datasource=2`
- `GET /cr/reportsplusengine/datasets/841800ea-53c4-4249-91fa-76ea0d60f6a4/data?cache=true&parameter.i_dashboardType=commcell&datasource=2`
- `GET /cr/reportsplusengine/datasets/GetSLACounts/data?cache=true&parameter.i_DashboardType=commcell&datasource=2`
- `GET /cr/reportsplusengine/datasets/a0f077a5-2dfe-4010-a957-57a24cae89a8/data`
- `GET /cr/reportsplusengine/datasets/b50b20ed-5fc4-4b4c-f7c4-fc6b84eb35cc/data?cache=true`
- `GET /cr/reportsplusengine/datasets/d0a73c45-b06d-4358-8d7e-d55d428ba75c/data?cache=true&parameter.i_DashboardType=commcell&datasource=2`
- `GET /cr/reportsplusengine/datasets/d7faef75-cf66-40a2-98ce-a2d0cc2a144b:2654b01f-9bb0-481e-b273-4b4fddc585b1/data/?offset=0&fields=[LicUsageType] AS [License ID],[Dial] AS [License],[Purchased] AS [Available Total (TB)],[PermTotal] AS [Permanent Purchased (TB)],[Eval] AS [Term Purchased (TB)],[Usage] AS [Used (TB)],[EvalExpiryDate] AS [EvalExpiryDate],[Summary] AS [Summary]&parameter.GUID=-1&limit=10`
- `GET /cr/reportsplusengine/datasets/d7faef75-cf66-40a2-98ce-a2d0cc2a144b:44cd7de8-ecb2-4ec8-8b2b-162491172eef/data/?offset=0&fields=[LicUsageType] AS [License ID],[Dial] AS [License],[Purchased] AS [Available Total (users)],[PermTotal] AS [Permanent Purchased (users)],[Eval] AS [Term Purchased (users)],[Usage] AS [Used (users)],[EvalExpiryDate] AS [EvalExpiryDate],[Summary] AS [Summary]&parameter.GUID=-1&limit=5`
- `GET /cr/reportsplusengine/datasets/d7faef75-cf66-40a2-98ce-a2d0cc2a144b:cc2e77ec-9315-4446-cd7e-44ef80a8860e/data/?offset=0&fields=[LicUsageType] AS [License ID],[Dial] AS [License],[Purchased] AS [Available Total (TB)],[PermTotal] AS [Permanent Purchased (TB)],[Eval] AS [Term Purchased (TB)],[Usage] AS [Used (TB)],[EvalExpiryDate] AS [EvalExpiryDate],[Summary] AS [Summary]&parameter.GUID=-1&limit=20`
- `GET /cr/reportsplusengine/datasets/d7faef75-cf66-40a2-98ce-a2d0cc2a144b:cd38c52a-e099-4252-d36f-3e2c54540f6f/data/?offset=0&fields=[LicUsageType] AS [License ID],[Dial] AS [License],[Purchased] AS [Available Total (instances)],[PermTotal] AS [Permanent Purchased (instances)],[Eval] AS [Term Purchased (instances)],[Usage] AS [Used (instances)],[EvalExpiryDate] AS [EvalExpiryDate],[Summary] AS [Summary]&parameter.GUID=-1&limit=5`
- `GET /cr/reportsplusengine/datasets/d7faef75-cf66-40a2-98ce-a2d0cc2a144b:f7c6b473-f99d-44b4-ff5e-466b55656500/data/?offset=0&fields=[LicUsageType] AS [License ID],[Dial] AS [License],[Purchased] AS [Available Total],[PermTotal] AS [Permanent Purchased],[Eval] AS [Term Purchased],[Usage] AS [Used],[EvalExpiryDate] AS [EvalExpiryDate],[Summary] AS [Summary]&parameter.GUID=-1&limit=20`
- `GET /cr/reportsplusengine/datasets/d7faef75-cf66-40a2-98ce-a2d0cc2a144b:feabb5ca-b6b7-4572-b0cb-39352c7e1b67/data/?cacheId=e76a6d07-2b1b-47b2-d97e-7a7f1a9793be&offset=0&fields=[Dial] AS [Dial],[Purchased] AS [Purchased],[PermTotal] AS [PermTotal],[Eval] AS [Eval],[Usage] AS [Usage],[TermDate] AS [TermDate],[EvalExpiryDate] AS [EvalExpiryDate]&isExport=false&componentName=Capacity Licenses&parameter.GUID=-1&limit=5&rawData=false`

### data_cube

- `GET /V2/EDiscoveryClients/Clients/4`
- `GET /dcube/GetDataSources`
- `GET /dcube/getAnalyticsEngine`

### data_discovery

- `GET /Asset/Discovery/Configuration`
- `GET /Asset/Discovery/Status`

### databases

- `GET /V4/Databases`

### dataroom

- `GET /Dataroom`

### db2_database

- `GET /Backupset/{BackupsetID}/DB2StorageGroups`
- `GET /Client/{ClientID}/DiscoverDB2Instances`

### db2_multi_node

- `GET /Instance/DB2Partitions`

### disaster_recovery_backup

- `GET /Commcell/DRBackup/Options`
- `GET /Commcell/DRBackup/Properties`

### disk_storage

- `GET /V4/Storage/Disk`
- `GET /V4/Storage/Disk/{storagePoolId}`

### domain

- `GET /CommCell/DomainController`
- `GET /IdentityServers`
- `GET /ThirdParty/App`

### drbackup

- `GET /V4/DRBackup/BackupDestination/SourceCopy/Eligible`
- `GET /V4/DRBackup/BackupDestinations`
- `GET /V4/DRBackup/Regions`
- `GET /V4/DRBackup/StoragePolicy`

### ediscovery

- `GET /V4/Ediscovery/Packages/{packageId}/AccessNodes`

### email_server

- `GET /V4/EmailServer`

### entity_tag

- `GET /V4/Tags/AssociatedEntities`
- `GET /V4/Tags/{tagId}/Values`

### entity_tags

- `GET /Ediscovery/Tags`

### epic_servers

- `GET /V4/EpicServers`

### exchange

- `GET /V4/Office365/Exchange`

### failover_group

- `GET /DR/JobStats`
- `GET /FailoverGroups`

### failover_groups

- `GET /V4/FailoverGroups`

### file_server

- `GET /Backupsets`

### file_servers

- `GET /V4/FileServers`

### global_exceptions

- `GET /V4/GlobalExceptions`

### google_workspace

- `GET /V4/GoogleWorkspace/Plans`

### hidden

- `GET /V4/user/{userId}/authenticationMethods`

### hybrid_file_stores

- `GET /V4/HybridFileStores`

### hyper_scale_storage

- `GET /V4/Storage/HyperScale`

### hypervisor

- `GET /V4/Hypervisor`
- `GET /VSATenantClientList/{instanceId}`
- `GET /v4/Cloud/OCI/QuickCreateLink/IAMCFT`

### identity_servers

- `GET /V4/IdentityServers`

### index_servers

- `GET /V4/IndexServers`

### instance

- `GET /databases/instances`

### instances

- `GET /V4/Instances`

### instant_clones

- `GET /V4/InstantClones`

### job

- `GET /Events`
- `GET /Events/{eventId}`
- `GET /Job`
- `GET /Job/{jobId}`
- `GET /Job/{jobId}/TaskDetails`
- `GET /Jobs/History`
- `GET /Jobs/active`

### key_management_server

- `GET /V4/KeyManagementServers`

### kubernetes

- `GET /V5/Kubernetes/Application`
- `GET /V5/Kubernetes/ApplicationGroup`
- `GET /V5/Kubernetes/Cluster`

### laptop

- `GET /V4/Laptop`

### laptop_devices

- `GET /Device`

### laptop_plan

- `GET /V4/LaptopPlan/{planId}/BackupDestinations`

### license

- `GET /Client/{clientId}/License`
- `GET /V4/License`

### local_storage

- `GET /V4/Storage/Local`

### media_agent

- `GET /MediaAgent/{MediaAgent}/ReconstructionJobs`
- `GET /MediaAgent/{MediaAgent}/RedistributionJobs`
- `GET /V4/DDB/MediaAgents`
- `GET /V4/mediaAgent`
- `GET /V4/mediaAgent/{mediaAgentId}`
- `GET /V4/mediaAgent/{mediaAgentId}/Associations`

### metallic

- `GET /V4/Hypervisors/azure`
- `GET /V4/azuredb/backupgateway`
- `GET /V4/azuredb/cloudaccount`
- `GET /V4/azuredb/mssql/credentials`
- `GET /V4/credentials/azure/cloudAccount`
- `GET /V4/credentials/azure/storage`
- `GET /V4/objectstorage/instance`
- `GET /V4/storage/cloud/azure`

### microsoft_azure_object_storage

- `GET /V4/azureobj/cloudaccounts`

### mssql_api

- `GET /sql/instances`

### multi_comm_cell

- `GET /V4/MultiCommCell`

### my_sqldatabases

- `GET /Client/{clientId}/instance/mysql/discover`

### network_topology

- `GET /CommServ/DataInterfacePairs`
- `GET /FirewallSummary/{clientId}`
- `GET /FirewallTopology`

### node

- `GET /V4/Nodes`

### office365

- `GET /V4/Office365`
- `GET /V4/Office365/Plans`

### one_drive

- `GET /V4/Office365/OneDrive`

### oracle_db

- `GET /Job/{JobId}/RMANLogs`

### organization

- `GET /EmailTemplates`
- `GET /NavigationSettings`
- `GET /Organization`

### plan

- `GET /Plan`
- `GET /V2/Plan/Eligible`
- `GET /V4/Plan/Summary`
- `GET /V4/Plan/{planId}/MediaAgents`
- `GET /V4/PlanIds`
- `GET /v2/Plan`
- `GET /v2/Plan/{PlanId}`
- `GET /v2/Plan/{PlanId}/Alerts`
- `GET /v2/Plan/{PlanId}/AssociatedEntities`
- `GET /v2/Plan/{PlanId}/Features`
- `GET /v2/Plan/{PlanId}/{entityName}`
- `GET /v4/Plan/Summary/{planId}`

### plan_rules

- `GET /V4/Plan/Rule`
- `GET /V4/Plan/Rule/Entities`
- `GET /V4/Plan/Rule/Entities/Exclude`
- `GET /V4/Plan/Rule/Settings`

### protection_group

- `GET /V4/ProtectionGroup/AWS`
- `GET /V4/ProtectionGroup/Azure`
- `GET /V4/ProtectionGroup/GCP`

### recovery_group

- `GET /RecoveryGroups`

### recovery_groups

- `GET /V4/RecoveryGroups`

### recovery_point_stores

- `GET /V4/RecoveryPointStores`

### recovery_runbook

- `GET /V4/RecoveryRunbook`

### recovery_target

- `GET /V4/RecoveryTargets`

### regions

- `GET /Regions`
- `GET /Regions/{regionId}`
- `GET /Regions/{regionId}/clients`
- `GET /V4/Regions`
- `GET /V4/Regions/{regionId}`

### replication

- `GET /Replications/Groups`
- `GET /Replications/Monitors/streaming`
- `GET /Task/{taskId}/Details`
- `GET /V2/Replications/Monitors/streaming`
- `GET /VMAllocationPolicy`

### replication_group

- `GET /V4/ReplicationGroup`

### replication_monitor

- `GET /V4/ArrayReplicationMonitor`

### reporting

- `GET /cr/reportsplusengine/datasets`
- `GET /cr/reportsplusengine/datasets/5e7dfa05-07cd-4beb-be9c-181a1722c2e8:571a5443-fb35-435e-b013-ecd1a6dcfb65/data`
- `GET /cr/reportsplusengine/datasets/METRICS_DEFAULT/data`
- `GET /cr/reportsplusengine/datasets/{dataSetId}/data`
- `GET /cr/reportsplusengine/reports?icludeDrafts=false&includeStoreVersions=false&includeMetricsReports=false`

### resource_pools

- `GET /V4/ResourcePool`

### restore

- `GET /Client/2/Hierarchy`

### role

- `GET /Role`
- `GET /Role/{roleId}`

### roles

- `GET /V4/Permissions`
- `GET /V4/Role`
- `GET /V4/Role/{roleId}`

### runbook_resources

- `GET /Cleanroom/Runbook/Resources`

### s3_object_storage

- `GET /CloudApps/AccessNodes`

### s3_vault

- `GET /V4/CVS3Endpoint/{ClientID}/state`

### salesforce

- `GET /MaskingPolicy/{InstanceId}`
- `GET /Salesforce/Organization`
- `GET /Salesforce/{ClientId}/GDPR/Requests`

### scheduleand_schedule_policy

- `GET /SchedulePolicy`
- `GET /SchedulePolicy/{taskId}`
- `GET /Schedules`
- `GET /Schedules/{taskId}`

### security_assembly

- `GET /Security/Assembly`

### server_group

- `GET /V4/ServerGroup`
- `POST /V4/ServerGroup`
- `DELETE /V4/ServerGroup/{serverGroupId}`
- `GET /V4/ServerGroup/{serverGroupId}`
- `PUT /V4/ServerGroup/{serverGroupId}`
- `GET /V4/ServerGroup/{serverGroupId}/DCPlan`

### server_plan

- `GET /V4/ServerPlan/{planId}`
- `GET /V4/ServerPlan/{planId}/BackupDestinations`
- `GET /V4/ServerPlan/{planId}/RPO`
- `GET /V5/ServerPlan/{planId}/BackupDestination/SourceCopy/Eligible`

### servers

- `GET /V4/Servers`
- `GET /V4/Servers/CommServeHostName`
- `GET /V4/Servers/Domain`
- `GET /V4/Servers/{serverId}/isVM`

### service_commcells

- `GET /V4/ServiceCommcells`

### sharepoint

- `GET /V4/Office365/SharePoint`

### snapshot

- `GET /V4/StorageArrays/Job/{jobId}/Snaps`
- `GET /V4/StorageArrays/{arrayId}/Snaps`

### snapshot_configurations

- `GET /V4/StorageArrays/Copy/{copyId}/Arrays/{arrayId}/Snap/Configs`
- `GET /V4/StorageArrays/Vendors`
- `GET /V4/StorageArrays/Vendors/{vendorId}`
- `GET /V4/StorageArrays/{arrayId}/Client/{clientId}/Snap/Configs`
- `GET /V4/StorageArrays/{arrayId}/Subclient/{subclientId}/Snap/Configs`

### snmp

- `GET /V4/Snmp`

### software_cache

- `GET /V4/SoftwareCache`
- `GET /V4/SoftwareCache/QualifiedServers`
- `GET /V4/SoftwareCache/{clientId}`

### solutions

- `GET /V4/Solutions`

### storage

- `GET /DriveController`
- `GET /Library`
- `GET /Library/{LibraryId}`
- `GET /MediaAgent`
- `GET /StoragePool`
- `GET /StoragePool/{StoragePoolId}`
- `GET /V2/StoragePolicy`
- `GET /V2/StoragePolicy/{storagePolicyId}`
- `GET /V2/StoragePolicy/{storagePolicyId}/Copy/{copyId}`
- `GET /V2/StoragePolicy/{storagePolicyId}/Copy/{copyId}/Size`
- `GET /V4/Storage/{storagePoolId}/associatedCopies`
- `GET /V4/StoragePool/{storagePoolId}/runningJobs`
- `GET /v2/MediaAgents`

### storage_arrays

- `GET /Snaps`

### subclient

- `GET /Subclient/{subclientId}/EmailPolicyAssociation`

### syslog_server

- `GET /V4/syslogServer`

### tape_storage

- `GET /V4/Storage/Tape`
- `GET /V4/Storage/Tape/Locations`
- `GET /V4/Storage/Tape/{libraryId}`
- `GET /V4/Storage/Tape/{libraryId}/Media`
- `GET /V4/VaultTrackerAction`
- `GET /V4/VaultTrackerPolicies`

### teams

- `GET /V4/Office365/Teams`

### threat_indicators

- `GET /Client/Anomaly`
- `GET /Client/AnomalyRecord`

### total_cost_of_ownership

- `GET /V4/TCO/AssessmentDetails`
- `GET /V4/TCO/AssessmentDiscoveryCriteria`
- `GET /V4/TCO/AuthenticatedUsers`

### untagged

- `GET /Asset/Discovery/Criteria`

### user

- `GET /User`
- `GET /User/{UserId}`
- `GET /UsersAndGroups`
- `GET /V4/user`
- `GET /V4/user/{userId}`

### user_group

- `GET /UserGroup`
- `GET /UserGroup/{UserGroupId}`
- `GET /V4/UserGroup`
- `POST /V4/UserGroup`
- `DELETE /V4/UserGroup/{userGroupId}`
- `GET /V4/UserGroup/{userGroupId}`
- `PUT /V4/UserGroup/{userGroupId}`

### virtual_machines

- `GET /V4/AccessNodes`
- `GET /V4/Kubernetes/ApplicationGroups`
- `GET /V4/Kubernetes/Applications`
- `GET /V4/Kubernetes/cluster`
- `GET /V4/VirtualMachines`

### virtualization

- `GET /Client/VMPseudoClient`
- `GET /VM`
- `GET /VSAclientlist`

### vm_group

- `GET /V4/VMGroups`

### vmprovisioning

- `GET /V4/VMProvisioning/Policy/{policyId}`
- `GET /V4/VMProvisioning/VirtualMachines`
- `GET /V4/VirtualLabs`

### workflow

- `GET /Workflow`
- `GET /Workflow/{WorkflowId}/definition`
- `GET /webhook`
