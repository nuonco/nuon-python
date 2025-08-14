# nuon.RunnersRunnerApi

All URIs are relative to *http://localhost:8081*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_terraform_workspace**](RunnersRunnerApi.md#create_terraform_workspace) | **POST** /v1/terraform-workspace | create terraform workspace
[**delete_terraform_workspace**](RunnersRunnerApi.md#delete_terraform_workspace) | **DELETE** /v1/terraform-workspace/{workspace_id} | delete terraform workspace
[**get_runner**](RunnersRunnerApi.md#get_runner) | **GET** /v1/runners/{runner_id} | get a runner
[**get_runner_job**](RunnersRunnerApi.md#get_runner_job) | **GET** /v1/runner-jobs/{runner_job_id} | get runner job
[**get_runner_job_executions**](RunnersRunnerApi.md#get_runner_job_executions) | **GET** /v1/runner-jobs/{runner_job_id}/executions | get runner job executions
[**get_runner_job_plan**](RunnersRunnerApi.md#get_runner_job_plan) | **GET** /v1/runner-jobs/{runner_job_id}/plan | get runner job plan
[**get_terraform_current_state_data**](RunnersRunnerApi.md#get_terraform_current_state_data) | **GET** /v1/terraform-backend | get current terraform
[**get_terraform_states**](RunnersRunnerApi.md#get_terraform_states) | **GET** /v1/runners/terraform-workspace/{workspace_id}/states | get terraform states
[**get_terraform_workspace**](RunnersRunnerApi.md#get_terraform_workspace) | **GET** /v1/terraform-workspace/{workspace_id} | get  terraform workspace
[**get_terraform_workspace_state_by_id**](RunnersRunnerApi.md#get_terraform_workspace_state_by_id) | **GET** /v1/runners/terraform-workspace/{workspace_id}/states/{state_id} | get terraform state by ID
[**get_terraform_workspace_state_resources**](RunnersRunnerApi.md#get_terraform_workspace_state_resources) | **GET** /v1/runners/terraform-workspace/{workspace_id}/states/{state_id}/resources | get terraform state resources
[**get_terraform_workspaces**](RunnersRunnerApi.md#get_terraform_workspaces) | **GET** /v1/terraform-workspaces | get  terraform workspaces
[**lock_terraform_workspace**](RunnersRunnerApi.md#lock_terraform_workspace) | **POST** /v1/terraform-workspaces/{workspace_id}/lock | lock terraform state
[**unlock_terraform_workspace**](RunnersRunnerApi.md#unlock_terraform_workspace) | **POST** /v1/terraform-workspaces/{workspace_id}/unlock | unlock terraform workspace
[**update_terraform_state**](RunnersRunnerApi.md#update_terraform_state) | **POST** /v1/terraform-backend | update terraform state


# **create_terraform_workspace**
> AppTerraformWorkspace create_terraform_workspace(service_create_terraform_workspace_request)

create terraform workspace

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_terraform_workspace import AppTerraformWorkspace
from nuon.models.service_create_terraform_workspace_request import ServiceCreateTerraformWorkspaceRequest
from nuon.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = nuon.Configuration(
    host = "http://localhost:8081"
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
    api_instance = nuon.RunnersRunnerApi(api_client)
    service_create_terraform_workspace_request = nuon.ServiceCreateTerraformWorkspaceRequest() # ServiceCreateTerraformWorkspaceRequest | Input

    try:
        # create terraform workspace
        api_response = api_instance.create_terraform_workspace(service_create_terraform_workspace_request)
        print("The response of RunnersRunnerApi->create_terraform_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnersRunnerApi->create_terraform_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_create_terraform_workspace_request** | [**ServiceCreateTerraformWorkspaceRequest**](ServiceCreateTerraformWorkspaceRequest.md)| Input | 

### Return type

[**AppTerraformWorkspace**](AppTerraformWorkspace.md)

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

# **delete_terraform_workspace**
> List[AppTerraformWorkspace] delete_terraform_workspace(workspace_id)

delete terraform workspace

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_terraform_workspace import AppTerraformWorkspace
from nuon.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = nuon.Configuration(
    host = "http://localhost:8081"
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
    api_instance = nuon.RunnersRunnerApi(api_client)
    workspace_id = 'workspace_id_example' # str | workspace ID

    try:
        # delete terraform workspace
        api_response = api_instance.delete_terraform_workspace(workspace_id)
        print("The response of RunnersRunnerApi->delete_terraform_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnersRunnerApi->delete_terraform_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| workspace ID | 

### Return type

[**List[AppTerraformWorkspace]**](AppTerraformWorkspace.md)

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

# **get_runner**
> AppRunner get_runner(runner_id)

get a runner

Return a runner. 

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_runner import AppRunner
from nuon.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = nuon.Configuration(
    host = "http://localhost:8081"
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
    api_instance = nuon.RunnersRunnerApi(api_client)
    runner_id = 'runner_id_example' # str | runner ID

    try:
        # get a runner
        api_response = api_instance.get_runner(runner_id)
        print("The response of RunnersRunnerApi->get_runner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnersRunnerApi->get_runner: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **runner_id** | **str**| runner ID | 

### Return type

[**AppRunner**](AppRunner.md)

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

# **get_runner_job**
> AppRunnerJob get_runner_job(runner_job_id)

get runner job

Return a runner job. 

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_runner_job import AppRunnerJob
from nuon.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = nuon.Configuration(
    host = "http://localhost:8081"
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
    api_instance = nuon.RunnersRunnerApi(api_client)
    runner_job_id = 'runner_job_id_example' # str | runner job ID

    try:
        # get runner job
        api_response = api_instance.get_runner_job(runner_job_id)
        print("The response of RunnersRunnerApi->get_runner_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnersRunnerApi->get_runner_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **runner_job_id** | **str**| runner job ID | 

### Return type

[**AppRunnerJob**](AppRunnerJob.md)

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

# **get_runner_job_executions**
> List[AppRunnerJobExecution] get_runner_job_executions(runner_job_id, offset=offset, limit=limit, page=page, x_nuon_pagination_enabled=x_nuon_pagination_enabled)

get runner job executions

Return executions for a runner job. 

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_runner_job_execution import AppRunnerJobExecution
from nuon.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = nuon.Configuration(
    host = "http://localhost:8081"
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
    api_instance = nuon.RunnersRunnerApi(api_client)
    runner_job_id = 'runner_job_id_example' # str | runner job ID
    offset = 0 # int | offset of results to return (optional) (default to 0)
    limit = 10 # int | limit of results to return (optional) (default to 10)
    page = 0 # int | page number of results to return (optional) (default to 0)
    x_nuon_pagination_enabled = True # bool | Enable pagination (optional)

    try:
        # get runner job executions
        api_response = api_instance.get_runner_job_executions(runner_job_id, offset=offset, limit=limit, page=page, x_nuon_pagination_enabled=x_nuon_pagination_enabled)
        print("The response of RunnersRunnerApi->get_runner_job_executions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnersRunnerApi->get_runner_job_executions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **runner_job_id** | **str**| runner job ID | 
 **offset** | **int**| offset of results to return | [optional] [default to 0]
 **limit** | **int**| limit of results to return | [optional] [default to 10]
 **page** | **int**| page number of results to return | [optional] [default to 0]
 **x_nuon_pagination_enabled** | **bool**| Enable pagination | [optional] 

### Return type

[**List[AppRunnerJobExecution]**](AppRunnerJobExecution.md)

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

# **get_runner_job_plan**
> str get_runner_job_plan(runner_job_id)

get runner job plan

Return a plan for a runner job. 

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = nuon.Configuration(
    host = "http://localhost:8081"
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
    api_instance = nuon.RunnersRunnerApi(api_client)
    runner_job_id = 'runner_job_id_example' # str | runner job ID

    try:
        # get runner job plan
        api_response = api_instance.get_runner_job_plan(runner_job_id)
        print("The response of RunnersRunnerApi->get_runner_job_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnersRunnerApi->get_runner_job_plan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **runner_job_id** | **str**| runner job ID | 

### Return type

**str**

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

# **get_terraform_current_state_data**
> AppTerraformWorkspaceState get_terraform_current_state_data()

get current terraform

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_terraform_workspace_state import AppTerraformWorkspaceState
from nuon.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = nuon.Configuration(
    host = "http://localhost:8081"
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
    api_instance = nuon.RunnersRunnerApi(api_client)

    try:
        # get current terraform
        api_response = api_instance.get_terraform_current_state_data()
        print("The response of RunnersRunnerApi->get_terraform_current_state_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnersRunnerApi->get_terraform_current_state_data: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AppTerraformWorkspaceState**](AppTerraformWorkspaceState.md)

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

# **get_terraform_states**
> List[AppTerraformWorkspaceState] get_terraform_states(workspace_id, offset=offset, limit=limit, page=page, x_nuon_pagination_enabled=x_nuon_pagination_enabled)

get terraform states

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_terraform_workspace_state import AppTerraformWorkspaceState
from nuon.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = nuon.Configuration(
    host = "http://localhost:8081"
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
    api_instance = nuon.RunnersRunnerApi(api_client)
    workspace_id = 'workspace_id_example' # str | workspace ID
    offset = 0 # int | offset of results to return (optional) (default to 0)
    limit = 10 # int | limit of results to return (optional) (default to 10)
    page = 0 # int | page number of results to return (optional) (default to 0)
    x_nuon_pagination_enabled = True # bool | Enable pagination (optional)

    try:
        # get terraform states
        api_response = api_instance.get_terraform_states(workspace_id, offset=offset, limit=limit, page=page, x_nuon_pagination_enabled=x_nuon_pagination_enabled)
        print("The response of RunnersRunnerApi->get_terraform_states:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnersRunnerApi->get_terraform_states: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| workspace ID | 
 **offset** | **int**| offset of results to return | [optional] [default to 0]
 **limit** | **int**| limit of results to return | [optional] [default to 10]
 **page** | **int**| page number of results to return | [optional] [default to 0]
 **x_nuon_pagination_enabled** | **bool**| Enable pagination | [optional] 

### Return type

[**List[AppTerraformWorkspaceState]**](AppTerraformWorkspaceState.md)

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

# **get_terraform_workspace**
> List[AppTerraformWorkspace] get_terraform_workspace(workspace_id)

get  terraform workspace

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_terraform_workspace import AppTerraformWorkspace
from nuon.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = nuon.Configuration(
    host = "http://localhost:8081"
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
    api_instance = nuon.RunnersRunnerApi(api_client)
    workspace_id = 'workspace_id_example' # str | workspace ID

    try:
        # get  terraform workspace
        api_response = api_instance.get_terraform_workspace(workspace_id)
        print("The response of RunnersRunnerApi->get_terraform_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnersRunnerApi->get_terraform_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| workspace ID | 

### Return type

[**List[AppTerraformWorkspace]**](AppTerraformWorkspace.md)

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

# **get_terraform_workspace_state_by_id**
> AppTerraformWorkspaceState get_terraform_workspace_state_by_id(workspace_id, state_id)

get terraform state by ID

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_terraform_workspace_state import AppTerraformWorkspaceState
from nuon.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = nuon.Configuration(
    host = "http://localhost:8081"
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
    api_instance = nuon.RunnersRunnerApi(api_client)
    workspace_id = 'workspace_id_example' # str | workspace ID
    state_id = 'state_id_example' # str | state ID

    try:
        # get terraform state by ID
        api_response = api_instance.get_terraform_workspace_state_by_id(workspace_id, state_id)
        print("The response of RunnersRunnerApi->get_terraform_workspace_state_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnersRunnerApi->get_terraform_workspace_state_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| workspace ID | 
 **state_id** | **str**| state ID | 

### Return type

[**AppTerraformWorkspaceState**](AppTerraformWorkspaceState.md)

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

# **get_terraform_workspace_state_resources**
> List[AppTerraformStateResource] get_terraform_workspace_state_resources(workspace_id, state_id)

get terraform state resources

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_terraform_state_resource import AppTerraformStateResource
from nuon.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = nuon.Configuration(
    host = "http://localhost:8081"
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
    api_instance = nuon.RunnersRunnerApi(api_client)
    workspace_id = 'workspace_id_example' # str | workspace ID
    state_id = 'state_id_example' # str | state ID

    try:
        # get terraform state resources
        api_response = api_instance.get_terraform_workspace_state_resources(workspace_id, state_id)
        print("The response of RunnersRunnerApi->get_terraform_workspace_state_resources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnersRunnerApi->get_terraform_workspace_state_resources: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| workspace ID | 
 **state_id** | **str**| state ID | 

### Return type

[**List[AppTerraformStateResource]**](AppTerraformStateResource.md)

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

# **get_terraform_workspaces**
> List[AppTerraformWorkspace] get_terraform_workspaces()

get  terraform workspaces

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_terraform_workspace import AppTerraformWorkspace
from nuon.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = nuon.Configuration(
    host = "http://localhost:8081"
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
    api_instance = nuon.RunnersRunnerApi(api_client)

    try:
        # get  terraform workspaces
        api_response = api_instance.get_terraform_workspaces()
        print("The response of RunnersRunnerApi->get_terraform_workspaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnersRunnerApi->get_terraform_workspaces: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[AppTerraformWorkspace]**](AppTerraformWorkspace.md)

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

# **lock_terraform_workspace**
> AppTerraformWorkspaceState lock_terraform_workspace(workspace_id, body, job_id=job_id)

lock terraform state

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_terraform_workspace_state import AppTerraformWorkspaceState
from nuon.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = nuon.Configuration(
    host = "http://localhost:8081"
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
    api_instance = nuon.RunnersRunnerApi(api_client)
    workspace_id = 'workspace_id_example' # str | workspace ID
    body = None # object | terraform workspace lock 
    job_id = 'job_id_example' # str | job ID (optional)

    try:
        # lock terraform state
        api_response = api_instance.lock_terraform_workspace(workspace_id, body, job_id=job_id)
        print("The response of RunnersRunnerApi->lock_terraform_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnersRunnerApi->lock_terraform_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| workspace ID | 
 **body** | **object**| terraform workspace lock  | 
 **job_id** | **str**| job ID | [optional] 

### Return type

[**AppTerraformWorkspaceState**](AppTerraformWorkspaceState.md)

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

# **unlock_terraform_workspace**
> AppTerraformWorkspaceState unlock_terraform_workspace(workspace_id, body)

unlock terraform workspace

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_terraform_workspace_state import AppTerraformWorkspaceState
from nuon.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = nuon.Configuration(
    host = "http://localhost:8081"
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
    api_instance = nuon.RunnersRunnerApi(api_client)
    workspace_id = 'workspace_id_example' # str | workspace ID
    body = None # object | terraform workspace unlock 

    try:
        # unlock terraform workspace
        api_response = api_instance.unlock_terraform_workspace(workspace_id, body)
        print("The response of RunnersRunnerApi->unlock_terraform_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnersRunnerApi->unlock_terraform_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| workspace ID | 
 **body** | **object**| terraform workspace unlock  | 

### Return type

[**AppTerraformWorkspaceState**](AppTerraformWorkspaceState.md)

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

# **update_terraform_state**
> AppTerraformWorkspaceState update_terraform_state(body)

update terraform state

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_terraform_workspace_state import AppTerraformWorkspaceState
from nuon.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = nuon.Configuration(
    host = "http://localhost:8081"
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
    api_instance = nuon.RunnersRunnerApi(api_client)
    body = None # object | Terraform state data

    try:
        # update terraform state
        api_response = api_instance.update_terraform_state(body)
        print("The response of RunnersRunnerApi->update_terraform_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnersRunnerApi->update_terraform_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**| Terraform state data | 

### Return type

[**AppTerraformWorkspaceState**](AppTerraformWorkspaceState.md)

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

