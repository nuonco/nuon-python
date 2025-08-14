# nuon.ActionsApi

All URIs are relative to *http://localhost:8081*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_action_workflow_config**](ActionsApi.md#create_action_workflow_config) | **POST** /v1/action-workflows/{action_workflow_id}/configs | create action workflow config
[**create_app_action_workflow**](ActionsApi.md#create_app_action_workflow) | **POST** /v1/apps/{app_id}/action-workflows | create an app
[**create_install_action_workflow_run**](ActionsApi.md#create_install_action_workflow_run) | **POST** /v1/installs/{install_id}/action-workflows/runs | create an action workflow run for an install
[**delete_action_workflow**](ActionsApi.md#delete_action_workflow) | **DELETE** /v1/action-workflows/{action_workflow_id} | delete an app
[**get_action_workflow**](ActionsApi.md#get_action_workflow) | **GET** /v1/action-workflows/{action_workflow_id} | get an app action workflow
[**get_action_workflow_config**](ActionsApi.md#get_action_workflow_config) | **GET** /v1/action-workflows/configs/{action_workflow_config_id} | get an app action workflow config
[**get_action_workflow_configs**](ActionsApi.md#get_action_workflow_configs) | **GET** /v1/action-workflows/{action_workflow_id}/configs | get action workflow for an app
[**get_action_workflow_latest_config**](ActionsApi.md#get_action_workflow_latest_config) | **GET** /v1/action-workflows/{action_workflow_id}/latest-config | get an app action workflow&#39;s latest config
[**get_action_workflows**](ActionsApi.md#get_action_workflows) | **GET** /v1/apps/{app_id}/action-workflows | get action workflows for an app
[**get_app_action_workflow**](ActionsApi.md#get_app_action_workflow) | **GET** /v1/apps/{app_id}/action-workflows/{action_workflow_id} | get an app action workflow
[**get_install_action_workflow_recent_runs**](ActionsApi.md#get_install_action_workflow_recent_runs) | **GET** /v1/installs/{install_id}/action-workflows/{action_workflow_id}/recent-runs | get recent runs for an action workflow by install id
[**get_install_action_workflow_run**](ActionsApi.md#get_install_action_workflow_run) | **GET** /v1/installs/{install_id}/action-workflows/runs/{run_id} | get action workflow runs by install id and run id
[**get_install_action_workflow_run_step**](ActionsApi.md#get_install_action_workflow_run_step) | **GET** /v1/installs/{install_id}/action-workflows/runs/{workflow_run_id}/steps/{step_id} | get action workflow run step by install id and step id
[**get_install_action_workflow_runs**](ActionsApi.md#get_install_action_workflow_runs) | **GET** /v1/installs/{install_id}/action-workflows/runs | get action workflow runs by install id
[**get_install_action_workflows_latest_runs**](ActionsApi.md#get_install_action_workflows_latest_runs) | **GET** /v1/installs/{install_id}/action-workflows/latest-runs | get latest runs for all action workflows by install id
[**update_app_action_workflow**](ActionsApi.md#update_app_action_workflow) | **PATCH** /v1/action-workflows/{action_workflow_id} | patch an app


# **create_action_workflow_config**
> AppActionWorkflowConfig create_action_workflow_config(action_workflow_id, service_create_action_workflow_config_request)

create action workflow config

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_action_workflow_config import AppActionWorkflowConfig
from nuon.models.service_create_action_workflow_config_request import ServiceCreateActionWorkflowConfigRequest
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
    api_instance = nuon.ActionsApi(api_client)
    action_workflow_id = 'action_workflow_id_example' # str | action workflow ID
    service_create_action_workflow_config_request = nuon.ServiceCreateActionWorkflowConfigRequest() # ServiceCreateActionWorkflowConfigRequest | Input

    try:
        # create action workflow config
        api_response = api_instance.create_action_workflow_config(action_workflow_id, service_create_action_workflow_config_request)
        print("The response of ActionsApi->create_action_workflow_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->create_action_workflow_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action_workflow_id** | **str**| action workflow ID | 
 **service_create_action_workflow_config_request** | [**ServiceCreateActionWorkflowConfigRequest**](ServiceCreateActionWorkflowConfigRequest.md)| Input | 

### Return type

[**AppActionWorkflowConfig**](AppActionWorkflowConfig.md)

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

# **create_app_action_workflow**
> AppActionWorkflow create_app_action_workflow(app_id, service_create_app_action_workflow_request)

create an app

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_action_workflow import AppActionWorkflow
from nuon.models.service_create_app_action_workflow_request import ServiceCreateAppActionWorkflowRequest
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
    api_instance = nuon.ActionsApi(api_client)
    app_id = 'app_id_example' # str | app ID
    service_create_app_action_workflow_request = nuon.ServiceCreateAppActionWorkflowRequest() # ServiceCreateAppActionWorkflowRequest | Input

    try:
        # create an app
        api_response = api_instance.create_app_action_workflow(app_id, service_create_app_action_workflow_request)
        print("The response of ActionsApi->create_app_action_workflow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->create_app_action_workflow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| app ID | 
 **service_create_app_action_workflow_request** | [**ServiceCreateAppActionWorkflowRequest**](ServiceCreateAppActionWorkflowRequest.md)| Input | 

### Return type

[**AppActionWorkflow**](AppActionWorkflow.md)

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

# **create_install_action_workflow_run**
> str create_install_action_workflow_run(install_id, service_create_install_action_workflow_run_request)

create an action workflow run for an install

AppWorkflowConfigId param has been deprecated and is no longer being consumed, the api uses currently install id to lookup related appworkflowconfigId 

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.service_create_install_action_workflow_run_request import ServiceCreateInstallActionWorkflowRunRequest
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
    api_instance = nuon.ActionsApi(api_client)
    install_id = 'install_id_example' # str | install ID
    service_create_install_action_workflow_run_request = nuon.ServiceCreateInstallActionWorkflowRunRequest() # ServiceCreateInstallActionWorkflowRunRequest | Input

    try:
        # create an action workflow run for an install
        api_response = api_instance.create_install_action_workflow_run(install_id, service_create_install_action_workflow_run_request)
        print("The response of ActionsApi->create_install_action_workflow_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->create_install_action_workflow_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **str**| install ID | 
 **service_create_install_action_workflow_run_request** | [**ServiceCreateInstallActionWorkflowRunRequest**](ServiceCreateInstallActionWorkflowRunRequest.md)| Input | 

### Return type

**str**

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

# **delete_action_workflow**
> bool delete_action_workflow(action_workflow_id)

delete an app

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
    api_instance = nuon.ActionsApi(api_client)
    action_workflow_id = 'action_workflow_id_example' # str | action workflow ID

    try:
        # delete an app
        api_response = api_instance.delete_action_workflow(action_workflow_id)
        print("The response of ActionsApi->delete_action_workflow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->delete_action_workflow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action_workflow_id** | **str**| action workflow ID | 

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

# **get_action_workflow**
> AppActionWorkflow get_action_workflow(action_workflow_id)

get an app action workflow

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_action_workflow import AppActionWorkflow
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
    api_instance = nuon.ActionsApi(api_client)
    action_workflow_id = 'action_workflow_id_example' # str | action workflow ID or name

    try:
        # get an app action workflow
        api_response = api_instance.get_action_workflow(action_workflow_id)
        print("The response of ActionsApi->get_action_workflow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->get_action_workflow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action_workflow_id** | **str**| action workflow ID or name | 

### Return type

[**AppActionWorkflow**](AppActionWorkflow.md)

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

# **get_action_workflow_config**
> AppActionWorkflowConfig get_action_workflow_config(action_workflow_config_id)

get an app action workflow config

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_action_workflow_config import AppActionWorkflowConfig
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
    api_instance = nuon.ActionsApi(api_client)
    action_workflow_config_id = 'action_workflow_config_id_example' # str | action workflow config ID

    try:
        # get an app action workflow config
        api_response = api_instance.get_action_workflow_config(action_workflow_config_id)
        print("The response of ActionsApi->get_action_workflow_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->get_action_workflow_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action_workflow_config_id** | **str**| action workflow config ID | 

### Return type

[**AppActionWorkflowConfig**](AppActionWorkflowConfig.md)

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

# **get_action_workflow_configs**
> List[AppActionWorkflowConfig] get_action_workflow_configs(action_workflow_id, offset=offset, limit=limit, page=page, x_nuon_pagination_enabled=x_nuon_pagination_enabled)

get action workflow for an app

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_action_workflow_config import AppActionWorkflowConfig
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
    api_instance = nuon.ActionsApi(api_client)
    action_workflow_id = 'action_workflow_id_example' # str | action workflow ID
    offset = 0 # int | offset of results to return (optional) (default to 0)
    limit = 10 # int | limit of results to return (optional) (default to 10)
    page = 0 # int | page number of results to return (optional) (default to 0)
    x_nuon_pagination_enabled = True # bool | Enable pagination (optional)

    try:
        # get action workflow for an app
        api_response = api_instance.get_action_workflow_configs(action_workflow_id, offset=offset, limit=limit, page=page, x_nuon_pagination_enabled=x_nuon_pagination_enabled)
        print("The response of ActionsApi->get_action_workflow_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->get_action_workflow_configs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action_workflow_id** | **str**| action workflow ID | 
 **offset** | **int**| offset of results to return | [optional] [default to 0]
 **limit** | **int**| limit of results to return | [optional] [default to 10]
 **page** | **int**| page number of results to return | [optional] [default to 0]
 **x_nuon_pagination_enabled** | **bool**| Enable pagination | [optional] 

### Return type

[**List[AppActionWorkflowConfig]**](AppActionWorkflowConfig.md)

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

# **get_action_workflow_latest_config**
> AppActionWorkflowConfig get_action_workflow_latest_config(action_workflow_id)

get an app action workflow's latest config

Return the latest config for an action workflow. 

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_action_workflow_config import AppActionWorkflowConfig
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
    api_instance = nuon.ActionsApi(api_client)
    action_workflow_id = 'action_workflow_id_example' # str | action workflow ID

    try:
        # get an app action workflow's latest config
        api_response = api_instance.get_action_workflow_latest_config(action_workflow_id)
        print("The response of ActionsApi->get_action_workflow_latest_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->get_action_workflow_latest_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action_workflow_id** | **str**| action workflow ID | 

### Return type

[**AppActionWorkflowConfig**](AppActionWorkflowConfig.md)

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

# **get_action_workflows**
> List[AppActionWorkflow] get_action_workflows(app_id, q=q, offset=offset, limit=limit, page=page, x_nuon_pagination_enabled=x_nuon_pagination_enabled)

get action workflows for an app

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_action_workflow import AppActionWorkflow
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
    api_instance = nuon.ActionsApi(api_client)
    app_id = 'app_id_example' # str | app ID
    q = 'q_example' # str | search query to filter action workflows by name (optional)
    offset = 0 # int | offset of results to return (optional) (default to 0)
    limit = 10 # int | limit of results to return (optional) (default to 10)
    page = 0 # int | page number of results to return (optional) (default to 0)
    x_nuon_pagination_enabled = True # bool | Enable pagination (optional)

    try:
        # get action workflows for an app
        api_response = api_instance.get_action_workflows(app_id, q=q, offset=offset, limit=limit, page=page, x_nuon_pagination_enabled=x_nuon_pagination_enabled)
        print("The response of ActionsApi->get_action_workflows:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->get_action_workflows: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| app ID | 
 **q** | **str**| search query to filter action workflows by name | [optional] 
 **offset** | **int**| offset of results to return | [optional] [default to 0]
 **limit** | **int**| limit of results to return | [optional] [default to 10]
 **page** | **int**| page number of results to return | [optional] [default to 0]
 **x_nuon_pagination_enabled** | **bool**| Enable pagination | [optional] 

### Return type

[**List[AppActionWorkflow]**](AppActionWorkflow.md)

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

# **get_app_action_workflow**
> AppActionWorkflow get_app_action_workflow(app_id, action_workflow_id)

get an app action workflow

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_action_workflow import AppActionWorkflow
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
    api_instance = nuon.ActionsApi(api_client)
    app_id = 'app_id_example' # str | app ID or name
    action_workflow_id = 'action_workflow_id_example' # str | action workflow ID or name

    try:
        # get an app action workflow
        api_response = api_instance.get_app_action_workflow(app_id, action_workflow_id)
        print("The response of ActionsApi->get_app_action_workflow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->get_app_action_workflow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| app ID or name | 
 **action_workflow_id** | **str**| action workflow ID or name | 

### Return type

[**AppActionWorkflow**](AppActionWorkflow.md)

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

# **get_install_action_workflow_recent_runs**
> AppInstallActionWorkflow get_install_action_workflow_recent_runs(install_id, action_workflow_id, offset=offset, limit=limit, page=page, x_nuon_pagination_enabled=x_nuon_pagination_enabled)

get recent runs for an action workflow by install id

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_install_action_workflow import AppInstallActionWorkflow
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
    api_instance = nuon.ActionsApi(api_client)
    install_id = 'install_id_example' # str | install ID
    action_workflow_id = 'action_workflow_id_example' # str | action workflow ID
    offset = 0 # int | offset of results to return (optional) (default to 0)
    limit = 10 # int | limit of results to return (optional) (default to 10)
    page = 0 # int | page number of results to return (optional) (default to 0)
    x_nuon_pagination_enabled = True # bool | Enable pagination (optional)

    try:
        # get recent runs for an action workflow by install id
        api_response = api_instance.get_install_action_workflow_recent_runs(install_id, action_workflow_id, offset=offset, limit=limit, page=page, x_nuon_pagination_enabled=x_nuon_pagination_enabled)
        print("The response of ActionsApi->get_install_action_workflow_recent_runs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->get_install_action_workflow_recent_runs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **str**| install ID | 
 **action_workflow_id** | **str**| action workflow ID | 
 **offset** | **int**| offset of results to return | [optional] [default to 0]
 **limit** | **int**| limit of results to return | [optional] [default to 10]
 **page** | **int**| page number of results to return | [optional] [default to 0]
 **x_nuon_pagination_enabled** | **bool**| Enable pagination | [optional] 

### Return type

[**AppInstallActionWorkflow**](AppInstallActionWorkflow.md)

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

# **get_install_action_workflow_run**
> AppInstallActionWorkflowRun get_install_action_workflow_run(install_id, run_id)

get action workflow runs by install id and run id

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_install_action_workflow_run import AppInstallActionWorkflowRun
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
    api_instance = nuon.ActionsApi(api_client)
    install_id = 'install_id_example' # str | install ID
    run_id = 'run_id_example' # str | run ID

    try:
        # get action workflow runs by install id and run id
        api_response = api_instance.get_install_action_workflow_run(install_id, run_id)
        print("The response of ActionsApi->get_install_action_workflow_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->get_install_action_workflow_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **str**| install ID | 
 **run_id** | **str**| run ID | 

### Return type

[**AppInstallActionWorkflowRun**](AppInstallActionWorkflowRun.md)

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

# **get_install_action_workflow_run_step**
> AppInstallActionWorkflowRunStep get_install_action_workflow_run_step(install_id, workflow_run_id, step_id)

get action workflow run step by install id and step id

Get an install action workflow run step. 

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_install_action_workflow_run_step import AppInstallActionWorkflowRunStep
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
    api_instance = nuon.ActionsApi(api_client)
    install_id = 'install_id_example' # str | install ID
    workflow_run_id = 'workflow_run_id_example' # str | workflow run ID
    step_id = 'step_id_example' # str | step ID

    try:
        # get action workflow run step by install id and step id
        api_response = api_instance.get_install_action_workflow_run_step(install_id, workflow_run_id, step_id)
        print("The response of ActionsApi->get_install_action_workflow_run_step:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->get_install_action_workflow_run_step: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **str**| install ID | 
 **workflow_run_id** | **str**| workflow run ID | 
 **step_id** | **str**| step ID | 

### Return type

[**AppInstallActionWorkflowRunStep**](AppInstallActionWorkflowRunStep.md)

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

# **get_install_action_workflow_runs**
> List[AppInstallActionWorkflowRun] get_install_action_workflow_runs(install_id, offset=offset, limit=limit, page=page, x_nuon_pagination_enabled=x_nuon_pagination_enabled)

get action workflow runs by install id

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_install_action_workflow_run import AppInstallActionWorkflowRun
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
    api_instance = nuon.ActionsApi(api_client)
    install_id = 'install_id_example' # str | install ID
    offset = 0 # int | offset of results to return (optional) (default to 0)
    limit = 10 # int | limit of results to return (optional) (default to 10)
    page = 0 # int | page number of results to return (optional) (default to 0)
    x_nuon_pagination_enabled = True # bool | Enable pagination (optional)

    try:
        # get action workflow runs by install id
        api_response = api_instance.get_install_action_workflow_runs(install_id, offset=offset, limit=limit, page=page, x_nuon_pagination_enabled=x_nuon_pagination_enabled)
        print("The response of ActionsApi->get_install_action_workflow_runs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->get_install_action_workflow_runs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **str**| install ID | 
 **offset** | **int**| offset of results to return | [optional] [default to 0]
 **limit** | **int**| limit of results to return | [optional] [default to 10]
 **page** | **int**| page number of results to return | [optional] [default to 0]
 **x_nuon_pagination_enabled** | **bool**| Enable pagination | [optional] 

### Return type

[**List[AppInstallActionWorkflowRun]**](AppInstallActionWorkflowRun.md)

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

# **get_install_action_workflows_latest_runs**
> List[AppInstallActionWorkflow] get_install_action_workflows_latest_runs(install_id, trigger_types=trigger_types, offset=offset, limit=limit, page=page, q=q, x_nuon_pagination_enabled=x_nuon_pagination_enabled)

get latest runs for all action workflows by install id

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_install_action_workflow import AppInstallActionWorkflow
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
    api_instance = nuon.ActionsApi(api_client)
    install_id = 'install_id_example' # str | install ID
    trigger_types = 'trigger_types_example' # str | filter by action workflow trigger by types (optional)
    offset = 0 # int | offset of results to return (optional) (default to 0)
    limit = 10 # int | limit of results to return (optional) (default to 10)
    page = 0 # int | page number of results to return (optional) (default to 0)
    q = 'q_example' # str | search query for action workflow name (optional)
    x_nuon_pagination_enabled = True # bool | Enable pagination (optional)

    try:
        # get latest runs for all action workflows by install id
        api_response = api_instance.get_install_action_workflows_latest_runs(install_id, trigger_types=trigger_types, offset=offset, limit=limit, page=page, q=q, x_nuon_pagination_enabled=x_nuon_pagination_enabled)
        print("The response of ActionsApi->get_install_action_workflows_latest_runs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->get_install_action_workflows_latest_runs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **str**| install ID | 
 **trigger_types** | **str**| filter by action workflow trigger by types | [optional] 
 **offset** | **int**| offset of results to return | [optional] [default to 0]
 **limit** | **int**| limit of results to return | [optional] [default to 10]
 **page** | **int**| page number of results to return | [optional] [default to 0]
 **q** | **str**| search query for action workflow name | [optional] 
 **x_nuon_pagination_enabled** | **bool**| Enable pagination | [optional] 

### Return type

[**List[AppInstallActionWorkflow]**](AppInstallActionWorkflow.md)

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

# **update_app_action_workflow**
> AppActionWorkflow update_app_action_workflow(action_workflow_id, service_update_action_workflow_request)

patch an app

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_action_workflow import AppActionWorkflow
from nuon.models.service_update_action_workflow_request import ServiceUpdateActionWorkflowRequest
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
    api_instance = nuon.ActionsApi(api_client)
    action_workflow_id = 'action_workflow_id_example' # str | action workflow ID
    service_update_action_workflow_request = nuon.ServiceUpdateActionWorkflowRequest() # ServiceUpdateActionWorkflowRequest | Input

    try:
        # patch an app
        api_response = api_instance.update_app_action_workflow(action_workflow_id, service_update_action_workflow_request)
        print("The response of ActionsApi->update_app_action_workflow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->update_app_action_workflow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action_workflow_id** | **str**| action workflow ID | 
 **service_update_action_workflow_request** | [**ServiceUpdateActionWorkflowRequest**](ServiceUpdateActionWorkflowRequest.md)| Input | 

### Return type

[**AppActionWorkflow**](AppActionWorkflow.md)

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

