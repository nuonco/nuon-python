# nuon.InstallersApi

All URIs are relative to *https://ctl.prod.nuon.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_app_installer**](InstallersApi.md#create_app_installer) | **POST** /v1/installers | create an app installer
[**delete_app_installer**](InstallersApi.md#delete_app_installer) | **DELETE** /v1/installers/{installer_id} | delete an app installer
[**get_app_installer**](InstallersApi.md#get_app_installer) | **GET** /v1/installers/{installer_id} | get an app installer
[**get_installers**](InstallersApi.md#get_installers) | **GET** /v1/installers | get installers for current org
[**installer_create_install**](InstallersApi.md#installer_create_install) | **POST** /v1/installer/{installer_slug}/installs | create an app install from an installer
[**installer_get_install**](InstallersApi.md#installer_get_install) | **GET** /v1/installer/{installer_slug}/install/{install_id} | get an installer install
[**render_app_installer**](InstallersApi.md#render_app_installer) | **GET** /v1/installer/{installer_slug}/render | render an app installer
[**update_app_installer**](InstallersApi.md#update_app_installer) | **PATCH** /v1/installers/{installer_id} | update an app installer


# **create_app_installer**
> AppAppInstaller create_app_installer(service_create_app_installer_request)

create an app installer

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_app_installer import AppAppInstaller
from nuon.models.service_create_app_installer_request import ServiceCreateAppInstallerRequest
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
    api_instance = nuon.InstallersApi(api_client)
    service_create_app_installer_request = nuon.ServiceCreateAppInstallerRequest() # ServiceCreateAppInstallerRequest | Input

    try:
        # create an app installer
        api_response = api_instance.create_app_installer(service_create_app_installer_request)
        print("The response of InstallersApi->create_app_installer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallersApi->create_app_installer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_create_app_installer_request** | [**ServiceCreateAppInstallerRequest**](ServiceCreateAppInstallerRequest.md)| Input | 

### Return type

[**AppAppInstaller**](AppAppInstaller.md)

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

# **delete_app_installer**
> bool delete_app_installer(installer_id)

delete an app installer

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
    api_instance = nuon.InstallersApi(api_client)
    installer_id = 'installer_id_example' # str | installer ID

    try:
        # delete an app installer
        api_response = api_instance.delete_app_installer(installer_id)
        print("The response of InstallersApi->delete_app_installer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallersApi->delete_app_installer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **installer_id** | **str**| installer ID | 

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

# **get_app_installer**
> AppAppInstaller get_app_installer(installer_id)

get an app installer

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_app_installer import AppAppInstaller
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
    api_instance = nuon.InstallersApi(api_client)
    installer_id = 'installer_id_example' # str | installer ID

    try:
        # get an app installer
        api_response = api_instance.get_app_installer(installer_id)
        print("The response of InstallersApi->get_app_installer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallersApi->get_app_installer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **installer_id** | **str**| installer ID | 

### Return type

[**AppAppInstaller**](AppAppInstaller.md)

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

# **get_installers**
> List[AppAppInstaller] get_installers()

get installers for current org

Return all installers for the current org. 

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_app_installer import AppAppInstaller
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
    api_instance = nuon.InstallersApi(api_client)

    try:
        # get installers for current org
        api_response = api_instance.get_installers()
        print("The response of InstallersApi->get_installers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallersApi->get_installers: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[AppAppInstaller]**](AppAppInstaller.md)

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

# **installer_create_install**
> AppInstall installer_create_install(installer_slug, service_create_install_request)

create an app install from an installer

### Example


```python
import time
import os
import nuon
from nuon.models.app_install import AppInstall
from nuon.models.service_create_install_request import ServiceCreateInstallRequest
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
    api_instance = nuon.InstallersApi(api_client)
    installer_slug = 'installer_slug_example' # str | installer slug or ID
    service_create_install_request = nuon.ServiceCreateInstallRequest() # ServiceCreateInstallRequest | Input

    try:
        # create an app install from an installer
        api_response = api_instance.installer_create_install(installer_slug, service_create_install_request)
        print("The response of InstallersApi->installer_create_install:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallersApi->installer_create_install: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **installer_slug** | **str**| installer slug or ID | 
 **service_create_install_request** | [**ServiceCreateInstallRequest**](ServiceCreateInstallRequest.md)| Input | 

### Return type

[**AppInstall**](AppInstall.md)

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

# **installer_get_install**
> AppInstall installer_get_install(installer_slug, install_id)

get an installer install

### Example


```python
import time
import os
import nuon
from nuon.models.app_install import AppInstall
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
    api_instance = nuon.InstallersApi(api_client)
    installer_slug = 'installer_slug_example' # str | installer slug or ID
    install_id = 'install_id_example' # str | install id

    try:
        # get an installer install
        api_response = api_instance.installer_get_install(installer_slug, install_id)
        print("The response of InstallersApi->installer_get_install:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallersApi->installer_get_install: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **installer_slug** | **str**| installer slug or ID | 
 **install_id** | **str**| install id | 

### Return type

[**AppInstall**](AppInstall.md)

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

# **render_app_installer**
> ServiceAppInstaller render_app_installer(installer_slug)

render an app installer

### Example


```python
import time
import os
import nuon
from nuon.models.service_app_installer import ServiceAppInstaller
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
    api_instance = nuon.InstallersApi(api_client)
    installer_slug = 'installer_slug_example' # str | installer slug or ID

    try:
        # render an app installer
        api_response = api_instance.render_app_installer(installer_slug)
        print("The response of InstallersApi->render_app_installer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallersApi->render_app_installer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **installer_slug** | **str**| installer slug or ID | 

### Return type

[**ServiceAppInstaller**](ServiceAppInstaller.md)

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

# **update_app_installer**
> AppAppInstaller update_app_installer(installer_id, service_update_app_installer_request)

update an app installer

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_app_installer import AppAppInstaller
from nuon.models.service_update_app_installer_request import ServiceUpdateAppInstallerRequest
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
    api_instance = nuon.InstallersApi(api_client)
    installer_id = 'installer_id_example' # str | installer ID
    service_update_app_installer_request = nuon.ServiceUpdateAppInstallerRequest() # ServiceUpdateAppInstallerRequest | Input

    try:
        # update an app installer
        api_response = api_instance.update_app_installer(installer_id, service_update_app_installer_request)
        print("The response of InstallersApi->update_app_installer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallersApi->update_app_installer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **installer_id** | **str**| installer ID | 
 **service_update_app_installer_request** | [**ServiceUpdateAppInstallerRequest**](ServiceUpdateAppInstallerRequest.md)| Input | 

### Return type

[**AppAppInstaller**](AppAppInstaller.md)

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

