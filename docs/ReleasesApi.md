# nuon.ReleasesApi

All URIs are relative to *https://ctl.prod.nuon.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_component_release**](ReleasesApi.md#create_component_release) | **POST** /v1/components/{component_id}/releases | create a release
[**get_app_releases**](ReleasesApi.md#get_app_releases) | **GET** /v1/apps/{app_id}/releases | get all releases for an app
[**get_component_releases**](ReleasesApi.md#get_component_releases) | **GET** /v1/components/{component_id}/releases | get all releases for a component
[**get_release**](ReleasesApi.md#get_release) | **GET** /v1/releases/{release_id} | get a release
[**get_release_steps**](ReleasesApi.md#get_release_steps) | **GET** /v1/releases/{release_id}/steps | get a release


# **create_component_release**
> AppComponentRelease create_component_release(component_id, service_create_component_release_request)

create a release

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import nuon
from nuon.models.app_component_release import AppComponentRelease
from nuon.models.service_create_component_release_request import ServiceCreateComponentReleaseRequest
from nuon.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://ctl.prod.nuon.co
# See configuration.py for a list of all supported configuration parameters.
configuration = nuon.Configuration(
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

# Configure API key authorization: OrgID
configuration.api_key['OrgID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['OrgID'] = 'Bearer'

# Enter a context with an instance of the API client
with nuon.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nuon.ReleasesApi(api_client)
    component_id = 'component_id_example' # str | component ID
    service_create_component_release_request = nuon.ServiceCreateComponentReleaseRequest() # ServiceCreateComponentReleaseRequest | Input

    try:
        # create a release
        api_response = api_instance.create_component_release(component_id, service_create_component_release_request)
        print("The response of ReleasesApi->create_component_release:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReleasesApi->create_component_release: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_id** | **str**| component ID | 
 **service_create_component_release_request** | [**ServiceCreateComponentReleaseRequest**](ServiceCreateComponentReleaseRequest.md)| Input | 

### Return type

[**AppComponentRelease**](AppComponentRelease.md)

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

# **get_app_releases**
> List[AppComponentRelease] get_app_releases(app_id)

get all releases for an app

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import nuon
from nuon.models.app_component_release import AppComponentRelease
from nuon.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://ctl.prod.nuon.co
# See configuration.py for a list of all supported configuration parameters.
configuration = nuon.Configuration(
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

# Configure API key authorization: OrgID
configuration.api_key['OrgID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['OrgID'] = 'Bearer'

# Enter a context with an instance of the API client
with nuon.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nuon.ReleasesApi(api_client)
    app_id = 'app_id_example' # str | app ID

    try:
        # get all releases for an app
        api_response = api_instance.get_app_releases(app_id)
        print("The response of ReleasesApi->get_app_releases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReleasesApi->get_app_releases: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| app ID | 

### Return type

[**List[AppComponentRelease]**](AppComponentRelease.md)

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

# **get_component_releases**
> List[AppComponentRelease] get_component_releases(component_id)

get all releases for a component

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import nuon
from nuon.models.app_component_release import AppComponentRelease
from nuon.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://ctl.prod.nuon.co
# See configuration.py for a list of all supported configuration parameters.
configuration = nuon.Configuration(
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

# Configure API key authorization: OrgID
configuration.api_key['OrgID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['OrgID'] = 'Bearer'

# Enter a context with an instance of the API client
with nuon.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nuon.ReleasesApi(api_client)
    component_id = 'component_id_example' # str | component ID

    try:
        # get all releases for a component
        api_response = api_instance.get_component_releases(component_id)
        print("The response of ReleasesApi->get_component_releases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReleasesApi->get_component_releases: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_id** | **str**| component ID | 

### Return type

[**List[AppComponentRelease]**](AppComponentRelease.md)

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

# **get_release**
> AppComponentRelease get_release(release_id)

get a release

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import nuon
from nuon.models.app_component_release import AppComponentRelease
from nuon.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://ctl.prod.nuon.co
# See configuration.py for a list of all supported configuration parameters.
configuration = nuon.Configuration(
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

# Configure API key authorization: OrgID
configuration.api_key['OrgID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['OrgID'] = 'Bearer'

# Enter a context with an instance of the API client
with nuon.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nuon.ReleasesApi(api_client)
    release_id = 'release_id_example' # str | release ID

    try:
        # get a release
        api_response = api_instance.get_release(release_id)
        print("The response of ReleasesApi->get_release:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReleasesApi->get_release: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **release_id** | **str**| release ID | 

### Return type

[**AppComponentRelease**](AppComponentRelease.md)

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

# **get_release_steps**
> List[AppComponentReleaseStep] get_release_steps(release_id)

get a release

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import nuon
from nuon.models.app_component_release_step import AppComponentReleaseStep
from nuon.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://ctl.prod.nuon.co
# See configuration.py for a list of all supported configuration parameters.
configuration = nuon.Configuration(
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

# Configure API key authorization: OrgID
configuration.api_key['OrgID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['OrgID'] = 'Bearer'

# Enter a context with an instance of the API client
with nuon.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nuon.ReleasesApi(api_client)
    release_id = 'release_id_example' # str | release ID

    try:
        # get a release
        api_response = api_instance.get_release_steps(release_id)
        print("The response of ReleasesApi->get_release_steps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReleasesApi->get_release_steps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **release_id** | **str**| release ID | 

### Return type

[**List[AppComponentReleaseStep]**](AppComponentReleaseStep.md)

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

