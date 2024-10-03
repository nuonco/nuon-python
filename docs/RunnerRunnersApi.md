# nuon.RunnerRunnersApi

All URIs are relative to *https://api.nuon.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_runner**](RunnerRunnersApi.md#get_runner) | **GET** /v1/runners/{runner_id} | get a runner


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
    api_instance = nuon.RunnerRunnersApi(api_client)
    runner_id = 'runner_id_example' # str | runner ID

    try:
        # get a runner
        api_response = api_instance.get_runner(runner_id)
        print("The response of RunnerRunnersApi->get_runner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnerRunnersApi->get_runner: %s\n" % e)
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

