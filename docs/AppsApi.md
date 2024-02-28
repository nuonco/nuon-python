# nuon.AppsApi

All URIs are relative to *https://ctl.prod.nuon.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_app**](AppsApi.md#create_app) | **POST** /v1/apps | create an app
[**create_app_config**](AppsApi.md#create_app_config) | **POST** /v1/apps/{app_id}/config | 
[**create_app_input_config**](AppsApi.md#create_app_input_config) | **POST** /v1/apps/{app_id}/input-config | 
[**create_app_runner_config**](AppsApi.md#create_app_runner_config) | **POST** /v1/apps/{app_id}/runner-config | create an app runner config
[**create_app_sandbox_config**](AppsApi.md#create_app_sandbox_config) | **POST** /v1/apps/{app_id}/sandbox-config | create an app sandbox config
[**delete_app**](AppsApi.md#delete_app) | **DELETE** /v1/apps/{app_id} | delete an app
[**get_app**](AppsApi.md#get_app) | **GET** /v1/apps/{app_id} | get an app
[**get_app_config_template**](AppsApi.md#get_app_config_template) | **GET** /v1/apps/{app_id}/template-config | get an app config template
[**get_app_configs**](AppsApi.md#get_app_configs) | **GET** /v1/apps/{app_id}/configs | get app configs
[**get_app_input_configs**](AppsApi.md#get_app_input_configs) | **GET** /v1/apps/{app_id}/input-configs | get app input configs
[**get_app_input_latest_config**](AppsApi.md#get_app_input_latest_config) | **GET** /v1/apps/{app_id}/input-latest-config | get latest app input config
[**get_app_latest_config**](AppsApi.md#get_app_latest_config) | **GET** /v1/apps/{app_id}/latest-config | get latest app config
[**get_app_runner_configs**](AppsApi.md#get_app_runner_configs) | **GET** /v1/apps/{app_id}/runner-configs | get app runner configs
[**get_app_runner_latest_config**](AppsApi.md#get_app_runner_latest_config) | **GET** /v1/apps/{app_id}/runner-latest-config | get latest app runner config
[**get_app_sandbox_configs**](AppsApi.md#get_app_sandbox_configs) | **GET** /v1/apps/{app_id}/sandbox-configs | get app sandbox configs
[**get_app_sandbox_latest_config**](AppsApi.md#get_app_sandbox_latest_config) | **GET** /v1/apps/{app_id}/sandbox-latest-config | get latest app sandbox config
[**get_apps**](AppsApi.md#get_apps) | **GET** /v1/apps | get all apps for the current org
[**update_app**](AppsApi.md#update_app) | **PATCH** /v1/apps/{app_id} | update an app


# **create_app**
> AppApp create_app(service_create_app_request)

create an app

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_app import AppApp
from nuon.models.service_create_app_request import ServiceCreateAppRequest
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
    api_instance = nuon.AppsApi(api_client)
    service_create_app_request = nuon.ServiceCreateAppRequest() # ServiceCreateAppRequest | Input

    try:
        # create an app
        api_response = api_instance.create_app(service_create_app_request)
        print("The response of AppsApi->create_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->create_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_create_app_request** | [**ServiceCreateAppRequest**](ServiceCreateAppRequest.md)| Input | 

### Return type

[**AppApp**](AppApp.md)

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

# **create_app_config**
> AppAppConfig create_app_config(app_id, service_create_app_config_request)



Create an app config, by pushing the contents of a config file.  The API will automatically configure the app according to the config file in the background. 

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_app_config import AppAppConfig
from nuon.models.service_create_app_config_request import ServiceCreateAppConfigRequest
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
    api_instance = nuon.AppsApi(api_client)
    app_id = 'app_id_example' # str | app ID
    service_create_app_config_request = nuon.ServiceCreateAppConfigRequest() # ServiceCreateAppConfigRequest | Input

    try:
        api_response = api_instance.create_app_config(app_id, service_create_app_config_request)
        print("The response of AppsApi->create_app_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->create_app_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| app ID | 
 **service_create_app_config_request** | [**ServiceCreateAppConfigRequest**](ServiceCreateAppConfigRequest.md)| Input | 

### Return type

[**AppAppConfig**](AppAppConfig.md)

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

# **create_app_input_config**
> AppAppInputConfig create_app_input_config(app_id, service_create_app_input_config_request)



### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_app_input_config import AppAppInputConfig
from nuon.models.service_create_app_input_config_request import ServiceCreateAppInputConfigRequest
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
    api_instance = nuon.AppsApi(api_client)
    app_id = 'app_id_example' # str | app ID
    service_create_app_input_config_request = nuon.ServiceCreateAppInputConfigRequest() # ServiceCreateAppInputConfigRequest | Input

    try:
        api_response = api_instance.create_app_input_config(app_id, service_create_app_input_config_request)
        print("The response of AppsApi->create_app_input_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->create_app_input_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| app ID | 
 **service_create_app_input_config_request** | [**ServiceCreateAppInputConfigRequest**](ServiceCreateAppInputConfigRequest.md)| Input | 

### Return type

[**AppAppInputConfig**](AppAppInputConfig.md)

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

# **create_app_runner_config**
> AppAppRunnerConfig create_app_runner_config(app_id, service_create_app_runner_config_request)

create an app runner config

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_app_runner_config import AppAppRunnerConfig
from nuon.models.service_create_app_runner_config_request import ServiceCreateAppRunnerConfigRequest
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
    api_instance = nuon.AppsApi(api_client)
    app_id = 'app_id_example' # str | app ID
    service_create_app_runner_config_request = nuon.ServiceCreateAppRunnerConfigRequest() # ServiceCreateAppRunnerConfigRequest | Input

    try:
        # create an app runner config
        api_response = api_instance.create_app_runner_config(app_id, service_create_app_runner_config_request)
        print("The response of AppsApi->create_app_runner_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->create_app_runner_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| app ID | 
 **service_create_app_runner_config_request** | [**ServiceCreateAppRunnerConfigRequest**](ServiceCreateAppRunnerConfigRequest.md)| Input | 

### Return type

[**AppAppRunnerConfig**](AppAppRunnerConfig.md)

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

# **create_app_sandbox_config**
> AppAppSandboxConfig create_app_sandbox_config(app_id, service_create_app_sandbox_config_request)

create an app sandbox config

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_app_sandbox_config import AppAppSandboxConfig
from nuon.models.service_create_app_sandbox_config_request import ServiceCreateAppSandboxConfigRequest
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
    api_instance = nuon.AppsApi(api_client)
    app_id = 'app_id_example' # str | app ID
    service_create_app_sandbox_config_request = nuon.ServiceCreateAppSandboxConfigRequest() # ServiceCreateAppSandboxConfigRequest | Input

    try:
        # create an app sandbox config
        api_response = api_instance.create_app_sandbox_config(app_id, service_create_app_sandbox_config_request)
        print("The response of AppsApi->create_app_sandbox_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->create_app_sandbox_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| app ID | 
 **service_create_app_sandbox_config_request** | [**ServiceCreateAppSandboxConfigRequest**](ServiceCreateAppSandboxConfigRequest.md)| Input | 

### Return type

[**AppAppSandboxConfig**](AppAppSandboxConfig.md)

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

# **delete_app**
> bool delete_app(app_id)

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
    api_instance = nuon.AppsApi(api_client)
    app_id = 'app_id_example' # str | app ID

    try:
        # delete an app
        api_response = api_instance.delete_app(app_id)
        print("The response of AppsApi->delete_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->delete_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| app ID | 

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

# **get_app**
> AppApp get_app(app_id)

get an app

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_app import AppApp
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
    api_instance = nuon.AppsApi(api_client)
    app_id = 'app_id_example' # str | app ID

    try:
        # get an app
        api_response = api_instance.get_app(app_id)
        print("The response of AppsApi->get_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->get_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| app ID | 

### Return type

[**AppApp**](AppApp.md)

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

# **get_app_config_template**
> ServiceAppConfigTemplate get_app_config_template(app_id, type)

get an app config template

Create an application template which provides a fully rendered config that can be modified and used to kickstart any application. 

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.service_app_config_template import ServiceAppConfigTemplate
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
    api_instance = nuon.AppsApi(api_client)
    app_id = 'app_id_example' # str | app ID
    type = 'type_example' # str | app template type

    try:
        # get an app config template
        api_response = api_instance.get_app_config_template(app_id, type)
        print("The response of AppsApi->get_app_config_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->get_app_config_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| app ID | 
 **type** | **str**| app template type | 

### Return type

[**ServiceAppConfigTemplate**](ServiceAppConfigTemplate.md)

### Authorization

[APIKey](../README.md#APIKey), [OrgID](../README.md#OrgID)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **get_app_configs**
> List[AppAppConfig] get_app_configs(app_id)

get app configs

Returns all configs for the app. 

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_app_config import AppAppConfig
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
    api_instance = nuon.AppsApi(api_client)
    app_id = 'app_id_example' # str | app ID

    try:
        # get app configs
        api_response = api_instance.get_app_configs(app_id)
        print("The response of AppsApi->get_app_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->get_app_configs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| app ID | 

### Return type

[**List[AppAppConfig]**](AppAppConfig.md)

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

# **get_app_input_configs**
> List[AppAppInputConfig] get_app_input_configs(app_id)

get app input configs

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_app_input_config import AppAppInputConfig
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
    api_instance = nuon.AppsApi(api_client)
    app_id = 'app_id_example' # str | app ID

    try:
        # get app input configs
        api_response = api_instance.get_app_input_configs(app_id)
        print("The response of AppsApi->get_app_input_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->get_app_input_configs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| app ID | 

### Return type

[**List[AppAppInputConfig]**](AppAppInputConfig.md)

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

# **get_app_input_latest_config**
> AppAppInputConfig get_app_input_latest_config(app_id)

get latest app input config

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_app_input_config import AppAppInputConfig
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
    api_instance = nuon.AppsApi(api_client)
    app_id = 'app_id_example' # str | app ID

    try:
        # get latest app input config
        api_response = api_instance.get_app_input_latest_config(app_id)
        print("The response of AppsApi->get_app_input_latest_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->get_app_input_latest_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| app ID | 

### Return type

[**AppAppInputConfig**](AppAppInputConfig.md)

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

# **get_app_latest_config**
> AppAppConfig get_app_latest_config(app_id)

get latest app config

Returns the most recent config for the provided app. 

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_app_config import AppAppConfig
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
    api_instance = nuon.AppsApi(api_client)
    app_id = 'app_id_example' # str | app ID

    try:
        # get latest app config
        api_response = api_instance.get_app_latest_config(app_id)
        print("The response of AppsApi->get_app_latest_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->get_app_latest_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| app ID | 

### Return type

[**AppAppConfig**](AppAppConfig.md)

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

# **get_app_runner_configs**
> List[AppAppRunnerConfig] get_app_runner_configs(app_id)

get app runner configs

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_app_runner_config import AppAppRunnerConfig
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
    api_instance = nuon.AppsApi(api_client)
    app_id = 'app_id_example' # str | app ID

    try:
        # get app runner configs
        api_response = api_instance.get_app_runner_configs(app_id)
        print("The response of AppsApi->get_app_runner_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->get_app_runner_configs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| app ID | 

### Return type

[**List[AppAppRunnerConfig]**](AppAppRunnerConfig.md)

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

# **get_app_runner_latest_config**
> AppAppRunnerConfig get_app_runner_latest_config(app_id)

get latest app runner config

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_app_runner_config import AppAppRunnerConfig
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
    api_instance = nuon.AppsApi(api_client)
    app_id = 'app_id_example' # str | app ID

    try:
        # get latest app runner config
        api_response = api_instance.get_app_runner_latest_config(app_id)
        print("The response of AppsApi->get_app_runner_latest_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->get_app_runner_latest_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| app ID | 

### Return type

[**AppAppRunnerConfig**](AppAppRunnerConfig.md)

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

# **get_app_sandbox_configs**
> List[AppAppSandboxConfig] get_app_sandbox_configs(app_id)

get app sandbox configs

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_app_sandbox_config import AppAppSandboxConfig
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
    api_instance = nuon.AppsApi(api_client)
    app_id = 'app_id_example' # str | app ID

    try:
        # get app sandbox configs
        api_response = api_instance.get_app_sandbox_configs(app_id)
        print("The response of AppsApi->get_app_sandbox_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->get_app_sandbox_configs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| app ID | 

### Return type

[**List[AppAppSandboxConfig]**](AppAppSandboxConfig.md)

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

# **get_app_sandbox_latest_config**
> AppAppSandboxConfig get_app_sandbox_latest_config(app_id)

get latest app sandbox config

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_app_sandbox_config import AppAppSandboxConfig
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
    api_instance = nuon.AppsApi(api_client)
    app_id = 'app_id_example' # str | app ID

    try:
        # get latest app sandbox config
        api_response = api_instance.get_app_sandbox_latest_config(app_id)
        print("The response of AppsApi->get_app_sandbox_latest_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->get_app_sandbox_latest_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| app ID | 

### Return type

[**AppAppSandboxConfig**](AppAppSandboxConfig.md)

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

# **get_apps**
> List[AppApp] get_apps()

get all apps for the current org

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_app import AppApp
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
    api_instance = nuon.AppsApi(api_client)

    try:
        # get all apps for the current org
        api_response = api_instance.get_apps()
        print("The response of AppsApi->get_apps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->get_apps: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[AppApp]**](AppApp.md)

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

# **update_app**
> AppApp update_app(app_id, service_update_app_request)

update an app

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_app import AppApp
from nuon.models.service_update_app_request import ServiceUpdateAppRequest
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
    api_instance = nuon.AppsApi(api_client)
    app_id = 'app_id_example' # str | app ID
    service_update_app_request = nuon.ServiceUpdateAppRequest() # ServiceUpdateAppRequest | Input

    try:
        # update an app
        api_response = api_instance.update_app(app_id, service_update_app_request)
        print("The response of AppsApi->update_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->update_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| app ID | 
 **service_update_app_request** | [**ServiceUpdateAppRequest**](ServiceUpdateAppRequest.md)| Input | 

### Return type

[**AppApp**](AppApp.md)

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

