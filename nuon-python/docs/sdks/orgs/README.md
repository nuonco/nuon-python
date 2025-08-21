# Orgs
(*orgs*)

## Overview

orgs

### Available Operations

* [get_orgs](#get_orgs) - Return current user's orgs
* [create_org](#create_org) - create a new org
* [delete_org](#delete_org) - Delete an org
* [get_org](#get_org) - Get an org
* [update_org](#update_org) - Update current org
* [get_org_acounts](#get_org_acounts) - Get user accounts for current org
* [get_org_invites](#get_org_invites) - Return org invites
* [create_org_invite](#create_org_invite) - Invite a user to the current org
* [remove_user](#remove_user) - Remove a user from the current org
* [get_org_runner_group](#get_org_runner_group) - Get an org's runner group
* [add_user](#add_user) - Add a user to the current org

## get_orgs

Return current user's orgs

### Example Usage

<!-- UsageSnippet language="python" operationID="GetOrgs" method="get" path="/v1/orgs" -->
```python
from nuon import Nuon
import os


with Nuon(
    api_key=os.getenv("NUON_API_KEY", ""),
) as n_client:

    res = n_client.orgs.get_orgs(offset=0, limit=10, page=0)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `offset`                                                            | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | offset of results to return                                         |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | limit of results to return                                          |
| `page`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | page number of results to return                                    |
| `x_nuon_pagination_enabled`                                         | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Enable pagination                                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.AppOrg]](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## create_org

create a new org

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateOrg" method="post" path="/v1/orgs" -->
```python
from nuon import Nuon
import os


with Nuon(
    api_key=os.getenv("NUON_API_KEY", ""),
) as n_client:

    res = n_client.orgs.create_org(name="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `name`                                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `use_sandbox_mode`                                                  | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | These fields are used to control the behaviour of the org.          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AppOrg](../../models/apporg.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## delete_org

Delete an org

### Example Usage

<!-- UsageSnippet language="python" operationID="DeleteOrg" method="delete" path="/v1/orgs/current" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.orgs.delete_org(security=models.DeleteOrgSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `security`                                                          | [models.DeleteOrgSecurity](../../deleteorgsecurity.md)              | :heavy_check_mark:                                                  | The security requirements to use for the request.                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[bool](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_org

Get an org

### Example Usage

<!-- UsageSnippet language="python" operationID="GetOrg" method="get" path="/v1/orgs/current" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.orgs.get_org(security=models.GetOrgSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `security`                                                          | [models.GetOrgSecurity](../../getorgsecurity.md)                    | :heavy_check_mark:                                                  | The security requirements to use for the request.                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AppOrg](../../models/apporg.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## update_org

Update current org

### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateOrg" method="patch" path="/v1/orgs/current" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.orgs.update_org(security=models.UpdateOrgSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), name="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `security`                                                          | [models.UpdateOrgSecurity](../../models/updateorgsecurity.md)       | :heavy_check_mark:                                                  | N/A                                                                 |
| `name`                                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AppOrg](../../models/apporg.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_org_acounts

Get user accounts for current org

### Example Usage

<!-- UsageSnippet language="python" operationID="GetOrgAcounts" method="get" path="/v1/orgs/current/accounts" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.orgs.get_org_acounts(security=models.GetOrgAcountsSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), offset=0, limit=10, page=0)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `security`                                                            | [models.GetOrgAcountsSecurity](../../models/getorgacountssecurity.md) | :heavy_check_mark:                                                    | N/A                                                                   |
| `offset`                                                              | *Optional[int]*                                                       | :heavy_minus_sign:                                                    | offset of results to return                                           |
| `limit`                                                               | *Optional[int]*                                                       | :heavy_minus_sign:                                                    | limit of results to return                                            |
| `page`                                                                | *Optional[int]*                                                       | :heavy_minus_sign:                                                    | page number of results to return                                      |
| `x_nuon_pagination_enabled`                                           | *Optional[bool]*                                                      | :heavy_minus_sign:                                                    | Enable pagination                                                     |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.AppAccount](../../models/appaccount.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_org_invites

Returns a list of all invites to the org.


### Example Usage

<!-- UsageSnippet language="python" operationID="GetOrgInvites" method="get" path="/v1/orgs/current/invites" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.orgs.get_org_invites(security=models.GetOrgInvitesSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), offset=0, limit=10, page=0)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `security`                                                            | [models.GetOrgInvitesSecurity](../../models/getorginvitessecurity.md) | :heavy_check_mark:                                                    | N/A                                                                   |
| `offset`                                                              | *Optional[int]*                                                       | :heavy_minus_sign:                                                    | offset of results to return                                           |
| `limit`                                                               | *Optional[int]*                                                       | :heavy_minus_sign:                                                    | limit of results to return                                            |
| `page`                                                                | *Optional[int]*                                                       | :heavy_minus_sign:                                                    | page number of results to return                                      |
| `x_nuon_pagination_enabled`                                           | *Optional[bool]*                                                      | :heavy_minus_sign:                                                    | Enable pagination                                                     |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[List[models.AppOrgInvite]](../../models/.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## create_org_invite

Invite a user (by email) to an org.

This user will receive an email, and when they next log into the application will be added to the org.


### Example Usage

<!-- UsageSnippet language="python" operationID="CreateOrgInvite" method="post" path="/v1/orgs/current/invites" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.orgs.create_org_invite(security=models.CreateOrgInviteSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), email="Demond.Boehm8@hotmail.com")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `security`                                                                | [models.CreateOrgInviteSecurity](../../models/createorginvitesecurity.md) | :heavy_check_mark:                                                        | N/A                                                                       |
| `email`                                                                   | *str*                                                                     | :heavy_check_mark:                                                        | N/A                                                                       |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.AppOrgInvite](../../models/apporginvite.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## remove_user

Remove a user from an org.


### Example Usage

<!-- UsageSnippet language="python" operationID="RemoveUser" method="post" path="/v1/orgs/current/remove-user" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.orgs.remove_user(security=models.RemoveUserSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `security`                                                          | [models.RemoveUserSecurity](../../models/removeusersecurity.md)     | :heavy_check_mark:                                                  | N/A                                                                 |
| `user_id`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AppAccount](../../models/appaccount.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## get_org_runner_group

Get the current org's runner group, which includes the runners and their settings.


### Example Usage

<!-- UsageSnippet language="python" operationID="GetOrgRunnerGroup" method="get" path="/v1/orgs/current/runner-group" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.orgs.get_org_runner_group(security=models.GetOrgRunnerGroupSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `security`                                                             | [models.GetOrgRunnerGroupSecurity](../../getorgrunnergroupsecurity.md) | :heavy_check_mark:                                                     | The security requirements to use for the request.                      |
| `retries`                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)       | :heavy_minus_sign:                                                     | Configuration to override the default retry behavior of the client.    |

### Response

**[models.AppRunnerGroup](../../models/apprunnergroup.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |

## add_user

Add a user to the current org

### Example Usage

<!-- UsageSnippet language="python" operationID="AddUser" method="post" path="/v1/orgs/current/user" -->
```python
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.orgs.add_user(security=models.AddUserSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `security`                                                          | [models.AddUserSecurity](../../models/addusersecurity.md)           | :heavy_check_mark:                                                  | N/A                                                                 |
| `user_id`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AppAccount](../../models/appaccount.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.StderrErrResponseError | 400, 401, 403, 404            | application/json              |
| errors.StderrErrResponseError | 500                           | application/json              |
| errors.NuonDefaultError       | 4XX, 5XX                      | \*/\*                         |