# nuon.ComponentsApi

All URIs are relative to *http://localhost:8081*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_component**](ComponentsApi.md#create_component) | **POST** /v1/apps/{app_id}/components | create a component
[**create_component_build**](ComponentsApi.md#create_component_build) | **POST** /v1/components/{component_id}/builds | create component build
[**create_docker_build_component_config**](ComponentsApi.md#create_docker_build_component_config) | **POST** /v1/components/{component_id}/configs/docker-build | create a docker build component config
[**create_external_image_component_config**](ComponentsApi.md#create_external_image_component_config) | **POST** /v1/components/{component_id}/configs/external-image | create an external image component config
[**create_helm_component_config**](ComponentsApi.md#create_helm_component_config) | **POST** /v1/components/{component_id}/configs/helm | create a helm component config
[**create_job_component_config**](ComponentsApi.md#create_job_component_config) | **POST** /v1/components/{component_id}/configs/job | create a job component config
[**create_kubernetes_manifest_component_config**](ComponentsApi.md#create_kubernetes_manifest_component_config) | **POST** /v1/components/{component_id}/configs/kubernetes-manifest | create a kubernetes manifest component config
[**create_terraform_module_component_config**](ComponentsApi.md#create_terraform_module_component_config) | **POST** /v1/components/{component_id}/configs/terraform-module | create a terraform component config
[**delete_component**](ComponentsApi.md#delete_component) | **DELETE** /v1/components/{component_id} | delete a component
[**get_app_component**](ComponentsApi.md#get_app_component) | **GET** /v1/apps/{app_id}/component/{component_name_or_id} | get a components for a specific app
[**get_app_components**](ComponentsApi.md#get_app_components) | **GET** /v1/apps/{app_id}/components | get all components for an app
[**get_build**](ComponentsApi.md#get_build) | **GET** /v1/components/builds/{build_id} | get a build
[**get_component**](ComponentsApi.md#get_component) | **GET** /v1/components/{component_id} | get a component
[**get_component_build**](ComponentsApi.md#get_component_build) | **GET** /v1/components/{component_id}/builds/{build_id} | get a build for a component
[**get_component_builds**](ComponentsApi.md#get_component_builds) | **GET** /v1/builds | get builds for components
[**get_component_config**](ComponentsApi.md#get_component_config) | **GET** /v1/components/{component_id}/configs/{config_id} | get all configs for a component
[**get_component_configs**](ComponentsApi.md#get_component_configs) | **GET** /v1/components/{component_id}/configs | get all configs for a component
[**get_component_dependencies**](ComponentsApi.md#get_component_dependencies) | **GET** /v1/components/{component_id}/dependencies | get a component&#39;s dependencies
[**get_component_dependents**](ComponentsApi.md#get_component_dependents) | **GET** /v1/components/{component_id}/dependents | get a component&#39;s children
[**get_component_latest_build**](ComponentsApi.md#get_component_latest_build) | **GET** /v1/components/{component_id}/builds/latest | get latest build for a component
[**get_component_latest_config**](ComponentsApi.md#get_component_latest_config) | **GET** /v1/components/{component_id}/configs/latest | get latest config for a component
[**get_org_components**](ComponentsApi.md#get_org_components) | **GET** /v1/components | get all components for an org
[**update_component**](ComponentsApi.md#update_component) | **PATCH** /v1/components/{component_id} | update a component


# **create_component**
> AppComponent create_component(app_id, service_create_component_request)

create a component

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_component import AppComponent
from nuon.models.service_create_component_request import ServiceCreateComponentRequest
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
    api_instance = nuon.ComponentsApi(api_client)
    app_id = 'app_id_example' # str | app ID
    service_create_component_request = nuon.ServiceCreateComponentRequest() # ServiceCreateComponentRequest | Input

    try:
        # create a component
        api_response = api_instance.create_component(app_id, service_create_component_request)
        print("The response of ComponentsApi->create_component:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComponentsApi->create_component: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| app ID | 
 **service_create_component_request** | [**ServiceCreateComponentRequest**](ServiceCreateComponentRequest.md)| Input | 

### Return type

[**AppComponent**](AppComponent.md)

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

# **create_component_build**
> AppComponentBuild create_component_build(component_id, service_create_component_build_request)

create component build

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_component_build import AppComponentBuild
from nuon.models.service_create_component_build_request import ServiceCreateComponentBuildRequest
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
    api_instance = nuon.ComponentsApi(api_client)
    component_id = 'component_id_example' # str | component ID
    service_create_component_build_request = nuon.ServiceCreateComponentBuildRequest() # ServiceCreateComponentBuildRequest | Input

    try:
        # create component build
        api_response = api_instance.create_component_build(component_id, service_create_component_build_request)
        print("The response of ComponentsApi->create_component_build:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComponentsApi->create_component_build: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_id** | **str**| component ID | 
 **service_create_component_build_request** | [**ServiceCreateComponentBuildRequest**](ServiceCreateComponentBuildRequest.md)| Input | 

### Return type

[**AppComponentBuild**](AppComponentBuild.md)

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

# **create_docker_build_component_config**
> AppDockerBuildComponentConfig create_docker_build_component_config(component_id, service_create_docker_build_component_config_request)

create a docker build component config

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_docker_build_component_config import AppDockerBuildComponentConfig
from nuon.models.service_create_docker_build_component_config_request import ServiceCreateDockerBuildComponentConfigRequest
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
    api_instance = nuon.ComponentsApi(api_client)
    component_id = 'component_id_example' # str | component ID
    service_create_docker_build_component_config_request = nuon.ServiceCreateDockerBuildComponentConfigRequest() # ServiceCreateDockerBuildComponentConfigRequest | Input

    try:
        # create a docker build component config
        api_response = api_instance.create_docker_build_component_config(component_id, service_create_docker_build_component_config_request)
        print("The response of ComponentsApi->create_docker_build_component_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComponentsApi->create_docker_build_component_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_id** | **str**| component ID | 
 **service_create_docker_build_component_config_request** | [**ServiceCreateDockerBuildComponentConfigRequest**](ServiceCreateDockerBuildComponentConfigRequest.md)| Input | 

### Return type

[**AppDockerBuildComponentConfig**](AppDockerBuildComponentConfig.md)

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

# **create_external_image_component_config**
> AppExternalImageComponentConfig create_external_image_component_config(component_id, service_create_external_image_component_config_request)

create an external image component config

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_external_image_component_config import AppExternalImageComponentConfig
from nuon.models.service_create_external_image_component_config_request import ServiceCreateExternalImageComponentConfigRequest
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
    api_instance = nuon.ComponentsApi(api_client)
    component_id = 'component_id_example' # str | component ID
    service_create_external_image_component_config_request = nuon.ServiceCreateExternalImageComponentConfigRequest() # ServiceCreateExternalImageComponentConfigRequest | Input

    try:
        # create an external image component config
        api_response = api_instance.create_external_image_component_config(component_id, service_create_external_image_component_config_request)
        print("The response of ComponentsApi->create_external_image_component_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComponentsApi->create_external_image_component_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_id** | **str**| component ID | 
 **service_create_external_image_component_config_request** | [**ServiceCreateExternalImageComponentConfigRequest**](ServiceCreateExternalImageComponentConfigRequest.md)| Input | 

### Return type

[**AppExternalImageComponentConfig**](AppExternalImageComponentConfig.md)

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

# **create_helm_component_config**
> AppHelmComponentConfig create_helm_component_config(component_id, service_create_helm_component_config_request)

create a helm component config

Create a helm component config. 

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_helm_component_config import AppHelmComponentConfig
from nuon.models.service_create_helm_component_config_request import ServiceCreateHelmComponentConfigRequest
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
    api_instance = nuon.ComponentsApi(api_client)
    component_id = 'component_id_example' # str | component ID
    service_create_helm_component_config_request = nuon.ServiceCreateHelmComponentConfigRequest() # ServiceCreateHelmComponentConfigRequest | Input

    try:
        # create a helm component config
        api_response = api_instance.create_helm_component_config(component_id, service_create_helm_component_config_request)
        print("The response of ComponentsApi->create_helm_component_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComponentsApi->create_helm_component_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_id** | **str**| component ID | 
 **service_create_helm_component_config_request** | [**ServiceCreateHelmComponentConfigRequest**](ServiceCreateHelmComponentConfigRequest.md)| Input | 

### Return type

[**AppHelmComponentConfig**](AppHelmComponentConfig.md)

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

# **create_job_component_config**
> AppJobComponentConfig create_job_component_config(component_id, service_create_job_component_config_request)

create a job component config

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_job_component_config import AppJobComponentConfig
from nuon.models.service_create_job_component_config_request import ServiceCreateJobComponentConfigRequest
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
    api_instance = nuon.ComponentsApi(api_client)
    component_id = 'component_id_example' # str | component ID
    service_create_job_component_config_request = nuon.ServiceCreateJobComponentConfigRequest() # ServiceCreateJobComponentConfigRequest | Input

    try:
        # create a job component config
        api_response = api_instance.create_job_component_config(component_id, service_create_job_component_config_request)
        print("The response of ComponentsApi->create_job_component_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComponentsApi->create_job_component_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_id** | **str**| component ID | 
 **service_create_job_component_config_request** | [**ServiceCreateJobComponentConfigRequest**](ServiceCreateJobComponentConfigRequest.md)| Input | 

### Return type

[**AppJobComponentConfig**](AppJobComponentConfig.md)

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

# **create_kubernetes_manifest_component_config**
> AppKubernetesManifestComponentConfig create_kubernetes_manifest_component_config(component_id, service_create_kubernetes_manifest_component_config_request)

create a kubernetes manifest component config

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_kubernetes_manifest_component_config import AppKubernetesManifestComponentConfig
from nuon.models.service_create_kubernetes_manifest_component_config_request import ServiceCreateKubernetesManifestComponentConfigRequest
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
    api_instance = nuon.ComponentsApi(api_client)
    component_id = 'component_id_example' # str | component ID
    service_create_kubernetes_manifest_component_config_request = nuon.ServiceCreateKubernetesManifestComponentConfigRequest() # ServiceCreateKubernetesManifestComponentConfigRequest | Input

    try:
        # create a kubernetes manifest component config
        api_response = api_instance.create_kubernetes_manifest_component_config(component_id, service_create_kubernetes_manifest_component_config_request)
        print("The response of ComponentsApi->create_kubernetes_manifest_component_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComponentsApi->create_kubernetes_manifest_component_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_id** | **str**| component ID | 
 **service_create_kubernetes_manifest_component_config_request** | [**ServiceCreateKubernetesManifestComponentConfigRequest**](ServiceCreateKubernetesManifestComponentConfigRequest.md)| Input | 

### Return type

[**AppKubernetesManifestComponentConfig**](AppKubernetesManifestComponentConfig.md)

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

# **create_terraform_module_component_config**
> AppTerraformModuleComponentConfig create_terraform_module_component_config(component_id, service_create_terraform_module_component_config_request)

create a terraform component config

Create a terraform component config. 

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_terraform_module_component_config import AppTerraformModuleComponentConfig
from nuon.models.service_create_terraform_module_component_config_request import ServiceCreateTerraformModuleComponentConfigRequest
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
    api_instance = nuon.ComponentsApi(api_client)
    component_id = 'component_id_example' # str | component ID
    service_create_terraform_module_component_config_request = nuon.ServiceCreateTerraformModuleComponentConfigRequest() # ServiceCreateTerraformModuleComponentConfigRequest | Input

    try:
        # create a terraform component config
        api_response = api_instance.create_terraform_module_component_config(component_id, service_create_terraform_module_component_config_request)
        print("The response of ComponentsApi->create_terraform_module_component_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComponentsApi->create_terraform_module_component_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_id** | **str**| component ID | 
 **service_create_terraform_module_component_config_request** | [**ServiceCreateTerraformModuleComponentConfigRequest**](ServiceCreateTerraformModuleComponentConfigRequest.md)| Input | 

### Return type

[**AppTerraformModuleComponentConfig**](AppTerraformModuleComponentConfig.md)

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

# **delete_component**
> bool delete_component(component_id)

delete a component

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
    api_instance = nuon.ComponentsApi(api_client)
    component_id = 'component_id_example' # str | component ID

    try:
        # delete a component
        api_response = api_instance.delete_component(component_id)
        print("The response of ComponentsApi->delete_component:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComponentsApi->delete_component: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_id** | **str**| component ID | 

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

# **get_app_component**
> AppComponent get_app_component(app_id, component_name_or_id)

get a components for a specific app

Return an app component by id or name. 

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_component import AppComponent
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
    api_instance = nuon.ComponentsApi(api_client)
    app_id = 'app_id_example' # str | app ID
    component_name_or_id = 'component_name_or_id_example' # str | name or ID

    try:
        # get a components for a specific app
        api_response = api_instance.get_app_component(app_id, component_name_or_id)
        print("The response of ComponentsApi->get_app_component:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComponentsApi->get_app_component: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| app ID | 
 **component_name_or_id** | **str**| name or ID | 

### Return type

[**AppComponent**](AppComponent.md)

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

# **get_app_components**
> List[AppComponent] get_app_components(app_id, q=q, types=types, offset=offset, limit=limit, page=page, x_nuon_pagination_enabled=x_nuon_pagination_enabled)

get all components for an app

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_component import AppComponent
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
    api_instance = nuon.ComponentsApi(api_client)
    app_id = 'app_id_example' # str | app ID
    q = 'q_example' # str | search query to filter components by name (optional)
    types = 'types_example' # str | comma-separated list of component types to filter by (e.g., terraform_module, helm_chart) (optional)
    offset = 0 # int | offset of results to return (optional) (default to 0)
    limit = 10 # int | limit of results to return (optional) (default to 10)
    page = 0 # int | page number of results to return (optional) (default to 0)
    x_nuon_pagination_enabled = True # bool | Enable pagination (optional)

    try:
        # get all components for an app
        api_response = api_instance.get_app_components(app_id, q=q, types=types, offset=offset, limit=limit, page=page, x_nuon_pagination_enabled=x_nuon_pagination_enabled)
        print("The response of ComponentsApi->get_app_components:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComponentsApi->get_app_components: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| app ID | 
 **q** | **str**| search query to filter components by name | [optional] 
 **types** | **str**| comma-separated list of component types to filter by (e.g., terraform_module, helm_chart) | [optional] 
 **offset** | **int**| offset of results to return | [optional] [default to 0]
 **limit** | **int**| limit of results to return | [optional] [default to 10]
 **page** | **int**| page number of results to return | [optional] [default to 0]
 **x_nuon_pagination_enabled** | **bool**| Enable pagination | [optional] 

### Return type

[**List[AppComponent]**](AppComponent.md)

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

# **get_build**
> AppComponentBuild get_build(build_id)

get a build

Returns builds for one or all components in an app. 

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_component_build import AppComponentBuild
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
    api_instance = nuon.ComponentsApi(api_client)
    build_id = 'build_id_example' # str | build ID

    try:
        # get a build
        api_response = api_instance.get_build(build_id)
        print("The response of ComponentsApi->get_build:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComponentsApi->get_build: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_id** | **str**| build ID | 

### Return type

[**AppComponentBuild**](AppComponentBuild.md)

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

# **get_component**
> AppComponent get_component(component_id)

get a component

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_component import AppComponent
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
    api_instance = nuon.ComponentsApi(api_client)
    component_id = 'component_id_example' # str | component ID

    try:
        # get a component
        api_response = api_instance.get_component(component_id)
        print("The response of ComponentsApi->get_component:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComponentsApi->get_component: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_id** | **str**| component ID | 

### Return type

[**AppComponent**](AppComponent.md)

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

# **get_component_build**
> AppComponentBuild get_component_build(component_id, build_id)

get a build for a component

Returns builds for one or all components in an app. 

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_component_build import AppComponentBuild
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
    api_instance = nuon.ComponentsApi(api_client)
    component_id = 'component_id_example' # str | component ID
    build_id = 'build_id_example' # str | build ID

    try:
        # get a build for a component
        api_response = api_instance.get_component_build(component_id, build_id)
        print("The response of ComponentsApi->get_component_build:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComponentsApi->get_component_build: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_id** | **str**| component ID | 
 **build_id** | **str**| build ID | 

### Return type

[**AppComponentBuild**](AppComponentBuild.md)

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

# **get_component_builds**
> List[AppComponentBuild] get_component_builds(component_id=component_id, app_id=app_id, offset=offset, limit=limit, page=page, x_nuon_pagination_enabled=x_nuon_pagination_enabled)

get builds for components

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_component_build import AppComponentBuild
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
    api_instance = nuon.ComponentsApi(api_client)
    component_id = 'component_id_example' # str | component id to filter by (optional)
    app_id = 'app_id_example' # str | app id to filter by (optional)
    offset = 0 # int | offset of results to return (optional) (default to 0)
    limit = 10 # int | limit of results to return (optional) (default to 10)
    page = 0 # int | page number of results to return (optional) (default to 0)
    x_nuon_pagination_enabled = True # bool | Enable pagination (optional)

    try:
        # get builds for components
        api_response = api_instance.get_component_builds(component_id=component_id, app_id=app_id, offset=offset, limit=limit, page=page, x_nuon_pagination_enabled=x_nuon_pagination_enabled)
        print("The response of ComponentsApi->get_component_builds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComponentsApi->get_component_builds: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_id** | **str**| component id to filter by | [optional] 
 **app_id** | **str**| app id to filter by | [optional] 
 **offset** | **int**| offset of results to return | [optional] [default to 0]
 **limit** | **int**| limit of results to return | [optional] [default to 10]
 **page** | **int**| page number of results to return | [optional] [default to 0]
 **x_nuon_pagination_enabled** | **bool**| Enable pagination | [optional] 

### Return type

[**List[AppComponentBuild]**](AppComponentBuild.md)

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

# **get_component_config**
> AppComponentConfigConnection get_component_config(component_id, config_id)

get all configs for a component

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_component_config_connection import AppComponentConfigConnection
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
    api_instance = nuon.ComponentsApi(api_client)
    component_id = 'component_id_example' # str | component ID
    config_id = 'config_id_example' # str | config ID

    try:
        # get all configs for a component
        api_response = api_instance.get_component_config(component_id, config_id)
        print("The response of ComponentsApi->get_component_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComponentsApi->get_component_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_id** | **str**| component ID | 
 **config_id** | **str**| config ID | 

### Return type

[**AppComponentConfigConnection**](AppComponentConfigConnection.md)

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

# **get_component_configs**
> List[AppComponentConfigConnection] get_component_configs(component_id, offset=offset, limit=limit, page=page, x_nuon_pagination_enabled=x_nuon_pagination_enabled)

get all configs for a component

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_component_config_connection import AppComponentConfigConnection
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
    api_instance = nuon.ComponentsApi(api_client)
    component_id = 'component_id_example' # str | component ID
    offset = 0 # int | offset of results to return (optional) (default to 0)
    limit = 10 # int | limit of results to return (optional) (default to 10)
    page = 0 # int | page number of results to return (optional) (default to 0)
    x_nuon_pagination_enabled = True # bool | Enable pagination (optional)

    try:
        # get all configs for a component
        api_response = api_instance.get_component_configs(component_id, offset=offset, limit=limit, page=page, x_nuon_pagination_enabled=x_nuon_pagination_enabled)
        print("The response of ComponentsApi->get_component_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComponentsApi->get_component_configs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_id** | **str**| component ID | 
 **offset** | **int**| offset of results to return | [optional] [default to 0]
 **limit** | **int**| limit of results to return | [optional] [default to 10]
 **page** | **int**| page number of results to return | [optional] [default to 0]
 **x_nuon_pagination_enabled** | **bool**| Enable pagination | [optional] 

### Return type

[**List[AppComponentConfigConnection]**](AppComponentConfigConnection.md)

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

# **get_component_dependencies**
> List[AppComponent] get_component_dependencies(component_id)

get a component's dependencies

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_component import AppComponent
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
    api_instance = nuon.ComponentsApi(api_client)
    component_id = 'component_id_example' # str | component ID

    try:
        # get a component's dependencies
        api_response = api_instance.get_component_dependencies(component_id)
        print("The response of ComponentsApi->get_component_dependencies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComponentsApi->get_component_dependencies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_id** | **str**| component ID | 

### Return type

[**List[AppComponent]**](AppComponent.md)

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

# **get_component_dependents**
> ServiceComponentChildren get_component_dependents(component_id)

get a component's children

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.service_component_children import ServiceComponentChildren
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
    api_instance = nuon.ComponentsApi(api_client)
    component_id = 'component_id_example' # str | component ID

    try:
        # get a component's children
        api_response = api_instance.get_component_dependents(component_id)
        print("The response of ComponentsApi->get_component_dependents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComponentsApi->get_component_dependents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_id** | **str**| component ID | 

### Return type

[**ServiceComponentChildren**](ServiceComponentChildren.md)

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

# **get_component_latest_build**
> AppComponentBuild get_component_latest_build(component_id)

get latest build for a component

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_component_build import AppComponentBuild
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
    api_instance = nuon.ComponentsApi(api_client)
    component_id = 'component_id_example' # str | component ID

    try:
        # get latest build for a component
        api_response = api_instance.get_component_latest_build(component_id)
        print("The response of ComponentsApi->get_component_latest_build:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComponentsApi->get_component_latest_build: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_id** | **str**| component ID | 

### Return type

[**AppComponentBuild**](AppComponentBuild.md)

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

# **get_component_latest_config**
> AppComponentConfigConnection get_component_latest_config(component_id)

get latest config for a component

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_component_config_connection import AppComponentConfigConnection
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
    api_instance = nuon.ComponentsApi(api_client)
    component_id = 'component_id_example' # str | component ID

    try:
        # get latest config for a component
        api_response = api_instance.get_component_latest_config(component_id)
        print("The response of ComponentsApi->get_component_latest_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComponentsApi->get_component_latest_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_id** | **str**| component ID | 

### Return type

[**AppComponentConfigConnection**](AppComponentConfigConnection.md)

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

# **get_org_components**
> List[AppComponent] get_org_components(offset=offset, limit=limit, page=page, x_nuon_pagination_enabled=x_nuon_pagination_enabled)

get all components for an org

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_component import AppComponent
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
    api_instance = nuon.ComponentsApi(api_client)
    offset = 0 # int | offset of results to return (optional) (default to 0)
    limit = 10 # int | limit of results to return (optional) (default to 10)
    page = 0 # int | page number of results to return (optional) (default to 0)
    x_nuon_pagination_enabled = True # bool | Enable pagination (optional)

    try:
        # get all components for an org
        api_response = api_instance.get_org_components(offset=offset, limit=limit, page=page, x_nuon_pagination_enabled=x_nuon_pagination_enabled)
        print("The response of ComponentsApi->get_org_components:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComponentsApi->get_org_components: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| offset of results to return | [optional] [default to 0]
 **limit** | **int**| limit of results to return | [optional] [default to 10]
 **page** | **int**| page number of results to return | [optional] [default to 0]
 **x_nuon_pagination_enabled** | **bool**| Enable pagination | [optional] 

### Return type

[**List[AppComponent]**](AppComponent.md)

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

# **update_component**
> AppComponent update_component(component_id, service_update_component_request)

update a component

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_component import AppComponent
from nuon.models.service_update_component_request import ServiceUpdateComponentRequest
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
    api_instance = nuon.ComponentsApi(api_client)
    component_id = 'component_id_example' # str | component ID
    service_update_component_request = nuon.ServiceUpdateComponentRequest() # ServiceUpdateComponentRequest | Input

    try:
        # update a component
        api_response = api_instance.update_component(component_id, service_update_component_request)
        print("The response of ComponentsApi->update_component:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComponentsApi->update_component: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_id** | **str**| component ID | 
 **service_update_component_request** | [**ServiceUpdateComponentRequest**](ServiceUpdateComponentRequest.md)| Input | 

### Return type

[**AppComponent**](AppComponent.md)

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

