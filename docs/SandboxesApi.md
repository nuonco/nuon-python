# openapi_client.SandboxesApi

All URIs are relative to *https://ctl.prod.nuon.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_sandbox**](SandboxesApi.md#get_sandbox) | **GET** /v1/sandboxes/{sandbox_id} | get a sandbox
[**get_sandbox_releases**](SandboxesApi.md#get_sandbox_releases) | **GET** /v1/sandboxes/{sandbox_id}/releases | get sandbox releases
[**get_sandboxes**](SandboxesApi.md#get_sandboxes) | **GET** /v1/sandboxes | get all sandboxes


# **get_sandbox**
> AppSandbox get_sandbox(sandbox_id)

get a sandbox

### Example

* Api Key Authentication (APIKey):

```python
import time
import os
import openapi_client
from openapi_client.models.app_sandbox import AppSandbox
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://ctl.prod.nuon.co
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://ctl.prod.nuon.co"
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SandboxesApi(api_client)
    sandbox_id = 'sandbox_id_example' # str | sandbox ID

    try:
        # get a sandbox
        api_response = api_instance.get_sandbox(sandbox_id)
        print("The response of SandboxesApi->get_sandbox:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SandboxesApi->get_sandbox: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sandbox_id** | **str**| sandbox ID | 

### Return type

[**AppSandbox**](AppSandbox.md)

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

# **get_sandbox_releases**
> List[AppSandboxRelease] get_sandbox_releases(sandbox_id)

get sandbox releases

### Example

* Api Key Authentication (APIKey):

```python
import time
import os
import openapi_client
from openapi_client.models.app_sandbox_release import AppSandboxRelease
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://ctl.prod.nuon.co
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://ctl.prod.nuon.co"
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SandboxesApi(api_client)
    sandbox_id = 'sandbox_id_example' # str | sandbox ID

    try:
        # get sandbox releases
        api_response = api_instance.get_sandbox_releases(sandbox_id)
        print("The response of SandboxesApi->get_sandbox_releases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SandboxesApi->get_sandbox_releases: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sandbox_id** | **str**| sandbox ID | 

### Return type

[**List[AppSandboxRelease]**](AppSandboxRelease.md)

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

# **get_sandboxes**
> List[AppSandbox] get_sandboxes()

get all sandboxes

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.app_sandbox import AppSandbox
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://ctl.prod.nuon.co
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://ctl.prod.nuon.co"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SandboxesApi(api_client)

    try:
        # get all sandboxes
        api_response = api_instance.get_sandboxes()
        print("The response of SandboxesApi->get_sandboxes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SandboxesApi->get_sandboxes: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[AppSandbox]**](AppSandbox.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

