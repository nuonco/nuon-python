# nuon.OrgsApi

All URIs are relative to *https://api.nuon.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user**](OrgsApi.md#add_user) | **POST** /v1/orgs/current/user | Add a user to the current org
[**create_org**](OrgsApi.md#create_org) | **POST** /v1/orgs | create a new org
[**create_org_invite**](OrgsApi.md#create_org_invite) | **POST** /v1/orgs/current/invites | Invite a user to the current org
[**delete_org**](OrgsApi.md#delete_org) | **DELETE** /v1/orgs/current | Delete an org
[**get_org**](OrgsApi.md#get_org) | **GET** /v1/orgs/current | Get an org
[**get_org_health_checks**](OrgsApi.md#get_org_health_checks) | **GET** /v1/orgs/current/health-checks | Get an org&#39;s health checks
[**get_org_invites**](OrgsApi.md#get_org_invites) | **GET** /v1/orgs/current/invites | Return org invites
[**get_org_runner_group**](OrgsApi.md#get_org_runner_group) | **GET** /v1/orgs/current/runner-group | Get an org&#39;s runner group
[**get_orgs**](OrgsApi.md#get_orgs) | **GET** /v1/orgs | Return current user&#39;s orgs
[**update_org**](OrgsApi.md#update_org) | **PATCH** /v1/orgs/current | Update current org


# **add_user**
> AppAccount add_user(service_create_org_user_request)

Add a user to the current org

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_account import AppAccount
from nuon.models.service_create_org_user_request import ServiceCreateOrgUserRequest
from nuon.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.nuon.co
# See configuration.py for a list of all supported configuration parameters.
configuration = nuon.Configuration(
    host = "https://api.nuon.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKey
configuration.api_key['APIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKey'] = 'Bearer'

# Configure API key authorization: OrgID
configuration.api_key['OrgID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['OrgID'] = 'Bearer'

# Enter a context with an instance of the API client
with nuon.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nuon.OrgsApi(api_client)
    service_create_org_user_request = nuon.ServiceCreateOrgUserRequest() # ServiceCreateOrgUserRequest | Input

    try:
        # Add a user to the current org
        api_response = api_instance.add_user(service_create_org_user_request)
        print("The response of OrgsApi->add_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->add_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_create_org_user_request** | [**ServiceCreateOrgUserRequest**](ServiceCreateOrgUserRequest.md)| Input | 

### Return type

[**AppAccount**](AppAccount.md)

### Authorization

[APIKey](../README.md#APIKey), [OrgID](../README.md#OrgID)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_org**
> AppOrg create_org(service_create_org_request)

create a new org

### Example

* Api Key Authentication (APIKey):

```python
import time
import os
import nuon
from nuon.models.app_org import AppOrg
from nuon.models.service_create_org_request import ServiceCreateOrgRequest
from nuon.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.nuon.co
# See configuration.py for a list of all supported configuration parameters.
configuration = nuon.Configuration(
    host = "https://api.nuon.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKey
configuration.api_key['APIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKey'] = 'Bearer'

# Enter a context with an instance of the API client
with nuon.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nuon.OrgsApi(api_client)
    service_create_org_request = nuon.ServiceCreateOrgRequest() # ServiceCreateOrgRequest | Input

    try:
        # create a new org
        api_response = api_instance.create_org(service_create_org_request)
        print("The response of OrgsApi->create_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->create_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_create_org_request** | [**ServiceCreateOrgRequest**](ServiceCreateOrgRequest.md)| Input | 

### Return type

[**AppOrg**](AppOrg.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_org_invite**
> AppOrgInvite create_org_invite(service_create_org_invite_request)

Invite a user to the current org

Invite a user (by email) to an org.  This user will receive an email, and when they next log into the application will be added to the org. 

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_org_invite import AppOrgInvite
from nuon.models.service_create_org_invite_request import ServiceCreateOrgInviteRequest
from nuon.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.nuon.co
# See configuration.py for a list of all supported configuration parameters.
configuration = nuon.Configuration(
    host = "https://api.nuon.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKey
configuration.api_key['APIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKey'] = 'Bearer'

# Configure API key authorization: OrgID
configuration.api_key['OrgID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['OrgID'] = 'Bearer'

# Enter a context with an instance of the API client
with nuon.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nuon.OrgsApi(api_client)
    service_create_org_invite_request = nuon.ServiceCreateOrgInviteRequest() # ServiceCreateOrgInviteRequest | Input

    try:
        # Invite a user to the current org
        api_response = api_instance.create_org_invite(service_create_org_invite_request)
        print("The response of OrgsApi->create_org_invite:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->create_org_invite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_create_org_invite_request** | [**ServiceCreateOrgInviteRequest**](ServiceCreateOrgInviteRequest.md)| Input | 

### Return type

[**AppOrgInvite**](AppOrgInvite.md)

### Authorization

[APIKey](../README.md#APIKey), [OrgID](../README.md#OrgID)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_org**
> bool delete_org()

Delete an org

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.nuon.co
# See configuration.py for a list of all supported configuration parameters.
configuration = nuon.Configuration(
    host = "https://api.nuon.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKey
configuration.api_key['APIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKey'] = 'Bearer'

# Configure API key authorization: OrgID
configuration.api_key['OrgID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['OrgID'] = 'Bearer'

# Enter a context with an instance of the API client
with nuon.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nuon.OrgsApi(api_client)

    try:
        # Delete an org
        api_response = api_instance.delete_org()
        print("The response of OrgsApi->delete_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->delete_org: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**bool**

### Authorization

[APIKey](../README.md#APIKey), [OrgID](../README.md#OrgID)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_org**
> AppOrg get_org()

Get an org

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_org import AppOrg
from nuon.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.nuon.co
# See configuration.py for a list of all supported configuration parameters.
configuration = nuon.Configuration(
    host = "https://api.nuon.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKey
configuration.api_key['APIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKey'] = 'Bearer'

# Configure API key authorization: OrgID
configuration.api_key['OrgID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['OrgID'] = 'Bearer'

# Enter a context with an instance of the API client
with nuon.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nuon.OrgsApi(api_client)

    try:
        # Get an org
        api_response = api_instance.get_org()
        print("The response of OrgsApi->get_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->get_org: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AppOrg**](AppOrg.md)

### Authorization

[APIKey](../README.md#APIKey), [OrgID](../README.md#OrgID)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_org_health_checks**
> List[AppOrgHealthCheck] get_org_health_checks(limit=limit)

Get an org's health checks

Fetch the most recent health checks for an org. Health checks are automatically performed once every 60 seconds. 

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_org_health_check import AppOrgHealthCheck
from nuon.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.nuon.co
# See configuration.py for a list of all supported configuration parameters.
configuration = nuon.Configuration(
    host = "https://api.nuon.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKey
configuration.api_key['APIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKey'] = 'Bearer'

# Configure API key authorization: OrgID
configuration.api_key['OrgID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['OrgID'] = 'Bearer'

# Enter a context with an instance of the API client
with nuon.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nuon.OrgsApi(api_client)
    limit = 60 # int | limit of health checks to return (optional) (default to 60)

    try:
        # Get an org's health checks
        api_response = api_instance.get_org_health_checks(limit=limit)
        print("The response of OrgsApi->get_org_health_checks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->get_org_health_checks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| limit of health checks to return | [optional] [default to 60]

### Return type

[**List[AppOrgHealthCheck]**](AppOrgHealthCheck.md)

### Authorization

[APIKey](../README.md#APIKey), [OrgID](../README.md#OrgID)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_org_invites**
> List[AppOrgInvite] get_org_invites(limit=limit)

Return org invites

Returns a list of all invites to the org. 

### Example

* Api Key Authentication (APIKey):

```python
import time
import os
import nuon
from nuon.models.app_org_invite import AppOrgInvite
from nuon.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.nuon.co
# See configuration.py for a list of all supported configuration parameters.
configuration = nuon.Configuration(
    host = "https://api.nuon.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKey
configuration.api_key['APIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKey'] = 'Bearer'

# Enter a context with an instance of the API client
with nuon.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nuon.OrgsApi(api_client)
    limit = 60 # int | limit of health checks to return (optional) (default to 60)

    try:
        # Return org invites
        api_response = api_instance.get_org_invites(limit=limit)
        print("The response of OrgsApi->get_org_invites:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->get_org_invites: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| limit of health checks to return | [optional] [default to 60]

### Return type

[**List[AppOrgInvite]**](AppOrgInvite.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_org_runner_group**
> AppRunnerGroup get_org_runner_group()

Get an org's runner group

Get the current org's runner group, which includes the runners and their settings. 

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_runner_group import AppRunnerGroup
from nuon.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.nuon.co
# See configuration.py for a list of all supported configuration parameters.
configuration = nuon.Configuration(
    host = "https://api.nuon.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKey
configuration.api_key['APIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKey'] = 'Bearer'

# Configure API key authorization: OrgID
configuration.api_key['OrgID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['OrgID'] = 'Bearer'

# Enter a context with an instance of the API client
with nuon.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nuon.OrgsApi(api_client)

    try:
        # Get an org's runner group
        api_response = api_instance.get_org_runner_group()
        print("The response of OrgsApi->get_org_runner_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->get_org_runner_group: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AppRunnerGroup**](AppRunnerGroup.md)

### Authorization

[APIKey](../README.md#APIKey), [OrgID](../README.md#OrgID)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_orgs**
> List[AppOrg] get_orgs()

Return current user's orgs

### Example

* Api Key Authentication (APIKey):

```python
import time
import os
import nuon
from nuon.models.app_org import AppOrg
from nuon.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.nuon.co
# See configuration.py for a list of all supported configuration parameters.
configuration = nuon.Configuration(
    host = "https://api.nuon.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKey
configuration.api_key['APIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKey'] = 'Bearer'

# Enter a context with an instance of the API client
with nuon.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nuon.OrgsApi(api_client)

    try:
        # Return current user's orgs
        api_response = api_instance.get_orgs()
        print("The response of OrgsApi->get_orgs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->get_orgs: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[AppOrg]**](AppOrg.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_org**
> AppOrg update_org(service_update_org_request)

Update current org

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_org import AppOrg
from nuon.models.service_update_org_request import ServiceUpdateOrgRequest
from nuon.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.nuon.co
# See configuration.py for a list of all supported configuration parameters.
configuration = nuon.Configuration(
    host = "https://api.nuon.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKey
configuration.api_key['APIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKey'] = 'Bearer'

# Configure API key authorization: OrgID
configuration.api_key['OrgID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['OrgID'] = 'Bearer'

# Enter a context with an instance of the API client
with nuon.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nuon.OrgsApi(api_client)
    service_update_org_request = nuon.ServiceUpdateOrgRequest() # ServiceUpdateOrgRequest | Input

    try:
        # Update current org
        api_response = api_instance.update_org(service_update_org_request)
        print("The response of OrgsApi->update_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->update_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_update_org_request** | [**ServiceUpdateOrgRequest**](ServiceUpdateOrgRequest.md)| Input | 

### Return type

[**AppOrg**](AppOrg.md)

### Authorization

[APIKey](../README.md#APIKey), [OrgID](../README.md#OrgID)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

