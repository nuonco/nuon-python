# nuon.ActionsRunnerApi

All URIs are relative to *http://localhost:8081*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_action_workflow_config**](ActionsRunnerApi.md#get_action_workflow_config) | **GET** /v1/action-workflows/configs/{action_workflow_config_id} | get an app action workflow config
[**get_action_workflow_latest_config**](ActionsRunnerApi.md#get_action_workflow_latest_config) | **GET** /v1/action-workflows/{action_workflow_id}/latest-config | get an app action workflow&#39;s latest config
[**get_install_action_workflow_run**](ActionsRunnerApi.md#get_install_action_workflow_run) | **GET** /v1/installs/{install_id}/action-workflows/runs/{run_id} | get action workflow runs by install id and run id


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
    api_instance = nuon.ActionsRunnerApi(api_client)
    action_workflow_config_id = 'action_workflow_config_id_example' # str | action workflow config ID

    try:
        # get an app action workflow config
        api_response = api_instance.get_action_workflow_config(action_workflow_config_id)
        print("The response of ActionsRunnerApi->get_action_workflow_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsRunnerApi->get_action_workflow_config: %s\n" % e)
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
    api_instance = nuon.ActionsRunnerApi(api_client)
    action_workflow_id = 'action_workflow_id_example' # str | action workflow ID

    try:
        # get an app action workflow's latest config
        api_response = api_instance.get_action_workflow_latest_config(action_workflow_id)
        print("The response of ActionsRunnerApi->get_action_workflow_latest_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsRunnerApi->get_action_workflow_latest_config: %s\n" % e)
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
    api_instance = nuon.ActionsRunnerApi(api_client)
    install_id = 'install_id_example' # str | install ID
    run_id = 'run_id_example' # str | run ID

    try:
        # get action workflow runs by install id and run id
        api_response = api_instance.get_install_action_workflow_run(install_id, run_id)
        print("The response of ActionsRunnerApi->get_install_action_workflow_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsRunnerApi->get_install_action_workflow_run: %s\n" % e)
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

