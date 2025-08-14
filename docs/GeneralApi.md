# nuon.GeneralApi

All URIs are relative to *http://localhost:8081*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_waitlist**](GeneralApi.md#create_waitlist) | **POST** /v1/general/waitlist | Allow user to be added to an org waitlist.
[**get_cli_config**](GeneralApi.md#get_cli_config) | **GET** /v1/general/cli-config | Get config for cli
[**get_cloud_platform_regions**](GeneralApi.md#get_cloud_platform_regions) | **GET** /v1/general/cloud-platform/{cloud_platform}/regions | Get regions for a cloud platform
[**get_config_schema**](GeneralApi.md#get_config_schema) | **GET** /v1/general/config-schema | Get jsonschema for config file
[**get_current_user**](GeneralApi.md#get_current_user) | **GET** /v1/general/current-user | Get current user


# **create_waitlist**
> AppWaitlist create_waitlist(service_waitlist_request)

Allow user to be added to an org waitlist.

### Example

* Api Key Authentication (APIKey):

```python
import time
import os
import nuon
from nuon.models.app_waitlist import AppWaitlist
from nuon.models.service_waitlist_request import ServiceWaitlistRequest
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

# Enter a context with an instance of the API client
with nuon.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nuon.GeneralApi(api_client)
    service_waitlist_request = nuon.ServiceWaitlistRequest() # ServiceWaitlistRequest | Input

    try:
        # Allow user to be added to an org waitlist.
        api_response = api_instance.create_waitlist(service_waitlist_request)
        print("The response of GeneralApi->create_waitlist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneralApi->create_waitlist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_waitlist_request** | [**ServiceWaitlistRequest**](ServiceWaitlistRequest.md)| Input | 

### Return type

[**AppWaitlist**](AppWaitlist.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cli_config**
> ServiceCLIConfig get_cli_config()

Get config for cli

### Example


```python
import time
import os
import nuon
from nuon.models.service_cli_config import ServiceCLIConfig
from nuon.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = nuon.Configuration(
    host = "http://localhost:8081"
)


# Enter a context with an instance of the API client
with nuon.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nuon.GeneralApi(api_client)

    try:
        # Get config for cli
        api_response = api_instance.get_cli_config()
        print("The response of GeneralApi->get_cli_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneralApi->get_cli_config: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ServiceCLIConfig**](ServiceCLIConfig.md)

### Authorization

No authorization required

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

# **get_cloud_platform_regions**
> List[AppCloudPlatformRegion] get_cloud_platform_regions(cloud_platform)

Get regions for a cloud platform

Return region metadata for the Nuon supported cloud platforms. 

### Example


```python
import time
import os
import nuon
from nuon.models.app_cloud_platform_region import AppCloudPlatformRegion
from nuon.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = nuon.Configuration(
    host = "http://localhost:8081"
)


# Enter a context with an instance of the API client
with nuon.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nuon.GeneralApi(api_client)
    cloud_platform = 'cloud_platform_example' # str | cloud platform

    try:
        # Get regions for a cloud platform
        api_response = api_instance.get_cloud_platform_regions(cloud_platform)
        print("The response of GeneralApi->get_cloud_platform_regions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneralApi->get_cloud_platform_regions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_platform** | **str**| cloud platform | 

### Return type

[**List[AppCloudPlatformRegion]**](AppCloudPlatformRegion.md)

### Authorization

No authorization required

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

# **get_config_schema**
> object get_config_schema(type=type)

Get jsonschema for config file

Return jsonschemas for Nuon configs. These can be used in frontmatter in most editors that have a TOML LSP (such as [Taplo](https://taplo.tamasfe.dev/) configured.  ```toml #:schema https://api.nuon.co/v1/general/config-schema?source=inputs  description = \"description\" ```  You can pass in a valid source argument to render within a specific config file:  - input - input-group - installer - sandbox - runner - docker_build - container_image - helm - terraform - job 

### Example


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


# Enter a context with an instance of the API client
with nuon.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nuon.GeneralApi(api_client)
    type = 'type_example' # str | return a schema for a source file (optional)

    try:
        # Get jsonschema for config file
        api_response = api_instance.get_config_schema(type=type)
        print("The response of GeneralApi->get_config_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneralApi->get_config_schema: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| return a schema for a source file | [optional] 

### Return type

**object**

### Authorization

No authorization required

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

# **get_current_user**
> AppAccount get_current_user()

Get current user

### Example

* Api Key Authentication (APIKey):

```python
import time
import os
import nuon
from nuon.models.app_account import AppAccount
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

# Enter a context with an instance of the API client
with nuon.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nuon.GeneralApi(api_client)

    try:
        # Get current user
        api_response = api_instance.get_current_user()
        print("The response of GeneralApi->get_current_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneralApi->get_current_user: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AppAccount**](AppAccount.md)

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

