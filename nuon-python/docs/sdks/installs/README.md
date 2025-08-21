# Installs
(*installs*)

## Overview

installs

### Available Operations

* [get_app_installs](#get_app_installs) - get all installs for an app
* [create_install](#create_install) - create an app install
* [get_install_workflow](#get_install_workflow) - get an install workflow
* [update_install_workflow](#update_install_workflow) - update an install workflow
* [cancel_install_workflow](#cancel_install_workflow) - cancel an ongoing install workflow
* [get_install_workflow_steps](#get_install_workflow_steps) - get an install workflow step
* [get_install_workflow_step](#get_install_workflow_step) - get an install workflow step
* [get_install_workflow_step_approval](#get_install_workflow_step_approval) - get an install workflow step approval
* [create_install_workflow_step_approval_response](#create_install_workflow_step_approval_response) - deploy a build to an install
* [get_org_installs](#get_org_installs) - get all installs for an org
* [get_install_sandbox_run](#get_install_sandbox_run) - get an install sandbox run
* [get_install_stack](#get_install_stack) - get an install stack by stack ID
* [delete_install](#delete_install) - delete an install
* [get_install](#get_install) - get an install
* [update_install](#update_install) - update an install
* [get_install_action_workflows](#get_install_action_workflows) - get an installs action workflows
* [get_install_action_workflow](#get_install_action_workflow) - get an install action workflow
* [get_install_audit_logs](#get_install_audit_logs) - get install audit logs
* [get_install_components](#get_install_components) - get an installs components
* [deploy_install_components](#deploy_install_components) - deploy all components on an install
* [get_install_components_summary](#get_install_components_summary) - get an installs components summary
* [teardown_install_components](#teardown_install_components) - teardown an install's components
* [get_install_component](#get_install_component) - get an install component
* [get_install_component_deploys](#get_install_component_deploys) - get an install components deploys
* [get_install_component_latest_deploy](#get_install_component_latest_deploy) - get the latest deploy for an install component
* [get_install_component_outputs](#get_install_component_outputs) - get an install component outputs
* [teardown_install_component](#teardown_install_component) - teardown an install component
* [create_install_config](#create_install_config) - create an install config
* [update_install_config](#update_install_config) - create an install config
* [get_install_deploys](#get_install_deploys) - get all deploys to an install
* [create_install_deploy](#create_install_deploy) - deploy a build to an install
* [get_install_latest_deploy](#get_install_latest_deploy) - get an install deploy
* [get_install_deploy](#get_install_deploy) - get an install deploy
* [deprovision_install](#deprovision_install) - deprovision an install
* [deprovision_install_sandbox](#deprovision_install_sandbox) - deprovision an install
* [get_install_events](#get_install_events) - get events for an install
* [get_install_event](#get_install_event) - get an install event
* [forget_install](#forget_install) - forget an install
* [get_install_inputs](#get_install_inputs) - get an installs inputs
* [update_install_inputs](#update_install_inputs) - Updates install input config for app
* [create_install_inputs](#create_install_inputs) - create install inputs
* [get_current_install_inputs](#get_current_install_inputs) - get an installs current inputs
* [phone_home](#phone_home) - phone home for an install
* [get_install_readme](#get_install_readme) - get install readme rendered with
* [reprovision_install](#reprovision_install) - reprovision an install
* [reprovision_install_sandbox](#reprovision_install_sandbox) - reprovision an install sandbox
* [~~retry_workflow~~](#retry_workflow) - rerun the workflow steps starting from input step id, can be used to retry a failed step :warning: **Deprecated**
* [get_install_runner_group](#get_install_runner_group) - Get an install's runner group
* [get_install_sandbox_runs](#get_install_sandbox_runs) - get an installs sandbox runs
* [get_install_stack_by_install_id](#get_install_stack_by_install_id) - get an install stack by install ID
* [get_install_stack_runs](#get_install_stack_runs) - get an install's stack runs
* [get_install_state](#get_install_state) - Get the current state of an install.
* [sync_secrets](#sync_secrets) - sync secrets install
* [get_workflows](#get_workflows) - get workflows
* [get_workflow](#get_workflow) - get a workflow
* [update_workflow](#update_workflow) - update a workflow
* [cancel_workflow](#cancel_workflow) - cancel an ongoing workflow
* [retry_owner_workflow_by_id](#retry_owner_workflow_by_id) - rerun the workflow steps starting from input step id, can be used to retry a failed step
* [get_workflow_steps](#get_workflow_steps) - get a workflow step
* [get_workflow_step](#get_workflow_step) - get a workflow step
* [get_workflow_step_approval](#get_workflow_step_approval) - get an workflow step approval
* [get_workflow_step_approval_contents](#get_workflow_step_approval_contents) - get a workflow step approval contents
* [create_workflow_step_approval_response](#create_workflow_step_approval_response) - deploy a build to an install

## get_app_installs

get all installs for an app

### Example Usage

<!-- UsageSnippet language="python" operationID="GetAppInstalls" method="get" path="/v1/apps/{app_id}/installs" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.get_app_installs(security=models.GetAppInstallsSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), app_id="<id>", offset=0, limit=10, page=0)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `security`                                                              | [models.GetAppInstallsSecurity](../../models/getappinstallssecurity.md) | :heavy_check_mark:                                                      | N/A                                                                     |
| `app_id`                                                                | *str*                                                                   | :heavy_check_mark:                                                      | app ID                                                                  |
| `q`                                                                     | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | search query                                                            |
| `offset`                                                                | *Optional[int]*                                                         | :heavy_minus_sign:                                                      | offset of results to return                                             |
| `limit`                                                                 | *Optional[int]*                                                         | :heavy_minus_sign:                                                      | limit of results to return                                              |
| `page`                                                                  | *Optional[int]*                                                         | :heavy_minus_sign:                                                      | page number of results to return                                        |
| `x_nuon_pagination_enabled`                                             | *Optional[bool]*                                                        | :heavy_minus_sign:                                                      | Enable pagination                                                       |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[List[models.AppInstall]](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## create_install

create an app install

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateInstall" method="post" path="/v1/apps/{app_id}/installs" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.create_install(security=models.CreateInstallSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), app_id="<id>", name="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `security`                                                                                            | [models.CreateInstallSecurity](../../models/createinstallsecurity.md)                                 | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `app_id`                                                                                              | *str*                                                                                                 | :heavy_check_mark:                                                                                    | app ID                                                                                                |
| `name`                                                                                                | *str*                                                                                                 | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `aws_account`                                                                                         | [Optional[models.AwsAccount]](../../models/awsaccount.md)                                             | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `azure_account`                                                                                       | [Optional[models.AzureAccount]](../../models/azureaccount.md)                                         | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `inputs`                                                                                              | Dict[str, *str*]                                                                                      | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `install_config`                                                                                      | [Optional[models.HelpersCreateInstallConfigParams]](../../models/helperscreateinstallconfigparams.md) | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |

### Response

**[models.AppInstall](../../models/appinstall.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_install_workflow

Return a workflow.


### Example Usage

<!-- UsageSnippet language="python" operationID="GetInstallWorkflow" method="get" path="/v1/install-workflows/{install_workflow_id}" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.get_install_workflow(security=models.GetInstallWorkflowSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), install_workflow_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `security`                                                                      | [models.GetInstallWorkflowSecurity](../../models/getinstallworkflowsecurity.md) | :heavy_check_mark:                                                              | N/A                                                                             |
| `install_workflow_id`                                                           | *str*                                                                           | :heavy_check_mark:                                                              | install workflow ID                                                             |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[models.AppWorkflow](../../models/appworkflow.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## update_install_workflow

update an install workflow

### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateInstallWorkflow" method="patch" path="/v1/install-workflows/{install_workflow_id}" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.update_install_workflow(security=models.UpdateInstallWorkflowSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), install_workflow_id="<id>", approval_option=models.AppInstallApprovalOption.APPROVE_ALL)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `security`                                                                            | [models.UpdateInstallWorkflowSecurity](../../models/updateinstallworkflowsecurity.md) | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `install_workflow_id`                                                                 | *str*                                                                                 | :heavy_check_mark:                                                                    | install workflow ID                                                                   |
| `approval_option`                                                                     | [models.AppInstallApprovalOption](../../models/appinstallapprovaloption.md)           | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.AppWorkflow](../../models/appworkflow.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## cancel_install_workflow

cancel an ongoing install workflow

### Example Usage

<!-- UsageSnippet language="python" operationID="CancelInstallWorkflow" method="post" path="/v1/install-workflows/{install_workflow_id}/cancel" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.cancel_install_workflow(security=models.CancelInstallWorkflowSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), install_workflow_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `security`                                                                            | [models.CancelInstallWorkflowSecurity](../../models/cancelinstallworkflowsecurity.md) | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `install_workflow_id`                                                                 | *str*                                                                                 | :heavy_check_mark:                                                                    | install workflow ID                                                                   |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[bool](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_install_workflow_steps

Return all steps for a workflow.


### Example Usage

<!-- UsageSnippet language="python" operationID="GetInstallWorkflowSteps" method="get" path="/v1/install-workflows/{install_workflow_id}/steps" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.get_install_workflow_steps(security=models.GetInstallWorkflowStepsSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), install_workflow_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `security`                                                                                | [models.GetInstallWorkflowStepsSecurity](../../models/getinstallworkflowstepssecurity.md) | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `install_workflow_id`                                                                     | *str*                                                                                     | :heavy_check_mark:                                                                        | install workflow ID                                                                       |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |

### Response

**[List[models.AppWorkflowStep]](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_install_workflow_step

Return a single workflow step.


### Example Usage

<!-- UsageSnippet language="python" operationID="GetInstallWorkflowStep" method="get" path="/v1/install-workflows/{install_workflow_id}/steps/{install_workflow_step_id}" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.get_install_workflow_step(security=models.GetInstallWorkflowStepSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), install_workflow_id="<id>", install_workflow_step_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `security`                                                                              | [models.GetInstallWorkflowStepSecurity](../../models/getinstallworkflowstepsecurity.md) | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `install_workflow_id`                                                                   | *str*                                                                                   | :heavy_check_mark:                                                                      | workflow id                                                                             |
| `install_workflow_step_id`                                                              | *str*                                                                                   | :heavy_check_mark:                                                                      | step id                                                                                 |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[models.AppWorkflowStep](../../models/appworkflowstep.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_install_workflow_step_approval

get an install workflow step approval

### Example Usage

<!-- UsageSnippet language="python" operationID="GetInstallWorkflowStepApproval" method="get" path="/v1/install-workflows/{install_workflow_id}/steps/{install_workflow_step_id}/approvals/{approval_id}" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.get_install_workflow_step_approval(security=models.GetInstallWorkflowStepApprovalSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), install_workflow_id="<id>", install_workflow_step_id="<id>", approval_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                               | Type                                                                                                    | Required                                                                                                | Description                                                                                             |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `security`                                                                                              | [models.GetInstallWorkflowStepApprovalSecurity](../../models/getinstallworkflowstepapprovalsecurity.md) | :heavy_check_mark:                                                                                      | N/A                                                                                                     |
| `install_workflow_id`                                                                                   | *str*                                                                                                   | :heavy_check_mark:                                                                                      | workflow id                                                                                             |
| `install_workflow_step_id`                                                                              | *str*                                                                                                   | :heavy_check_mark:                                                                                      | step id                                                                                                 |
| `approval_id`                                                                                           | *str*                                                                                                   | :heavy_check_mark:                                                                                      | approval id                                                                                             |
| `retries`                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                        | :heavy_minus_sign:                                                                                      | Configuration to override the default retry behavior of the client.                                     |

### Response

**[models.AppWorkflowStepApproval](../../models/appworkflowstepapproval.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## create_install_workflow_step_approval_response

deploy a build to an install

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateInstallWorkflowStepApprovalResponse" method="post" path="/v1/install-workflows/{install_workflow_id}/steps/{install_workflow_step_id}/approvals/{approval_id}/response" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.create_install_workflow_step_approval_response(security=models.CreateInstallWorkflowStepApprovalResponseSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), install_workflow_id="<id>", install_workflow_step_id="<id>", approval_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                     | Type                                                                                                                          | Required                                                                                                                      | Description                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                    | [models.CreateInstallWorkflowStepApprovalResponseSecurity](../../models/createinstallworkflowstepapprovalresponsesecurity.md) | :heavy_check_mark:                                                                                                            | N/A                                                                                                                           |
| `install_workflow_id`                                                                                                         | *str*                                                                                                                         | :heavy_check_mark:                                                                                                            | workflow id                                                                                                                   |
| `install_workflow_step_id`                                                                                                    | *str*                                                                                                                         | :heavy_check_mark:                                                                                                            | step id                                                                                                                       |
| `approval_id`                                                                                                                 | *str*                                                                                                                         | :heavy_check_mark:                                                                                                            | approval id                                                                                                                   |
| `note`                                                                                                                        | *Optional[str]*                                                                                                               | :heavy_minus_sign:                                                                                                            | N/A                                                                                                                           |
| `response_type`                                                                                                               | [Optional[models.AppWorkflowStepResponseType]](../../models/appworkflowstepresponsetype.md)                                   | :heavy_minus_sign:                                                                                                            | N/A                                                                                                                           |
| `retries`                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                              | :heavy_minus_sign:                                                                                                            | Configuration to override the default retry behavior of the client.                                                           |

### Response

**[models.AppWorkflowStepApprovalResponse](../../models/appworkflowstepapprovalresponse.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_org_installs

get all installs for an org

### Example Usage

<!-- UsageSnippet language="python" operationID="GetOrgInstalls" method="get" path="/v1/installs" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.get_org_installs(security=models.GetOrgInstallsSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), offset=0, limit=10, page=0)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `security`                                                              | [models.GetOrgInstallsSecurity](../../models/getorginstallssecurity.md) | :heavy_check_mark:                                                      | N/A                                                                     |
| `offset`                                                                | *Optional[int]*                                                         | :heavy_minus_sign:                                                      | offset of results to return                                             |
| `q`                                                                     | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | search query to filter installs by name                                 |
| `limit`                                                                 | *Optional[int]*                                                         | :heavy_minus_sign:                                                      | limit of results to return                                              |
| `page`                                                                  | *Optional[int]*                                                         | :heavy_minus_sign:                                                      | page number of results to return                                        |
| `x_nuon_pagination_enabled`                                             | *Optional[bool]*                                                        | :heavy_minus_sign:                                                      | Enable pagination                                                       |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[List[models.AppInstall]](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_install_sandbox_run

get an install sandbox run

### Example Usage

<!-- UsageSnippet language="python" operationID="GetInstallSandboxRun" method="get" path="/v1/installs/sandbox-runs/{run_id}" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.get_install_sandbox_run(security=models.GetInstallSandboxRunSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), run_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `security`                                                                          | [models.GetInstallSandboxRunSecurity](../../models/getinstallsandboxrunsecurity.md) | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `run_id`                                                                            | *str*                                                                               | :heavy_check_mark:                                                                  | run ID                                                                              |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.AppInstallSandboxRun](../../models/appinstallsandboxrun.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_install_stack

get an install stack by stack ID

### Example Usage

<!-- UsageSnippet language="python" operationID="GetInstallStack" method="get" path="/v1/installs/stacks/{stack_id}" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.get_install_stack(security=models.GetInstallStackSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), stack_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `security`                                                                | [models.GetInstallStackSecurity](../../models/getinstallstacksecurity.md) | :heavy_check_mark:                                                        | N/A                                                                       |
| `stack_id`                                                                | *str*                                                                     | :heavy_check_mark:                                                        | stack ID                                                                  |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.AppInstallStack](../../models/appinstallstack.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## delete_install

delete an install

### Example Usage

<!-- UsageSnippet language="python" operationID="DeleteInstall" method="delete" path="/v1/installs/{install_id}" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.delete_install(security=models.DeleteInstallSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), install_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `security`                                                            | [models.DeleteInstallSecurity](../../models/deleteinstallsecurity.md) | :heavy_check_mark:                                                    | N/A                                                                   |
| `install_id`                                                          | *str*                                                                 | :heavy_check_mark:                                                    | install ID                                                            |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[bool](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_install

Forget an install that has been deleted outside of nuon.

This should only be used in cases where an install was broken in an unordinary way and needs to be manually deleted so the parent resources can be deleted.


### Example Usage

<!-- UsageSnippet language="python" operationID="GetInstall" method="get" path="/v1/installs/{install_id}" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.get_install(security=models.GetInstallSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), install_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `security`                                                          | [models.GetInstallSecurity](../../models/getinstallsecurity.md)     | :heavy_check_mark:                                                  | N/A                                                                 |
| `install_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | install ID                                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AppInstall](../../models/appinstall.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## update_install

update an install

### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateInstall" method="patch" path="/v1/installs/{install_id}" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.update_install(security=models.UpdateInstallSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), install_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `security`                                                            | [models.UpdateInstallSecurity](../../models/updateinstallsecurity.md) | :heavy_check_mark:                                                    | N/A                                                                   |
| `install_id`                                                          | *str*                                                                 | :heavy_check_mark:                                                    | app ID                                                                |
| `name`                                                                | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | N/A                                                                   |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.AppInstall](../../models/appinstall.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_install_action_workflows

Get install action workflows.


### Example Usage

<!-- UsageSnippet language="python" operationID="GetInstallActionWorkflows" method="get" path="/v1/installs/{install_id}/action-workflows" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.get_install_action_workflows(security=models.GetInstallActionWorkflowsSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), install_id="<id>", offset=0, limit=10, page=0)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `security`                                                                                    | [models.GetInstallActionWorkflowsSecurity](../../models/getinstallactionworkflowssecurity.md) | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `install_id`                                                                                  | *str*                                                                                         | :heavy_check_mark:                                                                            | install ID                                                                                    |
| `offset`                                                                                      | *Optional[int]*                                                                               | :heavy_minus_sign:                                                                            | offset of results to return                                                                   |
| `limit`                                                                                       | *Optional[int]*                                                                               | :heavy_minus_sign:                                                                            | limit of results to return                                                                    |
| `page`                                                                                        | *Optional[int]*                                                                               | :heavy_minus_sign:                                                                            | page number of results to return                                                              |
| `x_nuon_pagination_enabled`                                                                   | *Optional[bool]*                                                                              | :heavy_minus_sign:                                                                            | Enable pagination                                                                             |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |

### Response

**[List[models.AppInstallActionWorkflow]](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_install_action_workflow

Get an install action workflow.


### Example Usage

<!-- UsageSnippet language="python" operationID="GetInstallActionWorkflow" method="get" path="/v1/installs/{install_id}/action-workflows/{action_workflow_id}" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.get_install_action_workflow(security=models.GetInstallActionWorkflowSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), install_id="<id>", action_workflow_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `security`                                                                                  | [models.GetInstallActionWorkflowSecurity](../../models/getinstallactionworkflowsecurity.md) | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `install_id`                                                                                | *str*                                                                                       | :heavy_check_mark:                                                                          | install ID                                                                                  |
| `action_workflow_id`                                                                        | *str*                                                                                       | :heavy_check_mark:                                                                          | workflow ID                                                                                 |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |

### Response

**[models.AppInstallActionWorkflow](../../models/appinstallactionworkflow.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_install_audit_logs

get install audit logs

### Example Usage

<!-- UsageSnippet language="python" operationID="GetInstallAuditLogs" method="get" path="/v1/installs/{install_id}/audit_logs" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.get_install_audit_logs(security=models.GetInstallAuditLogsSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), install_id="<id>", start="<value>", end="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `security`                                                                        | [models.GetInstallAuditLogsSecurity](../../models/getinstallauditlogssecurity.md) | :heavy_check_mark:                                                                | N/A                                                                               |
| `install_id`                                                                      | *str*                                                                             | :heavy_check_mark:                                                                | install ID                                                                        |
| `start`                                                                           | *str*                                                                             | :heavy_check_mark:                                                                | start timestamp for audit log range                                               |
| `end`                                                                             | *str*                                                                             | :heavy_check_mark:                                                                | end timestamp for audit log range                                                 |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[bytes](../../models/.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.NuonDefaultError | 4XX, 5XX                | \*/\*                   |

## get_install_components

get an installs components

### Example Usage

<!-- UsageSnippet language="python" operationID="GetInstallComponents" method="get" path="/v1/installs/{install_id}/components" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.get_install_components(security=models.GetInstallComponentsSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), install_id="<id>", offset=0, limit=10)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `security`                                                                          | [models.GetInstallComponentsSecurity](../../models/getinstallcomponentssecurity.md) | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `install_id`                                                                        | *str*                                                                               | :heavy_check_mark:                                                                  | install ID                                                                          |
| `offset`                                                                            | *Optional[int]*                                                                     | :heavy_minus_sign:                                                                  | offset of results to return                                                         |
| `limit`                                                                             | *Optional[int]*                                                                     | :heavy_minus_sign:                                                                  | limit of results to return                                                          |
| `x_nuon_pagination_enabled`                                                         | *Optional[bool]*                                                                    | :heavy_minus_sign:                                                                  | Enable pagination                                                                   |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[List[models.AppInstallComponent]](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## deploy_install_components

Deploy all components to an install.

This walks the graph order of the install's app, and will trigger a deploy for each on the specified install.


### Example Usage

<!-- UsageSnippet language="python" operationID="DeployInstallComponents" method="post" path="/v1/installs/{install_id}/components/deploy-all" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.deploy_install_components(security=models.DeployInstallComponentsSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), install_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `security`                                                                                | [models.DeployInstallComponentsSecurity](../../models/deployinstallcomponentssecurity.md) | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `install_id`                                                                              | *str*                                                                                     | :heavy_check_mark:                                                                        | install ID                                                                                |
| `plan_only`                                                                               | *Optional[bool]*                                                                          | :heavy_minus_sign:                                                                        | N/A                                                                                       |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |

### Response

**[str](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_install_components_summary

get an installs components summary

### Example Usage

<!-- UsageSnippet language="python" operationID="GetInstallComponentsSummary" method="get" path="/v1/installs/{install_id}/components/summary" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.get_install_components_summary(security=models.GetInstallComponentsSummarySecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), install_id="<id>", offset=0, limit=10, page=0)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                         | Type                                                                                              | Required                                                                                          | Description                                                                                       |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `security`                                                                                        | [models.GetInstallComponentsSummarySecurity](../../models/getinstallcomponentssummarysecurity.md) | :heavy_check_mark:                                                                                | N/A                                                                                               |
| `install_id`                                                                                      | *str*                                                                                             | :heavy_check_mark:                                                                                | install ID                                                                                        |
| `types`                                                                                           | *Optional[str]*                                                                                   | :heavy_minus_sign:                                                                                | component types to filter by                                                                      |
| `offset`                                                                                          | *Optional[int]*                                                                                   | :heavy_minus_sign:                                                                                | offset of results to return                                                                       |
| `limit`                                                                                           | *Optional[int]*                                                                                   | :heavy_minus_sign:                                                                                | limit of results to return                                                                        |
| `page`                                                                                            | *Optional[int]*                                                                                   | :heavy_minus_sign:                                                                                | page number of results to return                                                                  |
| `q`                                                                                               | *Optional[str]*                                                                                   | :heavy_minus_sign:                                                                                | search query for component name                                                                   |
| `x_nuon_pagination_enabled`                                                                       | *Optional[bool]*                                                                                  | :heavy_minus_sign:                                                                                | Enable pagination                                                                                 |
| `retries`                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                  | :heavy_minus_sign:                                                                                | Configuration to override the default retry behavior of the client.                               |

### Response

**[List[models.AppInstallComponentSummary]](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## teardown_install_components

Teardown all components on an install.


### Example Usage

<!-- UsageSnippet language="python" operationID="TeardownInstallComponents" method="post" path="/v1/installs/{install_id}/components/teardown-all" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.teardown_install_components(security=models.TeardownInstallComponentsSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), install_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `security`                                                                                    | [models.TeardownInstallComponentsSecurity](../../models/teardowninstallcomponentssecurity.md) | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `install_id`                                                                                  | *str*                                                                                         | :heavy_check_mark:                                                                            | install ID                                                                                    |
| `error_behavior`                                                                              | *Optional[str]*                                                                               | :heavy_minus_sign:                                                                            | N/A                                                                                           |
| `plan_only`                                                                                   | *Optional[bool]*                                                                              | :heavy_minus_sign:                                                                            | N/A                                                                                           |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |

### Response

**[str](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_install_component

get an install component

### Example Usage

<!-- UsageSnippet language="python" operationID="GetInstallComponent" method="get" path="/v1/installs/{install_id}/components/{component_id}" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.get_install_component(security=models.GetInstallComponentSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), install_id="<id>", component_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `security`                                                                        | [models.GetInstallComponentSecurity](../../models/getinstallcomponentsecurity.md) | :heavy_check_mark:                                                                | N/A                                                                               |
| `install_id`                                                                      | *str*                                                                             | :heavy_check_mark:                                                                | install ID                                                                        |
| `component_id`                                                                    | *str*                                                                             | :heavy_check_mark:                                                                | component ID                                                                      |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.AppInstallComponent](../../models/appinstallcomponent.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_install_component_deploys

get an install components deploys

### Example Usage

<!-- UsageSnippet language="python" operationID="GetInstallComponentDeploys" method="get" path="/v1/installs/{install_id}/components/{component_id}/deploys" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.get_install_component_deploys(security=models.GetInstallComponentDeploysSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), install_id="<id>", component_id="<id>", offset=0, limit=10, page=0)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `security`                                                                                      | [models.GetInstallComponentDeploysSecurity](../../models/getinstallcomponentdeployssecurity.md) | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `install_id`                                                                                    | *str*                                                                                           | :heavy_check_mark:                                                                              | install ID                                                                                      |
| `component_id`                                                                                  | *str*                                                                                           | :heavy_check_mark:                                                                              | component ID                                                                                    |
| `offset`                                                                                        | *Optional[int]*                                                                                 | :heavy_minus_sign:                                                                              | offset of results to return                                                                     |
| `limit`                                                                                         | *Optional[int]*                                                                                 | :heavy_minus_sign:                                                                              | limit of results to return                                                                      |
| `page`                                                                                          | *Optional[int]*                                                                                 | :heavy_minus_sign:                                                                              | page number of results to return                                                                |
| `x_nuon_pagination_enabled`                                                                     | *Optional[bool]*                                                                                | :heavy_minus_sign:                                                                              | Enable pagination                                                                               |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[List[models.AppInstallDeploy]](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_install_component_latest_deploy

get the latest deploy for an install component

### Example Usage

<!-- UsageSnippet language="python" operationID="GetInstallComponentLatestDeploy" method="get" path="/v1/installs/{install_id}/components/{component_id}/deploys/latest" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.get_install_component_latest_deploy(security=models.GetInstallComponentLatestDeploySecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), install_id="<id>", component_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                 | Type                                                                                                      | Required                                                                                                  | Description                                                                                               |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                | [models.GetInstallComponentLatestDeploySecurity](../../models/getinstallcomponentlatestdeploysecurity.md) | :heavy_check_mark:                                                                                        | N/A                                                                                                       |
| `install_id`                                                                                              | *str*                                                                                                     | :heavy_check_mark:                                                                                        | install ID                                                                                                |
| `component_id`                                                                                            | *str*                                                                                                     | :heavy_check_mark:                                                                                        | component ID                                                                                              |
| `retries`                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                          | :heavy_minus_sign:                                                                                        | Configuration to override the default retry behavior of the client.                                       |

### Response

**[models.AppInstallDeploy](../../models/appinstalldeploy.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_install_component_outputs

Return the latest outputs for a component.

**NOTE** requires a valid install.


### Example Usage

<!-- UsageSnippet language="python" operationID="GetInstallComponentOutputs" method="get" path="/v1/installs/{install_id}/components/{component_id}/outputs" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.get_install_component_outputs(security=models.GetInstallComponentOutputsSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), install_id="<id>", component_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `security`                                                                                      | [models.GetInstallComponentOutputsSecurity](../../models/getinstallcomponentoutputssecurity.md) | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `install_id`                                                                                    | *str*                                                                                           | :heavy_check_mark:                                                                              | install ID                                                                                      |
| `component_id`                                                                                  | *str*                                                                                           | :heavy_check_mark:                                                                              | component ID                                                                                    |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[Dict[str, Any]](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## teardown_install_component

teardown an install component

### Example Usage

<!-- UsageSnippet language="python" operationID="TeardownInstallComponent" method="post" path="/v1/installs/{install_id}/components/{component_id}/teardown" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.teardown_install_component(security=models.TeardownInstallComponentSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), install_id="<id>", component_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `security`                                                                                  | [models.TeardownInstallComponentSecurity](../../models/teardowninstallcomponentsecurity.md) | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `install_id`                                                                                | *str*                                                                                       | :heavy_check_mark:                                                                          | install ID                                                                                  |
| `component_id`                                                                              | *str*                                                                                       | :heavy_check_mark:                                                                          | component ID                                                                                |
| `error_behavior`                                                                            | *Optional[str]*                                                                             | :heavy_minus_sign:                                                                          | N/A                                                                                         |
| `plan_only`                                                                                 | *Optional[bool]*                                                                            | :heavy_minus_sign:                                                                          | N/A                                                                                         |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |

### Response

**[str](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## create_install_config

create an install config

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateInstallConfig" method="post" path="/v1/installs/{install_id}/configs" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.create_install_config(security=models.CreateInstallConfigSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), install_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `security`                                                                            | [models.CreateInstallConfigSecurity](../../models/createinstallconfigsecurity.md)     | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `install_id`                                                                          | *str*                                                                                 | :heavy_check_mark:                                                                    | install ID                                                                            |
| `approval_option`                                                                     | [Optional[models.AppInstallApprovalOption]](../../models/appinstallapprovaloption.md) | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.AppInstallConfig](../../models/appinstallconfig.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## update_install_config

create an install config

### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateInstallConfig" method="patch" path="/v1/installs/{install_id}/configs/{config_id}" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.update_install_config(security=models.UpdateInstallConfigSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), install_id="<id>", config_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `security`                                                                            | [models.UpdateInstallConfigSecurity](../../models/updateinstallconfigsecurity.md)     | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `install_id`                                                                          | *str*                                                                                 | :heavy_check_mark:                                                                    | install ID                                                                            |
| `config_id`                                                                           | *str*                                                                                 | :heavy_check_mark:                                                                    | config ID                                                                             |
| `approval_option`                                                                     | [Optional[models.AppInstallApprovalOption]](../../models/appinstallapprovaloption.md) | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.AppInstallConfig](../../models/appinstallconfig.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_install_deploys

get all deploys to an install

### Example Usage

<!-- UsageSnippet language="python" operationID="GetInstallDeploys" method="get" path="/v1/installs/{install_id}/deploys" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.get_install_deploys(security=models.GetInstallDeploysSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), install_id="<id>", offset=0, limit=10, page=0)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `security`                                                                    | [models.GetInstallDeploysSecurity](../../models/getinstalldeployssecurity.md) | :heavy_check_mark:                                                            | N/A                                                                           |
| `install_id`                                                                  | *str*                                                                         | :heavy_check_mark:                                                            | install ID                                                                    |
| `offset`                                                                      | *Optional[int]*                                                               | :heavy_minus_sign:                                                            | offset of results to return                                                   |
| `limit`                                                                       | *Optional[int]*                                                               | :heavy_minus_sign:                                                            | limit of results to return                                                    |
| `page`                                                                        | *Optional[int]*                                                               | :heavy_minus_sign:                                                            | page number of results to return                                              |
| `x_nuon_pagination_enabled`                                                   | *Optional[bool]*                                                              | :heavy_minus_sign:                                                            | Enable pagination                                                             |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[List[models.AppInstallDeploy]](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## create_install_deploy

deploy a build to an install

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateInstallDeploy" method="post" path="/v1/installs/{install_id}/deploys" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.create_install_deploy(security=models.CreateInstallDeploySecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), install_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `security`                                                                        | [models.CreateInstallDeploySecurity](../../models/createinstalldeploysecurity.md) | :heavy_check_mark:                                                                | N/A                                                                               |
| `install_id`                                                                      | *str*                                                                             | :heavy_check_mark:                                                                | install ID                                                                        |
| `build_id`                                                                        | *Optional[str]*                                                                   | :heavy_minus_sign:                                                                | N/A                                                                               |
| `deploy_dependents`                                                               | *Optional[bool]*                                                                  | :heavy_minus_sign:                                                                | N/A                                                                               |
| `plan_only`                                                                       | *Optional[bool]*                                                                  | :heavy_minus_sign:                                                                | N/A                                                                               |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.AppInstallDeploy](../../models/appinstalldeploy.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_install_latest_deploy

get an install deploy

### Example Usage

<!-- UsageSnippet language="python" operationID="GetInstallLatestDeploy" method="get" path="/v1/installs/{install_id}/deploys/latest" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.get_install_latest_deploy(security=models.GetInstallLatestDeploySecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), install_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `security`                                                                              | [models.GetInstallLatestDeploySecurity](../../models/getinstalllatestdeploysecurity.md) | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `install_id`                                                                            | *str*                                                                                   | :heavy_check_mark:                                                                      | install ID                                                                              |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[models.AppInstallDeploy](../../models/appinstalldeploy.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_install_deploy

get an install deploy

### Example Usage

<!-- UsageSnippet language="python" operationID="GetInstallDeploy" method="get" path="/v1/installs/{install_id}/deploys/{deploy_id}" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.get_install_deploy(security=models.GetInstallDeploySecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), install_id="<id>", deploy_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `security`                                                                  | [models.GetInstallDeploySecurity](../../models/getinstalldeploysecurity.md) | :heavy_check_mark:                                                          | N/A                                                                         |
| `install_id`                                                                | *str*                                                                       | :heavy_check_mark:                                                          | install ID                                                                  |
| `deploy_id`                                                                 | *str*                                                                       | :heavy_check_mark:                                                          | deploy ID                                                                   |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.AppInstallDeploy](../../models/appinstalldeploy.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## deprovision_install

Deprovision an install sandbox.


### Example Usage

<!-- UsageSnippet language="python" operationID="DeprovisionInstall" method="post" path="/v1/installs/{install_id}/deprovision" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.deprovision_install(security=models.DeprovisionInstallSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), install_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `security`                                                                      | [models.DeprovisionInstallSecurity](../../models/deprovisioninstallsecurity.md) | :heavy_check_mark:                                                              | N/A                                                                             |
| `install_id`                                                                    | *str*                                                                           | :heavy_check_mark:                                                              | install ID                                                                      |
| `error_behavior`                                                                | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | N/A                                                                             |
| `plan_only`                                                                     | *Optional[bool]*                                                                | :heavy_minus_sign:                                                              | N/A                                                                             |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[str](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## deprovision_install_sandbox

deprovision an install

### Example Usage

<!-- UsageSnippet language="python" operationID="DeprovisionInstallSandbox" method="post" path="/v1/installs/{install_id}/deprovision-sandbox" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.deprovision_install_sandbox(security=models.DeprovisionInstallSandboxSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), install_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `security`                                                                                    | [models.DeprovisionInstallSandboxSecurity](../../models/deprovisioninstallsandboxsecurity.md) | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `install_id`                                                                                  | *str*                                                                                         | :heavy_check_mark:                                                                            | install ID                                                                                    |
| `error_behavior`                                                                              | *Optional[str]*                                                                               | :heavy_minus_sign:                                                                            | N/A                                                                                           |
| `plan_only`                                                                                   | *Optional[bool]*                                                                              | :heavy_minus_sign:                                                                            | N/A                                                                                           |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |

### Response

**[str](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_install_events

# Get Install Events

Return an event stream for an install.


### Example Usage

<!-- UsageSnippet language="python" operationID="GetInstallEvents" method="get" path="/v1/installs/{install_id}/events" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.get_install_events(security=models.GetInstallEventsSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), install_id="<id>", offset=0, limit=10, page=0)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `security`                                                                  | [models.GetInstallEventsSecurity](../../models/getinstalleventssecurity.md) | :heavy_check_mark:                                                          | N/A                                                                         |
| `install_id`                                                                | *str*                                                                       | :heavy_check_mark:                                                          | install ID                                                                  |
| `offset`                                                                    | *Optional[int]*                                                             | :heavy_minus_sign:                                                          | offset of results to return                                                 |
| `limit`                                                                     | *Optional[int]*                                                             | :heavy_minus_sign:                                                          | limit of results to return                                                  |
| `page`                                                                      | *Optional[int]*                                                             | :heavy_minus_sign:                                                          | page number of results to return                                            |
| `x_nuon_pagination_enabled`                                                 | *Optional[bool]*                                                            | :heavy_minus_sign:                                                          | Enable pagination                                                           |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[List[models.AppInstallEvent]](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_install_event

Get a single install event.


### Example Usage

<!-- UsageSnippet language="python" operationID="GetInstallEvent" method="get" path="/v1/installs/{install_id}/events/{event_id}" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.get_install_event(security=models.GetInstallEventSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), install_id="<id>", event_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `security`                                                                | [models.GetInstallEventSecurity](../../models/getinstalleventsecurity.md) | :heavy_check_mark:                                                        | N/A                                                                       |
| `install_id`                                                              | *str*                                                                     | :heavy_check_mark:                                                        | install ID                                                                |
| `event_id`                                                                | *str*                                                                     | :heavy_check_mark:                                                        | event ID                                                                  |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.AppInstallEvent](../../models/appinstallevent.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## forget_install

Forget an install that has been deleted outside of nuon.

This should only be used in cases where an install was broken in an unordinary way and needs to be manually deleted so the parent resources can be deleted.


### Example Usage

<!-- UsageSnippet language="python" operationID="ForgetInstall" method="post" path="/v1/installs/{install_id}/forget" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.forget_install(security=models.ForgetInstallSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), install_id="<id>", service_forget_install_request={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `security`                                                                        | [models.ForgetInstallSecurity](../../models/forgetinstallsecurity.md)             | :heavy_check_mark:                                                                | N/A                                                                               |
| `install_id`                                                                      | *str*                                                                             | :heavy_check_mark:                                                                | install ID                                                                        |
| `service_forget_install_request`                                                  | [models.ServiceForgetInstallRequest](../../models/serviceforgetinstallrequest.md) | :heavy_check_mark:                                                                | Input                                                                             |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[bool](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 404                      | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_install_inputs

get an installs inputs

### Example Usage

<!-- UsageSnippet language="python" operationID="GetInstallInputs" method="get" path="/v1/installs/{install_id}/inputs" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.get_install_inputs(security=models.GetInstallInputsSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), install_id="<id>", offset=0, limit=10, page=0)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `security`                                                                  | [models.GetInstallInputsSecurity](../../models/getinstallinputssecurity.md) | :heavy_check_mark:                                                          | N/A                                                                         |
| `install_id`                                                                | *str*                                                                       | :heavy_check_mark:                                                          | install ID                                                                  |
| `offset`                                                                    | *Optional[int]*                                                             | :heavy_minus_sign:                                                          | offset of results to return                                                 |
| `limit`                                                                     | *Optional[int]*                                                             | :heavy_minus_sign:                                                          | limit of results to return                                                  |
| `page`                                                                      | *Optional[int]*                                                             | :heavy_minus_sign:                                                          | page number of results to return                                            |
| `x_nuon_pagination_enabled`                                                 | *Optional[bool]*                                                            | :heavy_minus_sign:                                                          | Enable pagination                                                           |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[List[models.AppInstallInputs]](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## update_install_inputs

Updates install input config for app

### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateInstallInputs" method="patch" path="/v1/installs/{install_id}/inputs" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.update_install_inputs(security=models.UpdateInstallInputsSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), install_id="<id>", inputs={
        "key": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `security`                                                                        | [models.UpdateInstallInputsSecurity](../../models/updateinstallinputssecurity.md) | :heavy_check_mark:                                                                | N/A                                                                               |
| `install_id`                                                                      | *str*                                                                             | :heavy_check_mark:                                                                | install ID                                                                        |
| `inputs`                                                                          | Dict[str, *str*]                                                                  | :heavy_check_mark:                                                                | N/A                                                                               |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.AppInstallInputs](../../models/appinstallinputs.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## create_install_inputs

create install inputs

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateInstallInputs" method="post" path="/v1/installs/{install_id}/inputs" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.create_install_inputs(security=models.CreateInstallInputsSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), install_id="<id>", inputs={

    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `security`                                                                        | [models.CreateInstallInputsSecurity](../../models/createinstallinputssecurity.md) | :heavy_check_mark:                                                                | N/A                                                                               |
| `install_id`                                                                      | *str*                                                                             | :heavy_check_mark:                                                                | install ID                                                                        |
| `inputs`                                                                          | Dict[str, *str*]                                                                  | :heavy_check_mark:                                                                | N/A                                                                               |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.AppInstallInputs](../../models/appinstallinputs.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_current_install_inputs

get an installs current inputs

### Example Usage

<!-- UsageSnippet language="python" operationID="GetCurrentInstallInputs" method="get" path="/v1/installs/{install_id}/inputs/current" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.get_current_install_inputs(security=models.GetCurrentInstallInputsSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), install_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `security`                                                                                | [models.GetCurrentInstallInputsSecurity](../../models/getcurrentinstallinputssecurity.md) | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `install_id`                                                                              | *str*                                                                                     | :heavy_check_mark:                                                                        | install ID                                                                                |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |

### Response

**[models.AppInstallInputs](../../models/appinstallinputs.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## phone_home

A public endpoint for phoning home from a runner AWS cloudformation stack upon successfully processing it.


### Example Usage

<!-- UsageSnippet language="python" operationID="PhoneHome" method="post" path="/v1/installs/{install_id}/phone-home/{phone_home_id}" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.phone_home(security=models.PhoneHomeSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), install_id="<id>", phone_home_id="<id>", request_body={
        "key": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `security`                                                          | [models.PhoneHomeSecurity](../../models/phonehomesecurity.md)       | :heavy_check_mark:                                                  | N/A                                                                 |
| `install_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | install ID                                                          |
| `phone_home_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | phone home ID                                                       |
| `request_body`                                                      | Dict[str, *Any*]                                                    | :heavy_check_mark:                                                  | Input                                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[str](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_install_readme

Returns the `app.readme` markdown with the values interpolated from the install
inputs and component outputs.


### Example Usage

<!-- UsageSnippet language="python" operationID="GetInstallReadme" method="get" path="/v1/installs/{install_id}/readme" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.get_install_readme(security=models.GetInstallReadmeSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), install_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `security`                                                                  | [models.GetInstallReadmeSecurity](../../models/getinstallreadmesecurity.md) | :heavy_check_mark:                                                          | N/A                                                                         |
| `install_id`                                                                | *str*                                                                       | :heavy_check_mark:                                                          | install ID                                                                  |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.ServiceReadme](../../models/servicereadme.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## reprovision_install

Reprovision an install sandbox.



### Example Usage

<!-- UsageSnippet language="python" operationID="ReprovisionInstall" method="post" path="/v1/installs/{install_id}/reprovision" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.reprovision_install(security=models.ReprovisionInstallSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), install_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `security`                                                                      | [models.ReprovisionInstallSecurity](../../models/reprovisioninstallsecurity.md) | :heavy_check_mark:                                                              | N/A                                                                             |
| `install_id`                                                                    | *str*                                                                           | :heavy_check_mark:                                                              | install ID                                                                      |
| `plan_only`                                                                     | *Optional[bool]*                                                                | :heavy_minus_sign:                                                              | N/A                                                                             |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[str](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## reprovision_install_sandbox

Reprovision an install sandbox and redeploy all components on top.


### Example Usage

<!-- UsageSnippet language="python" operationID="ReprovisionInstallSandbox" method="post" path="/v1/installs/{install_id}/reprovision-sandbox" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.reprovision_install_sandbox(security=models.ReprovisionInstallSandboxSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), install_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `security`                                                                                    | [models.ReprovisionInstallSandboxSecurity](../../models/reprovisioninstallsandboxsecurity.md) | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `install_id`                                                                                  | *str*                                                                                         | :heavy_check_mark:                                                                            | install ID                                                                                    |
| `plan_only`                                                                                   | *Optional[bool]*                                                                              | :heavy_minus_sign:                                                                            | N/A                                                                                           |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |

### Response

**[str](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## ~~retry_workflow~~

rerun the workflow steps starting from input step id, can be used to retry a failed step

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="RetryWorkflow" method="post" path="/v1/installs/{install_id}/retry-workflow" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.retry_workflow(security=models.RetryWorkflowSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), install_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `security`                                                            | [models.RetryWorkflowSecurity](../../models/retryworkflowsecurity.md) | :heavy_check_mark:                                                    | N/A                                                                   |
| `install_id`                                                          | *str*                                                                 | :heavy_check_mark:                                                    | install ID                                                            |
| `operation`                                                           | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | Retry indicates whether to retry the current step or not              |
| `step_id`                                                             | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | StepID is the ID of the step to start the retry from                  |
| `workflow_id`                                                         | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | N/A                                                                   |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.ServiceRetryWorkflowResponse](../../models/serviceretryworkflowresponse.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_install_runner_group

Return the runner group, including runners and settings for the provided install.


### Example Usage

<!-- UsageSnippet language="python" operationID="GetInstallRunnerGroup" method="get" path="/v1/installs/{install_id}/runner-group" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.get_install_runner_group(security=models.GetInstallRunnerGroupSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), install_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `security`                                                                            | [models.GetInstallRunnerGroupSecurity](../../models/getinstallrunnergroupsecurity.md) | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `install_id`                                                                          | *str*                                                                                 | :heavy_check_mark:                                                                    | install ID                                                                            |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.AppRunnerGroup](../../models/apprunnergroup.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_install_sandbox_runs

get an installs sandbox runs

### Example Usage

<!-- UsageSnippet language="python" operationID="GetInstallSandboxRuns" method="get" path="/v1/installs/{install_id}/sandbox-runs" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.get_install_sandbox_runs(security=models.GetInstallSandboxRunsSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), install_id="<id>", offset=0, limit=10, page=0)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `security`                                                                            | [models.GetInstallSandboxRunsSecurity](../../models/getinstallsandboxrunssecurity.md) | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `install_id`                                                                          | *str*                                                                                 | :heavy_check_mark:                                                                    | install ID                                                                            |
| `offset`                                                                              | *Optional[int]*                                                                       | :heavy_minus_sign:                                                                    | offset of results to return                                                           |
| `limit`                                                                               | *Optional[int]*                                                                       | :heavy_minus_sign:                                                                    | limit of results to return                                                            |
| `page`                                                                                | *Optional[int]*                                                                       | :heavy_minus_sign:                                                                    | page number of results to return                                                      |
| `x_nuon_pagination_enabled`                                                           | *Optional[bool]*                                                                      | :heavy_minus_sign:                                                                    | Enable pagination                                                                     |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[List[models.AppInstallSandboxRun]](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_install_stack_by_install_id

get an install stack by install ID

### Example Usage

<!-- UsageSnippet language="python" operationID="GetInstallStackByInstallID" method="get" path="/v1/installs/{install_id}/stack" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.get_install_stack_by_install_id(security=models.GetInstallStackByInstallIDSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), install_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `security`                                                                                      | [models.GetInstallStackByInstallIDSecurity](../../models/getinstallstackbyinstallidsecurity.md) | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `install_id`                                                                                    | *str*                                                                                           | :heavy_check_mark:                                                                              | install ID                                                                                      |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[models.AppInstallStack](../../models/appinstallstack.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_install_stack_runs

get install stack runs

### Example Usage

<!-- UsageSnippet language="python" operationID="GetInstallStackRuns" method="get" path="/v1/installs/{install_id}/stack-runs" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.get_install_stack_runs(security=models.GetInstallStackRunsSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), install_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `security`                                                                        | [models.GetInstallStackRunsSecurity](../../models/getinstallstackrunssecurity.md) | :heavy_check_mark:                                                                | N/A                                                                               |
| `install_id`                                                                      | *str*                                                                             | :heavy_check_mark:                                                                | install ID                                                                        |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.AppInstallStackVersionRun](../../models/appinstallstackversionrun.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_install_state

Get the current state of an install.

### Example Usage

<!-- UsageSnippet language="python" operationID="GetInstallState" method="get" path="/v1/installs/{install_id}/state" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.get_install_state(security=models.GetInstallStateSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), install_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `security`                                                                | [models.GetInstallStateSecurity](../../models/getinstallstatesecurity.md) | :heavy_check_mark:                                                        | N/A                                                                       |
| `install_id`                                                              | *str*                                                                     | :heavy_check_mark:                                                        | install ID                                                                |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.GithubComPowertoolsdevMonoPkgTypesStateState](../../models/githubcompowertoolsdevmonopkgtypesstatestate.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## sync_secrets

Execute the sync secrets workflow.


### Example Usage

<!-- UsageSnippet language="python" operationID="SyncSecrets" method="post" path="/v1/installs/{install_id}/sync-secrets" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.sync_secrets(security=models.SyncSecretsSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), install_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `security`                                                          | [models.SyncSecretsSecurity](../../models/syncsecretssecurity.md)   | :heavy_check_mark:                                                  | N/A                                                                 |
| `install_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | install ID                                                          |
| `plan_only`                                                         | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[str](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_workflows

Return workflows for an install.


### Example Usage

<!-- UsageSnippet language="python" operationID="GetWorkflows" method="get" path="/v1/installs/{install_id}/workflows" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.get_workflows(security=models.GetWorkflowsSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), install_id="<id>", offset=0, limit=10, page=0)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `security`                                                          | [models.GetWorkflowsSecurity](../../models/getworkflowssecurity.md) | :heavy_check_mark:                                                  | N/A                                                                 |
| `install_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | install ID                                                          |
| `offset`                                                            | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | offset of results to return                                         |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | limit of results to return                                          |
| `page`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | page number of results to return                                    |
| `x_nuon_pagination_enabled`                                         | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Enable pagination                                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.AppWorkflow]](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_workflow

Return a workflow.


### Example Usage

<!-- UsageSnippet language="python" operationID="GetWorkflow" method="get" path="/v1/workflows/{workflow_id}" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.get_workflow(security=models.GetWorkflowSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), workflow_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `security`                                                          | [models.GetWorkflowSecurity](../../models/getworkflowsecurity.md)   | :heavy_check_mark:                                                  | N/A                                                                 |
| `workflow_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | workflow ID                                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AppWorkflow](../../models/appworkflow.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## update_workflow

update a workflow

### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateWorkflow" method="patch" path="/v1/workflows/{workflow_id}" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.update_workflow(security=models.UpdateWorkflowSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), workflow_id="<id>", approval_option=models.AppInstallApprovalOption.APPROVE_ALL)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `security`                                                                  | [models.UpdateWorkflowSecurity](../../models/updateworkflowsecurity.md)     | :heavy_check_mark:                                                          | N/A                                                                         |
| `workflow_id`                                                               | *str*                                                                       | :heavy_check_mark:                                                          | workflow ID                                                                 |
| `approval_option`                                                           | [models.AppInstallApprovalOption](../../models/appinstallapprovaloption.md) | :heavy_check_mark:                                                          | N/A                                                                         |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.AppWorkflow](../../models/appworkflow.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## cancel_workflow

cancel an ongoing workflow

### Example Usage

<!-- UsageSnippet language="python" operationID="CancelWorkflow" method="post" path="/v1/workflows/{workflow_id}/cancel" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.cancel_workflow(security=models.CancelWorkflowSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), workflow_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `security`                                                              | [models.CancelWorkflowSecurity](../../models/cancelworkflowsecurity.md) | :heavy_check_mark:                                                      | N/A                                                                     |
| `workflow_id`                                                           | *str*                                                                   | :heavy_check_mark:                                                      | workflow ID                                                             |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[bool](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## retry_owner_workflow_by_id

rerun the workflow steps starting from input step id, can be used to retry a failed step

### Example Usage

<!-- UsageSnippet language="python" operationID="RetryOwnerWorkflowByID" method="post" path="/v1/workflows/{workflow_id}/retry" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.retry_owner_workflow_by_id(security=models.RetryOwnerWorkflowByIDSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), workflow_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `security`                                                                              | [models.RetryOwnerWorkflowByIDSecurity](../../models/retryownerworkflowbyidsecurity.md) | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `workflow_id`                                                                           | *str*                                                                                   | :heavy_check_mark:                                                                      | workflow ID                                                                             |
| `operation`                                                                             | *Optional[str]*                                                                         | :heavy_minus_sign:                                                                      | Retry indicates whether to retry the current step or not                                |
| `step_id`                                                                               | *Optional[str]*                                                                         | :heavy_minus_sign:                                                                      | StepID is the ID of the step to start the retry from                                    |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[models.ServiceRetryWorkflowByIDResponse](../../models/serviceretryworkflowbyidresponse.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_workflow_steps

Return all steps for a workflow.


### Example Usage

<!-- UsageSnippet language="python" operationID="GetWorkflowSteps" method="get" path="/v1/workflows/{workflow_id}/steps" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.get_workflow_steps(security=models.GetWorkflowStepsSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), workflow_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `security`                                                                  | [models.GetWorkflowStepsSecurity](../../models/getworkflowstepssecurity.md) | :heavy_check_mark:                                                          | N/A                                                                         |
| `workflow_id`                                                               | *str*                                                                       | :heavy_check_mark:                                                          | workflow ID                                                                 |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[List[models.AppWorkflowStep]](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_workflow_step

Return a single workflow step.


### Example Usage

<!-- UsageSnippet language="python" operationID="GetWorkflowStep" method="get" path="/v1/workflows/{workflow_id}/steps/{workflow_step_id}" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.get_workflow_step(security=models.GetWorkflowStepSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), workflow_id="<id>", workflow_step_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `security`                                                                | [models.GetWorkflowStepSecurity](../../models/getworkflowstepsecurity.md) | :heavy_check_mark:                                                        | N/A                                                                       |
| `workflow_id`                                                             | *str*                                                                     | :heavy_check_mark:                                                        | workflow id                                                               |
| `workflow_step_id`                                                        | *str*                                                                     | :heavy_check_mark:                                                        | step id                                                                   |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.AppWorkflowStep](../../models/appworkflowstep.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_workflow_step_approval

get an workflow step approval

### Example Usage

<!-- UsageSnippet language="python" operationID="GetWorkflowStepApproval" method="get" path="/v1/workflows/{workflow_id}/steps/{workflow_step_id}/approvals/{approval_id}" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.get_workflow_step_approval(security=models.GetWorkflowStepApprovalSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), workflow_id="<id>", workflow_step_id="<id>", approval_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `security`                                                                                | [models.GetWorkflowStepApprovalSecurity](../../models/getworkflowstepapprovalsecurity.md) | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `workflow_id`                                                                             | *str*                                                                                     | :heavy_check_mark:                                                                        | workflow id                                                                               |
| `workflow_step_id`                                                                        | *str*                                                                                     | :heavy_check_mark:                                                                        | step id                                                                                   |
| `approval_id`                                                                             | *str*                                                                                     | :heavy_check_mark:                                                                        | approval id                                                                               |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |

### Response

**[models.AppWorkflowStepApproval](../../models/appworkflowstepapproval.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_workflow_step_approval_contents

Return the contents of a json plan for an approval (compressed).


### Example Usage

<!-- UsageSnippet language="python" operationID="GetWorkflowStepApprovalContents" method="get" path="/v1/workflows/{workflow_id}/steps/{workflow_step_id}/approvals/{approval_id}/contents" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.get_workflow_step_approval_contents(security=models.GetWorkflowStepApprovalContentsSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), workflow_id="<id>", workflow_step_id="<id>", approval_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                 | Type                                                                                                      | Required                                                                                                  | Description                                                                                               |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                | [models.GetWorkflowStepApprovalContentsSecurity](../../models/getworkflowstepapprovalcontentssecurity.md) | :heavy_check_mark:                                                                                        | N/A                                                                                                       |
| `workflow_id`                                                                                             | *str*                                                                                                     | :heavy_check_mark:                                                                                        | workflow id                                                                                               |
| `workflow_step_id`                                                                                        | *str*                                                                                                     | :heavy_check_mark:                                                                                        | step id                                                                                                   |
| `approval_id`                                                                                             | *str*                                                                                                     | :heavy_check_mark:                                                                                        | approval id                                                                                               |
| `retries`                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                          | :heavy_minus_sign:                                                                                        | Configuration to override the default retry behavior of the client.                                       |

### Response

**[List[int]](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## create_workflow_step_approval_response

deploy a build to an install

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateWorkflowStepApprovalResponse" method="post" path="/v1/workflows/{workflow_id}/steps/{workflow_step_id}/approvals/{approval_id}/response" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installs.create_workflow_step_approval_response(security=models.CreateWorkflowStepApprovalResponseSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), workflow_id="<id>", workflow_step_id="<id>", approval_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                       | Type                                                                                                            | Required                                                                                                        | Description                                                                                                     |
| --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                      | [models.CreateWorkflowStepApprovalResponseSecurity](../../models/createworkflowstepapprovalresponsesecurity.md) | :heavy_check_mark:                                                                                              | N/A                                                                                                             |
| `workflow_id`                                                                                                   | *str*                                                                                                           | :heavy_check_mark:                                                                                              | workflow id                                                                                                     |
| `workflow_step_id`                                                                                              | *str*                                                                                                           | :heavy_check_mark:                                                                                              | step id                                                                                                         |
| `approval_id`                                                                                                   | *str*                                                                                                           | :heavy_check_mark:                                                                                              | approval id                                                                                                     |
| `note`                                                                                                          | *Optional[str]*                                                                                                 | :heavy_minus_sign:                                                                                              | N/A                                                                                                             |
| `response_type`                                                                                                 | [Optional[models.AppWorkflowStepResponseType]](../../models/appworkflowstepresponsetype.md)                     | :heavy_minus_sign:                                                                                              | N/A                                                                                                             |
| `retries`                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                | :heavy_minus_sign:                                                                                              | Configuration to override the default retry behavior of the client.                                             |

### Response

**[models.AppWorkflowStepApprovalResponse](../../models/appworkflowstepapprovalresponse.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |