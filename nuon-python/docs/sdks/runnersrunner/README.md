# RunnersRunner
(*runners_runner*)

## Overview

runners/runner

### Available Operations

* [get_runner_job](#get_runner_job) - get runner job
* [get_runner_job_executions](#get_runner_job_executions) - get runner job executions
* [get_runner_job_plan](#get_runner_job_plan) - get runner job plan
* [get_terraform_states](#get_terraform_states) - get terraform states
* [get_terraform_workspace_state_by_id](#get_terraform_workspace_state_by_id) - get terraform state by ID
* [get_terraform_workspace_state_resources](#get_terraform_workspace_state_resources) - get terraform state resources
* [get_runner](#get_runner) - get a runner
* [get_terraform_current_state_data](#get_terraform_current_state_data) - get current terraform
* [update_terraform_state](#update_terraform_state) - update terraform state
* [create_terraform_workspace](#create_terraform_workspace) - create terraform workspace
* [delete_terraform_workspace](#delete_terraform_workspace) - delete terraform workspace
* [get_terraform_workspace](#get_terraform_workspace) - get  terraform workspace
* [get_terraform_workspaces](#get_terraform_workspaces) - get  terraform workspaces
* [lock_terraform_workspace](#lock_terraform_workspace) - lock terraform state
* [unlock_terraform_workspace](#unlock_terraform_workspace) - unlock terraform workspace

## get_runner_job

Return a runner job.


### Example Usage

<!-- UsageSnippet language="python" operationID="GetRunnerJob" method="get" path="/v1/runner-jobs/{runner_job_id}" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.runners_runner.get_runner_job(security=models.GetRunnerJobSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), runner_job_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `security`                                                          | [models.GetRunnerJobSecurity](../../models/getrunnerjobsecurity.md) | :heavy_check_mark:                                                  | N/A                                                                 |
| `runner_job_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | runner job ID                                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AppRunnerJob](../../models/apprunnerjob.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_runner_job_executions

Return executions for a runner job.


### Example Usage

<!-- UsageSnippet language="python" operationID="GetRunnerJobExecutions" method="get" path="/v1/runner-jobs/{runner_job_id}/executions" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.runners_runner.get_runner_job_executions(security=models.GetRunnerJobExecutionsSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), runner_job_id="<id>", offset=0, limit=10, page=0)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `security`                                                                              | [models.GetRunnerJobExecutionsSecurity](../../models/getrunnerjobexecutionssecurity.md) | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `runner_job_id`                                                                         | *str*                                                                                   | :heavy_check_mark:                                                                      | runner job ID                                                                           |
| `offset`                                                                                | *Optional[int]*                                                                         | :heavy_minus_sign:                                                                      | offset of results to return                                                             |
| `limit`                                                                                 | *Optional[int]*                                                                         | :heavy_minus_sign:                                                                      | limit of results to return                                                              |
| `page`                                                                                  | *Optional[int]*                                                                         | :heavy_minus_sign:                                                                      | page number of results to return                                                        |
| `x_nuon_pagination_enabled`                                                             | *Optional[bool]*                                                                        | :heavy_minus_sign:                                                                      | Enable pagination                                                                       |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[List[models.AppRunnerJobExecution]](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_runner_job_plan

Return a plan for a runner job.


### Example Usage

<!-- UsageSnippet language="python" operationID="GetRunnerJobPlan" method="get" path="/v1/runner-jobs/{runner_job_id}/plan" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.runners_runner.get_runner_job_plan(security=models.GetRunnerJobPlanSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), runner_job_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `security`                                                                  | [models.GetRunnerJobPlanSecurity](../../models/getrunnerjobplansecurity.md) | :heavy_check_mark:                                                          | N/A                                                                         |
| `runner_job_id`                                                             | *str*                                                                       | :heavy_check_mark:                                                          | runner job ID                                                               |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[str](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_terraform_states

get terraform states

### Example Usage

<!-- UsageSnippet language="python" operationID="GetTerraformStates" method="get" path="/v1/runners/terraform-workspace/{workspace_id}/states" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.runners_runner.get_terraform_states(security=models.GetTerraformStatesSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), workspace_id="<id>", offset=0, limit=10, page=0)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `security`                                                                      | [models.GetTerraformStatesSecurity](../../models/getterraformstatessecurity.md) | :heavy_check_mark:                                                              | N/A                                                                             |
| `workspace_id`                                                                  | *str*                                                                           | :heavy_check_mark:                                                              | workspace ID                                                                    |
| `offset`                                                                        | *Optional[int]*                                                                 | :heavy_minus_sign:                                                              | offset of results to return                                                     |
| `limit`                                                                         | *Optional[int]*                                                                 | :heavy_minus_sign:                                                              | limit of results to return                                                      |
| `page`                                                                          | *Optional[int]*                                                                 | :heavy_minus_sign:                                                              | page number of results to return                                                |
| `x_nuon_pagination_enabled`                                                     | *Optional[bool]*                                                                | :heavy_minus_sign:                                                              | Enable pagination                                                               |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[List[models.AppTerraformWorkspaceState]](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_terraform_workspace_state_by_id

get terraform state by ID

### Example Usage

<!-- UsageSnippet language="python" operationID="GetTerraformWorkspaceStateByID" method="get" path="/v1/runners/terraform-workspace/{workspace_id}/states/{state_id}" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.runners_runner.get_terraform_workspace_state_by_id(security=models.GetTerraformWorkspaceStateByIDSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), workspace_id="<id>", state_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                               | Type                                                                                                    | Required                                                                                                | Description                                                                                             |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `security`                                                                                              | [models.GetTerraformWorkspaceStateByIDSecurity](../../models/getterraformworkspacestatebyidsecurity.md) | :heavy_check_mark:                                                                                      | N/A                                                                                                     |
| `workspace_id`                                                                                          | *str*                                                                                                   | :heavy_check_mark:                                                                                      | workspace ID                                                                                            |
| `state_id`                                                                                              | *str*                                                                                                   | :heavy_check_mark:                                                                                      | state ID                                                                                                |
| `retries`                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                        | :heavy_minus_sign:                                                                                      | Configuration to override the default retry behavior of the client.                                     |

### Response

**[models.AppTerraformWorkspaceState](../../models/appterraformworkspacestate.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_terraform_workspace_state_resources

get terraform state resources

### Example Usage

<!-- UsageSnippet language="python" operationID="GetTerraformWorkspaceStateResources" method="get" path="/v1/runners/terraform-workspace/{workspace_id}/states/{state_id}/resources" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.runners_runner.get_terraform_workspace_state_resources(security=models.GetTerraformWorkspaceStateResourcesSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), workspace_id="<id>", state_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                         | Type                                                                                                              | Required                                                                                                          | Description                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                        | [models.GetTerraformWorkspaceStateResourcesSecurity](../../models/getterraformworkspacestateresourcessecurity.md) | :heavy_check_mark:                                                                                                | N/A                                                                                                               |
| `workspace_id`                                                                                                    | *str*                                                                                                             | :heavy_check_mark:                                                                                                | workspace ID                                                                                                      |
| `state_id`                                                                                                        | *str*                                                                                                             | :heavy_check_mark:                                                                                                | state ID                                                                                                          |
| `retries`                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                  | :heavy_minus_sign:                                                                                                | Configuration to override the default retry behavior of the client.                                               |

### Response

**[List[models.AppTerraformStateResource]](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_runner

Return a runner.


### Example Usage

<!-- UsageSnippet language="python" operationID="GetRunner" method="get" path="/v1/runners/{runner_id}" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.runners_runner.get_runner(security=models.GetRunnerSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), runner_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `security`                                                          | [models.GetRunnerSecurity](../../models/getrunnersecurity.md)       | :heavy_check_mark:                                                  | N/A                                                                 |
| `runner_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | runner ID                                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AppRunner](../../models/apprunner.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_terraform_current_state_data

get current terraform

### Example Usage

<!-- UsageSnippet language="python" operationID="GetTerraformCurrentStateData" method="get" path="/v1/terraform-backend" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.runners_runner.get_terraform_current_state_data(security=models.GetTerraformCurrentStateDataSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `security`                                                                                   | [models.GetTerraformCurrentStateDataSecurity](../../getterraformcurrentstatedatasecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[models.AppTerraformWorkspaceState](../../models/appterraformworkspacestate.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## update_terraform_state

update terraform state

### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateTerraformState" method="post" path="/v1/terraform-backend" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.runners_runner.update_terraform_state(security=models.UpdateTerraformStateSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), request={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `request`                                                                         | [models.UpdateTerraformStateRequest](../../models/updateterraformstaterequest.md) | :heavy_check_mark:                                                                | The request object to use for the request.                                        |
| `security`                                                                        | [models.UpdateTerraformStateSecurity](../../updateterraformstatesecurity.md)      | :heavy_check_mark:                                                                | The security requirements to use for the request.                                 |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.AppTerraformWorkspaceState](../../models/appterraformworkspacestate.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## create_terraform_workspace

create terraform workspace

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateTerraformWorkspace" method="post" path="/v1/terraform-workspace" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.runners_runner.create_terraform_workspace(security=models.CreateTerraformWorkspaceSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), owner_id="<id>", owner_type="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `security`                                                                                  | [models.CreateTerraformWorkspaceSecurity](../../models/createterraformworkspacesecurity.md) | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `owner_id`                                                                                  | *str*                                                                                       | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `owner_type`                                                                                | *str*                                                                                       | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |

### Response

**[models.AppTerraformWorkspace](../../models/appterraformworkspace.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## delete_terraform_workspace

delete terraform workspace

### Example Usage

<!-- UsageSnippet language="python" operationID="DeleteTerraformWorkspace" method="delete" path="/v1/terraform-workspace/{workspace_id}" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.runners_runner.delete_terraform_workspace(security=models.DeleteTerraformWorkspaceSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), workspace_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `security`                                                                                  | [models.DeleteTerraformWorkspaceSecurity](../../models/deleteterraformworkspacesecurity.md) | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `workspace_id`                                                                              | *str*                                                                                       | :heavy_check_mark:                                                                          | workspace ID                                                                                |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |

### Response

**[List[models.AppTerraformWorkspace]](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_terraform_workspace

get  terraform workspace

### Example Usage

<!-- UsageSnippet language="python" operationID="GetTerraformWorkspace" method="get" path="/v1/terraform-workspace/{workspace_id}" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.runners_runner.get_terraform_workspace(security=models.GetTerraformWorkspaceSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), workspace_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `security`                                                                            | [models.GetTerraformWorkspaceSecurity](../../models/getterraformworkspacesecurity.md) | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `workspace_id`                                                                        | *str*                                                                                 | :heavy_check_mark:                                                                    | workspace ID                                                                          |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[List[models.AppTerraformWorkspace]](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_terraform_workspaces

get  terraform workspaces

### Example Usage

<!-- UsageSnippet language="python" operationID="GetTerraformWorkspaces" method="get" path="/v1/terraform-workspaces" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.runners_runner.get_terraform_workspaces(security=models.GetTerraformWorkspacesSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `security`                                                                       | [models.GetTerraformWorkspacesSecurity](../../getterraformworkspacessecurity.md) | :heavy_check_mark:                                                               | The security requirements to use for the request.                                |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[List[models.AppTerraformWorkspace]](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## lock_terraform_workspace

lock terraform state

### Example Usage

<!-- UsageSnippet language="python" operationID="LockTerraformWorkspace" method="post" path="/v1/terraform-workspaces/{workspace_id}/lock" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.runners_runner.lock_terraform_workspace(security=models.LockTerraformWorkspaceSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), workspace_id="<id>", request_body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `security`                                                                                    | [models.LockTerraformWorkspaceSecurity](../../models/lockterraformworkspacesecurity.md)       | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `workspace_id`                                                                                | *str*                                                                                         | :heavy_check_mark:                                                                            | workspace ID                                                                                  |
| `request_body`                                                                                | [models.LockTerraformWorkspaceRequestBody](../../models/lockterraformworkspacerequestbody.md) | :heavy_check_mark:                                                                            | terraform workspace lock                                                                      |
| `job_id`                                                                                      | *Optional[str]*                                                                               | :heavy_minus_sign:                                                                            | job ID                                                                                        |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |

### Response

**[models.AppTerraformWorkspaceState](../../models/appterraformworkspacestate.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## unlock_terraform_workspace

unlock terraform workspace

### Example Usage

<!-- UsageSnippet language="python" operationID="UnlockTerraformWorkspace" method="post" path="/v1/terraform-workspaces/{workspace_id}/unlock" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.runners_runner.unlock_terraform_workspace(security=models.UnlockTerraformWorkspaceSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), workspace_id="<id>", request_body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                         | Type                                                                                              | Required                                                                                          | Description                                                                                       |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `security`                                                                                        | [models.UnlockTerraformWorkspaceSecurity](../../models/unlockterraformworkspacesecurity.md)       | :heavy_check_mark:                                                                                | N/A                                                                                               |
| `workspace_id`                                                                                    | *str*                                                                                             | :heavy_check_mark:                                                                                | workspace ID                                                                                      |
| `request_body`                                                                                    | [models.UnlockTerraformWorkspaceRequestBody](../../models/unlockterraformworkspacerequestbody.md) | :heavy_check_mark:                                                                                | terraform workspace unlock                                                                        |
| `retries`                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                  | :heavy_minus_sign:                                                                                | Configuration to override the default retry behavior of the client.                               |

### Response

**[models.AppTerraformWorkspaceState](../../models/appterraformworkspacestate.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |