# General
(*general*)

## Overview

general

### Available Operations

* [get_cli_config](#get_cli_config) - Get config for cli
* [get_cloud_platform_regions](#get_cloud_platform_regions) - Get regions for a cloud platform
* [get_config_schema](#get_config_schema) - Get jsonschema for config file
* [get_current_user](#get_current_user) - Get current user
* [create_waitlist](#create_waitlist) - Allow user to be added to an org waitlist.

## get_cli_config

Get config for cli

### Example Usage

<!-- UsageSnippet language="python" operationID="GetCLIConfig" method="get" path="/v1/general/cli-config" -->
```python
from nuon import Nuon
import os


with Nuon(
    api_key=os.getenv("NUON_API_KEY", ""),
) as n_client:

    res = n_client.general.get_cli_config()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ServiceCLIConfig](../../models/servicecliconfig.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_cloud_platform_regions

Return region metadata for the Nuon supported cloud platforms.


### Example Usage

<!-- UsageSnippet language="python" operationID="GetCloudPlatformRegions" method="get" path="/v1/general/cloud-platform/{cloud_platform}/regions" -->
```python
from nuon import Nuon
import os


with Nuon(
    api_key=os.getenv("NUON_API_KEY", ""),
) as n_client:

    res = n_client.general.get_cloud_platform_regions(cloud_platform="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `cloud_platform`                                                    | *str*                                                               | :heavy_check_mark:                                                  | cloud platform                                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.AppCloudPlatformRegion]](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_config_schema

Return jsonschemas for Nuon configs. These can be used in frontmatter in most editors that have a TOML LSP (such as
[Taplo](https://taplo.tamasfe.dev/) configured.

```toml
#:schema https://api.nuon.co/v1/general/config-schema?source=inputs

description = "description"
```

You can pass in a valid source argument to render within a specific config file:

- input
- input-group
- installer
- sandbox
- runner
- docker_build
- container_image
- helm
- terraform
- job


### Example Usage

<!-- UsageSnippet language="python" operationID="GetConfigSchema" method="get" path="/v1/general/config-schema" -->
```python
from nuon import Nuon
import os


with Nuon(
    api_key=os.getenv("NUON_API_KEY", ""),
) as n_client:

    res = n_client.general.get_config_schema()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `type`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | return a schema for a source file                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetConfigSchemaResponse](../../models/getconfigschemaresponse.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_current_user

Get current user

### Example Usage

<!-- UsageSnippet language="python" operationID="GetCurrentUser" method="get" path="/v1/general/current-user" -->
```python
from nuon import Nuon
import os


with Nuon(
    api_key=os.getenv("NUON_API_KEY", ""),
) as n_client:

    res = n_client.general.get_current_user()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AppAccount](../../models/appaccount.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## create_waitlist

Allow user to be added to an org waitlist.

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateWaitlist" method="post" path="/v1/general/waitlist" -->
```python
from nuon import Nuon
import os


with Nuon(
    api_key=os.getenv("NUON_API_KEY", ""),
) as n_client:

    res = n_client.general.create_waitlist(org_name="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `org_name`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AppWaitlist](../../models/appwaitlist.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.NuonDefaultError | 4XX, 5XX                | \*/\*                   |