# nuon.RunnersRunnerApi

All URIs are relative to *https://api.nuon.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_runner_job**](RunnersRunnerApi.md#get_runner_job) | **GET** /v1/runner-jobs/{runner_job_id} | get runner job
[**get_runner_job_executions**](RunnersRunnerApi.md#get_runner_job_executions) | **GET** /v1/runner-jobs/{runner_job_id}/executions | get runner job executions
[**get_runner_job_plan**](RunnersRunnerApi.md#get_runner_job_plan) | **GET** /v1/runner-jobs/{runner_job_id}/plan | get runner job plan
[**get_runner_jobs**](RunnersRunnerApi.md#get_runner_jobs) | **GET** /v1/runners/{runner_id}/jobs | get runner jobs
[**get_runner_settings**](RunnersRunnerApi.md#get_runner_settings) | **GET** /v1/runners/{runner_id}/settings | get runner settings


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
> List[AppRunnerJobExecution] get_runner_job_executions(runner_job_id)

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
    api_instance = nuon.RunnersRunnerApi(api_client)
    runner_job_id = 'runner_job_id_example' # str | runner job ID

    try:
        # get runner job executions
        api_response = api_instance.get_runner_job_executions(runner_job_id)
        print("The response of RunnersRunnerApi->get_runner_job_executions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnersRunnerApi->get_runner_job_executions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **runner_job_id** | **str**| runner job ID | 

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

# **get_runner_jobs**
> List[AppRunnerJob] get_runner_jobs(runner_id, limit=limit, group=group, status=status)

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
    api_instance = nuon.RunnersRunnerApi(api_client)
    runner_id = 'runner_id_example' # str | runner ID
    limit = 10 # int | limit of jobs to return (optional) (default to 10)
    group = '"any"' # str | job group (optional) (default to '"any"')
    status = '"available"' # str | job status (optional) (default to '"available"')

    try:
        # get runner jobs
        api_response = api_instance.get_runner_jobs(runner_id, limit=limit, group=group, status=status)
        print("The response of RunnersRunnerApi->get_runner_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnersRunnerApi->get_runner_jobs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **runner_id** | **str**| runner ID | 
 **limit** | **int**| limit of jobs to return | [optional] [default to 10]
 **group** | **str**| job group | [optional] [default to &#39;&quot;any&quot;&#39;]
 **status** | **str**| job status | [optional] [default to &#39;&quot;available&quot;&#39;]

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
    api_instance = nuon.RunnersRunnerApi(api_client)
    runner_id = 'runner_id_example' # str | runner ID

    try:
        # get runner settings
        api_response = api_instance.get_runner_settings(runner_id)
        print("The response of RunnersRunnerApi->get_runner_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnersRunnerApi->get_runner_settings: %s\n" % e)
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
