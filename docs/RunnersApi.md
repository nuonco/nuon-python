# nuon.RunnersApi

All URIs are relative to *http://localhost:8081*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_runner_job**](RunnersApi.md#cancel_runner_job) | **POST** /v1/runner-jobs/{runner_job_id}/cancel | cancel runner job
[**create_terraform_workspace**](RunnersApi.md#create_terraform_workspace) | **POST** /v1/terraform-workspace | create terraform workspace
[**delete_terraform_workspace**](RunnersApi.md#delete_terraform_workspace) | **DELETE** /v1/terraform-workspace/{workspace_id} | delete terraform workspace
[**force_shut_down_runner**](RunnersApi.md#force_shut_down_runner) | **POST** /v1/runners/{runner_id}/force-shutdown | force shut down a runner
[**get_log_stream**](RunnersApi.md#get_log_stream) | **GET** /v1/log-streams/{log_stream_id} | get a log stream
[**get_runner**](RunnersApi.md#get_runner) | **GET** /v1/runners/{runner_id} | get a runner
[**get_runner_connect_status**](RunnersApi.md#get_runner_connect_status) | **GET** /v1/runners/{runner_id}/connected | get a runner connection satus based on heartbeat
[**get_runner_job**](RunnersApi.md#get_runner_job) | **GET** /v1/runner-jobs/{runner_job_id} | get runner job
[**get_runner_job_executions**](RunnersApi.md#get_runner_job_executions) | **GET** /v1/runner-jobs/{runner_job_id}/executions | get runner job executions
[**get_runner_job_plan**](RunnersApi.md#get_runner_job_plan) | **GET** /v1/runner-jobs/{runner_job_id}/plan | get runner job plan
[**get_runner_jobs**](RunnersApi.md#get_runner_jobs) | **GET** /v1/runners/{runner_id}/jobs | get runner jobs
[**get_runner_latest_heart_beat**](RunnersApi.md#get_runner_latest_heart_beat) | **GET** /v1/runners/{runner_id}/latest-heart-beat | get a runner
[**get_runner_recent_health_checks**](RunnersApi.md#get_runner_recent_health_checks) | **GET** /v1/runners/{runner_id}/recent-health-checks | get recent health checks
[**get_runner_settings**](RunnersApi.md#get_runner_settings) | **GET** /v1/runners/{runner_id}/settings | get runner settings
[**get_terraform_current_state_data**](RunnersApi.md#get_terraform_current_state_data) | **GET** /v1/terraform-backend | get current terraform
[**get_terraform_states**](RunnersApi.md#get_terraform_states) | **GET** /v1/runners/terraform-workspace/{workspace_id}/states | get terraform states
[**get_terraform_workspace**](RunnersApi.md#get_terraform_workspace) | **GET** /v1/terraform-workspace/{workspace_id} | get  terraform workspace
[**get_terraform_workspace_lock**](RunnersApi.md#get_terraform_workspace_lock) | **GET** /v1/terraform-workspaces/{workspace_id}/lock | get terraform workspace lock
[**get_terraform_workspace_state_by_id**](RunnersApi.md#get_terraform_workspace_state_by_id) | **GET** /v1/runners/terraform-workspace/{workspace_id}/states/{state_id} | get terraform state by ID
[**get_terraform_workspace_state_json_resources**](RunnersApi.md#get_terraform_workspace_state_json_resources) | **GET** /v1/runners/terraform-workspace/{workspace_id}/state-json/{state_id}/resources | get terraform state resources. This output is similar to \&quot;terraform state list\&quot;
[**get_terraform_workspace_state_resources**](RunnersApi.md#get_terraform_workspace_state_resources) | **GET** /v1/runners/terraform-workspace/{workspace_id}/states/{state_id}/resources | get terraform state resources
[**get_terraform_workspace_states_json**](RunnersApi.md#get_terraform_workspace_states_json) | **GET** /v1/runners/terraform-workspace/{workspace_id}/state-json | get terraform states json
[**get_terraform_workspace_states_jsonby_id**](RunnersApi.md#get_terraform_workspace_states_jsonby_id) | **GET** /v1/runners/terraform-workspace/{workspace_id}/state-json/{state_id} | get terraform state json by id. This output is same as \&quot;terraform show --json\&quot;
[**get_terraform_workspaces**](RunnersApi.md#get_terraform_workspaces) | **GET** /v1/terraform-workspaces | get  terraform workspaces
[**graceful_shut_down_runner**](RunnersApi.md#graceful_shut_down_runner) | **POST** /v1/runners/{runner_id}/graceful-shutdown | shut down a runner
[**lock_terraform_workspace**](RunnersApi.md#lock_terraform_workspace) | **POST** /v1/terraform-workspaces/{workspace_id}/lock | lock terraform state
[**log_stream_read_logs**](RunnersApi.md#log_stream_read_logs) | **GET** /v1/log-streams/{log_stream_id}/logs | read a log stream&#39;s logs
[**mng_vm_shut_down**](RunnersApi.md#mng_vm_shut_down) | **POST** /v1/runners/{runner_id}/mng/shutdown-vm | shut down an install runner VM
[**shut_down_runner_mng**](RunnersApi.md#shut_down_runner_mng) | **POST** /v1/runners/{runner_id}/mng/shutdown | shut down an install runner management process
[**unlock_terraform_workspace**](RunnersApi.md#unlock_terraform_workspace) | **POST** /v1/terraform-workspaces/{workspace_id}/unlock | unlock terraform workspace
[**update_runner_settings**](RunnersApi.md#update_runner_settings) | **PATCH** /v1/runners/{runner_id}/settings | update a runner job execution
[**update_terraform_state**](RunnersApi.md#update_terraform_state) | **POST** /v1/terraform-backend | update terraform state


# **cancel_runner_job**
> AppRunnerJob cancel_runner_job(runner_job_id, body)

cancel runner job

Cancel a runner job. 

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
    api_instance = nuon.RunnersApi(api_client)
    runner_job_id = 'runner_job_id_example' # str | runner job ID
    body = None # object | Input

    try:
        # cancel runner job
        api_response = api_instance.cancel_runner_job(runner_job_id, body)
        print("The response of RunnersApi->cancel_runner_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnersApi->cancel_runner_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **runner_job_id** | **str**| runner job ID | 
 **body** | **object**| Input | 

### Return type

[**AppRunnerJob**](AppRunnerJob.md)

### Authorization

[APIKey](../README.md#APIKey), [OrgID](../README.md#OrgID)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
    api_instance = nuon.RunnersApi(api_client)
    service_create_terraform_workspace_request = nuon.ServiceCreateTerraformWorkspaceRequest() # ServiceCreateTerraformWorkspaceRequest | Input

    try:
        # create terraform workspace
        api_response = api_instance.create_terraform_workspace(service_create_terraform_workspace_request)
        print("The response of RunnersApi->create_terraform_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnersApi->create_terraform_workspace: %s\n" % e)
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
    api_instance = nuon.RunnersApi(api_client)
    workspace_id = 'workspace_id_example' # str | workspace ID

    try:
        # delete terraform workspace
        api_response = api_instance.delete_terraform_workspace(workspace_id)
        print("The response of RunnersApi->delete_terraform_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnersApi->delete_terraform_workspace: %s\n" % e)
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

# **force_shut_down_runner**
> bool force_shut_down_runner(runner_id, body)

force shut down a runner

Force shutdown a runner.  This will result in jobs being lost/cancelled if they are in-flight. 

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
    api_instance = nuon.RunnersApi(api_client)
    runner_id = 'runner_id_example' # str | runner ID
    body = None # object | Input

    try:
        # force shut down a runner
        api_response = api_instance.force_shut_down_runner(runner_id, body)
        print("The response of RunnersApi->force_shut_down_runner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnersApi->force_shut_down_runner: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **runner_id** | **str**| runner ID | 
 **body** | **object**| Input | 

### Return type

**bool**

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

# **get_log_stream**
> AppLogStream get_log_stream(log_stream_id)

get a log stream

Return a log stream. 

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_log_stream import AppLogStream
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
    api_instance = nuon.RunnersApi(api_client)
    log_stream_id = 'log_stream_id_example' # str | log stream ID

    try:
        # get a log stream
        api_response = api_instance.get_log_stream(log_stream_id)
        print("The response of RunnersApi->get_log_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnersApi->get_log_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **log_stream_id** | **str**| log stream ID | 

### Return type

[**AppLogStream**](AppLogStream.md)

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
    api_instance = nuon.RunnersApi(api_client)
    runner_id = 'runner_id_example' # str | runner ID

    try:
        # get a runner
        api_response = api_instance.get_runner(runner_id)
        print("The response of RunnersApi->get_runner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnersApi->get_runner: %s\n" % e)
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

# **get_runner_connect_status**
> ServiceRunnerConnectionStatus get_runner_connect_status(runner_id)

get a runner connection satus based on heartbeat

# get runner connect status  The connected status is based on runner heartbeat:  if no heart beat found — false if heart beat > 15 seconds ago — false, hb timestamp if the heart beat < 15 seconds ago — true

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.service_runner_connection_status import ServiceRunnerConnectionStatus
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
    api_instance = nuon.RunnersApi(api_client)
    runner_id = 'runner_id_example' # str | runner ID

    try:
        # get a runner connection satus based on heartbeat
        api_response = api_instance.get_runner_connect_status(runner_id)
        print("The response of RunnersApi->get_runner_connect_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnersApi->get_runner_connect_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **runner_id** | **str**| runner ID | 

### Return type

[**ServiceRunnerConnectionStatus**](ServiceRunnerConnectionStatus.md)

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
    api_instance = nuon.RunnersApi(api_client)
    runner_job_id = 'runner_job_id_example' # str | runner job ID

    try:
        # get runner job
        api_response = api_instance.get_runner_job(runner_job_id)
        print("The response of RunnersApi->get_runner_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnersApi->get_runner_job: %s\n" % e)
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
    api_instance = nuon.RunnersApi(api_client)
    runner_job_id = 'runner_job_id_example' # str | runner job ID
    offset = 0 # int | offset of results to return (optional) (default to 0)
    limit = 10 # int | limit of results to return (optional) (default to 10)
    page = 0 # int | page number of results to return (optional) (default to 0)
    x_nuon_pagination_enabled = True # bool | Enable pagination (optional)

    try:
        # get runner job executions
        api_response = api_instance.get_runner_job_executions(runner_job_id, offset=offset, limit=limit, page=page, x_nuon_pagination_enabled=x_nuon_pagination_enabled)
        print("The response of RunnersApi->get_runner_job_executions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnersApi->get_runner_job_executions: %s\n" % e)
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
    api_instance = nuon.RunnersApi(api_client)
    runner_job_id = 'runner_job_id_example' # str | runner job ID

    try:
        # get runner job plan
        api_response = api_instance.get_runner_job_plan(runner_job_id)
        print("The response of RunnersApi->get_runner_job_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnersApi->get_runner_job_plan: %s\n" % e)
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

# **get_runner_jobs**
> List[AppRunnerJob] get_runner_jobs(runner_id, group=group, groups=groups, status=status, statuses=statuses, offset=offset, limit=limit, page=page, x_nuon_pagination_enabled=x_nuon_pagination_enabled)

get runner jobs

Return runner jobs. 

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
    api_instance = nuon.RunnersApi(api_client)
    runner_id = 'runner_id_example' # str | runner ID
    group = 'group_example' # str | job group (optional)
    groups = 'groups_example' # str | job groups (optional)
    status = 'status_example' # str | job status (optional)
    statuses = 'statuses_example' # str | job statuses (optional)
    offset = 0 # int | offset of jobs to return (optional) (default to 0)
    limit = 10 # int | limit of jobs to return (optional) (default to 10)
    page = 0 # int | page number of results to return (optional) (default to 0)
    x_nuon_pagination_enabled = True # bool | Enable pagination (optional)

    try:
        # get runner jobs
        api_response = api_instance.get_runner_jobs(runner_id, group=group, groups=groups, status=status, statuses=statuses, offset=offset, limit=limit, page=page, x_nuon_pagination_enabled=x_nuon_pagination_enabled)
        print("The response of RunnersApi->get_runner_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnersApi->get_runner_jobs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **runner_id** | **str**| runner ID | 
 **group** | **str**| job group | [optional] 
 **groups** | **str**| job groups | [optional] 
 **status** | **str**| job status | [optional] 
 **statuses** | **str**| job statuses | [optional] 
 **offset** | **int**| offset of jobs to return | [optional] [default to 0]
 **limit** | **int**| limit of jobs to return | [optional] [default to 10]
 **page** | **int**| page number of results to return | [optional] [default to 0]
 **x_nuon_pagination_enabled** | **bool**| Enable pagination | [optional] 

### Return type

[**List[AppRunnerJob]**](AppRunnerJob.md)

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

# **get_runner_latest_heart_beat**
> AppRunnerHeartBeat get_runner_latest_heart_beat(runner_id)

get a runner

 

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_runner_heart_beat import AppRunnerHeartBeat
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
    api_instance = nuon.RunnersApi(api_client)
    runner_id = 'runner_id_example' # str | runner ID

    try:
        # get a runner
        api_response = api_instance.get_runner_latest_heart_beat(runner_id)
        print("The response of RunnersApi->get_runner_latest_heart_beat:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnersApi->get_runner_latest_heart_beat: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **runner_id** | **str**| runner ID | 

### Return type

[**AppRunnerHeartBeat**](AppRunnerHeartBeat.md)

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

# **get_runner_recent_health_checks**
> List[AppRunnerHealthCheck] get_runner_recent_health_checks(runner_id, window=window, offset=offset, limit=limit, page=page, x_nuon_pagination_enabled=x_nuon_pagination_enabled)

get recent health checks

 

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_runner_health_check import AppRunnerHealthCheck
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
    api_instance = nuon.RunnersApi(api_client)
    runner_id = 'runner_id_example' # str | runner ID
    window = '1h' # str | window of health checks to return (optional) (default to '1h')
    offset = 0 # int | offset of results to return (optional) (default to 0)
    limit = 10 # int | limit of results to return (optional) (default to 10)
    page = 0 # int | page number of results to return (optional) (default to 0)
    x_nuon_pagination_enabled = True # bool | Enable pagination (optional)

    try:
        # get recent health checks
        api_response = api_instance.get_runner_recent_health_checks(runner_id, window=window, offset=offset, limit=limit, page=page, x_nuon_pagination_enabled=x_nuon_pagination_enabled)
        print("The response of RunnersApi->get_runner_recent_health_checks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnersApi->get_runner_recent_health_checks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **runner_id** | **str**| runner ID | 
 **window** | **str**| window of health checks to return | [optional] [default to &#39;1h&#39;]
 **offset** | **int**| offset of results to return | [optional] [default to 0]
 **limit** | **int**| limit of results to return | [optional] [default to 10]
 **page** | **int**| page number of results to return | [optional] [default to 0]
 **x_nuon_pagination_enabled** | **bool**| Enable pagination | [optional] 

### Return type

[**List[AppRunnerHealthCheck]**](AppRunnerHealthCheck.md)

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

# **get_runner_settings**
> AppRunnerGroupSettings get_runner_settings(runner_id)

get runner settings

Return runner settings for the provided runner. 

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_runner_group_settings import AppRunnerGroupSettings
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
    api_instance = nuon.RunnersApi(api_client)
    runner_id = 'runner_id_example' # str | runner ID

    try:
        # get runner settings
        api_response = api_instance.get_runner_settings(runner_id)
        print("The response of RunnersApi->get_runner_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnersApi->get_runner_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **runner_id** | **str**| runner ID | 

### Return type

[**AppRunnerGroupSettings**](AppRunnerGroupSettings.md)

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
    api_instance = nuon.RunnersApi(api_client)

    try:
        # get current terraform
        api_response = api_instance.get_terraform_current_state_data()
        print("The response of RunnersApi->get_terraform_current_state_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnersApi->get_terraform_current_state_data: %s\n" % e)
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
    api_instance = nuon.RunnersApi(api_client)
    workspace_id = 'workspace_id_example' # str | workspace ID
    offset = 0 # int | offset of results to return (optional) (default to 0)
    limit = 10 # int | limit of results to return (optional) (default to 10)
    page = 0 # int | page number of results to return (optional) (default to 0)
    x_nuon_pagination_enabled = True # bool | Enable pagination (optional)

    try:
        # get terraform states
        api_response = api_instance.get_terraform_states(workspace_id, offset=offset, limit=limit, page=page, x_nuon_pagination_enabled=x_nuon_pagination_enabled)
        print("The response of RunnersApi->get_terraform_states:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnersApi->get_terraform_states: %s\n" % e)
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
    api_instance = nuon.RunnersApi(api_client)
    workspace_id = 'workspace_id_example' # str | workspace ID

    try:
        # get  terraform workspace
        api_response = api_instance.get_terraform_workspace(workspace_id)
        print("The response of RunnersApi->get_terraform_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnersApi->get_terraform_workspace: %s\n" % e)
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

# **get_terraform_workspace_lock**
> AppTerraformWorkspaceLock get_terraform_workspace_lock(workspace_id)

get terraform workspace lock

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_terraform_workspace_lock import AppTerraformWorkspaceLock
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
    api_instance = nuon.RunnersApi(api_client)
    workspace_id = 'workspace_id_example' # str | workspace ID

    try:
        # get terraform workspace lock
        api_response = api_instance.get_terraform_workspace_lock(workspace_id)
        print("The response of RunnersApi->get_terraform_workspace_lock:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnersApi->get_terraform_workspace_lock: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| workspace ID | 

### Return type

[**AppTerraformWorkspaceLock**](AppTerraformWorkspaceLock.md)

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
    api_instance = nuon.RunnersApi(api_client)
    workspace_id = 'workspace_id_example' # str | workspace ID
    state_id = 'state_id_example' # str | state ID

    try:
        # get terraform state by ID
        api_response = api_instance.get_terraform_workspace_state_by_id(workspace_id, state_id)
        print("The response of RunnersApi->get_terraform_workspace_state_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnersApi->get_terraform_workspace_state_by_id: %s\n" % e)
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

# **get_terraform_workspace_state_json_resources**
> object get_terraform_workspace_state_json_resources(workspace_id, state_id)

get terraform state resources. This output is similar to \"terraform state list\"

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
    api_instance = nuon.RunnersApi(api_client)
    workspace_id = 'workspace_id_example' # str | workspace ID
    state_id = 'state_id_example' # str | state ID

    try:
        # get terraform state resources. This output is similar to \"terraform state list\"
        api_response = api_instance.get_terraform_workspace_state_json_resources(workspace_id, state_id)
        print("The response of RunnersApi->get_terraform_workspace_state_json_resources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnersApi->get_terraform_workspace_state_json_resources: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| workspace ID | 
 **state_id** | **str**| state ID | 

### Return type

**object**

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
    api_instance = nuon.RunnersApi(api_client)
    workspace_id = 'workspace_id_example' # str | workspace ID
    state_id = 'state_id_example' # str | state ID

    try:
        # get terraform state resources
        api_response = api_instance.get_terraform_workspace_state_resources(workspace_id, state_id)
        print("The response of RunnersApi->get_terraform_workspace_state_resources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnersApi->get_terraform_workspace_state_resources: %s\n" % e)
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

# **get_terraform_workspace_states_json**
> List[AppTerraformWorkspaceStateJSON] get_terraform_workspace_states_json(workspace_id, offset=offset, limit=limit, page=page, x_nuon_pagination_enabled=x_nuon_pagination_enabled)

get terraform states json

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_terraform_workspace_state_json import AppTerraformWorkspaceStateJSON
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
    api_instance = nuon.RunnersApi(api_client)
    workspace_id = 'workspace_id_example' # str | workspace ID
    offset = 0 # int | offset of results to return (optional) (default to 0)
    limit = 10 # int | limit of results to return (optional) (default to 10)
    page = 0 # int | page number of results to return (optional) (default to 0)
    x_nuon_pagination_enabled = True # bool | Enable pagination (optional)

    try:
        # get terraform states json
        api_response = api_instance.get_terraform_workspace_states_json(workspace_id, offset=offset, limit=limit, page=page, x_nuon_pagination_enabled=x_nuon_pagination_enabled)
        print("The response of RunnersApi->get_terraform_workspace_states_json:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnersApi->get_terraform_workspace_states_json: %s\n" % e)
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

[**List[AppTerraformWorkspaceStateJSON]**](AppTerraformWorkspaceStateJSON.md)

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

# **get_terraform_workspace_states_jsonby_id**
> object get_terraform_workspace_states_jsonby_id(workspace_id, state_id)

get terraform state json by id. This output is same as \"terraform show --json\"

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
    api_instance = nuon.RunnersApi(api_client)
    workspace_id = 'workspace_id_example' # str | workspace ID
    state_id = 'state_id_example' # str | terraform state ID

    try:
        # get terraform state json by id. This output is same as \"terraform show --json\"
        api_response = api_instance.get_terraform_workspace_states_jsonby_id(workspace_id, state_id)
        print("The response of RunnersApi->get_terraform_workspace_states_jsonby_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnersApi->get_terraform_workspace_states_jsonby_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| workspace ID | 
 **state_id** | **str**| terraform state ID | 

### Return type

**object**

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
    api_instance = nuon.RunnersApi(api_client)

    try:
        # get  terraform workspaces
        api_response = api_instance.get_terraform_workspaces()
        print("The response of RunnersApi->get_terraform_workspaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnersApi->get_terraform_workspaces: %s\n" % e)
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

# **graceful_shut_down_runner**
> bool graceful_shut_down_runner(runner_id, body)

shut down a runner

Gracefully shut down a runner.  _NOTE_ when a runner is unhealthy, the runner will not be able to pick up this job, so use force shut down instead. 

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
    api_instance = nuon.RunnersApi(api_client)
    runner_id = 'runner_id_example' # str | runner ID
    body = None # object | Input

    try:
        # shut down a runner
        api_response = api_instance.graceful_shut_down_runner(runner_id, body)
        print("The response of RunnersApi->graceful_shut_down_runner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnersApi->graceful_shut_down_runner: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **runner_id** | **str**| runner ID | 
 **body** | **object**| Input | 

### Return type

**bool**

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
    api_instance = nuon.RunnersApi(api_client)
    workspace_id = 'workspace_id_example' # str | workspace ID
    body = None # object | terraform workspace lock 
    job_id = 'job_id_example' # str | job ID (optional)

    try:
        # lock terraform state
        api_response = api_instance.lock_terraform_workspace(workspace_id, body, job_id=job_id)
        print("The response of RunnersApi->lock_terraform_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnersApi->lock_terraform_workspace: %s\n" % e)
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

# **log_stream_read_logs**
> List[AppOtelLogRecord] log_stream_read_logs(log_stream_id, x_nuon_api_offset)

read a log stream's logs

Read OTEL formatted logs for a log stream. 

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_otel_log_record import AppOtelLogRecord
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
    api_instance = nuon.RunnersApi(api_client)
    log_stream_id = 'log_stream_id_example' # str | log stream ID
    x_nuon_api_offset = 'x_nuon_api_offset_example' # str | log stream offset

    try:
        # read a log stream's logs
        api_response = api_instance.log_stream_read_logs(log_stream_id, x_nuon_api_offset)
        print("The response of RunnersApi->log_stream_read_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnersApi->log_stream_read_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **log_stream_id** | **str**| log stream ID | 
 **x_nuon_api_offset** | **str**| log stream offset | 

### Return type

[**List[AppOtelLogRecord]**](AppOtelLogRecord.md)

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

# **mng_vm_shut_down**
> bool mng_vm_shut_down(runner_id, body)

shut down an install runner VM

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
    api_instance = nuon.RunnersApi(api_client)
    runner_id = 'runner_id_example' # str | runner ID
    body = None # object | Input

    try:
        # shut down an install runner VM
        api_response = api_instance.mng_vm_shut_down(runner_id, body)
        print("The response of RunnersApi->mng_vm_shut_down:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnersApi->mng_vm_shut_down: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **runner_id** | **str**| runner ID | 
 **body** | **object**| Input | 

### Return type

**bool**

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

# **shut_down_runner_mng**
> bool shut_down_runner_mng(runner_id, body)

shut down an install runner management process

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
    api_instance = nuon.RunnersApi(api_client)
    runner_id = 'runner_id_example' # str | runner ID
    body = None # object | Input

    try:
        # shut down an install runner management process
        api_response = api_instance.shut_down_runner_mng(runner_id, body)
        print("The response of RunnersApi->shut_down_runner_mng:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnersApi->shut_down_runner_mng: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **runner_id** | **str**| runner ID | 
 **body** | **object**| Input | 

### Return type

**bool**

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
    api_instance = nuon.RunnersApi(api_client)
    workspace_id = 'workspace_id_example' # str | workspace ID
    body = None # object | terraform workspace unlock 

    try:
        # unlock terraform workspace
        api_response = api_instance.unlock_terraform_workspace(workspace_id, body)
        print("The response of RunnersApi->unlock_terraform_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnersApi->unlock_terraform_workspace: %s\n" % e)
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

# **update_runner_settings**
> AppRunnerJobExecution update_runner_settings(runner_id, service_update_runner_settings_request)

update a runner job execution

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_runner_job_execution import AppRunnerJobExecution
from nuon.models.service_update_runner_settings_request import ServiceUpdateRunnerSettingsRequest
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
    api_instance = nuon.RunnersApi(api_client)
    runner_id = 'runner_id_example' # str | runner ID
    service_update_runner_settings_request = nuon.ServiceUpdateRunnerSettingsRequest() # ServiceUpdateRunnerSettingsRequest | Input

    try:
        # update a runner job execution
        api_response = api_instance.update_runner_settings(runner_id, service_update_runner_settings_request)
        print("The response of RunnersApi->update_runner_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnersApi->update_runner_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **runner_id** | **str**| runner ID | 
 **service_update_runner_settings_request** | [**ServiceUpdateRunnerSettingsRequest**](ServiceUpdateRunnerSettingsRequest.md)| Input | 

### Return type

[**AppRunnerJobExecution**](AppRunnerJobExecution.md)

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
    api_instance = nuon.RunnersApi(api_client)
    body = None # object | Terraform state data

    try:
        # update terraform state
        api_response = api_instance.update_terraform_state(body)
        print("The response of RunnersApi->update_terraform_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnersApi->update_terraform_state: %s\n" % e)
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

