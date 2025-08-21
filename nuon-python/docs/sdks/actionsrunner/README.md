# ActionsRunner
(*actions_runner*)

## Overview

actions/runner

### Available Operations

* [get_action_workflow_config](#get_action_workflow_config) - get an app action workflow config
* [get_action_workflow_latest_config](#get_action_workflow_latest_config) - get an app action workflow's latest config
* [get_install_action_workflow_run](#get_install_action_workflow_run) - get action workflow runs by install id and run id

## get_action_workflow_config

get an app action workflow config

### Example Usage

<!-- UsageSnippet language="python" operationID="GetActionWorkflowConfig" method="get" path="/v1/action-workflows/configs/{action_workflow_config_id}" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.actions_runner.get_action_workflow_config(security=models.GetActionWorkflowConfigSecurity(
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

## get_action_workflow_latest_config

Return the latest config for an action workflow.


### Example Usage

<!-- UsageSnippet language="python" operationID="GetActionWorkflowLatestConfig" method="get" path="/v1/action-workflows/{action_workflow_id}/latest-config" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.actions_runner.get_action_workflow_latest_config(security=models.GetActionWorkflowLatestConfigSecurity(
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

## get_install_action_workflow_run

get action workflow runs by install id and run id

### Example Usage

<!-- UsageSnippet language="python" operationID="GetInstallActionWorkflowRun" method="get" path="/v1/installs/{install_id}/action-workflows/runs/{run_id}" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.actions_runner.get_install_action_workflow_run(security=models.GetInstallActionWorkflowRunSecurity(
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