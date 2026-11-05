# `cv.raw.workflow`: every read, live

> Recorded from a real Commvault 11.46 CommServe (11 SP46.30) on 2026-11-05 18:50 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `list_webhook` - GET /webhook

```python
cv.raw.workflow.list_webhook()
```

**On the wire**

- `GET /webhook` -> **200** (0.13 s)

  <details><summary>Answer</summary>

  ```json
  {
    "total": 0
  }
  ```

  </details>

## `list_workflow` - GET /Workflow

```python
cv.raw.workflow.list_workflow()
```

**On the wire**

- `GET /Workflow` -> **200** (0.44 s)

  <details><summary>Answer</summary>

  ```json
  {
    "container": [
      {
        "modifiedTime": 1787248203,
        "flags": 14,
        "interactive": 0,
        "description": "<html><div>&#xa;      APSS Add SysAdmin Role v1.0.2&#xa;    </div>&#xa;    <div>&#xa;      <br>&#xa;      This workflow will assign the SQL SYSADMIN role to the impersonation &#xa;      account that is provided. SA account credentials are required for this &#xa;      workflow.&#xa;    </div>&#xa;    <div>&#xa;      &#xa;    </div>&#xa;    <div>&#xa;      IMPORTANT: This workflow may take time to l... (528 characters)",
        "remoteRevision": "",
        "createdTime": 1787248203,
        "whatsNew": "",
        "version": 1,
        "revision": "$Revision: 192.0.2.49 $",
        "uniqueGuid": "be07421e-54db-4a99-bf99-e036f07b17b8",
        "restricted": 0,
        "creator": {
          "userGUID": "0172CBC5-2369-4A1E-A2D2-E4DB97635090",
          "userName": "user-02",
          "userId": 1
        },
        "deployments": [
          {
            "inputsXml": "<inputs />",
            "inputSchema": "<configuration xmlDefinition=\"&lt;configuration /&gt;\"><schema name=\"configuration\" className=\"\" defaultValue=\"\" type=\"\" listType=\"0\" attribute=\"0\" /></configuration>",
            "flags": 1,
            "description": "<html><div>&#xa;      APSS Add SysAdmin Role v1.0.2&#xa;    </div>&#xa;    <div>&#xa;      <br>&#xa;      This workflow will assign the SQL SYSADMIN role to the impersonation &#xa;      account that is provided. SA account credentials are required for this &#xa;      workflow.&#xa;    </div>&#xa;    <div>&#xa;      &#xa;    </div>&#xa;    <div>&#xa;      IMPORTANT: This workflow may take time to l... (528 characters)",
            "deployed": 1787607160,
            "deployId": 18,
            "version": 1,
            "client": {
              "clientName": "commserve-02",
              "displayName": "commserve-02",
              "clientId": 2
            },
            "inputForm": {
              "destPath": "H:\\commvaultdata\\JobResults",
              "properties": {
                "css": "",
                "javaScript": ""
              }
            }
          }
        ],
        "entity": {
          "workflowName": "APSS Add SysAdmin Role",
          "workflowId": 36
        }
      },
      {
        "modifiedTime": 1787248203,
        "flags": 14,
        "interactive": 0,
        "description": "<html><div>&#xa;      This workflow requires &quot;Proactive Support&quot; to be enabled in the Cloud &#xa;      Metrics control panel, and requires the &quot;APSS - Enable Activity for &#xa;      Disabled Subclients&quot; custom report.&#xa;    </div>&#xa;    <div>&#xa;      &#xa;    </div>&#xa;    <div>&#xa;      Run the custom report and click the button next to the subclient that &#xa;      wi... (655 characters)",
        "remoteRevision": "",
        "createdTime": 1787248203,
        "whatsNew": "",
        "version": 1,
        "revision": "$Revision: 192.0.2.49 $",
        "uniqueGuid": "ba458253-5bc1-4e65-9786-aa063230a212",
        "restricted": 0,
        "creator": {
          "userGUID": "0172CBC5-2369-4A1E-A2D2-E4DB97635090",
          "userName": "user-02",
          "userId": 1
        },
        "deployments": [
          {
            "inputsXml": "<inputs><subclientID class=\"java.lang.String\" _list_=\"false\" /><isGroupDisabled class=\"java.lang.Integer\" _list_=\"false\">0</isGroupDisabled><isClientDisabled class=\"java.lang.Integer\" _list_=\"false\">0</isClientDisabled><isAgentDisabled class=\"java.lang.Integer\" _list_=\"false\">0</isAgentDisabled><isSubclientDisabled class=\"java.lang.Integer\" _list_=\"false\">0</isSubclientDisabled><Client class=\"java... (619 characters)",
            "inputSchema": "<configuration xmlDefinition=\"&lt;configuration /&gt;\"><schema name=\"configuration\" className=\"\" defaultValue=\"\" type=\"\" listType=\"0\" attribute=\"0\" /></configuration>",
            "flags": 1,
            "description": "<html><div>&#xa;      This workflow requires &quot;Proactive Support&quot; to be enabled in the Cloud &#xa;      Metrics control panel, and requires the &quot;APSS - Enable Activity for &#xa;      Disabled Subclients&quot; custom report.&#xa;    </div>&#xa;    <div>&#xa;      &#xa;    </div>&#xa;    <div>&#xa;      Run the custom report and click the button next to the subclient that &#xa;      wi... (655 characters)",
            "deployed": 1787607161,
            "deployId": 19,
            "version": 1,
            "client": {
              "clientName": "commserve-02",
              "displayName": "commserve-02",
              "clientId": 2
            },
            "inputForm": {
              "destPath": "H:\\commvaultdata\\JobResults",
              "entries": [
                {
                  "hidden": false,
                  "defaultValue": "0",
                  "displayName": "Group Activity Is Disabled",
                  "className": "java.lang.Integer",
                  "type": "{http://host-89/2001/XMLSchema}integer",
                  "listType": false,
                  "required": false,
                  "inputName": "isGroupDisabled",
                  "minimumValue": "",
                  "inputType": "java.lang.Integer",
                  "attribute": false,
                  "documentation": "",
                  "readOnly": true,
                  "searchable": false,
                  "controlType": 0,
                  "name": "isGroupDisabled",
                  "maximumValue": "",
                  "defaultValues": [
                    "0"
                  ]
                },
                {
                  "hidden": false,
                  "displayName": "",
                  "className": "java.lang.String",
                  "type": "{http://host-89/2001/XMLSchema}string",
                  "listType": false,
                  "required": false,
                  "inputName": "Client",
                  "minimumValue": "",
                  "inputType": "java.lang.String",
                  "attribute": false,
                  "documentation": "",
                  "readOnly": true,
                  "searchable": false,
                  "controlType": 0,
                  "name": "Client",
                  "maximumValue": ""
                },
                {
                  "hidden": false,
                  "defaultValue": "0",
                  "displayName": "Client Activity Is Disabled",
                  "className": "java.lang.Integer",
                  "type": "{http://host-89/2001/XMLSchema}integer",
                  "listType": false,
                  "required": false,
                  "inputName": "isClientDisabled",
                  "minimumValue": "",
                  "inputType": "java.lang.Integer",
                  "attribute": false,
                  "documentation": "",
                  "readOnly": true,
                  "searchable": false,
                  "controlType": 0,
                  "name": "isClientDisabled",
                  "maximumValue": "",
                  "defaultValues": [
                    "0"
                  ]
                },
                "... 6 more"
              ],
              "properties": {
                "css": "",
                "javaScript": ""
              }
            }
          }
        ],
        "entity": {
          "workflowName": "APSS Enable Subclient Activity",
          "workflowId": 37
        }
      },
      {
        "modifiedTime": 1787248204,
        "flags": 14,
        "interactive": 0,
        "description": "This workflow requires \"Proactive Support\" to be enabled under the Cloud Metrics Reporting control panel and requires the \"APSS - Missed SLA Report\" from the software store.&#xd;&#xa;&#xd;&#xa;Run the custom report in the webconsole, and click the button next to the subclient that needs to be excluded from SLA.",
        "remoteRevision": "",
        "createdTime": 1787248204,
        "whatsNew": "",
        "version": 1,
        "revision": "$Revision: 192.0.2.49 $",
        "uniqueGuid": "8057d4af-6f15-47bd-8438-b12094a55c14",
        "restricted": 0,
        "creator": {
          "userGUID": "0172CBC5-2369-4A1E-A2D2-E4DB97635090",
          "userName": "user-02",
          "userId": 1
        },
        "deployments": [
          {
            "inputsXml": "<inputs><subclientID class=\"java.lang.String\" _list_=\"false\" /><Client class=\"java.lang.String\" _list_=\"false\" /><Agent class=\"java.lang.String\" _list_=\"false\" /><Subclient class=\"java.lang.String\" _list_=\"false\" /></inputs>",
            "inputSchema": "<configuration xmlDefinition=\"&lt;configuration /&gt;\"><schema name=\"configuration\" className=\"\" defaultValue=\"\" type=\"\" listType=\"0\" attribute=\"0\" /></configuration>",
            "flags": 1,
            "description": "This workflow requires \"Proactive Support\" to be enabled under the Cloud Metrics Reporting control panel and requires the \"APSS - Missed SLA Report\" from the software store.&#xd;&#xa;&#xd;&#xa;Run the custom report in the webconsole, and click the button next to the subclient that needs to be excluded from SLA.",
            "deployed": 1787607164,
            "deployId": 29,
            "version": 1,
            "client": {
              "clientName": "commserve-02",
              "displayName": "commserve-02",
              "clientId": 2
            },
            "inputForm": {
              "destPath": "H:\\commvaultdata\\JobResults",
              "entries": [
                {
                  "hidden": false,
                  "displayName": "Client:",
                  "className": "java.lang.String",
                  "type": "{http://host-89/2001/XMLSchema}string",
                  "listType": false,
                  "required": false,
                  "inputName": "Client",
                  "minimumValue": "",
                  "inputType": "java.lang.String",
                  "attribute": false,
                  "documentation": "",
                  "readOnly": true,
                  "searchable": false,
                  "controlType": 0,
                  "name": "Client",
                  "maximumValue": ""
                },
                {
                  "hidden": false,
                  "displayName": "Agent:",
                  "className": "java.lang.String",
                  "type": "{http://host-89/2001/XMLSchema}string",
                  "listType": false,
                  "required": false,
                  "inputName": "Agent",
                  "minimumValue": "",
                  "inputType": "java.lang.String",
                  "attribute": false,
                  "documentation": "",
                  "readOnly": true,
                  "searchable": false,
                  "controlType": 0,
                  "name": "Agent",
                  "maximumValue": ""
                },
                {
                  "hidden": false,
                  "displayName": "Subclient:",
                  "className": "java.lang.String",
                  "type": "{http://host-89/2001/XMLSchema}string",
                  "listType": false,
                  "required": false,
                  "inputName": "Subclient",
                  "minimumValue": "",
                  "inputType": "java.lang.String",
                  "attribute": false,
                  "documentation": "",
                  "readOnly": true,
                  "searchable": false,
                  "controlType": 0,
                  "name": "Subclient",
                  "maximumValue": ""
                },
                "... 1 more"
              ],
              "properties": {
                "css": "",
                "javaScript": ""
              }
            }
          }
        ],
        "entity": {
          "workflowName": "APSS Exclude SLA",
          "workflowId": 47
        }
      },
      "... 65 more"
    ]
  }
  ```

  </details>

## `get_wapi` - GET /wapi/{workflowname}

> **SKIPPED** on this run: nothing on this server to look at here

```python
cv.raw.workflow.get_wapi(...)
```

## `get_workflow_definition` - GET /Workflow/{WorkflowId}/definition

```python
cv.raw.workflow.get_workflow_definition('1')
```

**On the wire**

- `GET /Workflow/1/definition` -> **200** (0.15 s)

  <details><summary>Answer</summary>

  ```
  <Workflow_GetWorkflowResponse />
  ```

  </details>
