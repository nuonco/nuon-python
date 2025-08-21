# Components
(*components*)

## Overview

components

### Available Operations

* [get_app_component](#get_app_component) - get a components for a specific app
* [get_app_components](#get_app_components) - get all components for an app
* [create_component](#create_component) - create a component
* [get_component_builds](#get_component_builds) - get builds for components
* [get_org_components](#get_org_components) - get all components for an org
* [get_build](#get_build) - get a build
* [delete_component](#delete_component) - delete a component
* [get_component](#get_component) - get a component
* [update_component](#update_component) - update a component
* [create_component_build](#create_component_build) - create component build
* [get_component_latest_build](#get_component_latest_build) - get latest build for a component
* [get_component_build](#get_component_build) - get a build for a component
* [get_component_configs](#get_component_configs) - get all configs for a component
* [create_docker_build_component_config](#create_docker_build_component_config) - create a docker build component config
* [create_external_image_component_config](#create_external_image_component_config) - create an external image component config
* [create_helm_component_config](#create_helm_component_config) - create a helm component config
* [create_job_component_config](#create_job_component_config) - create a job component config
* [create_kubernetes_manifest_component_config](#create_kubernetes_manifest_component_config) - create a kubernetes manifest component config
* [get_component_latest_config](#get_component_latest_config) - get latest config for a component
* [create_terraform_module_component_config](#create_terraform_module_component_config) - create a terraform component config
* [get_component_config](#get_component_config) - get all configs for a component
* [get_component_dependencies](#get_component_dependencies) - get a component's dependencies
* [get_component_dependents](#get_component_dependents) - get a component's children

## get_app_component

Return an app component by id or name.


### Example Usage

<!-- UsageSnippet language="python" operationID="GetAppComponent" method="get" path="/v1/apps/{app_id}/component/{component_name_or_id}" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.components.get_app_component(security=models.GetAppComponentSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), app_id="<id>", component_name_or_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `security`                                                                | [models.GetAppComponentSecurity](../../models/getappcomponentsecurity.md) | :heavy_check_mark:                                                        | N/A                                                                       |
| `app_id`                                                                  | *str*                                                                     | :heavy_check_mark:                                                        | app ID                                                                    |
| `component_name_or_id`                                                    | *str*                                                                     | :heavy_check_mark:                                                        | name or ID                                                                |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.AppComponent](../../models/appcomponent.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_app_components

get all components for an app

### Example Usage

<!-- UsageSnippet language="python" operationID="GetAppComponents" method="get" path="/v1/apps/{app_id}/components" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.components.get_app_components(security=models.GetAppComponentsSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), app_id="<id>", offset=0, limit=10, page=0)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `security`                                                                                | [models.GetAppComponentsSecurity](../../models/getappcomponentssecurity.md)               | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `app_id`                                                                                  | *str*                                                                                     | :heavy_check_mark:                                                                        | app ID                                                                                    |
| `q`                                                                                       | *Optional[str]*                                                                           | :heavy_minus_sign:                                                                        | search query to filter components by name                                                 |
| `types`                                                                                   | *Optional[str]*                                                                           | :heavy_minus_sign:                                                                        | comma-separated list of component types to filter by (e.g., terraform_module, helm_chart) |
| `offset`                                                                                  | *Optional[int]*                                                                           | :heavy_minus_sign:                                                                        | offset of results to return                                                               |
| `limit`                                                                                   | *Optional[int]*                                                                           | :heavy_minus_sign:                                                                        | limit of results to return                                                                |
| `page`                                                                                    | *Optional[int]*                                                                           | :heavy_minus_sign:                                                                        | page number of results to return                                                          |
| `x_nuon_pagination_enabled`                                                               | *Optional[bool]*                                                                          | :heavy_minus_sign:                                                                        | Enable pagination                                                                         |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |

### Response

**[List[models.AppComponent]](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## create_component

create a component

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateComponent" method="post" path="/v1/apps/{app_id}/components" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.components.create_component(security=models.CreateComponentSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), app_id="<id>", name="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `security`                                                                | [models.CreateComponentSecurity](../../models/createcomponentsecurity.md) | :heavy_check_mark:                                                        | N/A                                                                       |
| `app_id`                                                                  | *str*                                                                     | :heavy_check_mark:                                                        | app ID                                                                    |
| `name`                                                                    | *str*                                                                     | :heavy_check_mark:                                                        | N/A                                                                       |
| `dependencies`                                                            | List[*str*]                                                               | :heavy_minus_sign:                                                        | N/A                                                                       |
| `var_name`                                                                | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | N/A                                                                       |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.AppComponent](../../models/appcomponent.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_component_builds

get builds for components

### Example Usage

<!-- UsageSnippet language="python" operationID="GetComponentBuilds" method="get" path="/v1/builds" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.components.get_component_builds(security=models.GetComponentBuildsSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), offset=0, limit=10, page=0)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `security`                                                                      | [models.GetComponentBuildsSecurity](../../models/getcomponentbuildssecurity.md) | :heavy_check_mark:                                                              | N/A                                                                             |
| `component_id`                                                                  | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | component id to filter by                                                       |
| `app_id`                                                                        | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | app id to filter by                                                             |
| `offset`                                                                        | *Optional[int]*                                                                 | :heavy_minus_sign:                                                              | offset of results to return                                                     |
| `limit`                                                                         | *Optional[int]*                                                                 | :heavy_minus_sign:                                                              | limit of results to return                                                      |
| `page`                                                                          | *Optional[int]*                                                                 | :heavy_minus_sign:                                                              | page number of results to return                                                |
| `x_nuon_pagination_enabled`                                                     | *Optional[bool]*                                                                | :heavy_minus_sign:                                                              | Enable pagination                                                               |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[List[models.AppComponentBuild]](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_org_components

get all components for an org

### Example Usage

<!-- UsageSnippet language="python" operationID="GetOrgComponents" method="get" path="/v1/components" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.components.get_org_components(security=models.GetOrgComponentsSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), offset=0, limit=10, page=0)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `security`                                                                  | [models.GetOrgComponentsSecurity](../../models/getorgcomponentssecurity.md) | :heavy_check_mark:                                                          | N/A                                                                         |
| `offset`                                                                    | *Optional[int]*                                                             | :heavy_minus_sign:                                                          | offset of results to return                                                 |
| `limit`                                                                     | *Optional[int]*                                                             | :heavy_minus_sign:                                                          | limit of results to return                                                  |
| `page`                                                                      | *Optional[int]*                                                             | :heavy_minus_sign:                                                          | page number of results to return                                            |
| `x_nuon_pagination_enabled`                                                 | *Optional[bool]*                                                            | :heavy_minus_sign:                                                          | Enable pagination                                                           |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[List[models.AppComponent]](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_build

Returns builds for one or all components in an app.


### Example Usage

<!-- UsageSnippet language="python" operationID="GetBuild" method="get" path="/v1/components/builds/{build_id}" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.components.get_build(security=models.GetBuildSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), build_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `security`                                                          | [models.GetBuildSecurity](../../models/getbuildsecurity.md)         | :heavy_check_mark:                                                  | N/A                                                                 |
| `build_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | build ID                                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AppComponentBuild](../../models/appcomponentbuild.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## delete_component

delete a component

### Example Usage

<!-- UsageSnippet language="python" operationID="DeleteComponent" method="delete" path="/v1/components/{component_id}" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.components.delete_component(security=models.DeleteComponentSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), component_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `security`                                                                | [models.DeleteComponentSecurity](../../models/deletecomponentsecurity.md) | :heavy_check_mark:                                                        | N/A                                                                       |
| `component_id`                                                            | *str*                                                                     | :heavy_check_mark:                                                        | component ID                                                              |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[bool](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_component

get a component

### Example Usage

<!-- UsageSnippet language="python" operationID="GetComponent" method="get" path="/v1/components/{component_id}" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.components.get_component(security=models.GetComponentSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), component_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `security`                                                          | [models.GetComponentSecurity](../../models/getcomponentsecurity.md) | :heavy_check_mark:                                                  | N/A                                                                 |
| `component_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | component ID                                                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AppComponent](../../models/appcomponent.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## update_component

update a component

### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateComponent" method="patch" path="/v1/components/{component_id}" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.components.update_component(security=models.UpdateComponentSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), component_id="<id>", name="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `security`                                                                | [models.UpdateComponentSecurity](../../models/updatecomponentsecurity.md) | :heavy_check_mark:                                                        | N/A                                                                       |
| `component_id`                                                            | *str*                                                                     | :heavy_check_mark:                                                        | component ID                                                              |
| `name`                                                                    | *str*                                                                     | :heavy_check_mark:                                                        | N/A                                                                       |
| `dependencies`                                                            | List[*str*]                                                               | :heavy_minus_sign:                                                        | N/A                                                                       |
| `var_name`                                                                | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | N/A                                                                       |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.AppComponent](../../models/appcomponent.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## create_component_build

create component build

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateComponentBuild" method="post" path="/v1/components/{component_id}/builds" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.components.create_component_build(security=models.CreateComponentBuildSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), component_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `security`                                                                          | [models.CreateComponentBuildSecurity](../../models/createcomponentbuildsecurity.md) | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `component_id`                                                                      | *str*                                                                               | :heavy_check_mark:                                                                  | component ID                                                                        |
| `git_ref`                                                                           | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `use_latest`                                                                        | *Optional[bool]*                                                                    | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.AppComponentBuild](../../models/appcomponentbuild.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_component_latest_build

get latest build for a component

### Example Usage

<!-- UsageSnippet language="python" operationID="GetComponentLatestBuild" method="get" path="/v1/components/{component_id}/builds/latest" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.components.get_component_latest_build(security=models.GetComponentLatestBuildSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), component_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `security`                                                                                | [models.GetComponentLatestBuildSecurity](../../models/getcomponentlatestbuildsecurity.md) | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `component_id`                                                                            | *str*                                                                                     | :heavy_check_mark:                                                                        | component ID                                                                              |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |

### Response

**[models.AppComponentBuild](../../models/appcomponentbuild.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_component_build

Returns builds for one or all components in an app.


### Example Usage

<!-- UsageSnippet language="python" operationID="GetComponentBuild" method="get" path="/v1/components/{component_id}/builds/{build_id}" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.components.get_component_build(security=models.GetComponentBuildSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), component_id="<id>", build_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `security`                                                                    | [models.GetComponentBuildSecurity](../../models/getcomponentbuildsecurity.md) | :heavy_check_mark:                                                            | N/A                                                                           |
| `component_id`                                                                | *str*                                                                         | :heavy_check_mark:                                                            | component ID                                                                  |
| `build_id`                                                                    | *str*                                                                         | :heavy_check_mark:                                                            | build ID                                                                      |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[models.AppComponentBuild](../../models/appcomponentbuild.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_component_configs

get all configs for a component

### Example Usage

<!-- UsageSnippet language="python" operationID="GetComponentConfigs" method="get" path="/v1/components/{component_id}/configs" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.components.get_component_configs(security=models.GetComponentConfigsSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), component_id="<id>", offset=0, limit=10, page=0)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `security`                                                                        | [models.GetComponentConfigsSecurity](../../models/getcomponentconfigssecurity.md) | :heavy_check_mark:                                                                | N/A                                                                               |
| `component_id`                                                                    | *str*                                                                             | :heavy_check_mark:                                                                | component ID                                                                      |
| `offset`                                                                          | *Optional[int]*                                                                   | :heavy_minus_sign:                                                                | offset of results to return                                                       |
| `limit`                                                                           | *Optional[int]*                                                                   | :heavy_minus_sign:                                                                | limit of results to return                                                        |
| `page`                                                                            | *Optional[int]*                                                                   | :heavy_minus_sign:                                                                | page number of results to return                                                  |
| `x_nuon_pagination_enabled`                                                       | *Optional[bool]*                                                                  | :heavy_minus_sign:                                                                | Enable pagination                                                                 |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[List[models.AppComponentConfigConnection]](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## create_docker_build_component_config

create a docker build component config

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateDockerBuildComponentConfig" method="post" path="/v1/components/{component_id}/configs/docker-build" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.components.create_docker_build_component_config(security=models.CreateDockerBuildComponentConfigSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), component_id="<id>", dockerfile="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                         | Type                                                                                                              | Required                                                                                                          | Description                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                        | [models.CreateDockerBuildComponentConfigSecurity](../../models/createdockerbuildcomponentconfigsecurity.md)       | :heavy_check_mark:                                                                                                | N/A                                                                                                               |
| `component_id`                                                                                                    | *str*                                                                                                             | :heavy_check_mark:                                                                                                | component ID                                                                                                      |
| `dockerfile`                                                                                                      | *str*                                                                                                             | :heavy_check_mark:                                                                                                | N/A                                                                                                               |
| `app_config_id`                                                                                                   | *Optional[str]*                                                                                                   | :heavy_minus_sign:                                                                                                | N/A                                                                                                               |
| `build_args`                                                                                                      | List[*str*]                                                                                                       | :heavy_minus_sign:                                                                                                | N/A                                                                                                               |
| `checksum`                                                                                                        | *Optional[str]*                                                                                                   | :heavy_minus_sign:                                                                                                | N/A                                                                                                               |
| `connected_github_vcs_config`                                                                                     | [Optional[models.ServiceConnectedGithubVCSConfigRequest]](../../models/serviceconnectedgithubvcsconfigrequest.md) | :heavy_minus_sign:                                                                                                | N/A                                                                                                               |
| `dependencies`                                                                                                    | List[*str*]                                                                                                       | :heavy_minus_sign:                                                                                                | N/A                                                                                                               |
| `env_vars`                                                                                                        | Dict[str, *str*]                                                                                                  | :heavy_minus_sign:                                                                                                | N/A                                                                                                               |
| `public_git_vcs_config`                                                                                           | [Optional[models.ServicePublicGitVCSConfigRequest]](../../models/servicepublicgitvcsconfigrequest.md)             | :heavy_minus_sign:                                                                                                | N/A                                                                                                               |
| `references`                                                                                                      | List[*str*]                                                                                                       | :heavy_minus_sign:                                                                                                | N/A                                                                                                               |
| `target`                                                                                                          | *Optional[str]*                                                                                                   | :heavy_minus_sign:                                                                                                | N/A                                                                                                               |
| `retries`                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                  | :heavy_minus_sign:                                                                                                | Configuration to override the default retry behavior of the client.                                               |

### Response

**[models.AppDockerBuildComponentConfig](../../models/appdockerbuildcomponentconfig.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## create_external_image_component_config

create an external image component config

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateExternalImageComponentConfig" method="post" path="/v1/components/{component_id}/configs/external-image" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.components.create_external_image_component_config(security=models.CreateExternalImageComponentConfigSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), component_id="<id>", image_url="https://acidic-obligation.com", tag="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                       | Type                                                                                                            | Required                                                                                                        | Description                                                                                                     |
| --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                      | [models.CreateExternalImageComponentConfigSecurity](../../models/createexternalimagecomponentconfigsecurity.md) | :heavy_check_mark:                                                                                              | N/A                                                                                                             |
| `component_id`                                                                                                  | *str*                                                                                                           | :heavy_check_mark:                                                                                              | component ID                                                                                                    |
| `image_url`                                                                                                     | *str*                                                                                                           | :heavy_check_mark:                                                                                              | N/A                                                                                                             |
| `tag`                                                                                                           | *str*                                                                                                           | :heavy_check_mark:                                                                                              | N/A                                                                                                             |
| `app_config_id`                                                                                                 | *Optional[str]*                                                                                                 | :heavy_minus_sign:                                                                                              | N/A                                                                                                             |
| `aws_ecr_image_config`                                                                                          | [Optional[models.ServiceAwsECRImageConfigRequest]](../../models/serviceawsecrimageconfigrequest.md)             | :heavy_minus_sign:                                                                                              | N/A                                                                                                             |
| `checksum`                                                                                                      | *Optional[str]*                                                                                                 | :heavy_minus_sign:                                                                                              | N/A                                                                                                             |
| `dependencies`                                                                                                  | List[*str*]                                                                                                     | :heavy_minus_sign:                                                                                              | N/A                                                                                                             |
| `references`                                                                                                    | List[*str*]                                                                                                     | :heavy_minus_sign:                                                                                              | N/A                                                                                                             |
| `retries`                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                | :heavy_minus_sign:                                                                                              | Configuration to override the default retry behavior of the client.                                             |

### Response

**[models.AppExternalImageComponentConfig](../../models/appexternalimagecomponentconfig.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## create_helm_component_config

Create a helm component config.


### Example Usage

<!-- UsageSnippet language="python" operationID="CreateHelmComponentConfig" method="post" path="/v1/components/{component_id}/configs/helm" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.components.create_helm_component_config(security=models.CreateHelmComponentConfigSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), component_id="<id>", chart_name="<value>", values={
        "key": "<value>",
        "key1": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                         | Type                                                                                                              | Required                                                                                                          | Description                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                        | [models.CreateHelmComponentConfigSecurity](../../models/createhelmcomponentconfigsecurity.md)                     | :heavy_check_mark:                                                                                                | N/A                                                                                                               |
| `component_id`                                                                                                    | *str*                                                                                                             | :heavy_check_mark:                                                                                                | component ID                                                                                                      |
| `chart_name`                                                                                                      | *str*                                                                                                             | :heavy_check_mark:                                                                                                | N/A                                                                                                               |
| `values`                                                                                                          | Dict[str, *str*]                                                                                                  | :heavy_check_mark:                                                                                                | N/A                                                                                                               |
| `app_config_id`                                                                                                   | *Optional[str]*                                                                                                   | :heavy_minus_sign:                                                                                                | N/A                                                                                                               |
| `checksum`                                                                                                        | *Optional[str]*                                                                                                   | :heavy_minus_sign:                                                                                                | N/A                                                                                                               |
| `connected_github_vcs_config`                                                                                     | [Optional[models.ServiceConnectedGithubVCSConfigRequest]](../../models/serviceconnectedgithubvcsconfigrequest.md) | :heavy_minus_sign:                                                                                                | N/A                                                                                                               |
| `dependencies`                                                                                                    | List[*str*]                                                                                                       | :heavy_minus_sign:                                                                                                | N/A                                                                                                               |
| `namespace`                                                                                                       | *Optional[str]*                                                                                                   | :heavy_minus_sign:                                                                                                | N/A                                                                                                               |
| `public_git_vcs_config`                                                                                           | [Optional[models.ServicePublicGitVCSConfigRequest]](../../models/servicepublicgitvcsconfigrequest.md)             | :heavy_minus_sign:                                                                                                | N/A                                                                                                               |
| `references`                                                                                                      | List[*str*]                                                                                                       | :heavy_minus_sign:                                                                                                | N/A                                                                                                               |
| `storage_driver`                                                                                                  | *Optional[str]*                                                                                                   | :heavy_minus_sign:                                                                                                | N/A                                                                                                               |
| `take_ownership`                                                                                                  | *Optional[bool]*                                                                                                  | :heavy_minus_sign:                                                                                                | N/A                                                                                                               |
| `values_files`                                                                                                    | List[*str*]                                                                                                       | :heavy_minus_sign:                                                                                                | N/A                                                                                                               |
| `retries`                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                  | :heavy_minus_sign:                                                                                                | Configuration to override the default retry behavior of the client.                                               |

### Response

**[models.AppHelmComponentConfig](../../models/apphelmcomponentconfig.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## create_job_component_config

create a job component config

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateJobComponentConfig" method="post" path="/v1/components/{component_id}/configs/job" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.components.create_job_component_config(security=models.CreateJobComponentConfigSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), component_id="<id>", image_url="https://puzzled-valuable.org/", tag="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `security`                                                                                  | [models.CreateJobComponentConfigSecurity](../../models/createjobcomponentconfigsecurity.md) | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `component_id`                                                                              | *str*                                                                                       | :heavy_check_mark:                                                                          | component ID                                                                                |
| `image_url`                                                                                 | *str*                                                                                       | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `tag`                                                                                       | *str*                                                                                       | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `app_config_id`                                                                             | *Optional[str]*                                                                             | :heavy_minus_sign:                                                                          | N/A                                                                                         |
| `args`                                                                                      | List[*str*]                                                                                 | :heavy_minus_sign:                                                                          | N/A                                                                                         |
| `checksum`                                                                                  | *Optional[str]*                                                                             | :heavy_minus_sign:                                                                          | N/A                                                                                         |
| `cmd`                                                                                       | List[*str*]                                                                                 | :heavy_minus_sign:                                                                          | N/A                                                                                         |
| `env_vars`                                                                                  | Dict[str, *str*]                                                                            | :heavy_minus_sign:                                                                          | N/A                                                                                         |
| `references`                                                                                | List[*str*]                                                                                 | :heavy_minus_sign:                                                                          | N/A                                                                                         |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |

### Response

**[models.AppJobComponentConfig](../../models/appjobcomponentconfig.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## create_kubernetes_manifest_component_config

create a kubernetes manifest component config

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateKubernetesManifestComponentConfig" method="post" path="/v1/components/{component_id}/configs/kubernetes-manifest" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.components.create_kubernetes_manifest_component_config(security=models.CreateKubernetesManifestComponentConfigSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), component_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                 | Type                                                                                                                      | Required                                                                                                                  | Description                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                | [models.CreateKubernetesManifestComponentConfigSecurity](../../models/createkubernetesmanifestcomponentconfigsecurity.md) | :heavy_check_mark:                                                                                                        | N/A                                                                                                                       |
| `component_id`                                                                                                            | *str*                                                                                                                     | :heavy_check_mark:                                                                                                        | component ID                                                                                                              |
| `app_config_id`                                                                                                           | *Optional[str]*                                                                                                           | :heavy_minus_sign:                                                                                                        | N/A                                                                                                                       |
| `checksum`                                                                                                                | *Optional[str]*                                                                                                           | :heavy_minus_sign:                                                                                                        | N/A                                                                                                                       |
| `dependencies`                                                                                                            | List[*str*]                                                                                                               | :heavy_minus_sign:                                                                                                        | N/A                                                                                                                       |
| `manifest`                                                                                                                | *Optional[str]*                                                                                                           | :heavy_minus_sign:                                                                                                        | N/A                                                                                                                       |
| `namespace`                                                                                                               | *Optional[str]*                                                                                                           | :heavy_minus_sign:                                                                                                        | N/A                                                                                                                       |
| `references`                                                                                                              | List[*str*]                                                                                                               | :heavy_minus_sign:                                                                                                        | N/A                                                                                                                       |
| `retries`                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                          | :heavy_minus_sign:                                                                                                        | Configuration to override the default retry behavior of the client.                                                       |

### Response

**[models.AppKubernetesManifestComponentConfig](../../models/appkubernetesmanifestcomponentconfig.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_component_latest_config

get latest config for a component

### Example Usage

<!-- UsageSnippet language="python" operationID="GetComponentLatestConfig" method="get" path="/v1/components/{component_id}/configs/latest" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.components.get_component_latest_config(security=models.GetComponentLatestConfigSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), component_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `security`                                                                                  | [models.GetComponentLatestConfigSecurity](../../models/getcomponentlatestconfigsecurity.md) | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `component_id`                                                                              | *str*                                                                                       | :heavy_check_mark:                                                                          | component ID                                                                                |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |

### Response

**[models.AppComponentConfigConnection](../../models/appcomponentconfigconnection.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## create_terraform_module_component_config

Create a terraform component config.


### Example Usage

<!-- UsageSnippet language="python" operationID="CreateTerraformModuleComponentConfig" method="post" path="/v1/components/{component_id}/configs/terraform-module" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.components.create_terraform_module_component_config(security=models.CreateTerraformModuleComponentConfigSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), component_id="<id>", env_vars={
        "key": "<value>",
        "key1": "<value>",
    }, variables={

    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                           | Type                                                                                                                | Required                                                                                                            | Description                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                          | [models.CreateTerraformModuleComponentConfigSecurity](../../models/createterraformmodulecomponentconfigsecurity.md) | :heavy_check_mark:                                                                                                  | N/A                                                                                                                 |
| `component_id`                                                                                                      | *str*                                                                                                               | :heavy_check_mark:                                                                                                  | component ID                                                                                                        |
| `env_vars`                                                                                                          | Dict[str, *str*]                                                                                                    | :heavy_check_mark:                                                                                                  | N/A                                                                                                                 |
| `variables`                                                                                                         | Dict[str, *str*]                                                                                                    | :heavy_check_mark:                                                                                                  | N/A                                                                                                                 |
| `app_config_id`                                                                                                     | *Optional[str]*                                                                                                     | :heavy_minus_sign:                                                                                                  | N/A                                                                                                                 |
| `checksum`                                                                                                          | *Optional[str]*                                                                                                     | :heavy_minus_sign:                                                                                                  | N/A                                                                                                                 |
| `connected_github_vcs_config`                                                                                       | [Optional[models.ServiceConnectedGithubVCSConfigRequest]](../../models/serviceconnectedgithubvcsconfigrequest.md)   | :heavy_minus_sign:                                                                                                  | N/A                                                                                                                 |
| `dependencies`                                                                                                      | List[*str*]                                                                                                         | :heavy_minus_sign:                                                                                                  | N/A                                                                                                                 |
| `public_git_vcs_config`                                                                                             | [Optional[models.ServicePublicGitVCSConfigRequest]](../../models/servicepublicgitvcsconfigrequest.md)               | :heavy_minus_sign:                                                                                                  | N/A                                                                                                                 |
| `references`                                                                                                        | List[*str*]                                                                                                         | :heavy_minus_sign:                                                                                                  | N/A                                                                                                                 |
| `variables_files`                                                                                                   | List[*str*]                                                                                                         | :heavy_minus_sign:                                                                                                  | N/A                                                                                                                 |
| `version`                                                                                                           | *Optional[str]*                                                                                                     | :heavy_minus_sign:                                                                                                  | N/A                                                                                                                 |
| `retries`                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                    | :heavy_minus_sign:                                                                                                  | Configuration to override the default retry behavior of the client.                                                 |

### Response

**[models.AppTerraformModuleComponentConfig](../../models/appterraformmodulecomponentconfig.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_component_config

get all configs for a component

### Example Usage

<!-- UsageSnippet language="python" operationID="GetComponentConfig" method="get" path="/v1/components/{component_id}/configs/{config_id}" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.components.get_component_config(security=models.GetComponentConfigSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), component_id="<id>", config_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `security`                                                                      | [models.GetComponentConfigSecurity](../../models/getcomponentconfigsecurity.md) | :heavy_check_mark:                                                              | N/A                                                                             |
| `component_id`                                                                  | *str*                                                                           | :heavy_check_mark:                                                              | component ID                                                                    |
| `config_id`                                                                     | *str*                                                                           | :heavy_check_mark:                                                              | config ID                                                                       |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[models.AppComponentConfigConnection](../../models/appcomponentconfigconnection.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_component_dependencies

get a component's dependencies

### Example Usage

<!-- UsageSnippet language="python" operationID="GetComponentDependencies" method="get" path="/v1/components/{component_id}/dependencies" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.components.get_component_dependencies(security=models.GetComponentDependenciesSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), component_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `security`                                                                                  | [models.GetComponentDependenciesSecurity](../../models/getcomponentdependenciessecurity.md) | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `component_id`                                                                              | *str*                                                                                       | :heavy_check_mark:                                                                          | component ID                                                                                |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |

### Response

**[List[models.AppComponent]](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_component_dependents

get a component's children

### Example Usage

<!-- UsageSnippet language="python" operationID="GetComponentDependents" method="get" path="/v1/components/{component_id}/dependents" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.components.get_component_dependents(security=models.GetComponentDependentsSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), component_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `security`                                                                              | [models.GetComponentDependentsSecurity](../../models/getcomponentdependentssecurity.md) | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `component_id`                                                                          | *str*                                                                                   | :heavy_check_mark:                                                                      | component ID                                                                            |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[models.ServiceComponentChildren](../../models/servicecomponentchildren.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |