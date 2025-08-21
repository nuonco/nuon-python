# Apps
(*apps*)

## Overview

apps

### Available Operations

* [get_apps](#get_apps) - get all apps for the current org
* [create_app](#create_app) - create an app
* [delete_app](#delete_app) - delete an app
* [get_app](#get_app) - get an app
* [update_app](#update_app) - update an app
* [get_app_branches](#get_app_branches) - get app branches
* [create_app_branch](#create_app_branch) - Cancel a runner job.

* [get_app_branch_app_configs](#get_app_branch_app_configs) - get app branch app configs
* [create_app_break_glass_config](#create_app_break_glass_config) - Create a break glass config for an app.

* [get_app_break_glass_config](#get_app_break_glass_config) - get app break_glass config
* [create_app_config](#create_app_config) - Create an app config, by pushing the contents of a config file.

The API will automatically configure the app according to the config file in the background.

* [get_app_config](#get_app_config) - get an app config
* [update_app_config](#update_app_config) - Update an app config, setting status and state.

* [get_app_config_graph](#get_app_config_graph) - get an app config graph
* [update_app_config_installs](#update_app_config_installs)
* [get_app_configs](#get_app_configs) - get app configs
* [create_app_input_config](#create_app_input_config) - App input configs allow you to declare the inputs for your application, and do things such as require customer inputs or 
expose configuration knobs in your application.

* [get_app_input_configs](#get_app_input_configs) - get app input configs
* [get_app_input_config](#get_app_input_config) - get app input config
* [get_app_input_latest_config](#get_app_input_latest_config) - get latest app input config
* [get_latest_app_break_glass_config](#get_latest_app_break_glass_config) - get latest app input config
* [get_latest_app_permissions_config](#get_latest_app_permissions_config) - get latest app permissions config
* [get_latest_app_policies_config](#get_latest_app_policies_config) - get latest app policies config
* [get_latest_app_secrets_config](#get_latest_app_secrets_config) - get latest app secrets config
* [get_app_latest_config](#get_app_latest_config) - get latest app config
* [create_app_permissions_config](#create_app_permissions_config) - Create app permissions config.

* [get_app_permissions_config](#get_app_permissions_config) - get app permissions config
* [create_app_policies_config](#create_app_policies_config) - Create app policies config.

* [get_app_policies_config](#get_app_policies_config) - get app policies config
* [get_app_runner_configs](#get_app_runner_configs) - get app runner configs
* [create_app_runner_config](#create_app_runner_config) - create an app runner config
* [get_app_runner_latest_config](#get_app_runner_latest_config) - get latest app runner config
* [create_app_sandbox_config](#create_app_sandbox_config) - create an app sandbox config
* [get_app_sandbox_configs](#get_app_sandbox_configs) - get app sandbox configs
* [get_app_sandbox_latest_config](#get_app_sandbox_latest_config) - get latest app sandbox config
* [create_app_secret](#create_app_secret) - create an app secret
* [delete_app_secret](#delete_app_secret) - delete an app secret
* [get_app_secrets](#get_app_secrets) - get app secrets
* [create_app_secrets_config](#create_app_secrets_config) - Create an app secrets config.

* [get_app_secrets_config](#get_app_secrets_config) - get app secrets config
* [create_app_stack_config](#create_app_stack_config) - create an app stack config
* [get_app_stack_config](#get_app_stack_config) - get app stack config
* [get_app_config_template](#get_app_config_template) - get an app config template

## get_apps

get all apps for the current org

### Example Usage

<!-- UsageSnippet language="python" operationID="GetApps" method="get" path="/v1/apps" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.apps.get_apps(security=models.GetAppsSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), offset=0, limit=10, page=0)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `security`                                                          | [models.GetAppsSecurity](../../models/getappssecurity.md)           | :heavy_check_mark:                                                  | N/A                                                                 |
| `offset`                                                            | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | offset of jobs to return                                            |
| `q`                                                                 | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | search query to filter apps by name                                 |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | limit of jobs to return                                             |
| `page`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | page number of results to return                                    |
| `x_nuon_pagination_enabled`                                         | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Enable pagination                                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.AppApp]](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## create_app

create an app

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateApp" method="post" path="/v1/apps" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.apps.create_app(security=models.CreateAppSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), name="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `security`                                                          | [models.CreateAppSecurity](../../models/createappsecurity.md)       | :heavy_check_mark:                                                  | N/A                                                                 |
| `name`                                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `description`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `display_name`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `slack_webhook_url`                                                 | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AppApp](../../models/appapp.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## delete_app

delete an app

### Example Usage

<!-- UsageSnippet language="python" operationID="DeleteApp" method="delete" path="/v1/apps/{app_id}" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.apps.delete_app(security=models.DeleteAppSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), app_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `security`                                                          | [models.DeleteAppSecurity](../../models/deleteappsecurity.md)       | :heavy_check_mark:                                                  | N/A                                                                 |
| `app_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | app ID                                                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[bool](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_app

Return an app.


### Example Usage

<!-- UsageSnippet language="python" operationID="GetApp" method="get" path="/v1/apps/{app_id}" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.apps.get_app(security=models.GetAppSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), app_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `security`                                                          | [models.GetAppSecurity](../../models/getappsecurity.md)             | :heavy_check_mark:                                                  | N/A                                                                 |
| `app_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | app ID                                                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AppApp](../../models/appapp.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## update_app

update an app

### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateApp" method="patch" path="/v1/apps/{app_id}" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.apps.update_app(security=models.UpdateAppSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), app_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `security`                                                          | [models.UpdateAppSecurity](../../models/updateappsecurity.md)       | :heavy_check_mark:                                                  | N/A                                                                 |
| `app_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | app ID                                                              |
| `config_directory`                                                  | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `config_repo`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `description`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `display_name`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `name`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `slack_webhook_url`                                                 | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AppApp](../../models/appapp.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_app_branches

get app branches

### Example Usage

<!-- UsageSnippet language="python" operationID="GetAppBranches" method="get" path="/v1/apps/{app_id}/branches" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.apps.get_app_branches(security=models.GetAppBranchesSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), app_id="<id>", offset=0, limit=10, page=0)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `security`                                                              | [models.GetAppBranchesSecurity](../../models/getappbranchessecurity.md) | :heavy_check_mark:                                                      | N/A                                                                     |
| `app_id`                                                                | *str*                                                                   | :heavy_check_mark:                                                      | app ID                                                                  |
| `offset`                                                                | *Optional[int]*                                                         | :heavy_minus_sign:                                                      | offset of branches to return                                            |
| `limit`                                                                 | *Optional[int]*                                                         | :heavy_minus_sign:                                                      | limit of branches to return                                             |
| `page`                                                                  | *Optional[int]*                                                         | :heavy_minus_sign:                                                      | page number of results to return                                        |
| `x_nuon_pagination_enabled`                                             | *Optional[bool]*                                                        | :heavy_minus_sign:                                                      | Enable pagination                                                       |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[List[models.AppAppBranch]](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## create_app_branch

Cancel a runner job.


### Example Usage

<!-- UsageSnippet language="python" operationID="CreateAppBranch" method="post" path="/v1/apps/{app_id}/branches" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.apps.create_app_branch(security=models.CreateAppBranchSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), app_id="<id>", connected_github_vcs_config_id="<id>", name="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `security`                                                                | [models.CreateAppBranchSecurity](../../models/createappbranchsecurity.md) | :heavy_check_mark:                                                        | N/A                                                                       |
| `app_id`                                                                  | *str*                                                                     | :heavy_check_mark:                                                        | app ID                                                                    |
| `connected_github_vcs_config_id`                                          | *str*                                                                     | :heavy_check_mark:                                                        | N/A                                                                       |
| `name`                                                                    | *str*                                                                     | :heavy_check_mark:                                                        | N/A                                                                       |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.AppAppBranch](../../models/appappbranch.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_app_branch_app_configs

get app branch app configs

### Example Usage

<!-- UsageSnippet language="python" operationID="GetAppBranchAppConfigs" method="get" path="/v1/apps/{app_id}/branches/{app_branch_id}/configs" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.apps.get_app_branch_app_configs(security=models.GetAppBranchAppConfigsSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), app_id="<id>", app_branch_id="<id>", offset=0, limit=10, page=0)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `security`                                                                              | [models.GetAppBranchAppConfigsSecurity](../../models/getappbranchappconfigssecurity.md) | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `app_id`                                                                                | *str*                                                                                   | :heavy_check_mark:                                                                      | app ID                                                                                  |
| `app_branch_id`                                                                         | *str*                                                                                   | :heavy_check_mark:                                                                      | app branch ID                                                                           |
| `offset`                                                                                | *Optional[int]*                                                                         | :heavy_minus_sign:                                                                      | offset of branches to return                                                            |
| `limit`                                                                                 | *Optional[int]*                                                                         | :heavy_minus_sign:                                                                      | limit of branches to return                                                             |
| `page`                                                                                  | *Optional[int]*                                                                         | :heavy_minus_sign:                                                                      | page number of results to return                                                        |
| `x_nuon_pagination_enabled`                                                             | *Optional[bool]*                                                                        | :heavy_minus_sign:                                                                      | Enable pagination                                                                       |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[List[models.AppAppConfig]](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## create_app_break_glass_config

Create a break glass config for an app.


### Example Usage

<!-- UsageSnippet language="python" operationID="CreateAppBreakGlassConfig" method="post" path="/v1/apps/{app_id}/break-glass-configs" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.apps.create_app_break_glass_config(security=models.CreateAppBreakGlassConfigSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), app_id="<id>", app_config_id="<id>", roles=[])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `security`                                                                                    | [models.CreateAppBreakGlassConfigSecurity](../../models/createappbreakglassconfigsecurity.md) | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `app_id`                                                                                      | *str*                                                                                         | :heavy_check_mark:                                                                            | app ID                                                                                        |
| `app_config_id`                                                                               | *str*                                                                                         | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `roles`                                                                                       | List[[models.ServiceAppAWSIAMRoleConfig](../../models/serviceappawsiamroleconfig.md)]         | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |

### Response

**[models.AppAppBreakGlassConfig](../../models/appappbreakglassconfig.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_app_break_glass_config

Return an app break glass config by id.


### Example Usage

<!-- UsageSnippet language="python" operationID="GetAppBreakGlassConfig" method="get" path="/v1/apps/{app_id}/break-glass-configs/{break_glass_config_id}" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.apps.get_app_break_glass_config(security=models.GetAppBreakGlassConfigSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), app_id="<id>", break_glass_config_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `security`                                                                              | [models.GetAppBreakGlassConfigSecurity](../../models/getappbreakglassconfigsecurity.md) | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `app_id`                                                                                | *str*                                                                                   | :heavy_check_mark:                                                                      | app ID                                                                                  |
| `break_glass_config_id`                                                                 | *str*                                                                                   | :heavy_check_mark:                                                                      | app break glass config ID                                                               |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[models.AppAppBreakGlassConfig](../../models/appappbreakglassconfig.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## create_app_config

Create an app config, by pushing the contents of a config file.

The API will automatically configure the app according to the config file in the background.


### Example Usage

<!-- UsageSnippet language="python" operationID="CreateAppConfig" method="post" path="/v1/apps/{app_id}/config" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.apps.create_app_config(security=models.CreateAppConfigSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), app_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `security`                                                                | [models.CreateAppConfigSecurity](../../models/createappconfigsecurity.md) | :heavy_check_mark:                                                        | N/A                                                                       |
| `app_id`                                                                  | *str*                                                                     | :heavy_check_mark:                                                        | app ID                                                                    |
| `cli_version`                                                             | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | N/A                                                                       |
| `readme`                                                                  | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | not required Readme                                                       |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.AppAppConfig](../../models/appappconfig.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_app_config

Fetch an app config by id.


### Example Usage

<!-- UsageSnippet language="python" operationID="GetAppConfig" method="get" path="/v1/apps/{app_id}/config/{app_config_id}" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.apps.get_app_config(security=models.GetAppConfigSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), app_id="<id>", app_config_id="<id>", recurse=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `security`                                                          | [models.GetAppConfigSecurity](../../models/getappconfigsecurity.md) | :heavy_check_mark:                                                  | N/A                                                                 |
| `app_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | app ID                                                              |
| `app_config_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | app config ID                                                       |
| `recurse`                                                           | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | load all children configs                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AppAppConfig](../../models/appappconfig.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## update_app_config

Update an app config, setting status and state.


### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateAppConfig" method="patch" path="/v1/apps/{app_id}/config/{app_config_id}" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.apps.update_app_config(security=models.UpdateAppConfigSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), app_id="<id>", app_config_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `security`                                                                | [models.UpdateAppConfigSecurity](../../models/updateappconfigsecurity.md) | :heavy_check_mark:                                                        | N/A                                                                       |
| `app_id`                                                                  | *str*                                                                     | :heavy_check_mark:                                                        | app ID                                                                    |
| `app_config_id`                                                           | *str*                                                                     | :heavy_check_mark:                                                        | app config ID                                                             |
| `component_ids`                                                           | List[*str*]                                                               | :heavy_minus_sign:                                                        | N/A                                                                       |
| `state`                                                                   | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | N/A                                                                       |
| `status`                                                                  | [Optional[models.AppAppConfigStatus]](../../models/appappconfigstatus.md) | :heavy_minus_sign:                                                        | N/A                                                                       |
| `status_description`                                                      | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | N/A                                                                       |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.AppAppConfig](../../models/appappconfig.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_app_config_graph

Return raw graphviz data as a string that can be used to visualize a graph for an app.

Note, for more complex viewing recommend to copy this output directly into [Graphviz
viewer](https://dreampuf.github.io/GraphvizOnline).


### Example Usage

<!-- UsageSnippet language="python" operationID="GetAppConfigGraph" method="get" path="/v1/apps/{app_id}/config/{app_config_id}/graph" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.apps.get_app_config_graph(security=models.GetAppConfigGraphSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), app_id="<id>", app_config_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `security`                                                                    | [models.GetAppConfigGraphSecurity](../../models/getappconfiggraphsecurity.md) | :heavy_check_mark:                                                            | N/A                                                                           |
| `app_id`                                                                      | *str*                                                                         | :heavy_check_mark:                                                            | app ID                                                                        |
| `app_config_id`                                                               | *str*                                                                         | :heavy_check_mark:                                                            | app config ID                                                                 |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[str](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## update_app_config_installs

### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateAppConfigInstalls" method="post" path="/v1/apps/{app_id}/config/{app_config_id}/update-installs" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.apps.update_app_config_installs(security=models.UpdateAppConfigInstallsSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), app_id="<id>", app_config_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `security`                                                                                | [models.UpdateAppConfigInstallsSecurity](../../models/updateappconfiginstallssecurity.md) | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `app_id`                                                                                  | *str*                                                                                     | :heavy_check_mark:                                                                        | app ID                                                                                    |
| `app_config_id`                                                                           | *str*                                                                                     | :heavy_check_mark:                                                                        | app config ID                                                                             |
| `install_i_ds`                                                                            | List[*str*]                                                                               | :heavy_minus_sign:                                                                        | N/A                                                                                       |
| `update_all`                                                                              | *Optional[bool]*                                                                          | :heavy_minus_sign:                                                                        | N/A                                                                                       |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |

### Response

**[str](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_app_configs

Returns all configs for the app.


### Example Usage

<!-- UsageSnippet language="python" operationID="GetAppConfigs" method="get" path="/v1/apps/{app_id}/configs" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.apps.get_app_configs(security=models.GetAppConfigsSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), app_id="<id>", offset=0, limit=10, page=0)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `security`                                                            | [models.GetAppConfigsSecurity](../../models/getappconfigssecurity.md) | :heavy_check_mark:                                                    | N/A                                                                   |
| `app_id`                                                              | *str*                                                                 | :heavy_check_mark:                                                    | app ID                                                                |
| `offset`                                                              | *Optional[int]*                                                       | :heavy_minus_sign:                                                    | offset of jobs to return                                              |
| `limit`                                                               | *Optional[int]*                                                       | :heavy_minus_sign:                                                    | limit of jobs to return                                               |
| `page`                                                                | *Optional[int]*                                                       | :heavy_minus_sign:                                                    | page number of results to return                                      |
| `x_nuon_pagination_enabled`                                           | *Optional[bool]*                                                      | :heavy_minus_sign:                                                    | Enable pagination                                                     |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[List[models.AppAppConfig]](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## create_app_input_config

App input configs allow you to declare the inputs for your application, and do things such as require customer inputs or 
expose configuration knobs in your application.


### Example Usage

<!-- UsageSnippet language="python" operationID="CreateAppInputConfig" method="post" path="/v1/apps/{app_id}/input-config" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.apps.create_app_input_config(security=models.CreateAppInputConfigSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), app_id="<id>", groups={

    }, inputs={

    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `security`                                                                          | [models.CreateAppInputConfigSecurity](../../models/createappinputconfigsecurity.md) | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `app_id`                                                                            | *str*                                                                               | :heavy_check_mark:                                                                  | app ID                                                                              |
| `groups`                                                                            | Dict[str, [models.ServiceAppGroupRequest](../../models/serviceappgrouprequest.md)]  | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `inputs`                                                                            | Dict[str, [models.ServiceAppInputRequest](../../models/serviceappinputrequest.md)]  | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `app_config_id`                                                                     | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.AppAppInputConfig](../../models/appappinputconfig.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_app_input_configs

get app input configs

### Example Usage

<!-- UsageSnippet language="python" operationID="GetAppInputConfigs" method="get" path="/v1/apps/{app_id}/input-configs" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.apps.get_app_input_configs(security=models.GetAppInputConfigsSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), app_id="<id>", offset=0, limit=10, page=0)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `security`                                                                      | [models.GetAppInputConfigsSecurity](../../models/getappinputconfigssecurity.md) | :heavy_check_mark:                                                              | N/A                                                                             |
| `app_id`                                                                        | *str*                                                                           | :heavy_check_mark:                                                              | app ID                                                                          |
| `offset`                                                                        | *Optional[int]*                                                                 | :heavy_minus_sign:                                                              | offset of jobs to return                                                        |
| `limit`                                                                         | *Optional[int]*                                                                 | :heavy_minus_sign:                                                              | limit of jobs to return                                                         |
| `page`                                                                          | *Optional[int]*                                                                 | :heavy_minus_sign:                                                              | page number of results to return                                                |
| `x_nuon_pagination_enabled`                                                     | *Optional[bool]*                                                                | :heavy_minus_sign:                                                              | Enable pagination                                                               |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[List[models.AppAppInputConfig]](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_app_input_config

Return an input config by id.


### Example Usage

<!-- UsageSnippet language="python" operationID="GetAppInputConfig" method="get" path="/v1/apps/{app_id}/input-configs/{input_config_id}" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.apps.get_app_input_config(security=models.GetAppInputConfigSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), app_id="<id>", input_config_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `security`                                                                    | [models.GetAppInputConfigSecurity](../../models/getappinputconfigsecurity.md) | :heavy_check_mark:                                                            | N/A                                                                           |
| `app_id`                                                                      | *str*                                                                         | :heavy_check_mark:                                                            | app ID                                                                        |
| `input_config_id`                                                             | *str*                                                                         | :heavy_check_mark:                                                            | input config ID                                                               |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[models.AppAppInputConfig](../../models/appappinputconfig.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_app_input_latest_config

get latest app input config

### Example Usage

<!-- UsageSnippet language="python" operationID="GetAppInputLatestConfig" method="get" path="/v1/apps/{app_id}/input-latest-config" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.apps.get_app_input_latest_config(security=models.GetAppInputLatestConfigSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), app_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `security`                                                                                | [models.GetAppInputLatestConfigSecurity](../../models/getappinputlatestconfigsecurity.md) | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `app_id`                                                                                  | *str*                                                                                     | :heavy_check_mark:                                                                        | app ID                                                                                    |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |

### Response

**[models.AppAppInputConfig](../../models/appappinputconfig.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_latest_app_break_glass_config

Get the latest break glass config for an app.


### Example Usage

<!-- UsageSnippet language="python" operationID="GetLatestAppBreakGlassConfig" method="get" path="/v1/apps/{app_id}/latest-app-break-glass-config" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.apps.get_latest_app_break_glass_config(security=models.GetLatestAppBreakGlassConfigSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), app_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                           | Type                                                                                                | Required                                                                                            | Description                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `security`                                                                                          | [models.GetLatestAppBreakGlassConfigSecurity](../../models/getlatestappbreakglassconfigsecurity.md) | :heavy_check_mark:                                                                                  | N/A                                                                                                 |
| `app_id`                                                                                            | *str*                                                                                               | :heavy_check_mark:                                                                                  | app ID                                                                                              |
| `retries`                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                    | :heavy_minus_sign:                                                                                  | Configuration to override the default retry behavior of the client.                                 |

### Response

**[models.AppAppBreakGlassConfig](../../models/appappbreakglassconfig.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_latest_app_permissions_config

Get the latest app permissions config.


### Example Usage

<!-- UsageSnippet language="python" operationID="GetLatestAppPermissionsConfig" method="get" path="/v1/apps/{app_id}/latest-app-permissions-config" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.apps.get_latest_app_permissions_config(security=models.GetLatestAppPermissionsConfigSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), app_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `security`                                                                                            | [models.GetLatestAppPermissionsConfigSecurity](../../models/getlatestapppermissionsconfigsecurity.md) | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `app_id`                                                                                              | *str*                                                                                                 | :heavy_check_mark:                                                                                    | app ID                                                                                                |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |

### Response

**[models.AppAppPermissionsConfig](../../models/appapppermissionsconfig.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_latest_app_policies_config

Get latest app policies config.


### Example Usage

<!-- UsageSnippet language="python" operationID="GetLatestAppPoliciesConfig" method="get" path="/v1/apps/{app_id}/latest-app-policies-config" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.apps.get_latest_app_policies_config(security=models.GetLatestAppPoliciesConfigSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), app_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `security`                                                                                      | [models.GetLatestAppPoliciesConfigSecurity](../../models/getlatestapppoliciesconfigsecurity.md) | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `app_id`                                                                                        | *str*                                                                                           | :heavy_check_mark:                                                                              | app ID                                                                                          |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[models.AppAppPoliciesConfig](../../models/appapppoliciesconfig.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_latest_app_secrets_config

Get the latest app secrets config.


### Example Usage

<!-- UsageSnippet language="python" operationID="GetLatestAppSecretsConfig" method="get" path="/v1/apps/{app_id}/latest-app-secrets-config" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.apps.get_latest_app_secrets_config(security=models.GetLatestAppSecretsConfigSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), app_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `security`                                                                                    | [models.GetLatestAppSecretsConfigSecurity](../../models/getlatestappsecretsconfigsecurity.md) | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `app_id`                                                                                      | *str*                                                                                         | :heavy_check_mark:                                                                            | app ID                                                                                        |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |

### Response

**[models.AppAppSecretsConfig](../../models/appappsecretsconfig.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_app_latest_config

Returns the most recent config for the provided app.


### Example Usage

<!-- UsageSnippet language="python" operationID="GetAppLatestConfig" method="get" path="/v1/apps/{app_id}/latest-config" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.apps.get_app_latest_config(security=models.GetAppLatestConfigSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), app_id="<id>", recurse=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `security`                                                                      | [models.GetAppLatestConfigSecurity](../../models/getapplatestconfigsecurity.md) | :heavy_check_mark:                                                              | N/A                                                                             |
| `app_id`                                                                        | *str*                                                                           | :heavy_check_mark:                                                              | app ID                                                                          |
| `recurse`                                                                       | *Optional[bool]*                                                                | :heavy_minus_sign:                                                              | load all children configs                                                       |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[models.AppAppConfig](../../models/appappconfig.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## create_app_permissions_config

Create app permissions config.


### Example Usage

<!-- UsageSnippet language="python" operationID="CreateAppPermissionsConfig" method="post" path="/v1/apps/{app_id}/permissions-configs" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.apps.create_app_permissions_config(security=models.CreateAppPermissionsConfigSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), app_id="<id>", app_config_id="<id>", deprovision_role={
        "description": "tribe familiar even at uh-huh gah despite hmph",
        "display_name": "Amos33",
        "name": "<value>",
    }, maintenance_role={
        "description": "opposite ack toward neaten obtrude black-and-white yawningly ugh shallow horn",
        "display_name": "Jennie.Wintheiser",
        "name": "<value>",
    }, provision_role={
        "description": "inasmuch unique cleave via",
        "display_name": "Lonzo.Haley",
        "name": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `security`                                                                                      | [models.CreateAppPermissionsConfigSecurity](../../models/createapppermissionsconfigsecurity.md) | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `app_id`                                                                                        | *str*                                                                                           | :heavy_check_mark:                                                                              | app ID                                                                                          |
| `app_config_id`                                                                                 | *str*                                                                                           | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `deprovision_role`                                                                              | [models.ServiceAppAWSIAMRoleConfig](../../models/serviceappawsiamroleconfig.md)                 | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `maintenance_role`                                                                              | [models.ServiceAppAWSIAMRoleConfig](../../models/serviceappawsiamroleconfig.md)                 | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `provision_role`                                                                                | [models.ServiceAppAWSIAMRoleConfig](../../models/serviceappawsiamroleconfig.md)                 | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[models.AppAppPermissionsConfig](../../models/appapppermissionsconfig.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_app_permissions_config

Return an app permissions config by id.


### Example Usage

<!-- UsageSnippet language="python" operationID="GetAppPermissionsConfig" method="get" path="/v1/apps/{app_id}/permissions-configs/{permissions_config_id}" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.apps.get_app_permissions_config(security=models.GetAppPermissionsConfigSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), app_id="<id>", permissions_config_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `security`                                                                                | [models.GetAppPermissionsConfigSecurity](../../models/getapppermissionsconfigsecurity.md) | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `app_id`                                                                                  | *str*                                                                                     | :heavy_check_mark:                                                                        | app ID                                                                                    |
| `permissions_config_id`                                                                   | *str*                                                                                     | :heavy_check_mark:                                                                        | input config ID                                                                           |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |

### Response

**[models.AppAppPermissionsConfig](../../models/appapppermissionsconfig.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## create_app_policies_config

Create app policies config.


### Example Usage

<!-- UsageSnippet language="python" operationID="CreateAppPoliciesConfig" method="post" path="/v1/apps/{app_id}/policies-configs" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.apps.create_app_policies_config(security=models.CreateAppPoliciesConfigSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), app_id="<id>", app_config_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `security`                                                                                | [models.CreateAppPoliciesConfigSecurity](../../models/createapppoliciesconfigsecurity.md) | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `app_id`                                                                                  | *str*                                                                                     | :heavy_check_mark:                                                                        | app ID                                                                                    |
| `app_config_id`                                                                           | *str*                                                                                     | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `policies`                                                                                | List[[models.ServiceAppPolicyConfig](../../models/serviceapppolicyconfig.md)]             | :heavy_minus_sign:                                                                        | N/A                                                                                       |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |

### Response

**[models.AppAppPoliciesConfig](../../models/appapppoliciesconfig.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_app_policies_config

Return an app policy config by id.


### Example Usage

<!-- UsageSnippet language="python" operationID="GetAppPoliciesConfig" method="get" path="/v1/apps/{app_id}/policies-configs/{policies_config_id}" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.apps.get_app_policies_config(security=models.GetAppPoliciesConfigSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), app_id="<id>", policies_config_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `security`                                                                          | [models.GetAppPoliciesConfigSecurity](../../models/getapppoliciesconfigsecurity.md) | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `app_id`                                                                            | *str*                                                                               | :heavy_check_mark:                                                                  | app ID                                                                              |
| `policies_config_id`                                                                | *str*                                                                               | :heavy_check_mark:                                                                  | input policies config ID                                                            |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.AppAppPoliciesConfig](../../models/appapppoliciesconfig.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_app_runner_configs

get app runner configs

### Example Usage

<!-- UsageSnippet language="python" operationID="GetAppRunnerConfigs" method="get" path="/v1/apps/{app_id}/runner-configs" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.apps.get_app_runner_configs(security=models.GetAppRunnerConfigsSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), app_id="<id>", offset=0, limit=10, page=0)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `security`                                                                        | [models.GetAppRunnerConfigsSecurity](../../models/getapprunnerconfigssecurity.md) | :heavy_check_mark:                                                                | N/A                                                                               |
| `app_id`                                                                          | *str*                                                                             | :heavy_check_mark:                                                                | app ID                                                                            |
| `offset`                                                                          | *Optional[int]*                                                                   | :heavy_minus_sign:                                                                | offset of jobs to return                                                          |
| `limit`                                                                           | *Optional[int]*                                                                   | :heavy_minus_sign:                                                                | limit of jobs to return                                                           |
| `page`                                                                            | *Optional[int]*                                                                   | :heavy_minus_sign:                                                                | page number of results to return                                                  |
| `x_nuon_pagination_enabled`                                                       | *Optional[bool]*                                                                  | :heavy_minus_sign:                                                                | Enable pagination                                                                 |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[List[models.AppAppRunnerConfig]](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## create_app_runner_config

create an app runner config

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateAppRunnerConfig" method="post" path="/v1/apps/{app_id}/runner-configs" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.apps.create_app_runner_config(security=models.CreateAppRunnerConfigSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), app_id="<id>", type_=models.AppAppRunnerType.AWS_EKS)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `security`                                                                                            | [models.CreateAppRunnerConfigSecurity](../../models/createapprunnerconfigsecurity.md)                 | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `app_id`                                                                                              | *str*                                                                                                 | :heavy_check_mark:                                                                                    | app ID                                                                                                |
| `type`                                                                                                | [models.AppAppRunnerType](../../models/appapprunnertype.md)                                           | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `app_config_id`                                                                                       | *Optional[str]*                                                                                       | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `env_vars`                                                                                            | Dict[str, *str*]                                                                                      | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `helm_driver`                                                                                         | [Optional[models.AppAppRunnerConfigHelmDriverType]](../../models/appapprunnerconfighelmdrivertype.md) | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `init_script_url`                                                                                     | *Optional[str]*                                                                                       | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |

### Response

**[models.AppAppRunnerConfig](../../models/appapprunnerconfig.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_app_runner_latest_config

get latest app runner config

### Example Usage

<!-- UsageSnippet language="python" operationID="GetAppRunnerLatestConfig" method="get" path="/v1/apps/{app_id}/runner-latest-config" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.apps.get_app_runner_latest_config(security=models.GetAppRunnerLatestConfigSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), app_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `security`                                                                                  | [models.GetAppRunnerLatestConfigSecurity](../../models/getapprunnerlatestconfigsecurity.md) | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `app_id`                                                                                    | *str*                                                                                       | :heavy_check_mark:                                                                          | app ID                                                                                      |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |

### Response

**[models.AppAppRunnerConfig](../../models/appapprunnerconfig.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## create_app_sandbox_config

create an app sandbox config

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateAppSandboxConfig" method="post" path="/v1/apps/{app_id}/sandbox-config" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.apps.create_app_sandbox_config(security=models.CreateAppSandboxConfigSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), app_id="<id>", env_vars={

    }, terraform_version="<value>", variables={
        "key": "<value>",
        "key1": "<value>",
        "key2": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                       | Type                                                                                                                            | Required                                                                                                                        | Description                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                      | [models.CreateAppSandboxConfigSecurity](../../models/createappsandboxconfigsecurity.md)                                         | :heavy_check_mark:                                                                                                              | N/A                                                                                                                             |
| `app_id`                                                                                                                        | *str*                                                                                                                           | :heavy_check_mark:                                                                                                              | app ID                                                                                                                          |
| `env_vars`                                                                                                                      | Dict[str, *str*]                                                                                                                | :heavy_check_mark:                                                                                                              | N/A                                                                                                                             |
| `terraform_version`                                                                                                             | *str*                                                                                                                           | :heavy_check_mark:                                                                                                              | N/A                                                                                                                             |
| `variables`                                                                                                                     | Dict[str, *str*]                                                                                                                | :heavy_check_mark:                                                                                                              | N/A                                                                                                                             |
| `app_config_id`                                                                                                                 | *Optional[str]*                                                                                                                 | :heavy_minus_sign:                                                                                                              | N/A                                                                                                                             |
| `connected_github_vcs_config`                                                                                                   | [Optional[models.ServiceConnectedGithubVCSSandboxConfigRequest]](../../models/serviceconnectedgithubvcssandboxconfigrequest.md) | :heavy_minus_sign:                                                                                                              | N/A                                                                                                                             |
| `public_git_vcs_config`                                                                                                         | [Optional[models.ServicePublicGitVCSSandboxConfigRequest]](../../models/servicepublicgitvcssandboxconfigrequest.md)             | :heavy_minus_sign:                                                                                                              | N/A                                                                                                                             |
| `variables_files`                                                                                                               | List[*str*]                                                                                                                     | :heavy_minus_sign:                                                                                                              | N/A                                                                                                                             |
| `retries`                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                | :heavy_minus_sign:                                                                                                              | Configuration to override the default retry behavior of the client.                                                             |

### Response

**[models.AppAppSandboxConfig](../../models/appappsandboxconfig.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_app_sandbox_configs

get app sandbox configs

### Example Usage

<!-- UsageSnippet language="python" operationID="GetAppSandboxConfigs" method="get" path="/v1/apps/{app_id}/sandbox-configs" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.apps.get_app_sandbox_configs(security=models.GetAppSandboxConfigsSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), app_id="<id>", offset=0, limit=10, page=0)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `security`                                                                          | [models.GetAppSandboxConfigsSecurity](../../models/getappsandboxconfigssecurity.md) | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `app_id`                                                                            | *str*                                                                               | :heavy_check_mark:                                                                  | app ID                                                                              |
| `offset`                                                                            | *Optional[int]*                                                                     | :heavy_minus_sign:                                                                  | offset of jobs to return                                                            |
| `limit`                                                                             | *Optional[int]*                                                                     | :heavy_minus_sign:                                                                  | limit of jobs to return                                                             |
| `page`                                                                              | *Optional[int]*                                                                     | :heavy_minus_sign:                                                                  | page number of results to return                                                    |
| `x_nuon_pagination_enabled`                                                         | *Optional[bool]*                                                                    | :heavy_minus_sign:                                                                  | Enable pagination                                                                   |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[List[models.AppAppSandboxConfig]](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_app_sandbox_latest_config

get latest app sandbox config

### Example Usage

<!-- UsageSnippet language="python" operationID="GetAppSandboxLatestConfig" method="get" path="/v1/apps/{app_id}/sandbox-latest-config" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.apps.get_app_sandbox_latest_config(security=models.GetAppSandboxLatestConfigSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), app_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `security`                                                                                    | [models.GetAppSandboxLatestConfigSecurity](../../models/getappsandboxlatestconfigsecurity.md) | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `app_id`                                                                                      | *str*                                                                                         | :heavy_check_mark:                                                                            | app ID                                                                                        |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |

### Response

**[models.AppAppSandboxConfig](../../models/appappsandboxconfig.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## create_app_secret

Create an app secret that can be used to configure components. To reference an app secret, use `.nuon.secrets.<secret_name>`.

**NOTE** secrets can only be written, or deleted, not read.


### Example Usage

<!-- UsageSnippet language="python" operationID="CreateAppSecret" method="post" path="/v1/apps/{app_id}/secret" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.apps.create_app_secret(security=models.CreateAppSecretSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), app_id="<id>", name="<value>", value="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `security`                                                                | [models.CreateAppSecretSecurity](../../models/createappsecretsecurity.md) | :heavy_check_mark:                                                        | N/A                                                                       |
| `app_id`                                                                  | *str*                                                                     | :heavy_check_mark:                                                        | app ID                                                                    |
| `name`                                                                    | *str*                                                                     | :heavy_check_mark:                                                        | N/A                                                                       |
| `value`                                                                   | *str*                                                                     | :heavy_check_mark:                                                        | N/A                                                                       |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.AppAppSecret](../../models/appappsecret.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## delete_app_secret

Delete an app secret.


### Example Usage

<!-- UsageSnippet language="python" operationID="DeleteAppSecret" method="delete" path="/v1/apps/{app_id}/secret/{secret_id}" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.apps.delete_app_secret(security=models.DeleteAppSecretSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), app_id="<id>", secret_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `security`                                                                | [models.DeleteAppSecretSecurity](../../models/deleteappsecretsecurity.md) | :heavy_check_mark:                                                        | N/A                                                                       |
| `app_id`                                                                  | *str*                                                                     | :heavy_check_mark:                                                        | app ID                                                                    |
| `secret_id`                                                               | *str*                                                                     | :heavy_check_mark:                                                        | secret ID                                                                 |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[bool](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_app_secrets

List all secrets for an app.

**NOTE** this does not return any sensitive values, as secrets are write only.


### Example Usage

<!-- UsageSnippet language="python" operationID="GetAppSecrets" method="get" path="/v1/apps/{app_id}/secrets" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.apps.get_app_secrets(security=models.GetAppSecretsSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), app_id="<id>", offset=0, limit=10, page=0)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `security`                                                            | [models.GetAppSecretsSecurity](../../models/getappsecretssecurity.md) | :heavy_check_mark:                                                    | N/A                                                                   |
| `app_id`                                                              | *str*                                                                 | :heavy_check_mark:                                                    | app ID                                                                |
| `offset`                                                              | *Optional[int]*                                                       | :heavy_minus_sign:                                                    | offset of jobs to return                                              |
| `limit`                                                               | *Optional[int]*                                                       | :heavy_minus_sign:                                                    | limit of jobs to return                                               |
| `page`                                                                | *Optional[int]*                                                       | :heavy_minus_sign:                                                    | page number of results to return                                      |
| `x_nuon_pagination_enabled`                                           | *Optional[bool]*                                                      | :heavy_minus_sign:                                                    | Enable pagination                                                     |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[List[models.AppAppSecret]](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## create_app_secrets_config

Create an app secrets config.


### Example Usage

<!-- UsageSnippet language="python" operationID="CreateAppSecretsConfig" method="post" path="/v1/apps/{app_id}/secrets-configs" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.apps.create_app_secrets_config(security=models.CreateAppSecretsConfigSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), app_id="<id>", app_config_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `security`                                                                              | [models.CreateAppSecretsConfigSecurity](../../models/createappsecretsconfigsecurity.md) | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `app_id`                                                                                | *str*                                                                                   | :heavy_check_mark:                                                                      | app ID                                                                                  |
| `app_config_id`                                                                         | *str*                                                                                   | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `secrets`                                                                               | List[[models.ServiceAppSecretConfig](../../models/serviceappsecretconfig.md)]           | :heavy_minus_sign:                                                                      | N/A                                                                                     |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[models.AppAppSecretsConfig](../../models/appappsecretsconfig.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_app_secrets_config

Return an app secrets config by id.


### Example Usage

<!-- UsageSnippet language="python" operationID="GetAppSecretsConfig" method="get" path="/v1/apps/{app_id}/secrets-configs/{app_secrets_config_id}" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.apps.get_app_secrets_config(security=models.GetAppSecretsConfigSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), app_id="<id>", app_secrets_config_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `security`                                                                        | [models.GetAppSecretsConfigSecurity](../../models/getappsecretsconfigsecurity.md) | :heavy_check_mark:                                                                | N/A                                                                               |
| `app_id`                                                                          | *str*                                                                             | :heavy_check_mark:                                                                | app ID                                                                            |
| `app_secrets_config_id`                                                           | *str*                                                                             | :heavy_check_mark:                                                                | app secrets config ID                                                             |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.AppAppSecretsConfig](../../models/appappsecretsconfig.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## create_app_stack_config

Create a cloudformation stack config


### Example Usage

<!-- UsageSnippet language="python" operationID="CreateAppStackConfig" method="post" path="/v1/apps/{app_id}/stack-configs" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.apps.create_app_stack_config(security=models.CreateAppStackConfigSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), app_id="<id>", app_config_id="<id>", description="abaft handy sidetrack between culminate though gasp hearten", name="<value>", type_=models.AppStackType.AWS_CLOUDFORMATION)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `security`                                                                          | [models.CreateAppStackConfigSecurity](../../models/createappstackconfigsecurity.md) | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `app_id`                                                                            | *str*                                                                               | :heavy_check_mark:                                                                  | app ID                                                                              |
| `app_config_id`                                                                     | *str*                                                                               | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `description`                                                                       | *str*                                                                               | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `name`                                                                              | *str*                                                                               | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `type`                                                                              | [models.AppStackType](../../models/appstacktype.md)                                 | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `runner_nested_template_url`                                                        | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `vpc_nested_template_url`                                                           | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.AppAppStackConfig](../../models/appappstackconfig.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_app_stack_config

Return a cloudformation stack config


### Example Usage

<!-- UsageSnippet language="python" operationID="GetAppStackConfig" method="get" path="/v1/apps/{app_id}/stack-configs/{config_id}" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.apps.get_app_stack_config(security=models.GetAppStackConfigSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), app_id="<id>", config_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `security`                                                                    | [models.GetAppStackConfigSecurity](../../models/getappstackconfigsecurity.md) | :heavy_check_mark:                                                            | N/A                                                                           |
| `app_id`                                                                      | *str*                                                                         | :heavy_check_mark:                                                            | app ID                                                                        |
| `config_id`                                                                   | *str*                                                                         | :heavy_check_mark:                                                            | app stack config ID                                                           |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[models.AppAppStackConfig](../../models/appappstackconfig.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_app_config_template

Create an application template which provides a fully rendered config that can be modified and used to kickstart any application.


### Example Usage

<!-- UsageSnippet language="python" operationID="GetAppConfigTemplate" method="get" path="/v1/apps/{app_id}/template-config" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.apps.get_app_config_template(security=models.GetAppConfigTemplateSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), app_id="<id>", type_=models.Type.AWS_EKS)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `security`                                                                          | [models.GetAppConfigTemplateSecurity](../../models/getappconfigtemplatesecurity.md) | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `app_id`                                                                            | *str*                                                                               | :heavy_check_mark:                                                                  | app ID                                                                              |
| `type`                                                                              | [models.Type](../../models/type.md)                                                 | :heavy_check_mark:                                                                  | app template type                                                                   |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.ServiceAppConfigTemplate](../../models/serviceappconfigtemplate.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |