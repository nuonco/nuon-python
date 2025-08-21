# Installers
(*installers*)

## Overview

installers

### Available Operations

* [render_installer](#render_installer) - render an installer
* [get_installers](#get_installers) - get installers for current org
* [create_installer](#create_installer) - create an installer
* [delete_installer](#delete_installer) - delete an installer
* [get_installer](#get_installer) - get an installer
* [update_installer](#update_installer) - update an installer

## render_installer

render an installer

### Example Usage

<!-- UsageSnippet language="python" operationID="RenderInstaller" method="get" path="/v1/installer/{installer_id}/render" -->
```python
from nuon import Nuon
import os


with Nuon(
    api_key=os.getenv("NUON_API_KEY", ""),
) as n_client:

    res = n_client.installers.render_installer(installer_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `installer_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | installer ID                                                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ServiceRenderedInstaller](../../models/servicerenderedinstaller.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_installers

Return all installers for the current org.


### Example Usage

<!-- UsageSnippet language="python" operationID="GetInstallers" method="get" path="/v1/installers" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installers.get_installers(security=models.GetInstallersSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), offset=0, limit=10, page=0)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `security`                                                            | [models.GetInstallersSecurity](../../models/getinstallerssecurity.md) | :heavy_check_mark:                                                    | N/A                                                                   |
| `offset`                                                              | *Optional[int]*                                                       | :heavy_minus_sign:                                                    | offset of results to return                                           |
| `limit`                                                               | *Optional[int]*                                                       | :heavy_minus_sign:                                                    | limit of results to return                                            |
| `page`                                                                | *Optional[int]*                                                       | :heavy_minus_sign:                                                    | page number of results to return                                      |
| `x_nuon_pagination_enabled`                                           | *Optional[bool]*                                                      | :heavy_minus_sign:                                                    | Enable pagination                                                     |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[List[models.AppInstaller]](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## create_installer

create an installer

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateInstaller" method="post" path="/v1/installers" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installers.create_installer(security=models.CreateInstallerSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), app_ids=[
        "<value 1>",
        "<value 2>",
    ], name="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                       | Type                                                                                                            | Required                                                                                                        | Description                                                                                                     |
| --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                      | [models.CreateInstallerSecurity](../../models/createinstallersecurity.md)                                       | :heavy_check_mark:                                                                                              | N/A                                                                                                             |
| `app_ids`                                                                                                       | List[*str*]                                                                                                     | :heavy_check_mark:                                                                                              | N/A                                                                                                             |
| `name`                                                                                                          | *str*                                                                                                           | :heavy_check_mark:                                                                                              | N/A                                                                                                             |
| `metadata`                                                                                                      | [Optional[models.ServiceCreateInstallerRequestMetadata]](../../models/servicecreateinstallerrequestmetadata.md) | :heavy_minus_sign:                                                                                              | N/A                                                                                                             |
| `retries`                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                | :heavy_minus_sign:                                                                                              | Configuration to override the default retry behavior of the client.                                             |

### Response

**[models.AppInstaller](../../models/appinstaller.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## delete_installer

delete an installer

### Example Usage

<!-- UsageSnippet language="python" operationID="DeleteInstaller" method="delete" path="/v1/installers/{installer_id}" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installers.delete_installer(security=models.DeleteInstallerSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), installer_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `security`                                                                | [models.DeleteInstallerSecurity](../../models/deleteinstallersecurity.md) | :heavy_check_mark:                                                        | N/A                                                                       |
| `installer_id`                                                            | *str*                                                                     | :heavy_check_mark:                                                        | installer ID                                                              |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[bool](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_installer

get an installer

### Example Usage

<!-- UsageSnippet language="python" operationID="GetInstaller" method="get" path="/v1/installers/{installer_id}" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installers.get_installer(security=models.GetInstallerSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), installer_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `security`                                                          | [models.GetInstallerSecurity](../../models/getinstallersecurity.md) | :heavy_check_mark:                                                  | N/A                                                                 |
| `installer_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | installer ID                                                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AppInstaller](../../models/appinstaller.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## update_installer

update an installer

### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateInstaller" method="patch" path="/v1/installers/{installer_id}" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.installers.update_installer(security=models.UpdateInstallerSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), installer_id="<id>", app_ids=[
        "<value 1>",
    ], name="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                       | Type                                                                                                            | Required                                                                                                        | Description                                                                                                     |
| --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                      | [models.UpdateInstallerSecurity](../../models/updateinstallersecurity.md)                                       | :heavy_check_mark:                                                                                              | N/A                                                                                                             |
| `installer_id`                                                                                                  | *str*                                                                                                           | :heavy_check_mark:                                                                                              | installer ID                                                                                                    |
| `app_ids`                                                                                                       | List[*str*]                                                                                                     | :heavy_check_mark:                                                                                              | N/A                                                                                                             |
| `name`                                                                                                          | *str*                                                                                                           | :heavy_check_mark:                                                                                              | N/A                                                                                                             |
| `metadata`                                                                                                      | [Optional[models.ServiceUpdateInstallerRequestMetadata]](../../models/serviceupdateinstallerrequestmetadata.md) | :heavy_minus_sign:                                                                                              | N/A                                                                                                             |
| `retries`                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                | :heavy_minus_sign:                                                                                              | Configuration to override the default retry behavior of the client.                                             |

### Response

**[models.AppInstaller](../../models/appinstaller.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |