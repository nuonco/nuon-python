# Runners
(*runners*)

## Overview

runners

### Available Operations

* [get_log_stream](#get_log_stream) - get a log stream
* [log_stream_read_logs](#log_stream_read_logs) - read a log stream's logs
* [get_runner_job](#get_runner_job) - get runner job
* [cancel_runner_job](#cancel_runner_job) - cancel runner job
* [get_runner_job_executions](#get_runner_job_executions) - get runner job executions
* [get_runner_job_plan](#get_runner_job_plan) - get runner job plan
* [get_terraform_workspace_states_json](#get_terraform_workspace_states_json) - get terraform states json
* [get_terraform_workspace_states_json_by_id](#get_terraform_workspace_states_json_by_id) - get terraform state json by id. This output is same as "terraform show --json"
* [get_terraform_workspace_state_json_resources](#get_terraform_workspace_state_json_resources) - get terraform state resources. This output is similar to "terraform state list"
* [get_terraform_states](#get_terraform_states) - get terraform states
* [get_terraform_workspace_state_by_id](#get_terraform_workspace_state_by_id) - get terraform state by ID
* [get_terraform_workspace_state_resources](#get_terraform_workspace_state_resources) - get terraform state resources
* [get_runner](#get_runner) - get a runner
* [get_runner_connect_status](#get_runner_connect_status) - get a runner connection satus based on heartbeat
* [force_shut_down_runner](#force_shut_down_runner) - force shut down a runner
* [graceful_shut_down_runner](#graceful_shut_down_runner) - shut down a runner
* [get_runner_jobs](#get_runner_jobs) - get runner jobs
* [get_runner_latest_heart_beat](#get_runner_latest_heart_beat) - get a runner
* [shut_down_runner_mng](#shut_down_runner_mng) - shut down an install runner management process
* [mng_vm_shut_down](#mng_vm_shut_down) - shut down an install runner VM
* [update_runner_mng](#update_runner_mng) - shut down an install runner management process
* [get_runner_recent_health_checks](#get_runner_recent_health_checks) - get recent health checks
* [get_runner_settings](#get_runner_settings) - get runner settings
* [update_runner_settings](#update_runner_settings) - update a runner job execution
* [get_terraform_current_state_data](#get_terraform_current_state_data) - get current terraform
* [update_terraform_state](#update_terraform_state) - update terraform state
* [create_terraform_workspace](#create_terraform_workspace) - create terraform workspace
* [delete_terraform_workspace](#delete_terraform_workspace) - delete terraform workspace
* [get_terraform_workspace](#get_terraform_workspace) - get  terraform workspace
* [get_terraform_workspaces](#get_terraform_workspaces) - get  terraform workspaces
* [get_terraform_workspace_lock](#get_terraform_workspace_lock) - get terraform workspace lock
* [lock_terraform_workspace](#lock_terraform_workspace) - lock terraform state
* [unlock_terraform_workspace](#unlock_terraform_workspace) - unlock terraform workspace

## get_log_stream

Return a log stream.


### Example Usage

<!-- UsageSnippet language="python" operationID="GetLogStream" method="get" path="/v1/log-streams/{log_stream_id}" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.runners.get_log_stream(security=models.GetLogStreamSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), log_stream_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `security`                                                          | [models.GetLogStreamSecurity](../../models/getlogstreamsecurity.md) | :heavy_check_mark:                                                  | N/A                                                                 |
| `log_stream_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | log stream ID                                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AppLogStream](../../models/applogstream.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## log_stream_read_logs

Read OTEL formatted logs for a log stream.


### Example Usage

<!-- UsageSnippet language="python" operationID="LogStreamReadLogs" method="get" path="/v1/log-streams/{log_stream_id}/logs" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.runners.log_stream_read_logs(security=models.LogStreamReadLogsSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), log_stream_id="<id>", x_nuon_api_offset="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `security`                                                                    | [models.LogStreamReadLogsSecurity](../../models/logstreamreadlogssecurity.md) | :heavy_check_mark:                                                            | N/A                                                                           |
| `log_stream_id`                                                               | *str*                                                                         | :heavy_check_mark:                                                            | log stream ID                                                                 |
| `x_nuon_api_offset`                                                           | *str*                                                                         | :heavy_check_mark:                                                            | log stream offset                                                             |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[List[models.AppOtelLogRecord]](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_runner_job

Return a runner job.


### Example Usage

<!-- UsageSnippet language="python" operationID="GetRunnerJob" method="get" path="/v1/runner-jobs/{runner_job_id}" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.runners.get_runner_job(security=models.GetRunnerJobSecurity(
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

## cancel_runner_job

Cancel a runner job.


### Example Usage

<!-- UsageSnippet language="python" operationID="CancelRunnerJob" method="post" path="/v1/runner-jobs/{runner_job_id}/cancel" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.runners.cancel_runner_job(security=models.CancelRunnerJobSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), runner_job_id="<id>", service_cancel_runner_job_request={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `security`                                                                            | [models.CancelRunnerJobSecurity](../../models/cancelrunnerjobsecurity.md)             | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `runner_job_id`                                                                       | *str*                                                                                 | :heavy_check_mark:                                                                    | runner job ID                                                                         |
| `service_cancel_runner_job_request`                                                   | [models.ServiceCancelRunnerJobRequest](../../models/servicecancelrunnerjobrequest.md) | :heavy_check_mark:                                                                    | Input                                                                                 |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

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

    res = n_client.runners.get_runner_job_executions(security=models.GetRunnerJobExecutionsSecurity(
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

    res = n_client.runners.get_runner_job_plan(security=models.GetRunnerJobPlanSecurity(
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

## get_terraform_workspace_states_json

get terraform states json

### Example Usage

<!-- UsageSnippet language="python" operationID="GetTerraformWorkspaceStatesJSON" method="get" path="/v1/runners/terraform-workspace/{workspace_id}/state-json" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.runners.get_terraform_workspace_states_json(security=models.GetTerraformWorkspaceStatesJSONSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), workspace_id="<id>", offset=0, limit=10, page=0)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                 | Type                                                                                                      | Required                                                                                                  | Description                                                                                               |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                | [models.GetTerraformWorkspaceStatesJSONSecurity](../../models/getterraformworkspacestatesjsonsecurity.md) | :heavy_check_mark:                                                                                        | N/A                                                                                                       |
| `workspace_id`                                                                                            | *str*                                                                                                     | :heavy_check_mark:                                                                                        | workspace ID                                                                                              |
| `offset`                                                                                                  | *Optional[int]*                                                                                           | :heavy_minus_sign:                                                                                        | offset of results to return                                                                               |
| `limit`                                                                                                   | *Optional[int]*                                                                                           | :heavy_minus_sign:                                                                                        | limit of results to return                                                                                |
| `page`                                                                                                    | *Optional[int]*                                                                                           | :heavy_minus_sign:                                                                                        | page number of results to return                                                                          |
| `x_nuon_pagination_enabled`                                                                               | *Optional[bool]*                                                                                          | :heavy_minus_sign:                                                                                        | Enable pagination                                                                                         |
| `retries`                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                          | :heavy_minus_sign:                                                                                        | Configuration to override the default retry behavior of the client.                                       |

### Response

**[List[models.AppTerraformWorkspaceStateJSON]](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_terraform_workspace_states_json_by_id

get terraform state json by id. This output is same as "terraform show --json"

### Example Usage

<!-- UsageSnippet language="python" operationID="GetTerraformWorkspaceStatesJSONByID" method="get" path="/v1/runners/terraform-workspace/{workspace_id}/state-json/{state_id}" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.runners.get_terraform_workspace_states_json_by_id(security=models.GetTerraformWorkspaceStatesJSONByIDSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), workspace_id="<id>", state_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                         | Type                                                                                                              | Required                                                                                                          | Description                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                        | [models.GetTerraformWorkspaceStatesJSONByIDSecurity](../../models/getterraformworkspacestatesjsonbyidsecurity.md) | :heavy_check_mark:                                                                                                | N/A                                                                                                               |
| `workspace_id`                                                                                                    | *str*                                                                                                             | :heavy_check_mark:                                                                                                | workspace ID                                                                                                      |
| `state_id`                                                                                                        | *str*                                                                                                             | :heavy_check_mark:                                                                                                | terraform state ID                                                                                                |
| `retries`                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                  | :heavy_minus_sign:                                                                                                | Configuration to override the default retry behavior of the client.                                               |

### Response

**[models.GetTerraformWorkspaceStatesJSONByIDResponse](../../models/getterraformworkspacestatesjsonbyidresponse.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_terraform_workspace_state_json_resources

get terraform state resources. This output is similar to "terraform state list"

### Example Usage

<!-- UsageSnippet language="python" operationID="GetTerraformWorkspaceStateJSONResources" method="get" path="/v1/runners/terraform-workspace/{workspace_id}/state-json/{state_id}/resources" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.runners.get_terraform_workspace_state_json_resources(security=models.GetTerraformWorkspaceStateJSONResourcesSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), workspace_id="<id>", state_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                 | Type                                                                                                                      | Required                                                                                                                  | Description                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                | [models.GetTerraformWorkspaceStateJSONResourcesSecurity](../../models/getterraformworkspacestatejsonresourcessecurity.md) | :heavy_check_mark:                                                                                                        | N/A                                                                                                                       |
| `workspace_id`                                                                                                            | *str*                                                                                                                     | :heavy_check_mark:                                                                                                        | workspace ID                                                                                                              |
| `state_id`                                                                                                                | *str*                                                                                                                     | :heavy_check_mark:                                                                                                        | state ID                                                                                                                  |
| `retries`                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                          | :heavy_minus_sign:                                                                                                        | Configuration to override the default retry behavior of the client.                                                       |

### Response

**[models.GetTerraformWorkspaceStateJSONResourcesResponse](../../models/getterraformworkspacestatejsonresourcesresponse.md)**

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

    res = n_client.runners.get_terraform_states(security=models.GetTerraformStatesSecurity(
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

    res = n_client.runners.get_terraform_workspace_state_by_id(security=models.GetTerraformWorkspaceStateByIDSecurity(
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

    res = n_client.runners.get_terraform_workspace_state_resources(security=models.GetTerraformWorkspaceStateResourcesSecurity(
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

    res = n_client.runners.get_runner(security=models.GetRunnerSecurity(
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

## get_runner_connect_status

# get runner connect status

The connected status is based on runner heartbeat:

if no heart beat found — false
if heart beat > 15 seconds ago — false, hb timestamp
if the heart beat < 15 seconds ago — true

### Example Usage

<!-- UsageSnippet language="python" operationID="GetRunnerConnectStatus" method="get" path="/v1/runners/{runner_id}/connected" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.runners.get_runner_connect_status(security=models.GetRunnerConnectStatusSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), runner_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `security`                                                                              | [models.GetRunnerConnectStatusSecurity](../../models/getrunnerconnectstatussecurity.md) | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `runner_id`                                                                             | *str*                                                                                   | :heavy_check_mark:                                                                      | runner ID                                                                               |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[models.ServiceRunnerConnectionStatus](../../models/servicerunnerconnectionstatus.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## force_shut_down_runner

Force shutdown a runner.

This will result in jobs being lost/cancelled if they are in-flight.


### Example Usage

<!-- UsageSnippet language="python" operationID="ForceShutDownRunner" method="post" path="/v1/runners/{runner_id}/force-shutdown" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.runners.force_shut_down_runner(security=models.ForceShutDownRunnerSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), runner_id="<id>", service_force_shutdown_request={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `security`                                                                        | [models.ForceShutDownRunnerSecurity](../../models/forceshutdownrunnersecurity.md) | :heavy_check_mark:                                                                | N/A                                                                               |
| `runner_id`                                                                       | *str*                                                                             | :heavy_check_mark:                                                                | runner ID                                                                         |
| `service_force_shutdown_request`                                                  | [models.ServiceForceShutdownRequest](../../models/serviceforceshutdownrequest.md) | :heavy_check_mark:                                                                | Input                                                                             |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[bool](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## graceful_shut_down_runner

Gracefully shut down a runner.

_NOTE_ when a runner is unhealthy, the runner will not be able to pick up this job, so use force shut down instead.


### Example Usage

<!-- UsageSnippet language="python" operationID="GracefulShutDownRunner" method="post" path="/v1/runners/{runner_id}/graceful-shutdown" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.runners.graceful_shut_down_runner(security=models.GracefulShutDownRunnerSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), runner_id="<id>", service_graceful_shutdown_request={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `security`                                                                              | [models.GracefulShutDownRunnerSecurity](../../models/gracefulshutdownrunnersecurity.md) | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `runner_id`                                                                             | *str*                                                                                   | :heavy_check_mark:                                                                      | runner ID                                                                               |
| `service_graceful_shutdown_request`                                                     | [models.ServiceGracefulShutdownRequest](../../models/servicegracefulshutdownrequest.md) | :heavy_check_mark:                                                                      | Input                                                                                   |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[bool](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_runner_jobs

Return runner jobs.


### Example Usage

<!-- UsageSnippet language="python" operationID="GetRunnerJobs" method="get" path="/v1/runners/{runner_id}/jobs" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.runners.get_runner_jobs(security=models.GetRunnerJobsSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), runner_id="<id>", offset=0, limit=10, page=0)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `security`                                                            | [models.GetRunnerJobsSecurity](../../models/getrunnerjobssecurity.md) | :heavy_check_mark:                                                    | N/A                                                                   |
| `runner_id`                                                           | *str*                                                                 | :heavy_check_mark:                                                    | runner ID                                                             |
| `group`                                                               | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | job group                                                             |
| `groups`                                                              | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | job groups                                                            |
| `status`                                                              | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | job status                                                            |
| `statuses`                                                            | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | job statuses                                                          |
| `offset`                                                              | *Optional[int]*                                                       | :heavy_minus_sign:                                                    | offset of jobs to return                                              |
| `limit`                                                               | *Optional[int]*                                                       | :heavy_minus_sign:                                                    | limit of jobs to return                                               |
| `page`                                                                | *Optional[int]*                                                       | :heavy_minus_sign:                                                    | page number of results to return                                      |
| `x_nuon_pagination_enabled`                                           | *Optional[bool]*                                                      | :heavy_minus_sign:                                                    | Enable pagination                                                     |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[List[models.AppRunnerJob]](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_runner_latest_heart_beat




### Example Usage

<!-- UsageSnippet language="python" operationID="GetRunnerLatestHeartBeat" method="get" path="/v1/runners/{runner_id}/latest-heart-beat" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.runners.get_runner_latest_heart_beat(security=models.GetRunnerLatestHeartBeatSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), runner_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `security`                                                                                  | [models.GetRunnerLatestHeartBeatSecurity](../../models/getrunnerlatestheartbeatsecurity.md) | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `runner_id`                                                                                 | *str*                                                                                       | :heavy_check_mark:                                                                          | runner ID                                                                                   |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |

### Response

**[models.AppRunnerHeartBeat](../../models/apprunnerheartbeat.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## shut_down_runner_mng

shut down an install runner management process

### Example Usage

<!-- UsageSnippet language="python" operationID="ShutDownRunnerMng" method="post" path="/v1/runners/{runner_id}/mng/shutdown" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.runners.shut_down_runner_mng(security=models.ShutDownRunnerMngSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), runner_id="<id>", service_mng_shut_down_request={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `security`                                                                    | [models.ShutDownRunnerMngSecurity](../../models/shutdownrunnermngsecurity.md) | :heavy_check_mark:                                                            | N/A                                                                           |
| `runner_id`                                                                   | *str*                                                                         | :heavy_check_mark:                                                            | runner ID                                                                     |
| `service_mng_shut_down_request`                                               | [models.ServiceMngShutDownRequest](../../models/servicemngshutdownrequest.md) | :heavy_check_mark:                                                            | Input                                                                         |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[bool](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## mng_vm_shut_down

shut down an install runner VM

### Example Usage

<!-- UsageSnippet language="python" operationID="MngVMShutDown" method="post" path="/v1/runners/{runner_id}/mng/shutdown-vm" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.runners.mng_vm_shut_down(security=models.MngVMShutDownSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), runner_id="<id>", service_mng_vm_shut_down_request={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `security`                                                                        | [models.MngVMShutDownSecurity](../../models/mngvmshutdownsecurity.md)             | :heavy_check_mark:                                                                | N/A                                                                               |
| `runner_id`                                                                       | *str*                                                                             | :heavy_check_mark:                                                                | runner ID                                                                         |
| `service_mng_vm_shut_down_request`                                                | [models.ServiceMngVMShutDownRequest](../../models/servicemngvmshutdownrequest.md) | :heavy_check_mark:                                                                | Input                                                                             |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[bool](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## update_runner_mng

shut down an install runner management process

### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateRunnerMng" method="post" path="/v1/runners/{runner_id}/mng/update" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.runners.update_runner_mng(security=models.UpdateRunnerMngSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), runner_id="<id>", service_mng_update_request={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `security`                                                                | [models.UpdateRunnerMngSecurity](../../models/updaterunnermngsecurity.md) | :heavy_check_mark:                                                        | N/A                                                                       |
| `runner_id`                                                               | *str*                                                                     | :heavy_check_mark:                                                        | runner ID                                                                 |
| `service_mng_update_request`                                              | [models.ServiceMngUpdateRequest](../../models/servicemngupdaterequest.md) | :heavy_check_mark:                                                        | Input                                                                     |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[bool](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_runner_recent_health_checks




### Example Usage

<!-- UsageSnippet language="python" operationID="GetRunnerRecentHealthChecks" method="get" path="/v1/runners/{runner_id}/recent-health-checks" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.runners.get_runner_recent_health_checks(security=models.GetRunnerRecentHealthChecksSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), runner_id="<id>", window="1h", offset=0, limit=10, page=0)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                         | Type                                                                                              | Required                                                                                          | Description                                                                                       |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `security`                                                                                        | [models.GetRunnerRecentHealthChecksSecurity](../../models/getrunnerrecenthealthcheckssecurity.md) | :heavy_check_mark:                                                                                | N/A                                                                                               |
| `runner_id`                                                                                       | *str*                                                                                             | :heavy_check_mark:                                                                                | runner ID                                                                                         |
| `window`                                                                                          | *Optional[str]*                                                                                   | :heavy_minus_sign:                                                                                | window of health checks to return                                                                 |
| `offset`                                                                                          | *Optional[int]*                                                                                   | :heavy_minus_sign:                                                                                | offset of results to return                                                                       |
| `limit`                                                                                           | *Optional[int]*                                                                                   | :heavy_minus_sign:                                                                                | limit of results to return                                                                        |
| `page`                                                                                            | *Optional[int]*                                                                                   | :heavy_minus_sign:                                                                                | page number of results to return                                                                  |
| `x_nuon_pagination_enabled`                                                                       | *Optional[bool]*                                                                                  | :heavy_minus_sign:                                                                                | Enable pagination                                                                                 |
| `retries`                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                  | :heavy_minus_sign:                                                                                | Configuration to override the default retry behavior of the client.                               |

### Response

**[List[models.AppRunnerHealthCheck]](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_runner_settings

Return runner settings for the provided runner.


### Example Usage

<!-- UsageSnippet language="python" operationID="GetRunnerSettings" method="get" path="/v1/runners/{runner_id}/settings" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.runners.get_runner_settings(security=models.GetRunnerSettingsSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), runner_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `security`                                                                    | [models.GetRunnerSettingsSecurity](../../models/getrunnersettingssecurity.md) | :heavy_check_mark:                                                            | N/A                                                                           |
| `runner_id`                                                                   | *str*                                                                         | :heavy_check_mark:                                                            | runner ID                                                                     |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[models.AppRunnerGroupSettings](../../models/apprunnergroupsettings.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## update_runner_settings

update a runner job execution

### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateRunnerSettings" method="patch" path="/v1/runners/{runner_id}/settings" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.runners.update_runner_settings(security=models.UpdateRunnerSettingsSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), runner_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `security`                                                                          | [models.UpdateRunnerSettingsSecurity](../../models/updaterunnersettingssecurity.md) | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `runner_id`                                                                         | *str*                                                                               | :heavy_check_mark:                                                                  | runner ID                                                                           |
| `aws_max_instance_lifetime`                                                         | *Optional[int]*                                                                     | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `container_image_tag`                                                               | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `container_image_url`                                                               | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `org_awsiam_role_arn`                                                               | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `org_k8s_service_account_name`                                                      | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `runner_api_url`                                                                    | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.AppRunnerJobExecution](../../models/apprunnerjobexecution.md)**

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

    res = n_client.runners.get_terraform_current_state_data(security=models.GetTerraformCurrentStateDataSecurity(
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

    res = n_client.runners.update_terraform_state(security=models.UpdateTerraformStateSecurity(
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

    res = n_client.runners.create_terraform_workspace(security=models.CreateTerraformWorkspaceSecurity(
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

    res = n_client.runners.delete_terraform_workspace(security=models.DeleteTerraformWorkspaceSecurity(
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

    res = n_client.runners.get_terraform_workspace(security=models.GetTerraformWorkspaceSecurity(
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

    res = n_client.runners.get_terraform_workspaces(security=models.GetTerraformWorkspacesSecurity(
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

## get_terraform_workspace_lock

get terraform workspace lock

### Example Usage

<!-- UsageSnippet language="python" operationID="GetTerraformWorkspaceLock" method="get" path="/v1/terraform-workspaces/{workspace_id}/lock" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.runners.get_terraform_workspace_lock(security=models.GetTerraformWorkspaceLockSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), workspace_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `security`                                                                                    | [models.GetTerraformWorkspaceLockSecurity](../../models/getterraformworkspacelocksecurity.md) | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `workspace_id`                                                                                | *str*                                                                                         | :heavy_check_mark:                                                                            | workspace ID                                                                                  |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |

### Response

**[models.AppTerraformWorkspaceLock](../../models/appterraformworkspacelock.md)**

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

    res = n_client.runners.lock_terraform_workspace(security=models.LockTerraformWorkspaceSecurity(
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

    res = n_client.runners.unlock_terraform_workspace(security=models.UnlockTerraformWorkspaceSecurity(
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