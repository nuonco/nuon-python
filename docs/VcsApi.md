# nuon.VcsApi

All URIs are relative to *https://ctl.prod.nuon.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_vcs_connection**](VcsApi.md#create_vcs_connection) | **POST** /v1/vcs/connections | create a vcs connection for Github
[**create_vcs_connection_callback**](VcsApi.md#create_vcs_connection_callback) | **POST** /v1/vcs/connection-callback | public connection to create a vcs connection via a callback
[**get_all_vcs_connected_repos**](VcsApi.md#get_all_vcs_connected_repos) | **GET** /v1/vcs/connected-repos | get all vcs connected repos for an org
[**get_org_vcs_connections**](VcsApi.md#get_org_vcs_connections) | **GET** /v1/vcs/connections | get vcs connection for an org
[**get_vcs_connection**](VcsApi.md#get_vcs_connection) | **GET** /v1/vcs/connections/{connection_id} | returns a vcs connection for an org


# **create_vcs_connection**
> AppVCSConnection create_vcs_connection(service_create_connection_request)

create a vcs connection for Github

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import nuon
from nuon.models.app_vcs_connection import AppVCSConnection
from nuon.models.service_create_connection_request import ServiceCreateConnectionRequest
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
    api_instance = nuon.VcsApi(api_client)
    service_create_connection_request = nuon.ServiceCreateConnectionRequest() # ServiceCreateConnectionRequest | Input

    try:
        # create a vcs connection for Github
        api_response = api_instance.create_vcs_connection(service_create_connection_request)
        print("The response of VcsApi->create_vcs_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VcsApi->create_vcs_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_create_connection_request** | [**ServiceCreateConnectionRequest**](ServiceCreateConnectionRequest.md)| Input | 

### Return type

[**AppVCSConnection**](AppVCSConnection.md)

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

# **create_vcs_connection_callback**
> AppVCSConnection create_vcs_connection_callback(service_create_connection_callback_request)

public connection to create a vcs connection via a callback

### Example


```python
import nuon
from nuon.models.app_vcs_connection import AppVCSConnection
from nuon.models.service_create_connection_callback_request import ServiceCreateConnectionCallbackRequest
from nuon.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://ctl.prod.nuon.co
# See configuration.py for a list of all supported configuration parameters.
configuration = nuon.Configuration(
    host = "https://ctl.prod.nuon.co"
)


# Enter a context with an instance of the API client
with nuon.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nuon.VcsApi(api_client)
    service_create_connection_callback_request = nuon.ServiceCreateConnectionCallbackRequest() # ServiceCreateConnectionCallbackRequest | Input

    try:
        # public connection to create a vcs connection via a callback
        api_response = api_instance.create_vcs_connection_callback(service_create_connection_callback_request)
        print("The response of VcsApi->create_vcs_connection_callback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VcsApi->create_vcs_connection_callback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_create_connection_callback_request** | [**ServiceCreateConnectionCallbackRequest**](ServiceCreateConnectionCallbackRequest.md)| Input | 

### Return type

[**AppVCSConnection**](AppVCSConnection.md)

### Authorization

No authorization required

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

# **get_all_vcs_connected_repos**
> List[ServiceRepository] get_all_vcs_connected_repos()

get all vcs connected repos for an org

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import nuon
from nuon.models.service_repository import ServiceRepository
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
    api_instance = nuon.VcsApi(api_client)

    try:
        # get all vcs connected repos for an org
        api_response = api_instance.get_all_vcs_connected_repos()
        print("The response of VcsApi->get_all_vcs_connected_repos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VcsApi->get_all_vcs_connected_repos: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ServiceRepository]**](ServiceRepository.md)

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

# **get_org_vcs_connections**
> List[AppVCSConnection] get_org_vcs_connections()

get vcs connection for an org

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import nuon
from nuon.models.app_vcs_connection import AppVCSConnection
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
    api_instance = nuon.VcsApi(api_client)

    try:
        # get vcs connection for an org
        api_response = api_instance.get_org_vcs_connections()
        print("The response of VcsApi->get_org_vcs_connections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VcsApi->get_org_vcs_connections: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[AppVCSConnection]**](AppVCSConnection.md)

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

# **get_vcs_connection**
> AppVCSConnection get_vcs_connection(connection_id)

returns a vcs connection for an org

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import nuon
from nuon.models.app_vcs_connection import AppVCSConnection
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
    api_instance = nuon.VcsApi(api_client)
    connection_id = 'connection_id_example' # str | connection ID

    try:
        # returns a vcs connection for an org
        api_response = api_instance.get_vcs_connection(connection_id)
        print("The response of VcsApi->get_vcs_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VcsApi->get_vcs_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**| connection ID | 

### Return type

[**AppVCSConnection**](AppVCSConnection.md)

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

