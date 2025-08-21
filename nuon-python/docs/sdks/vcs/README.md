# Vcs
(*vcs*)

## Overview

vcs

### Available Operations

* [create_vcs_connection_callback](#create_vcs_connection_callback) - public connection to create a vcs connection via a callback
* [get_org_vcs_connections](#get_org_vcs_connections) - get vcs connection for an org
* [create_vcs_connection](#create_vcs_connection) - create a vcs connection for Github
* [get_vcs_connection](#get_vcs_connection) - returns a vcs connection for an org

## create_vcs_connection_callback

public connection to create a vcs connection via a callback

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateVCSConnectionCallback" method="post" path="/v1/vcs/connection-callback" -->
```python
from nuon import Nuon
import os


with Nuon(
    api_key=os.getenv("NUON_API_KEY", ""),
) as n_client:

    res = n_client.vcs.create_vcs_connection_callback(github_install_id="<id>", org_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `github_install_id`                                                 | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `org_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AppVCSConnection](../../models/appvcsconnection.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_org_vcs_connections

get vcs connection for an org

### Example Usage

<!-- UsageSnippet language="python" operationID="GetOrgVCSConnections" method="get" path="/v1/vcs/connections" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.vcs.get_org_vcs_connections(security=models.GetOrgVCSConnectionsSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), offset=0, limit=10, page=0)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `security`                                                                          | [models.GetOrgVCSConnectionsSecurity](../../models/getorgvcsconnectionssecurity.md) | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `offset`                                                                            | *Optional[int]*                                                                     | :heavy_minus_sign:                                                                  | offset of results to return                                                         |
| `limit`                                                                             | *Optional[int]*                                                                     | :heavy_minus_sign:                                                                  | limit of results to return                                                          |
| `page`                                                                              | *Optional[int]*                                                                     | :heavy_minus_sign:                                                                  | page number of results to return                                                    |
| `x_nuon_pagination_enabled`                                                         | *Optional[bool]*                                                                    | :heavy_minus_sign:                                                                  | Enable pagination                                                                   |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[List[models.AppVCSConnection]](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## create_vcs_connection

create a vcs connection for Github

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateVCSConnection" method="post" path="/v1/vcs/connections" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.vcs.create_vcs_connection(security=models.CreateVCSConnectionSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), github_install_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `security`                                                                        | [models.CreateVCSConnectionSecurity](../../models/createvcsconnectionsecurity.md) | :heavy_check_mark:                                                                | N/A                                                                               |
| `github_install_id`                                                               | *str*                                                                             | :heavy_check_mark:                                                                | N/A                                                                               |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.AppVCSConnection](../../models/appvcsconnection.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_vcs_connection

returns a vcs connection for an org

### Example Usage

<!-- UsageSnippet language="python" operationID="GetVCSConnection" method="get" path="/v1/vcs/connections/{connection_id}" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.vcs.get_vcs_connection(security=models.GetVCSConnectionSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), connection_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `security`                                                                  | [models.GetVCSConnectionSecurity](../../models/getvcsconnectionsecurity.md) | :heavy_check_mark:                                                          | N/A                                                                         |
| `connection_id`                                                             | *str*                                                                       | :heavy_check_mark:                                                          | connection ID                                                               |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.AppVCSConnection](../../models/appvcsconnection.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |