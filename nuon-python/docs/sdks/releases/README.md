# Releases
(*releases*)

## Overview

releases

### Available Operations

* [get_app_releases](#get_app_releases) - get all releases for an app
* [get_component_releases](#get_component_releases) - get all releases for a component
* [create_component_release](#create_component_release) - create a release
* [get_release](#get_release) - get a release
* [get_release_steps](#get_release_steps) - get a release

## get_app_releases

get all releases for an app

### Example Usage

<!-- UsageSnippet language="python" operationID="GetAppReleases" method="get" path="/v1/apps/{app_id}/releases" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.releases.get_app_releases(security=models.GetAppReleasesSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), app_id="<id>", offset=0, limit=10, page=0)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `security`                                                              | [models.GetAppReleasesSecurity](../../models/getappreleasessecurity.md) | :heavy_check_mark:                                                      | N/A                                                                     |
| `app_id`                                                                | *str*                                                                   | :heavy_check_mark:                                                      | app ID                                                                  |
| `offset`                                                                | *Optional[int]*                                                         | :heavy_minus_sign:                                                      | offset of results to return                                             |
| `limit`                                                                 | *Optional[int]*                                                         | :heavy_minus_sign:                                                      | limit of results to return                                              |
| `page`                                                                  | *Optional[int]*                                                         | :heavy_minus_sign:                                                      | page number of results to return                                        |
| `x_nuon_pagination_enabled`                                             | *Optional[bool]*                                                        | :heavy_minus_sign:                                                      | Enable pagination                                                       |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[List[models.AppComponentRelease]](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_component_releases

get all releases for a component

### Example Usage

<!-- UsageSnippet language="python" operationID="GetComponentReleases" method="get" path="/v1/components/{component_id}/releases" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.releases.get_component_releases(security=models.GetComponentReleasesSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), component_id="<id>", offset=0, limit=10, page=0)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `security`                                                                          | [models.GetComponentReleasesSecurity](../../models/getcomponentreleasessecurity.md) | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `component_id`                                                                      | *str*                                                                               | :heavy_check_mark:                                                                  | component ID                                                                        |
| `offset`                                                                            | *Optional[int]*                                                                     | :heavy_minus_sign:                                                                  | offset of results to return                                                         |
| `limit`                                                                             | *Optional[int]*                                                                     | :heavy_minus_sign:                                                                  | limit of results to return                                                          |
| `page`                                                                              | *Optional[int]*                                                                     | :heavy_minus_sign:                                                                  | page number of results to return                                                    |
| `x_nuon_pagination_enabled`                                                         | *Optional[bool]*                                                                    | :heavy_minus_sign:                                                                  | Enable pagination                                                                   |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[List[models.AppComponentRelease]](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## create_component_release

create a release

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateComponentRelease" method="post" path="/v1/components/{component_id}/releases" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.releases.create_component_release(security=models.CreateComponentReleaseSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), component_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `security`                                                                              | [models.CreateComponentReleaseSecurity](../../models/createcomponentreleasesecurity.md) | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `component_id`                                                                          | *str*                                                                                   | :heavy_check_mark:                                                                      | component ID                                                                            |
| `auto_build`                                                                            | *Optional[bool]*                                                                        | :heavy_minus_sign:                                                                      | N/A                                                                                     |
| `build_id`                                                                              | *Optional[str]*                                                                         | :heavy_minus_sign:                                                                      | N/A                                                                                     |
| `install_ids`                                                                           | List[*str*]                                                                             | :heavy_minus_sign:                                                                      | N/A                                                                                     |
| `strategy`                                                                              | [Optional[models.Strategy]](../../models/strategy.md)                                   | :heavy_minus_sign:                                                                      | N/A                                                                                     |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[models.AppComponentRelease](../../models/appcomponentrelease.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_release

get a release

### Example Usage

<!-- UsageSnippet language="python" operationID="GetRelease" method="get" path="/v1/releases/{release_id}" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.releases.get_release(security=models.GetReleaseSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), release_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `security`                                                          | [models.GetReleaseSecurity](../../models/getreleasesecurity.md)     | :heavy_check_mark:                                                  | N/A                                                                 |
| `release_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | release ID                                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AppComponentRelease](../../models/appcomponentrelease.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_release_steps

get a release

### Example Usage

<!-- UsageSnippet language="python" operationID="GetReleaseSteps" method="get" path="/v1/releases/{release_id}/steps" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.releases.get_release_steps(security=models.GetReleaseStepsSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), release_id="<id>", offset=0, limit=10, page=0)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `security`                                                                | [models.GetReleaseStepsSecurity](../../models/getreleasestepssecurity.md) | :heavy_check_mark:                                                        | N/A                                                                       |
| `release_id`                                                              | *str*                                                                     | :heavy_check_mark:                                                        | release ID                                                                |
| `offset`                                                                  | *Optional[int]*                                                           | :heavy_minus_sign:                                                        | offset of results to return                                               |
| `limit`                                                                   | *Optional[int]*                                                           | :heavy_minus_sign:                                                        | limit of results to return                                                |
| `page`                                                                    | *Optional[int]*                                                           | :heavy_minus_sign:                                                        | page number of results to return                                          |
| `x_nuon_pagination_enabled`                                               | *Optional[bool]*                                                          | :heavy_minus_sign:                                                        | Enable pagination                                                         |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[List[models.AppComponentReleaseStep]](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |