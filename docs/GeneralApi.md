# nuon.GeneralApi

All URIs are relative to *https://ctl.prod.nuon.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cli_config**](GeneralApi.md#get_cli_config) | **GET** /v1/general/cli-config | Get config for cli
[**get_current_user**](GeneralApi.md#get_current_user) | **GET** /v1/general/current-user | Get current user
[**publish_metrics**](GeneralApi.md#publish_metrics) | **POST** /v1/general/metrics | Publish a metric from different Nuon clients for telemetry purposes.


# **get_cli_config**
> ServiceCLIConfig get_cli_config()

Get config for cli

### Example


```python
import nuon
from nuon.models.service_cli_config import ServiceCLIConfig
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

# **get_current_user**
> AppUserToken get_current_user()

Get current user

### Example

* Api Key Authentication (APIKey):

```python
import nuon
from nuon.models.app_user_token import AppUserToken
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

[**AppUserToken**](AppUserToken.md)

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

# **publish_metrics**
> str publish_metrics(service_publish_metric_input)

Publish a metric from different Nuon clients for telemetry purposes.

### Example

* Api Key Authentication (APIKey):

```python
import nuon
from nuon.models.service_publish_metric_input import ServicePublishMetricInput
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

# Enter a context with an instance of the API client
with nuon.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nuon.GeneralApi(api_client)
    service_publish_metric_input = [nuon.ServicePublishMetricInput()] # List[ServicePublishMetricInput] | Input

    try:
        # Publish a metric from different Nuon clients for telemetry purposes.
        api_response = api_instance.publish_metrics(service_publish_metric_input)
        print("The response of GeneralApi->publish_metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneralApi->publish_metrics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_publish_metric_input** | [**List[ServicePublishMetricInput]**](ServicePublishMetricInput.md)| Input | 

### Return type

**str**

### Authorization

[APIKey](../README.md#APIKey)

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

