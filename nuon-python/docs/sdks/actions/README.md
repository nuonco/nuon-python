# Actions
(*actions*)

## Overview

actions

### Available Operations

* [get_action_workflow_config](#get_action_workflow_config) - get an app action workflow config
* [delete_action_workflow](#delete_action_workflow) - delete an app
* [get_action_workflow](#get_action_workflow) - get an app action workflow
* [update_app_action_workflow](#update_app_action_workflow) - patch an app
* [get_action_workflow_configs](#get_action_workflow_configs) - get action workflow for an app
* [create_action_workflow_config](#create_action_workflow_config) - create action workflow config
* [get_action_workflow_latest_config](#get_action_workflow_latest_config) - get an app action workflow's latest config
* [get_action_workflows](#get_action_workflows) - get action workflows for an app
* [create_app_action_workflow](#create_app_action_workflow) - create an app
* [get_app_action_workflow](#get_app_action_workflow) - get an app action workflow
* [get_install_action_workflows_latest_runs](#get_install_action_workflows_latest_runs) - get latest runs for all action workflows by install id
* [get_install_action_workflow_runs](#get_install_action_workflow_runs) - get action workflow runs by install id
* [create_install_action_workflow_run](#create_install_action_workflow_run) - create an action workflow run for an install
* [get_install_action_workflow_run](#get_install_action_workflow_run) - get action workflow runs by install id and run id
* [get_install_action_workflow_run_step](#get_install_action_workflow_run_step) - get action workflow run step by install id and step id
* [get_install_action_workflow_recent_runs](#get_install_action_workflow_recent_runs) - get recent runs for an action workflow by install id

## get_action_workflow_config

get an app action workflow config

### Example Usage

<!-- UsageSnippet language="python" operationID="GetActionWorkflowConfig" method="get" path="/v1/action-workflows/configs/{action_workflow_config_id}" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.actions.get_action_workflow_config(security=models.GetActionWorkflowConfigSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), action_workflow_config_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `security`                                                                                | [models.GetActionWorkflowConfigSecurity](../../models/getactionworkflowconfigsecurity.md) | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `action_workflow_config_id`                                                               | *str*                                                                                     | :heavy_check_mark:                                                                        | action workflow config ID                                                                 |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |

### Response

**[models.AppActionWorkflowConfig](../../models/appactionworkflowconfig.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## delete_action_workflow

delete an app

### Example Usage

<!-- UsageSnippet language="python" operationID="DeleteActionWorkflow" method="delete" path="/v1/action-workflows/{action_workflow_id}" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.actions.delete_action_workflow(security=models.DeleteActionWorkflowSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), action_workflow_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `security`                                                                          | [models.DeleteActionWorkflowSecurity](../../models/deleteactionworkflowsecurity.md) | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `action_workflow_id`                                                                | *str*                                                                               | :heavy_check_mark:                                                                  | action workflow ID                                                                  |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[bool](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_action_workflow

get an app action workflow

### Example Usage

<!-- UsageSnippet language="python" operationID="GetActionWorkflow" method="get" path="/v1/action-workflows/{action_workflow_id}" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.actions.get_action_workflow(security=models.GetActionWorkflowSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), action_workflow_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `security`                                                                    | [models.GetActionWorkflowSecurity](../../models/getactionworkflowsecurity.md) | :heavy_check_mark:                                                            | N/A                                                                           |
| `action_workflow_id`                                                          | *str*                                                                         | :heavy_check_mark:                                                            | action workflow ID or name                                                    |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[models.AppActionWorkflow](../../models/appactionworkflow.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## update_app_action_workflow

patch an app

### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateAppActionWorkflow" method="patch" path="/v1/action-workflows/{action_workflow_id}" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.actions.update_app_action_workflow(security=models.UpdateAppActionWorkflowSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), action_workflow_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `security`                                                                                | [models.UpdateAppActionWorkflowSecurity](../../models/updateappactionworkflowsecurity.md) | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `action_workflow_id`                                                                      | *str*                                                                                     | :heavy_check_mark:                                                                        | action workflow ID                                                                        |
| `name`                                                                                    | *Optional[str]*                                                                           | :heavy_minus_sign:                                                                        | N/A                                                                                       |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |

### Response

**[models.AppActionWorkflow](../../models/appactionworkflow.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_action_workflow_configs

get action workflow for an app

### Example Usage

<!-- UsageSnippet language="python" operationID="GetActionWorkflowConfigs" method="get" path="/v1/action-workflows/{action_workflow_id}/configs" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.actions.get_action_workflow_configs(security=models.GetActionWorkflowConfigsSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), action_workflow_id="<id>", offset=0, limit=10, page=0)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `security`                                                                                  | [models.GetActionWorkflowConfigsSecurity](../../models/getactionworkflowconfigssecurity.md) | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `action_workflow_id`                                                                        | *str*                                                                                       | :heavy_check_mark:                                                                          | action workflow ID                                                                          |
| `offset`                                                                                    | *Optional[int]*                                                                             | :heavy_minus_sign:                                                                          | offset of results to return                                                                 |
| `limit`                                                                                     | *Optional[int]*                                                                             | :heavy_minus_sign:                                                                          | limit of results to return                                                                  |
| `page`                                                                                      | *Optional[int]*                                                                             | :heavy_minus_sign:                                                                          | page number of results to return                                                            |
| `x_nuon_pagination_enabled`                                                                 | *Optional[bool]*                                                                            | :heavy_minus_sign:                                                                          | Enable pagination                                                                           |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |

### Response

**[List[models.AppActionWorkflowConfig]](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## create_action_workflow_config

create action workflow config

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateActionWorkflowConfig" method="post" path="/v1/action-workflows/{action_workflow_id}/configs" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.actions.create_action_workflow_config(security=models.CreateActionWorkflowConfigSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), action_workflow_id="<id>", app_config_id="<id>", steps=[], triggers=[
        {
            "type": models.AppActionWorkflowTriggerType.POST_DEPLOY_ALL_COMPONENTS,
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                       | Type                                                                                                                            | Required                                                                                                                        | Description                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                      | [models.CreateActionWorkflowConfigSecurity](../../models/createactionworkflowconfigsecurity.md)                                 | :heavy_check_mark:                                                                                                              | N/A                                                                                                                             |
| `action_workflow_id`                                                                                                            | *str*                                                                                                                           | :heavy_check_mark:                                                                                                              | action workflow ID                                                                                                              |
| `app_config_id`                                                                                                                 | *str*                                                                                                                           | :heavy_check_mark:                                                                                                              | N/A                                                                                                                             |
| `steps`                                                                                                                         | List[[models.ServiceCreateActionWorkflowConfigStepRequest](../../models/servicecreateactionworkflowconfigsteprequest.md)]       | :heavy_check_mark:                                                                                                              | N/A                                                                                                                             |
| `triggers`                                                                                                                      | List[[models.ServiceCreateActionWorkflowConfigTriggerRequest](../../models/servicecreateactionworkflowconfigtriggerrequest.md)] | :heavy_check_mark:                                                                                                              | N/A                                                                                                                             |
| `dependencies`                                                                                                                  | List[*str*]                                                                                                                     | :heavy_minus_sign:                                                                                                              | N/A                                                                                                                             |
| `references`                                                                                                                    | List[*str*]                                                                                                                     | :heavy_minus_sign:                                                                                                              | N/A                                                                                                                             |
| `timeout`                                                                                                                       | *Optional[int]*                                                                                                                 | :heavy_minus_sign:                                                                                                              | N/A                                                                                                                             |
| `retries`                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                | :heavy_minus_sign:                                                                                                              | Configuration to override the default retry behavior of the client.                                                             |

### Response

**[models.AppActionWorkflowConfig](../../models/appactionworkflowconfig.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_action_workflow_latest_config

Return the latest config for an action workflow.


### Example Usage

<!-- UsageSnippet language="python" operationID="GetActionWorkflowLatestConfig" method="get" path="/v1/action-workflows/{action_workflow_id}/latest-config" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.actions.get_action_workflow_latest_config(security=models.GetActionWorkflowLatestConfigSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), action_workflow_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `security`                                                                                            | [models.GetActionWorkflowLatestConfigSecurity](../../models/getactionworkflowlatestconfigsecurity.md) | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `action_workflow_id`                                                                                  | *str*                                                                                                 | :heavy_check_mark:                                                                                    | action workflow ID                                                                                    |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |

### Response

**[models.AppActionWorkflowConfig](../../models/appactionworkflowconfig.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_action_workflows

get action workflows for an app

### Example Usage

<!-- UsageSnippet language="python" operationID="GetActionWorkflows" method="get" path="/v1/apps/{app_id}/action-workflows" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.actions.get_action_workflows(security=models.GetActionWorkflowsSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), app_id="<id>", offset=0, limit=10, page=0)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `security`                                                                      | [models.GetActionWorkflowsSecurity](../../models/getactionworkflowssecurity.md) | :heavy_check_mark:                                                              | N/A                                                                             |
| `app_id`                                                                        | *str*                                                                           | :heavy_check_mark:                                                              | app ID                                                                          |
| `q`                                                                             | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | search query to filter action workflows by name                                 |
| `offset`                                                                        | *Optional[int]*                                                                 | :heavy_minus_sign:                                                              | offset of results to return                                                     |
| `limit`                                                                         | *Optional[int]*                                                                 | :heavy_minus_sign:                                                              | limit of results to return                                                      |
| `page`                                                                          | *Optional[int]*                                                                 | :heavy_minus_sign:                                                              | page number of results to return                                                |
| `x_nuon_pagination_enabled`                                                     | *Optional[bool]*                                                                | :heavy_minus_sign:                                                              | Enable pagination                                                               |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[List[models.AppActionWorkflow]](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## create_app_action_workflow

create an app

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateAppActionWorkflow" method="post" path="/v1/apps/{app_id}/action-workflows" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.actions.create_app_action_workflow(security=models.CreateAppActionWorkflowSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), app_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `security`                                                                                | [models.CreateAppActionWorkflowSecurity](../../models/createappactionworkflowsecurity.md) | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `app_id`                                                                                  | *str*                                                                                     | :heavy_check_mark:                                                                        | app ID                                                                                    |
| `name`                                                                                    | *Optional[str]*                                                                           | :heavy_minus_sign:                                                                        | N/A                                                                                       |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |

### Response

**[models.AppActionWorkflow](../../models/appactionworkflow.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_app_action_workflow

get an app action workflow

### Example Usage

<!-- UsageSnippet language="python" operationID="GetAppActionWorkflow" method="get" path="/v1/apps/{app_id}/action-workflows/{action_workflow_id}" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.actions.get_app_action_workflow(security=models.GetAppActionWorkflowSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), app_id="<id>", action_workflow_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `security`                                                                          | [models.GetAppActionWorkflowSecurity](../../models/getappactionworkflowsecurity.md) | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `app_id`                                                                            | *str*                                                                               | :heavy_check_mark:                                                                  | app ID or name                                                                      |
| `action_workflow_id`                                                                | *str*                                                                               | :heavy_check_mark:                                                                  | action workflow ID or name                                                          |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.AppActionWorkflow](../../models/appactionworkflow.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_install_action_workflows_latest_runs

get latest runs for all action workflows by install id

### Example Usage

<!-- UsageSnippet language="python" operationID="GetInstallActionWorkflowsLatestRuns" method="get" path="/v1/installs/{install_id}/action-workflows/latest-runs" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.actions.get_install_action_workflows_latest_runs(security=models.GetInstallActionWorkflowsLatestRunsSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), install_id="<id>", offset=0, limit=10, page=0)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                         | Type                                                                                                              | Required                                                                                                          | Description                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                        | [models.GetInstallActionWorkflowsLatestRunsSecurity](../../models/getinstallactionworkflowslatestrunssecurity.md) | :heavy_check_mark:                                                                                                | N/A                                                                                                               |
| `install_id`                                                                                                      | *str*                                                                                                             | :heavy_check_mark:                                                                                                | install ID                                                                                                        |
| `trigger_types`                                                                                                   | *Optional[str]*                                                                                                   | :heavy_minus_sign:                                                                                                | filter by action workflow trigger by types                                                                        |
| `offset`                                                                                                          | *Optional[int]*                                                                                                   | :heavy_minus_sign:                                                                                                | offset of results to return                                                                                       |
| `limit`                                                                                                           | *Optional[int]*                                                                                                   | :heavy_minus_sign:                                                                                                | limit of results to return                                                                                        |
| `page`                                                                                                            | *Optional[int]*                                                                                                   | :heavy_minus_sign:                                                                                                | page number of results to return                                                                                  |
| `q`                                                                                                               | *Optional[str]*                                                                                                   | :heavy_minus_sign:                                                                                                | search query for action workflow name                                                                             |
| `x_nuon_pagination_enabled`                                                                                       | *Optional[bool]*                                                                                                  | :heavy_minus_sign:                                                                                                | Enable pagination                                                                                                 |
| `retries`                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                  | :heavy_minus_sign:                                                                                                | Configuration to override the default retry behavior of the client.                                               |

### Response

**[List[models.AppInstallActionWorkflow]](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_install_action_workflow_runs

get action workflow runs by install id

### Example Usage

<!-- UsageSnippet language="python" operationID="GetInstallActionWorkflowRuns" method="get" path="/v1/installs/{install_id}/action-workflows/runs" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.actions.get_install_action_workflow_runs(security=models.GetInstallActionWorkflowRunsSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), install_id="<id>", offset=0, limit=10, page=0)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                           | Type                                                                                                | Required                                                                                            | Description                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `security`                                                                                          | [models.GetInstallActionWorkflowRunsSecurity](../../models/getinstallactionworkflowrunssecurity.md) | :heavy_check_mark:                                                                                  | N/A                                                                                                 |
| `install_id`                                                                                        | *str*                                                                                               | :heavy_check_mark:                                                                                  | install ID                                                                                          |
| `offset`                                                                                            | *Optional[int]*                                                                                     | :heavy_minus_sign:                                                                                  | offset of results to return                                                                         |
| `limit`                                                                                             | *Optional[int]*                                                                                     | :heavy_minus_sign:                                                                                  | limit of results to return                                                                          |
| `page`                                                                                              | *Optional[int]*                                                                                     | :heavy_minus_sign:                                                                                  | page number of results to return                                                                    |
| `x_nuon_pagination_enabled`                                                                         | *Optional[bool]*                                                                                    | :heavy_minus_sign:                                                                                  | Enable pagination                                                                                   |
| `retries`                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                    | :heavy_minus_sign:                                                                                  | Configuration to override the default retry behavior of the client.                                 |

### Response

**[List[models.AppInstallActionWorkflowRun]](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## create_install_action_workflow_run

AppWorkflowConfigId param has been deprecated and is no longer being consumed, the api uses currently install id to lookup related appworkflowconfigId


### Example Usage

<!-- UsageSnippet language="python" operationID="CreateInstallActionWorkflowRun" method="post" path="/v1/installs/{install_id}/action-workflows/runs" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.actions.create_install_action_workflow_run(security=models.CreateInstallActionWorkflowRunSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), install_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                               | Type                                                                                                    | Required                                                                                                | Description                                                                                             |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `security`                                                                                              | [models.CreateInstallActionWorkflowRunSecurity](../../models/createinstallactionworkflowrunsecurity.md) | :heavy_check_mark:                                                                                      | N/A                                                                                                     |
| `install_id`                                                                                            | *str*                                                                                                   | :heavy_check_mark:                                                                                      | install ID                                                                                              |
| `action_workflow_config_id`                                                                             | *Optional[str]*                                                                                         | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |
| `run_env_vars`                                                                                          | Dict[str, *str*]                                                                                        | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |
| `retries`                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                        | :heavy_minus_sign:                                                                                      | Configuration to override the default retry behavior of the client.                                     |

### Response

**[str](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_install_action_workflow_run

get action workflow runs by install id and run id

### Example Usage

<!-- UsageSnippet language="python" operationID="GetInstallActionWorkflowRun" method="get" path="/v1/installs/{install_id}/action-workflows/runs/{run_id}" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.actions.get_install_action_workflow_run(security=models.GetInstallActionWorkflowRunSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), install_id="<id>", run_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                         | Type                                                                                              | Required                                                                                          | Description                                                                                       |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `security`                                                                                        | [models.GetInstallActionWorkflowRunSecurity](../../models/getinstallactionworkflowrunsecurity.md) | :heavy_check_mark:                                                                                | N/A                                                                                               |
| `install_id`                                                                                      | *str*                                                                                             | :heavy_check_mark:                                                                                | install ID                                                                                        |
| `run_id`                                                                                          | *str*                                                                                             | :heavy_check_mark:                                                                                | run ID                                                                                            |
| `retries`                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                  | :heavy_minus_sign:                                                                                | Configuration to override the default retry behavior of the client.                               |

### Response

**[models.AppInstallActionWorkflowRun](../../models/appinstallactionworkflowrun.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_install_action_workflow_run_step

Get an install action workflow run step.


### Example Usage

<!-- UsageSnippet language="python" operationID="GetInstallActionWorkflowRunStep" method="get" path="/v1/installs/{install_id}/action-workflows/runs/{workflow_run_id}/steps/{step_id}" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.actions.get_install_action_workflow_run_step(security=models.GetInstallActionWorkflowRunStepSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), install_id="<id>", workflow_run_id="<id>", step_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                 | Type                                                                                                      | Required                                                                                                  | Description                                                                                               |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                | [models.GetInstallActionWorkflowRunStepSecurity](../../models/getinstallactionworkflowrunstepsecurity.md) | :heavy_check_mark:                                                                                        | N/A                                                                                                       |
| `install_id`                                                                                              | *str*                                                                                                     | :heavy_check_mark:                                                                                        | install ID                                                                                                |
| `workflow_run_id`                                                                                         | *str*                                                                                                     | :heavy_check_mark:                                                                                        | workflow run ID                                                                                           |
| `step_id`                                                                                                 | *str*                                                                                                     | :heavy_check_mark:                                                                                        | step ID                                                                                                   |
| `retries`                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                          | :heavy_minus_sign:                                                                                        | Configuration to override the default retry behavior of the client.                                       |

### Response

**[models.AppInstallActionWorkflowRunStep](../../models/appinstallactionworkflowrunstep.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_install_action_workflow_recent_runs

get recent runs for an action workflow by install id

### Example Usage

<!-- UsageSnippet language="python" operationID="GetInstallActionWorkflowRecentRuns" method="get" path="/v1/installs/{install_id}/action-workflows/{action_workflow_id}/recent-runs" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.actions.get_install_action_workflow_recent_runs(security=models.GetInstallActionWorkflowRecentRunsSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), install_id="<id>", action_workflow_id="<id>", offset=0, limit=10, page=0)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                       | Type                                                                                                            | Required                                                                                                        | Description                                                                                                     |
| --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                      | [models.GetInstallActionWorkflowRecentRunsSecurity](../../models/getinstallactionworkflowrecentrunssecurity.md) | :heavy_check_mark:                                                                                              | N/A                                                                                                             |
| `install_id`                                                                                                    | *str*                                                                                                           | :heavy_check_mark:                                                                                              | install ID                                                                                                      |
| `action_workflow_id`                                                                                            | *str*                                                                                                           | :heavy_check_mark:                                                                                              | action workflow ID                                                                                              |
| `offset`                                                                                                        | *Optional[int]*                                                                                                 | :heavy_minus_sign:                                                                                              | offset of results to return                                                                                     |
| `limit`                                                                                                         | *Optional[int]*                                                                                                 | :heavy_minus_sign:                                                                                              | limit of results to return                                                                                      |
| `page`                                                                                                          | *Optional[int]*                                                                                                 | :heavy_minus_sign:                                                                                              | page number of results to return                                                                                |
| `x_nuon_pagination_enabled`                                                                                     | *Optional[bool]*                                                                                                | :heavy_minus_sign:                                                                                              | Enable pagination                                                                                               |
| `retries`                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                | :heavy_minus_sign:                                                                                              | Configuration to override the default retry behavior of the client.                                             |

### Response

**[models.AppInstallActionWorkflow](../../models/appinstallactionworkflow.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |