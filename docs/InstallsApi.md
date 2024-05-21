# nuon.InstallsApi

All URIs are relative to *https://api.nuon.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_install**](InstallsApi.md#create_install) | **POST** /v1/apps/{app_id}/installs | create an app install
[**create_install_deploy**](InstallsApi.md#create_install_deploy) | **POST** /v1/installs/{install_id}/deploys | deploy a build to an install
[**create_install_inputs**](InstallsApi.md#create_install_inputs) | **POST** /v1/installs/{install_id}/inputs | create install inputs
[**delete_install**](InstallsApi.md#delete_install) | **DELETE** /v1/installs/{install_id} | delete an install
[**deprovision_install**](InstallsApi.md#deprovision_install) | **POST** /v1/installs/{install_id}/deprovision | deprovision an install
[**get_app_installs**](InstallsApi.md#get_app_installs) | **GET** /v1/apps/{app_id}/installs | get all installs for an app
[**get_current_install_inputs**](InstallsApi.md#get_current_install_inputs) | **GET** /v1/installs/{install_id}/inputs/current | get an installs current inputs
[**get_install**](InstallsApi.md#get_install) | **GET** /v1/installs/{install_id} | get an install
[**get_install_component**](InstallsApi.md#get_install_component) | **GET** /v1/installs/{install_id}/component/{component_id} | get an install component
[**get_install_component_deploys**](InstallsApi.md#get_install_component_deploys) | **GET** /v1/installs/{install_id}/components/{component_id}/deploys | get an install components deploys
[**get_install_component_latest_deploy**](InstallsApi.md#get_install_component_latest_deploy) | **GET** /v1/installs/{install_id}/components/{component_id}/deploys/latest | get the latest deploy for an install component
[**get_install_components**](InstallsApi.md#get_install_components) | **GET** /v1/installs/{install_id}/components | get an installs components
[**get_install_deploy**](InstallsApi.md#get_install_deploy) | **GET** /v1/installs/{install_id}/deploys/{deploy_id} | get an install deploy
[**get_install_deploy_logs**](InstallsApi.md#get_install_deploy_logs) | **GET** /v1/installs/{install_id}/deploys/{deploy_id}/logs | get install deploy logs
[**get_install_deploy_plan**](InstallsApi.md#get_install_deploy_plan) | **GET** /v1/installs/{install_id}/deploys/{deploy_id}/plan | get install deploy plan
[**get_install_deploys**](InstallsApi.md#get_install_deploys) | **GET** /v1/installs/{install_id}/deploys | get all deploys to an install
[**get_install_event**](InstallsApi.md#get_install_event) | **GET** /v1/installs/{install_id}/events/{event_id} | get an install event
[**get_install_events**](InstallsApi.md#get_install_events) | **GET** /v1/installs/{install_id}/events | get events for an install
[**get_install_inputs**](InstallsApi.md#get_install_inputs) | **GET** /v1/installs/{install_id}/inputs | get an installs inputs
[**get_install_latest_deploy**](InstallsApi.md#get_install_latest_deploy) | **GET** /v1/installs/{install_id}/deploys/latest | get an install deploy
[**get_install_sandbox_run_logs**](InstallsApi.md#get_install_sandbox_run_logs) | **GET** /v1/installs/{install_id}/sandbox-run/{run_id}/logs | get install sandbox run logs
[**get_install_sandbox_runs**](InstallsApi.md#get_install_sandbox_runs) | **GET** /v1/installs/{install_id}/sandbox-runs | get an installs sandbox runs
[**get_org_installs**](InstallsApi.md#get_org_installs) | **GET** /v1/installs | get all installs for an org
[**reprovision_install**](InstallsApi.md#reprovision_install) | **POST** /v1/installs/{install_id}/reprovision | reprovision an install
[**teardown_install_component**](InstallsApi.md#teardown_install_component) | **POST** /v1/installs/{install_id}/components/{component_id}/teardown | teardown an install component
[**teardown_install_components**](InstallsApi.md#teardown_install_components) | **POST** /v1/installs/{install_id}/components/teardown-all | teardown an install&#39;s components
[**update_install**](InstallsApi.md#update_install) | **PATCH** /v1/installs/{install_id} | update an install


# **create_install**
> AppInstall create_install(app_id, service_create_install_request)

create an app install

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_install import AppInstall
from nuon.models.service_create_install_request import ServiceCreateInstallRequest
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
    api_instance = nuon.InstallsApi(api_client)
    app_id = 'app_id_example' # str | app ID
    service_create_install_request = nuon.ServiceCreateInstallRequest() # ServiceCreateInstallRequest | Input

    try:
        # create an app install
        api_response = api_instance.create_install(app_id, service_create_install_request)
        print("The response of InstallsApi->create_install:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->create_install: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| app ID | 
 **service_create_install_request** | [**ServiceCreateInstallRequest**](ServiceCreateInstallRequest.md)| Input | 

### Return type

[**AppInstall**](AppInstall.md)

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

# **create_install_deploy**
> AppInstallDeploy create_install_deploy(install_id, service_create_install_deploy_request)

deploy a build to an install

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_install_deploy import AppInstallDeploy
from nuon.models.service_create_install_deploy_request import ServiceCreateInstallDeployRequest
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
    api_instance = nuon.InstallsApi(api_client)
    install_id = 'install_id_example' # str | install ID
    service_create_install_deploy_request = nuon.ServiceCreateInstallDeployRequest() # ServiceCreateInstallDeployRequest | Input

    try:
        # deploy a build to an install
        api_response = api_instance.create_install_deploy(install_id, service_create_install_deploy_request)
        print("The response of InstallsApi->create_install_deploy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->create_install_deploy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **str**| install ID | 
 **service_create_install_deploy_request** | [**ServiceCreateInstallDeployRequest**](ServiceCreateInstallDeployRequest.md)| Input | 

### Return type

[**AppInstallDeploy**](AppInstallDeploy.md)

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

# **create_install_inputs**
> AppInstallInputs create_install_inputs(install_id, service_create_install_inputs_request)

create install inputs

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_install_inputs import AppInstallInputs
from nuon.models.service_create_install_inputs_request import ServiceCreateInstallInputsRequest
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
    api_instance = nuon.InstallsApi(api_client)
    install_id = 'install_id_example' # str | install ID
    service_create_install_inputs_request = nuon.ServiceCreateInstallInputsRequest() # ServiceCreateInstallInputsRequest | Input

    try:
        # create install inputs
        api_response = api_instance.create_install_inputs(install_id, service_create_install_inputs_request)
        print("The response of InstallsApi->create_install_inputs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->create_install_inputs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **str**| install ID | 
 **service_create_install_inputs_request** | [**ServiceCreateInstallInputsRequest**](ServiceCreateInstallInputsRequest.md)| Input | 

### Return type

[**AppInstallInputs**](AppInstallInputs.md)

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

# **delete_install**
> bool delete_install(install_id)

delete an install

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
    api_instance = nuon.InstallsApi(api_client)
    install_id = 'install_id_example' # str | install ID

    try:
        # delete an install
        api_response = api_instance.delete_install(install_id)
        print("The response of InstallsApi->delete_install:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->delete_install: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **str**| install ID | 

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

# **deprovision_install**
> str deprovision_install(install_id, body)

deprovision an install

Deprovision an install sandbox. 

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
    api_instance = nuon.InstallsApi(api_client)
    install_id = 'install_id_example' # str | install ID
    body = None # object | Input

    try:
        # deprovision an install
        api_response = api_instance.deprovision_install(install_id, body)
        print("The response of InstallsApi->deprovision_install:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->deprovision_install: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **str**| install ID | 
 **body** | **object**| Input | 

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
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_installs**
> List[AppInstall] get_app_installs(app_id)

get all installs for an app

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_install import AppInstall
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
    api_instance = nuon.InstallsApi(api_client)
    app_id = 'app_id_example' # str | app ID

    try:
        # get all installs for an app
        api_response = api_instance.get_app_installs(app_id)
        print("The response of InstallsApi->get_app_installs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->get_app_installs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| app ID | 

### Return type

[**List[AppInstall]**](AppInstall.md)

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

# **get_current_install_inputs**
> AppInstallInputs get_current_install_inputs(install_id)

get an installs current inputs

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_install_inputs import AppInstallInputs
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
    api_instance = nuon.InstallsApi(api_client)
    install_id = 'install_id_example' # str | install ID

    try:
        # get an installs current inputs
        api_response = api_instance.get_current_install_inputs(install_id)
        print("The response of InstallsApi->get_current_install_inputs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->get_current_install_inputs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **str**| install ID | 

### Return type

[**AppInstallInputs**](AppInstallInputs.md)

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

# **get_install**
> AppInstall get_install(install_id)

get an install

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_install import AppInstall
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
    api_instance = nuon.InstallsApi(api_client)
    install_id = 'install_id_example' # str | install ID

    try:
        # get an install
        api_response = api_instance.get_install(install_id)
        print("The response of InstallsApi->get_install:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->get_install: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **str**| install ID | 

### Return type

[**AppInstall**](AppInstall.md)

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

# **get_install_component**
> AppInstallComponent get_install_component(install_id, component_id)

get an install component

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_install_component import AppInstallComponent
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
    api_instance = nuon.InstallsApi(api_client)
    install_id = 'install_id_example' # str | install ID
    component_id = 'component_id_example' # str | component ID

    try:
        # get an install component
        api_response = api_instance.get_install_component(install_id, component_id)
        print("The response of InstallsApi->get_install_component:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->get_install_component: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **str**| install ID | 
 **component_id** | **str**| component ID | 

### Return type

[**AppInstallComponent**](AppInstallComponent.md)

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

# **get_install_component_deploys**
> List[AppInstallDeploy] get_install_component_deploys(install_id, component_id)

get an install components deploys

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_install_deploy import AppInstallDeploy
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
    api_instance = nuon.InstallsApi(api_client)
    install_id = 'install_id_example' # str | install ID
    component_id = 'component_id_example' # str | component ID

    try:
        # get an install components deploys
        api_response = api_instance.get_install_component_deploys(install_id, component_id)
        print("The response of InstallsApi->get_install_component_deploys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->get_install_component_deploys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **str**| install ID | 
 **component_id** | **str**| component ID | 

### Return type

[**List[AppInstallDeploy]**](AppInstallDeploy.md)

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

# **get_install_component_latest_deploy**
> AppInstallDeploy get_install_component_latest_deploy(install_id, component_id)

get the latest deploy for an install component

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_install_deploy import AppInstallDeploy
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
    api_instance = nuon.InstallsApi(api_client)
    install_id = 'install_id_example' # str | install ID
    component_id = 'component_id_example' # str | component ID

    try:
        # get the latest deploy for an install component
        api_response = api_instance.get_install_component_latest_deploy(install_id, component_id)
        print("The response of InstallsApi->get_install_component_latest_deploy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->get_install_component_latest_deploy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **str**| install ID | 
 **component_id** | **str**| component ID | 

### Return type

[**AppInstallDeploy**](AppInstallDeploy.md)

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

# **get_install_components**
> List[AppInstallComponent] get_install_components(install_id)

get an installs components

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_install_component import AppInstallComponent
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
    api_instance = nuon.InstallsApi(api_client)
    install_id = 'install_id_example' # str | install ID

    try:
        # get an installs components
        api_response = api_instance.get_install_components(install_id)
        print("The response of InstallsApi->get_install_components:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->get_install_components: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **str**| install ID | 

### Return type

[**List[AppInstallComponent]**](AppInstallComponent.md)

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

# **get_install_deploy**
> AppInstallDeploy get_install_deploy(install_id, deploy_id)

get an install deploy

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_install_deploy import AppInstallDeploy
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
    api_instance = nuon.InstallsApi(api_client)
    install_id = 'install_id_example' # str | install ID
    deploy_id = 'deploy_id_example' # str | deploy ID

    try:
        # get an install deploy
        api_response = api_instance.get_install_deploy(install_id, deploy_id)
        print("The response of InstallsApi->get_install_deploy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->get_install_deploy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **str**| install ID | 
 **deploy_id** | **str**| deploy ID | 

### Return type

[**AppInstallDeploy**](AppInstallDeploy.md)

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

# **get_install_deploy_logs**
> List[object] get_install_deploy_logs(install_id, deploy_id)

get install deploy logs

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
    api_instance = nuon.InstallsApi(api_client)
    install_id = 'install_id_example' # str | install ID
    deploy_id = 'deploy_id_example' # str | deploy ID

    try:
        # get install deploy logs
        api_response = api_instance.get_install_deploy_logs(install_id, deploy_id)
        print("The response of InstallsApi->get_install_deploy_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->get_install_deploy_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **str**| install ID | 
 **deploy_id** | **str**| deploy ID | 

### Return type

**List[object]**

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

# **get_install_deploy_plan**
> Planv1Plan get_install_deploy_plan(install_id, deploy_id)

get install deploy plan

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.planv1_plan import Planv1Plan
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
    api_instance = nuon.InstallsApi(api_client)
    install_id = 'install_id_example' # str | install ID
    deploy_id = 'deploy_id_example' # str | deploy ID

    try:
        # get install deploy plan
        api_response = api_instance.get_install_deploy_plan(install_id, deploy_id)
        print("The response of InstallsApi->get_install_deploy_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->get_install_deploy_plan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **str**| install ID | 
 **deploy_id** | **str**| deploy ID | 

### Return type

[**Planv1Plan**](Planv1Plan.md)

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

# **get_install_deploys**
> List[AppInstallDeploy] get_install_deploys(install_id)

get all deploys to an install

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_install_deploy import AppInstallDeploy
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
    api_instance = nuon.InstallsApi(api_client)
    install_id = 'install_id_example' # str | install ID

    try:
        # get all deploys to an install
        api_response = api_instance.get_install_deploys(install_id)
        print("The response of InstallsApi->get_install_deploys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->get_install_deploys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **str**| install ID | 

### Return type

[**List[AppInstallDeploy]**](AppInstallDeploy.md)

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

# **get_install_event**
> AppInstallEvent get_install_event(install_id, event_id)

get an install event

Get a single install event. 

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_install_event import AppInstallEvent
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
    api_instance = nuon.InstallsApi(api_client)
    install_id = 'install_id_example' # str | install ID
    event_id = 'event_id_example' # str | event ID

    try:
        # get an install event
        api_response = api_instance.get_install_event(install_id, event_id)
        print("The response of InstallsApi->get_install_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->get_install_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **str**| install ID | 
 **event_id** | **str**| event ID | 

### Return type

[**AppInstallEvent**](AppInstallEvent.md)

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

# **get_install_events**
> List[AppInstallEvent] get_install_events(install_id)

get events for an install

# Get Install Events  Return an event stream for an install. 

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_install_event import AppInstallEvent
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
    api_instance = nuon.InstallsApi(api_client)
    install_id = 'install_id_example' # str | install ID

    try:
        # get events for an install
        api_response = api_instance.get_install_events(install_id)
        print("The response of InstallsApi->get_install_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->get_install_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **str**| install ID | 

### Return type

[**List[AppInstallEvent]**](AppInstallEvent.md)

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

# **get_install_inputs**
> List[AppInstallInputs] get_install_inputs(install_id)

get an installs inputs

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_install_inputs import AppInstallInputs
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
    api_instance = nuon.InstallsApi(api_client)
    install_id = 'install_id_example' # str | install ID

    try:
        # get an installs inputs
        api_response = api_instance.get_install_inputs(install_id)
        print("The response of InstallsApi->get_install_inputs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->get_install_inputs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **str**| install ID | 

### Return type

[**List[AppInstallInputs]**](AppInstallInputs.md)

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

# **get_install_latest_deploy**
> AppInstallDeploy get_install_latest_deploy(install_id)

get an install deploy

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_install_deploy import AppInstallDeploy
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
    api_instance = nuon.InstallsApi(api_client)
    install_id = 'install_id_example' # str | install ID

    try:
        # get an install deploy
        api_response = api_instance.get_install_latest_deploy(install_id)
        print("The response of InstallsApi->get_install_latest_deploy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->get_install_latest_deploy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **str**| install ID | 

### Return type

[**AppInstallDeploy**](AppInstallDeploy.md)

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

# **get_install_sandbox_run_logs**
> List[object] get_install_sandbox_run_logs(install_id, run_id)

get install sandbox run logs

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
    api_instance = nuon.InstallsApi(api_client)
    install_id = 'install_id_example' # str | install ID
    run_id = 'run_id_example' # str | run ID

    try:
        # get install sandbox run logs
        api_response = api_instance.get_install_sandbox_run_logs(install_id, run_id)
        print("The response of InstallsApi->get_install_sandbox_run_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->get_install_sandbox_run_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **str**| install ID | 
 **run_id** | **str**| run ID | 

### Return type

**List[object]**

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

# **get_install_sandbox_runs**
> List[AppInstallSandboxRun] get_install_sandbox_runs(install_id)

get an installs sandbox runs

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_install_sandbox_run import AppInstallSandboxRun
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
    api_instance = nuon.InstallsApi(api_client)
    install_id = 'install_id_example' # str | install ID

    try:
        # get an installs sandbox runs
        api_response = api_instance.get_install_sandbox_runs(install_id)
        print("The response of InstallsApi->get_install_sandbox_runs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->get_install_sandbox_runs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **str**| install ID | 

### Return type

[**List[AppInstallSandboxRun]**](AppInstallSandboxRun.md)

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

# **get_org_installs**
> List[AppInstall] get_org_installs()

get all installs for an org

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_install import AppInstall
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
    api_instance = nuon.InstallsApi(api_client)

    try:
        # get all installs for an org
        api_response = api_instance.get_org_installs()
        print("The response of InstallsApi->get_org_installs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->get_org_installs: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[AppInstall]**](AppInstall.md)

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

# **reprovision_install**
> str reprovision_install(install_id, body)

reprovision an install

Reprovision an install sandbox.  

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
    api_instance = nuon.InstallsApi(api_client)
    install_id = 'install_id_example' # str | install ID
    body = None # object | Input

    try:
        # reprovision an install
        api_response = api_instance.reprovision_install(install_id, body)
        print("The response of InstallsApi->reprovision_install:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->reprovision_install: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **str**| install ID | 
 **body** | **object**| Input | 

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
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teardown_install_component**
> AppInstallDeploy teardown_install_component(install_id, component_id)

teardown an install component

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_install_deploy import AppInstallDeploy
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
    api_instance = nuon.InstallsApi(api_client)
    install_id = 'install_id_example' # str | install ID
    component_id = 'component_id_example' # str | component ID

    try:
        # teardown an install component
        api_response = api_instance.teardown_install_component(install_id, component_id)
        print("The response of InstallsApi->teardown_install_component:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->teardown_install_component: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **str**| install ID | 
 **component_id** | **str**| component ID | 

### Return type

[**AppInstallDeploy**](AppInstallDeploy.md)

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

# **teardown_install_components**
> str teardown_install_components(install_id, body)

teardown an install's components

Teardown all components on an install. 

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
    api_instance = nuon.InstallsApi(api_client)
    install_id = 'install_id_example' # str | install ID
    body = None # object | Input

    try:
        # teardown an install's components
        api_response = api_instance.teardown_install_components(install_id, body)
        print("The response of InstallsApi->teardown_install_components:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->teardown_install_components: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **str**| install ID | 
 **body** | **object**| Input | 

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
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_install**
> AppInstall update_install(install_id, service_update_install_request)

update an install

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_install import AppInstall
from nuon.models.service_update_install_request import ServiceUpdateInstallRequest
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
    api_instance = nuon.InstallsApi(api_client)
    install_id = 'install_id_example' # str | app ID
    service_update_install_request = nuon.ServiceUpdateInstallRequest() # ServiceUpdateInstallRequest | Input

    try:
        # update an install
        api_response = api_instance.update_install(install_id, service_update_install_request)
        print("The response of InstallsApi->update_install:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->update_install: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **str**| app ID | 
 **service_update_install_request** | [**ServiceUpdateInstallRequest**](ServiceUpdateInstallRequest.md)| Input | 

### Return type

[**AppInstall**](AppInstall.md)

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

