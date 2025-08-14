# nuon.AppsApi

All URIs are relative to *http://localhost:8081*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_app**](AppsApi.md#create_app) | **POST** /v1/apps | create an app
[**create_app_branch**](AppsApi.md#create_app_branch) | **POST** /v1/apps/{app_id}/branches | 
[**create_app_break_glass_config**](AppsApi.md#create_app_break_glass_config) | **POST** /v1/apps/{app_id}/break-glass-configs | 
[**create_app_config**](AppsApi.md#create_app_config) | **POST** /v1/apps/{app_id}/config | 
[**create_app_input_config**](AppsApi.md#create_app_input_config) | **POST** /v1/apps/{app_id}/input-config | 
[**create_app_permissions_config**](AppsApi.md#create_app_permissions_config) | **POST** /v1/apps/{app_id}/permissions-configs | 
[**create_app_policies_config**](AppsApi.md#create_app_policies_config) | **POST** /v1/apps/{app_id}/policies-configs | 
[**create_app_runner_config**](AppsApi.md#create_app_runner_config) | **POST** /v1/apps/{app_id}/runner-configs | create an app runner config
[**create_app_sandbox_config**](AppsApi.md#create_app_sandbox_config) | **POST** /v1/apps/{app_id}/sandbox-config | create an app sandbox config
[**create_app_secret**](AppsApi.md#create_app_secret) | **POST** /v1/apps/{app_id}/secret | create an app secret
[**create_app_secrets_config**](AppsApi.md#create_app_secrets_config) | **POST** /v1/apps/{app_id}/secrets-configs | 
[**create_app_stack_config**](AppsApi.md#create_app_stack_config) | **POST** /v1/apps/{app_id}/stack-configs | create an app stack config
[**delete_app**](AppsApi.md#delete_app) | **DELETE** /v1/apps/{app_id} | delete an app
[**delete_app_secret**](AppsApi.md#delete_app_secret) | **DELETE** /v1/apps/{app_id}/secret/{secret_id} | delete an app secret
[**get_app**](AppsApi.md#get_app) | **GET** /v1/apps/{app_id} | get an app
[**get_app_branch_app_configs**](AppsApi.md#get_app_branch_app_configs) | **GET** /v1/apps/{app_id}/branches/{app_branch_id}/configs | get app branch app configs
[**get_app_branches**](AppsApi.md#get_app_branches) | **GET** /v1/apps/{app_id}/branches | get app branches
[**get_app_break_glass_config**](AppsApi.md#get_app_break_glass_config) | **GET** /v1/apps/{app_id}/break-glass-configs/{break_glass_config_id} | get app break_glass config
[**get_app_config**](AppsApi.md#get_app_config) | **GET** /v1/apps/{app_id}/config/{app_config_id} | get an app config
[**get_app_config_graph**](AppsApi.md#get_app_config_graph) | **GET** /v1/apps/{app_id}/config/{app_config_id}/graph | get an app config graph
[**get_app_config_template**](AppsApi.md#get_app_config_template) | **GET** /v1/apps/{app_id}/template-config | get an app config template
[**get_app_configs**](AppsApi.md#get_app_configs) | **GET** /v1/apps/{app_id}/configs | get app configs
[**get_app_input_config**](AppsApi.md#get_app_input_config) | **GET** /v1/apps/{app_id}/input-configs/{input_config_id} | get app input config
[**get_app_input_configs**](AppsApi.md#get_app_input_configs) | **GET** /v1/apps/{app_id}/input-configs | get app input configs
[**get_app_input_latest_config**](AppsApi.md#get_app_input_latest_config) | **GET** /v1/apps/{app_id}/input-latest-config | get latest app input config
[**get_app_latest_config**](AppsApi.md#get_app_latest_config) | **GET** /v1/apps/{app_id}/latest-config | get latest app config
[**get_app_permissions_config**](AppsApi.md#get_app_permissions_config) | **GET** /v1/apps/{app_id}/permissions-configs/{permissions_config_id} | get app permissions config
[**get_app_policies_config**](AppsApi.md#get_app_policies_config) | **GET** /v1/apps/{app_id}/policies-configs/{policies_config_id} | get app policies config
[**get_app_runner_configs**](AppsApi.md#get_app_runner_configs) | **GET** /v1/apps/{app_id}/runner-configs | get app runner configs
[**get_app_runner_latest_config**](AppsApi.md#get_app_runner_latest_config) | **GET** /v1/apps/{app_id}/runner-latest-config | get latest app runner config
[**get_app_sandbox_configs**](AppsApi.md#get_app_sandbox_configs) | **GET** /v1/apps/{app_id}/sandbox-configs | get app sandbox configs
[**get_app_sandbox_latest_config**](AppsApi.md#get_app_sandbox_latest_config) | **GET** /v1/apps/{app_id}/sandbox-latest-config | get latest app sandbox config
[**get_app_secrets**](AppsApi.md#get_app_secrets) | **GET** /v1/apps/{app_id}/secrets | get app secrets
[**get_app_secrets_config**](AppsApi.md#get_app_secrets_config) | **GET** /v1/apps/{app_id}/secrets-configs/{app_secrets_config_id} | get app secrets config
[**get_app_stack_config**](AppsApi.md#get_app_stack_config) | **GET** /v1/apps/{app_id}/stack-configs/{config_id} | get app stack config
[**get_apps**](AppsApi.md#get_apps) | **GET** /v1/apps | get all apps for the current org
[**get_latest_app_break_glass_config**](AppsApi.md#get_latest_app_break_glass_config) | **GET** /v1/apps/{app_id}/latest-app-break-glass-config | get latest app input config
[**get_latest_app_permissions_config**](AppsApi.md#get_latest_app_permissions_config) | **GET** /v1/apps/{app_id}/latest-app-permissions-config | get latest app permissions config
[**get_latest_app_policies_config**](AppsApi.md#get_latest_app_policies_config) | **GET** /v1/apps/{app_id}/latest-app-policies-config | get latest app policies config
[**get_latest_app_secrets_config**](AppsApi.md#get_latest_app_secrets_config) | **GET** /v1/apps/{app_id}/latest-app-secrets-config | get latest app secrets config
[**update_app**](AppsApi.md#update_app) | **PATCH** /v1/apps/{app_id} | update an app
[**update_app_config**](AppsApi.md#update_app_config) | **PATCH** /v1/apps/{app_id}/config/{app_config_id} | 
[**update_app_config_installs**](AppsApi.md#update_app_config_installs) | **POST** /v1/apps/{app_id}/config/{app_config_id}/update-installs | 


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

# **create_app_branch**
> AppAppBranch create_app_branch(app_id, service_create_app_branch_request)



Cancel a runner job. 

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_app_branch import AppAppBranch
from nuon.models.service_create_app_branch_request import ServiceCreateAppBranchRequest
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
    api_instance = nuon.AppsApi(api_client)
    app_id = 'app_id_example' # str | app ID
    service_create_app_branch_request = nuon.ServiceCreateAppBranchRequest() # ServiceCreateAppBranchRequest | Input

    try:
        api_response = api_instance.create_app_branch(app_id, service_create_app_branch_request)
        print("The response of AppsApi->create_app_branch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->create_app_branch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| app ID | 
 **service_create_app_branch_request** | [**ServiceCreateAppBranchRequest**](ServiceCreateAppBranchRequest.md)| Input | 

### Return type

[**AppAppBranch**](AppAppBranch.md)

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

# **create_app_break_glass_config**
> AppAppBreakGlassConfig create_app_break_glass_config(app_id, service_create_app_break_glass_config_request)



Create a break glass config for an app. 

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_app_break_glass_config import AppAppBreakGlassConfig
from nuon.models.service_create_app_break_glass_config_request import ServiceCreateAppBreakGlassConfigRequest
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
    api_instance = nuon.AppsApi(api_client)
    app_id = 'app_id_example' # str | app ID
    service_create_app_break_glass_config_request = nuon.ServiceCreateAppBreakGlassConfigRequest() # ServiceCreateAppBreakGlassConfigRequest | Input

    try:
        api_response = api_instance.create_app_break_glass_config(app_id, service_create_app_break_glass_config_request)
        print("The response of AppsApi->create_app_break_glass_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->create_app_break_glass_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| app ID | 
 **service_create_app_break_glass_config_request** | [**ServiceCreateAppBreakGlassConfigRequest**](ServiceCreateAppBreakGlassConfigRequest.md)| Input | 

### Return type

[**AppAppBreakGlassConfig**](AppAppBreakGlassConfig.md)

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



App input configs allow you to declare the inputs for your application, and do things such as require customer inputs or  expose configuration knobs in your application. 

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

# **create_app_permissions_config**
> AppAppPermissionsConfig create_app_permissions_config(app_id, service_create_app_permissions_config_request)



Create app permissions config. 

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_app_permissions_config import AppAppPermissionsConfig
from nuon.models.service_create_app_permissions_config_request import ServiceCreateAppPermissionsConfigRequest
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
    api_instance = nuon.AppsApi(api_client)
    app_id = 'app_id_example' # str | app ID
    service_create_app_permissions_config_request = nuon.ServiceCreateAppPermissionsConfigRequest() # ServiceCreateAppPermissionsConfigRequest | Input

    try:
        api_response = api_instance.create_app_permissions_config(app_id, service_create_app_permissions_config_request)
        print("The response of AppsApi->create_app_permissions_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->create_app_permissions_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| app ID | 
 **service_create_app_permissions_config_request** | [**ServiceCreateAppPermissionsConfigRequest**](ServiceCreateAppPermissionsConfigRequest.md)| Input | 

### Return type

[**AppAppPermissionsConfig**](AppAppPermissionsConfig.md)

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

# **create_app_policies_config**
> AppAppPoliciesConfig create_app_policies_config(app_id, service_create_app_policies_config_request)



Create app policies config. 

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_app_policies_config import AppAppPoliciesConfig
from nuon.models.service_create_app_policies_config_request import ServiceCreateAppPoliciesConfigRequest
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
    api_instance = nuon.AppsApi(api_client)
    app_id = 'app_id_example' # str | app ID
    service_create_app_policies_config_request = nuon.ServiceCreateAppPoliciesConfigRequest() # ServiceCreateAppPoliciesConfigRequest | Input

    try:
        api_response = api_instance.create_app_policies_config(app_id, service_create_app_policies_config_request)
        print("The response of AppsApi->create_app_policies_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->create_app_policies_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| app ID | 
 **service_create_app_policies_config_request** | [**ServiceCreateAppPoliciesConfigRequest**](ServiceCreateAppPoliciesConfigRequest.md)| Input | 

### Return type

[**AppAppPoliciesConfig**](AppAppPoliciesConfig.md)

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

# **create_app_secret**
> AppAppSecret create_app_secret(app_id, service_create_app_secret_request)

create an app secret

Create an app secret that can be used to configure components. To reference an app secret, use `.nuon.secrets.<secret_name>`.  **NOTE** secrets can only be written, or deleted, not read. 

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_app_secret import AppAppSecret
from nuon.models.service_create_app_secret_request import ServiceCreateAppSecretRequest
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
    api_instance = nuon.AppsApi(api_client)
    app_id = 'app_id_example' # str | app ID
    service_create_app_secret_request = nuon.ServiceCreateAppSecretRequest() # ServiceCreateAppSecretRequest | Input

    try:
        # create an app secret
        api_response = api_instance.create_app_secret(app_id, service_create_app_secret_request)
        print("The response of AppsApi->create_app_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->create_app_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| app ID | 
 **service_create_app_secret_request** | [**ServiceCreateAppSecretRequest**](ServiceCreateAppSecretRequest.md)| Input | 

### Return type

[**AppAppSecret**](AppAppSecret.md)

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

# **create_app_secrets_config**
> AppAppSecretsConfig create_app_secrets_config(app_id, service_create_app_secrets_config_request)



Create an app secrets config. 

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_app_secrets_config import AppAppSecretsConfig
from nuon.models.service_create_app_secrets_config_request import ServiceCreateAppSecretsConfigRequest
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
    api_instance = nuon.AppsApi(api_client)
    app_id = 'app_id_example' # str | app ID
    service_create_app_secrets_config_request = nuon.ServiceCreateAppSecretsConfigRequest() # ServiceCreateAppSecretsConfigRequest | Input

    try:
        api_response = api_instance.create_app_secrets_config(app_id, service_create_app_secrets_config_request)
        print("The response of AppsApi->create_app_secrets_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->create_app_secrets_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| app ID | 
 **service_create_app_secrets_config_request** | [**ServiceCreateAppSecretsConfigRequest**](ServiceCreateAppSecretsConfigRequest.md)| Input | 

### Return type

[**AppAppSecretsConfig**](AppAppSecretsConfig.md)

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

# **create_app_stack_config**
> AppAppStackConfig create_app_stack_config(app_id, service_create_app_stack_config_request)

create an app stack config

Create a cloudformation stack config 

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_app_stack_config import AppAppStackConfig
from nuon.models.service_create_app_stack_config_request import ServiceCreateAppStackConfigRequest
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
    api_instance = nuon.AppsApi(api_client)
    app_id = 'app_id_example' # str | app ID
    service_create_app_stack_config_request = nuon.ServiceCreateAppStackConfigRequest() # ServiceCreateAppStackConfigRequest | Input

    try:
        # create an app stack config
        api_response = api_instance.create_app_stack_config(app_id, service_create_app_stack_config_request)
        print("The response of AppsApi->create_app_stack_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->create_app_stack_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| app ID | 
 **service_create_app_stack_config_request** | [**ServiceCreateAppStackConfigRequest**](ServiceCreateAppStackConfigRequest.md)| Input | 

### Return type

[**AppAppStackConfig**](AppAppStackConfig.md)

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

# **delete_app_secret**
> bool delete_app_secret(app_id, secret_id)

delete an app secret

Delete an app secret. 

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
    api_instance = nuon.AppsApi(api_client)
    app_id = 'app_id_example' # str | app ID
    secret_id = 'secret_id_example' # str | secret ID

    try:
        # delete an app secret
        api_response = api_instance.delete_app_secret(app_id, secret_id)
        print("The response of AppsApi->delete_app_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->delete_app_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| app ID | 
 **secret_id** | **str**| secret ID | 

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

Return an app. 

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

# **get_app_branch_app_configs**
> List[AppAppConfig] get_app_branch_app_configs(app_id, app_branch_id, offset=offset, limit=limit, page=page, x_nuon_pagination_enabled=x_nuon_pagination_enabled)

get app branch app configs

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
    api_instance = nuon.AppsApi(api_client)
    app_id = 'app_id_example' # str | app ID
    app_branch_id = 'app_branch_id_example' # str | app branch ID
    offset = 0 # int | offset of branches to return (optional) (default to 0)
    limit = 10 # int | limit of branches to return (optional) (default to 10)
    page = 0 # int | page number of results to return (optional) (default to 0)
    x_nuon_pagination_enabled = True # bool | Enable pagination (optional)

    try:
        # get app branch app configs
        api_response = api_instance.get_app_branch_app_configs(app_id, app_branch_id, offset=offset, limit=limit, page=page, x_nuon_pagination_enabled=x_nuon_pagination_enabled)
        print("The response of AppsApi->get_app_branch_app_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->get_app_branch_app_configs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| app ID | 
 **app_branch_id** | **str**| app branch ID | 
 **offset** | **int**| offset of branches to return | [optional] [default to 0]
 **limit** | **int**| limit of branches to return | [optional] [default to 10]
 **page** | **int**| page number of results to return | [optional] [default to 0]
 **x_nuon_pagination_enabled** | **bool**| Enable pagination | [optional] 

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

# **get_app_branches**
> List[AppAppBranch] get_app_branches(app_id, offset=offset, limit=limit, page=page, x_nuon_pagination_enabled=x_nuon_pagination_enabled)

get app branches

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_app_branch import AppAppBranch
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
    api_instance = nuon.AppsApi(api_client)
    app_id = 'app_id_example' # str | app ID
    offset = 0 # int | offset of branches to return (optional) (default to 0)
    limit = 10 # int | limit of branches to return (optional) (default to 10)
    page = 0 # int | page number of results to return (optional) (default to 0)
    x_nuon_pagination_enabled = True # bool | Enable pagination (optional)

    try:
        # get app branches
        api_response = api_instance.get_app_branches(app_id, offset=offset, limit=limit, page=page, x_nuon_pagination_enabled=x_nuon_pagination_enabled)
        print("The response of AppsApi->get_app_branches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->get_app_branches: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| app ID | 
 **offset** | **int**| offset of branches to return | [optional] [default to 0]
 **limit** | **int**| limit of branches to return | [optional] [default to 10]
 **page** | **int**| page number of results to return | [optional] [default to 0]
 **x_nuon_pagination_enabled** | **bool**| Enable pagination | [optional] 

### Return type

[**List[AppAppBranch]**](AppAppBranch.md)

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

# **get_app_break_glass_config**
> AppAppBreakGlassConfig get_app_break_glass_config(app_id, break_glass_config_id)

get app break_glass config

Return an app break glass config by id. 

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_app_break_glass_config import AppAppBreakGlassConfig
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
    api_instance = nuon.AppsApi(api_client)
    app_id = 'app_id_example' # str | app ID
    break_glass_config_id = 'break_glass_config_id_example' # str | app break glass config ID

    try:
        # get app break_glass config
        api_response = api_instance.get_app_break_glass_config(app_id, break_glass_config_id)
        print("The response of AppsApi->get_app_break_glass_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->get_app_break_glass_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| app ID | 
 **break_glass_config_id** | **str**| app break glass config ID | 

### Return type

[**AppAppBreakGlassConfig**](AppAppBreakGlassConfig.md)

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

# **get_app_config**
> AppAppConfig get_app_config(app_id, app_config_id, recurse=recurse)

get an app config

Fetch an app config by id. 

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
    api_instance = nuon.AppsApi(api_client)
    app_id = 'app_id_example' # str | app ID
    app_config_id = 'app_config_id_example' # str | app config ID
    recurse = False # bool | load all children configs (optional) (default to False)

    try:
        # get an app config
        api_response = api_instance.get_app_config(app_id, app_config_id, recurse=recurse)
        print("The response of AppsApi->get_app_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->get_app_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| app ID | 
 **app_config_id** | **str**| app config ID | 
 **recurse** | **bool**| load all children configs | [optional] [default to False]

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

# **get_app_config_graph**
> str get_app_config_graph(app_id, app_config_id)

get an app config graph

Return raw graphviz data as a string that can be used to visualize a graph for an app.  Note, for more complex viewing recommend to copy this output directly into [Graphviz viewer](https://dreampuf.github.io/GraphvizOnline). 

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
    api_instance = nuon.AppsApi(api_client)
    app_id = 'app_id_example' # str | app ID
    app_config_id = 'app_config_id_example' # str | app config ID

    try:
        # get an app config graph
        api_response = api_instance.get_app_config_graph(app_id, app_config_id)
        print("The response of AppsApi->get_app_config_graph:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->get_app_config_graph: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| app ID | 
 **app_config_id** | **str**| app config ID | 

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
> List[AppAppConfig] get_app_configs(app_id, offset=offset, limit=limit, page=page, x_nuon_pagination_enabled=x_nuon_pagination_enabled)

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
    api_instance = nuon.AppsApi(api_client)
    app_id = 'app_id_example' # str | app ID
    offset = 0 # int | offset of jobs to return (optional) (default to 0)
    limit = 10 # int | limit of jobs to return (optional) (default to 10)
    page = 0 # int | page number of results to return (optional) (default to 0)
    x_nuon_pagination_enabled = True # bool | Enable pagination (optional)

    try:
        # get app configs
        api_response = api_instance.get_app_configs(app_id, offset=offset, limit=limit, page=page, x_nuon_pagination_enabled=x_nuon_pagination_enabled)
        print("The response of AppsApi->get_app_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->get_app_configs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| app ID | 
 **offset** | **int**| offset of jobs to return | [optional] [default to 0]
 **limit** | **int**| limit of jobs to return | [optional] [default to 10]
 **page** | **int**| page number of results to return | [optional] [default to 0]
 **x_nuon_pagination_enabled** | **bool**| Enable pagination | [optional] 

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

# **get_app_input_config**
> AppAppInputConfig get_app_input_config(app_id, input_config_id)

get app input config

Return an input config by id. 

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
    api_instance = nuon.AppsApi(api_client)
    app_id = 'app_id_example' # str | app ID
    input_config_id = 'input_config_id_example' # str | input config ID

    try:
        # get app input config
        api_response = api_instance.get_app_input_config(app_id, input_config_id)
        print("The response of AppsApi->get_app_input_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->get_app_input_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| app ID | 
 **input_config_id** | **str**| input config ID | 

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

# **get_app_input_configs**
> List[AppAppInputConfig] get_app_input_configs(app_id, offset=offset, limit=limit, page=page, x_nuon_pagination_enabled=x_nuon_pagination_enabled)

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
    api_instance = nuon.AppsApi(api_client)
    app_id = 'app_id_example' # str | app ID
    offset = 0 # int | offset of jobs to return (optional) (default to 0)
    limit = 10 # int | limit of jobs to return (optional) (default to 10)
    page = 0 # int | page number of results to return (optional) (default to 0)
    x_nuon_pagination_enabled = True # bool | Enable pagination (optional)

    try:
        # get app input configs
        api_response = api_instance.get_app_input_configs(app_id, offset=offset, limit=limit, page=page, x_nuon_pagination_enabled=x_nuon_pagination_enabled)
        print("The response of AppsApi->get_app_input_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->get_app_input_configs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| app ID | 
 **offset** | **int**| offset of jobs to return | [optional] [default to 0]
 **limit** | **int**| limit of jobs to return | [optional] [default to 10]
 **page** | **int**| page number of results to return | [optional] [default to 0]
 **x_nuon_pagination_enabled** | **bool**| Enable pagination | [optional] 

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
> AppAppConfig get_app_latest_config(app_id, recurse=recurse)

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
    api_instance = nuon.AppsApi(api_client)
    app_id = 'app_id_example' # str | app ID
    recurse = False # bool | load all children configs (optional) (default to False)

    try:
        # get latest app config
        api_response = api_instance.get_app_latest_config(app_id, recurse=recurse)
        print("The response of AppsApi->get_app_latest_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->get_app_latest_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| app ID | 
 **recurse** | **bool**| load all children configs | [optional] [default to False]

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

# **get_app_permissions_config**
> AppAppPermissionsConfig get_app_permissions_config(app_id, permissions_config_id)

get app permissions config

Return an app permissions config by id. 

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_app_permissions_config import AppAppPermissionsConfig
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
    api_instance = nuon.AppsApi(api_client)
    app_id = 'app_id_example' # str | app ID
    permissions_config_id = 'permissions_config_id_example' # str | input config ID

    try:
        # get app permissions config
        api_response = api_instance.get_app_permissions_config(app_id, permissions_config_id)
        print("The response of AppsApi->get_app_permissions_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->get_app_permissions_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| app ID | 
 **permissions_config_id** | **str**| input config ID | 

### Return type

[**AppAppPermissionsConfig**](AppAppPermissionsConfig.md)

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

# **get_app_policies_config**
> AppAppPoliciesConfig get_app_policies_config(app_id, policies_config_id)

get app policies config

Return an app policy config by id. 

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_app_policies_config import AppAppPoliciesConfig
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
    api_instance = nuon.AppsApi(api_client)
    app_id = 'app_id_example' # str | app ID
    policies_config_id = 'policies_config_id_example' # str | input policies config ID

    try:
        # get app policies config
        api_response = api_instance.get_app_policies_config(app_id, policies_config_id)
        print("The response of AppsApi->get_app_policies_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->get_app_policies_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| app ID | 
 **policies_config_id** | **str**| input policies config ID | 

### Return type

[**AppAppPoliciesConfig**](AppAppPoliciesConfig.md)

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
> List[AppAppRunnerConfig] get_app_runner_configs(app_id, offset=offset, limit=limit, page=page, x_nuon_pagination_enabled=x_nuon_pagination_enabled)

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
    api_instance = nuon.AppsApi(api_client)
    app_id = 'app_id_example' # str | app ID
    offset = 0 # int | offset of jobs to return (optional) (default to 0)
    limit = 10 # int | limit of jobs to return (optional) (default to 10)
    page = 0 # int | page number of results to return (optional) (default to 0)
    x_nuon_pagination_enabled = True # bool | Enable pagination (optional)

    try:
        # get app runner configs
        api_response = api_instance.get_app_runner_configs(app_id, offset=offset, limit=limit, page=page, x_nuon_pagination_enabled=x_nuon_pagination_enabled)
        print("The response of AppsApi->get_app_runner_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->get_app_runner_configs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| app ID | 
 **offset** | **int**| offset of jobs to return | [optional] [default to 0]
 **limit** | **int**| limit of jobs to return | [optional] [default to 10]
 **page** | **int**| page number of results to return | [optional] [default to 0]
 **x_nuon_pagination_enabled** | **bool**| Enable pagination | [optional] 

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
> List[AppAppSandboxConfig] get_app_sandbox_configs(app_id, offset=offset, limit=limit, page=page, x_nuon_pagination_enabled=x_nuon_pagination_enabled)

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
    api_instance = nuon.AppsApi(api_client)
    app_id = 'app_id_example' # str | app ID
    offset = 0 # int | offset of jobs to return (optional) (default to 0)
    limit = 10 # int | limit of jobs to return (optional) (default to 10)
    page = 0 # int | page number of results to return (optional) (default to 0)
    x_nuon_pagination_enabled = True # bool | Enable pagination (optional)

    try:
        # get app sandbox configs
        api_response = api_instance.get_app_sandbox_configs(app_id, offset=offset, limit=limit, page=page, x_nuon_pagination_enabled=x_nuon_pagination_enabled)
        print("The response of AppsApi->get_app_sandbox_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->get_app_sandbox_configs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| app ID | 
 **offset** | **int**| offset of jobs to return | [optional] [default to 0]
 **limit** | **int**| limit of jobs to return | [optional] [default to 10]
 **page** | **int**| page number of results to return | [optional] [default to 0]
 **x_nuon_pagination_enabled** | **bool**| Enable pagination | [optional] 

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

# **get_app_secrets**
> List[AppAppSecret] get_app_secrets(app_id, offset=offset, limit=limit, page=page, x_nuon_pagination_enabled=x_nuon_pagination_enabled)

get app secrets

List all secrets for an app.  **NOTE** this does not return any sensitive values, as secrets are write only. 

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_app_secret import AppAppSecret
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
    api_instance = nuon.AppsApi(api_client)
    app_id = 'app_id_example' # str | app ID
    offset = 0 # int | offset of jobs to return (optional) (default to 0)
    limit = 10 # int | limit of jobs to return (optional) (default to 10)
    page = 0 # int | page number of results to return (optional) (default to 0)
    x_nuon_pagination_enabled = True # bool | Enable pagination (optional)

    try:
        # get app secrets
        api_response = api_instance.get_app_secrets(app_id, offset=offset, limit=limit, page=page, x_nuon_pagination_enabled=x_nuon_pagination_enabled)
        print("The response of AppsApi->get_app_secrets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->get_app_secrets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| app ID | 
 **offset** | **int**| offset of jobs to return | [optional] [default to 0]
 **limit** | **int**| limit of jobs to return | [optional] [default to 10]
 **page** | **int**| page number of results to return | [optional] [default to 0]
 **x_nuon_pagination_enabled** | **bool**| Enable pagination | [optional] 

### Return type

[**List[AppAppSecret]**](AppAppSecret.md)

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

# **get_app_secrets_config**
> AppAppSecretsConfig get_app_secrets_config(app_id, app_secrets_config_id)

get app secrets config

Return an app secrets config by id. 

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_app_secrets_config import AppAppSecretsConfig
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
    api_instance = nuon.AppsApi(api_client)
    app_id = 'app_id_example' # str | app ID
    app_secrets_config_id = 'app_secrets_config_id_example' # str | app secrets config ID

    try:
        # get app secrets config
        api_response = api_instance.get_app_secrets_config(app_id, app_secrets_config_id)
        print("The response of AppsApi->get_app_secrets_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->get_app_secrets_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| app ID | 
 **app_secrets_config_id** | **str**| app secrets config ID | 

### Return type

[**AppAppSecretsConfig**](AppAppSecretsConfig.md)

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

# **get_app_stack_config**
> AppAppStackConfig get_app_stack_config(app_id, config_id)

get app stack config

Return a cloudformation stack config 

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_app_stack_config import AppAppStackConfig
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
    api_instance = nuon.AppsApi(api_client)
    app_id = 'app_id_example' # str | app ID
    config_id = 'config_id_example' # str | app stack config ID

    try:
        # get app stack config
        api_response = api_instance.get_app_stack_config(app_id, config_id)
        print("The response of AppsApi->get_app_stack_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->get_app_stack_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| app ID | 
 **config_id** | **str**| app stack config ID | 

### Return type

[**AppAppStackConfig**](AppAppStackConfig.md)

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
> List[AppApp] get_apps(offset=offset, q=q, limit=limit, page=page, x_nuon_pagination_enabled=x_nuon_pagination_enabled)

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
    api_instance = nuon.AppsApi(api_client)
    offset = 0 # int | offset of jobs to return (optional) (default to 0)
    q = 'q_example' # str | search query to filter apps by name (optional)
    limit = 10 # int | limit of jobs to return (optional) (default to 10)
    page = 0 # int | page number of results to return (optional) (default to 0)
    x_nuon_pagination_enabled = True # bool | Enable pagination (optional)

    try:
        # get all apps for the current org
        api_response = api_instance.get_apps(offset=offset, q=q, limit=limit, page=page, x_nuon_pagination_enabled=x_nuon_pagination_enabled)
        print("The response of AppsApi->get_apps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->get_apps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| offset of jobs to return | [optional] [default to 0]
 **q** | **str**| search query to filter apps by name | [optional] 
 **limit** | **int**| limit of jobs to return | [optional] [default to 10]
 **page** | **int**| page number of results to return | [optional] [default to 0]
 **x_nuon_pagination_enabled** | **bool**| Enable pagination | [optional] 

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

# **get_latest_app_break_glass_config**
> AppAppBreakGlassConfig get_latest_app_break_glass_config(app_id)

get latest app input config

Get the latest break glass config for an app. 

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_app_break_glass_config import AppAppBreakGlassConfig
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
    api_instance = nuon.AppsApi(api_client)
    app_id = 'app_id_example' # str | app ID

    try:
        # get latest app input config
        api_response = api_instance.get_latest_app_break_glass_config(app_id)
        print("The response of AppsApi->get_latest_app_break_glass_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->get_latest_app_break_glass_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| app ID | 

### Return type

[**AppAppBreakGlassConfig**](AppAppBreakGlassConfig.md)

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

# **get_latest_app_permissions_config**
> AppAppPermissionsConfig get_latest_app_permissions_config(app_id)

get latest app permissions config

Get the latest app permissions config. 

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_app_permissions_config import AppAppPermissionsConfig
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
    api_instance = nuon.AppsApi(api_client)
    app_id = 'app_id_example' # str | app ID

    try:
        # get latest app permissions config
        api_response = api_instance.get_latest_app_permissions_config(app_id)
        print("The response of AppsApi->get_latest_app_permissions_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->get_latest_app_permissions_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| app ID | 

### Return type

[**AppAppPermissionsConfig**](AppAppPermissionsConfig.md)

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

# **get_latest_app_policies_config**
> AppAppPoliciesConfig get_latest_app_policies_config(app_id)

get latest app policies config

Get latest app policies config. 

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_app_policies_config import AppAppPoliciesConfig
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
    api_instance = nuon.AppsApi(api_client)
    app_id = 'app_id_example' # str | app ID

    try:
        # get latest app policies config
        api_response = api_instance.get_latest_app_policies_config(app_id)
        print("The response of AppsApi->get_latest_app_policies_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->get_latest_app_policies_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| app ID | 

### Return type

[**AppAppPoliciesConfig**](AppAppPoliciesConfig.md)

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

# **get_latest_app_secrets_config**
> AppAppSecretsConfig get_latest_app_secrets_config(app_id)

get latest app secrets config

Get the latest app secrets config. 

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_app_secrets_config import AppAppSecretsConfig
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
    api_instance = nuon.AppsApi(api_client)
    app_id = 'app_id_example' # str | app ID

    try:
        # get latest app secrets config
        api_response = api_instance.get_latest_app_secrets_config(app_id)
        print("The response of AppsApi->get_latest_app_secrets_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->get_latest_app_secrets_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| app ID | 

### Return type

[**AppAppSecretsConfig**](AppAppSecretsConfig.md)

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

# **update_app_config**
> AppAppConfig update_app_config(app_id, app_config_id, service_update_app_config_request)



Update an app config, setting status and state. 

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_app_config import AppAppConfig
from nuon.models.service_update_app_config_request import ServiceUpdateAppConfigRequest
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
    api_instance = nuon.AppsApi(api_client)
    app_id = 'app_id_example' # str | app ID
    app_config_id = 'app_config_id_example' # str | app config ID
    service_update_app_config_request = nuon.ServiceUpdateAppConfigRequest() # ServiceUpdateAppConfigRequest | Input

    try:
        api_response = api_instance.update_app_config(app_id, app_config_id, service_update_app_config_request)
        print("The response of AppsApi->update_app_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->update_app_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| app ID | 
 **app_config_id** | **str**| app config ID | 
 **service_update_app_config_request** | [**ServiceUpdateAppConfigRequest**](ServiceUpdateAppConfigRequest.md)| Input | 

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

# **update_app_config_installs**
> str update_app_config_installs(app_id, app_config_id, service_update_app_config_installs_request)



### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.service_update_app_config_installs_request import ServiceUpdateAppConfigInstallsRequest
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
    api_instance = nuon.AppsApi(api_client)
    app_id = 'app_id_example' # str | app ID
    app_config_id = 'app_config_id_example' # str | app config ID
    service_update_app_config_installs_request = nuon.ServiceUpdateAppConfigInstallsRequest() # ServiceUpdateAppConfigInstallsRequest | Input

    try:
        api_response = api_instance.update_app_config_installs(app_id, app_config_id, service_update_app_config_installs_request)
        print("The response of AppsApi->update_app_config_installs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->update_app_config_installs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| app ID | 
 **app_config_id** | **str**| app config ID | 
 **service_update_app_config_installs_request** | [**ServiceUpdateAppConfigInstallsRequest**](ServiceUpdateAppConfigInstallsRequest.md)| Input | 

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
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

