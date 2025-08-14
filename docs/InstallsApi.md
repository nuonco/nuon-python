# nuon.InstallsApi

All URIs are relative to *http://localhost:8081*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_install_workflow**](InstallsApi.md#cancel_install_workflow) | **POST** /v1/install-workflows/{install_workflow_id}/cancel | cancel an ongoing install workflow
[**cancel_workflow**](InstallsApi.md#cancel_workflow) | **POST** /v1/workflows/{workflow_id}/cancel | cancel an ongoing workflow
[**create_install**](InstallsApi.md#create_install) | **POST** /v1/apps/{app_id}/installs | create an app install
[**create_install_config**](InstallsApi.md#create_install_config) | **POST** /v1/installs/{install_id}/configs | create an install config
[**create_install_deploy**](InstallsApi.md#create_install_deploy) | **POST** /v1/installs/{install_id}/deploys | deploy a build to an install
[**create_install_inputs**](InstallsApi.md#create_install_inputs) | **POST** /v1/installs/{install_id}/inputs | create install inputs
[**create_install_workflow_step_approval_response**](InstallsApi.md#create_install_workflow_step_approval_response) | **POST** /v1/install-workflows/{install_workflow_id}/steps/{install_workflow_step_id}/approvals/{approval_id}/response | deploy a build to an install
[**create_workflow_step_approval_response**](InstallsApi.md#create_workflow_step_approval_response) | **POST** /v1/workflows/{workflow_id}/steps/{workflow_step_id}/approvals/{approval_id}/response | deploy a build to an install
[**delete_install**](InstallsApi.md#delete_install) | **DELETE** /v1/installs/{install_id} | delete an install
[**deploy_install_components**](InstallsApi.md#deploy_install_components) | **POST** /v1/installs/{install_id}/components/deploy-all | deploy all components on an install
[**deprovision_install**](InstallsApi.md#deprovision_install) | **POST** /v1/installs/{install_id}/deprovision | deprovision an install
[**deprovision_install_sandbox**](InstallsApi.md#deprovision_install_sandbox) | **POST** /v1/installs/{install_id}/deprovision-sandbox | deprovision an install
[**forget_install**](InstallsApi.md#forget_install) | **POST** /v1/installs/{install_id}/forget | forget an install
[**get_app_installs**](InstallsApi.md#get_app_installs) | **GET** /v1/apps/{app_id}/installs | get all installs for an app
[**get_current_install_inputs**](InstallsApi.md#get_current_install_inputs) | **GET** /v1/installs/{install_id}/inputs/current | get an installs current inputs
[**get_install**](InstallsApi.md#get_install) | **GET** /v1/installs/{install_id} | get an install
[**get_install_action_workflow**](InstallsApi.md#get_install_action_workflow) | **GET** /v1/installs/{install_id}/action-workflows/{action_workflow_id} | get an install action workflow
[**get_install_action_workflows**](InstallsApi.md#get_install_action_workflows) | **GET** /v1/installs/{install_id}/action-workflows | get an installs action workflows
[**get_install_audit_logs**](InstallsApi.md#get_install_audit_logs) | **GET** /v1/installs/{install_id}/audit_logs | get install audit logs
[**get_install_component**](InstallsApi.md#get_install_component) | **GET** /v1/installs/{install_id}/components/{component_id} | get an install component
[**get_install_component_deploys**](InstallsApi.md#get_install_component_deploys) | **GET** /v1/installs/{install_id}/components/{component_id}/deploys | get an install components deploys
[**get_install_component_latest_deploy**](InstallsApi.md#get_install_component_latest_deploy) | **GET** /v1/installs/{install_id}/components/{component_id}/deploys/latest | get the latest deploy for an install component
[**get_install_component_outputs**](InstallsApi.md#get_install_component_outputs) | **GET** /v1/installs/{install_id}/components/{component_id}/outputs | get an install component outputs
[**get_install_components**](InstallsApi.md#get_install_components) | **GET** /v1/installs/{install_id}/components | get an installs components
[**get_install_components_summary**](InstallsApi.md#get_install_components_summary) | **GET** /v1/installs/{install_id}/components/summary | get an installs components summary
[**get_install_deploy**](InstallsApi.md#get_install_deploy) | **GET** /v1/installs/{install_id}/deploys/{deploy_id} | get an install deploy
[**get_install_deploys**](InstallsApi.md#get_install_deploys) | **GET** /v1/installs/{install_id}/deploys | get all deploys to an install
[**get_install_event**](InstallsApi.md#get_install_event) | **GET** /v1/installs/{install_id}/events/{event_id} | get an install event
[**get_install_events**](InstallsApi.md#get_install_events) | **GET** /v1/installs/{install_id}/events | get events for an install
[**get_install_inputs**](InstallsApi.md#get_install_inputs) | **GET** /v1/installs/{install_id}/inputs | get an installs inputs
[**get_install_latest_deploy**](InstallsApi.md#get_install_latest_deploy) | **GET** /v1/installs/{install_id}/deploys/latest | get an install deploy
[**get_install_readme**](InstallsApi.md#get_install_readme) | **GET** /v1/installs/{install_id}/readme | get install readme rendered with
[**get_install_runner_group**](InstallsApi.md#get_install_runner_group) | **GET** /v1/installs/{install_id}/runner-group | Get an install&#39;s runner group
[**get_install_sandbox_run**](InstallsApi.md#get_install_sandbox_run) | **GET** /v1/installs/sandbox-runs/{run_id} | get an install sandbox run
[**get_install_sandbox_runs**](InstallsApi.md#get_install_sandbox_runs) | **GET** /v1/installs/{install_id}/sandbox-runs | get an installs sandbox runs
[**get_install_stack**](InstallsApi.md#get_install_stack) | **GET** /v1/installs/stacks/{stack_id} | get an install stack by stack ID
[**get_install_stack_by_install_id**](InstallsApi.md#get_install_stack_by_install_id) | **GET** /v1/installs/{install_id}/stack | get an install stack by install ID
[**get_install_stack_runs**](InstallsApi.md#get_install_stack_runs) | **GET** /v1/installs/{install_id}/stack-runs | get an install&#39;s stack runs
[**get_install_state**](InstallsApi.md#get_install_state) | **GET** /v1/installs/{install_id}/state | Get the current state of an install.
[**get_install_workflow**](InstallsApi.md#get_install_workflow) | **GET** /v1/install-workflows/{install_workflow_id} | get an install workflow
[**get_install_workflow_step**](InstallsApi.md#get_install_workflow_step) | **GET** /v1/install-workflows/{install_workflow_id}/steps/{install_workflow_step_id} | get an install workflow step
[**get_install_workflow_step_approval**](InstallsApi.md#get_install_workflow_step_approval) | **GET** /v1/install-workflows/{install_workflow_id}/steps/{install_workflow_step_id}/approvals/{approval_id} | get an install workflow step approval
[**get_install_workflow_steps**](InstallsApi.md#get_install_workflow_steps) | **GET** /v1/install-workflows/{install_workflow_id}/steps | get an install workflow step
[**get_org_installs**](InstallsApi.md#get_org_installs) | **GET** /v1/installs | get all installs for an org
[**get_workflow**](InstallsApi.md#get_workflow) | **GET** /v1/workflows/{workflow_id} | get a workflow
[**get_workflow_step**](InstallsApi.md#get_workflow_step) | **GET** /v1/workflows/{workflow_id}/steps/{workflow_step_id} | get a workflow step
[**get_workflow_step_approval**](InstallsApi.md#get_workflow_step_approval) | **GET** /v1/workflows/{workflow_id}/steps/{workflow_step_id}/approvals/{approval_id} | get an workflow step approval
[**get_workflow_step_approval_contents**](InstallsApi.md#get_workflow_step_approval_contents) | **GET** /v1/workflows/{workflow_id}/steps/{workflow_step_id}/approvals/{approval_id}/contents | get a workflow step approval contents
[**get_workflow_steps**](InstallsApi.md#get_workflow_steps) | **GET** /v1/workflows/{workflow_id}/steps | get a workflow step
[**get_workflows**](InstallsApi.md#get_workflows) | **GET** /v1/installs/{install_id}/workflows | get workflows
[**phone_home**](InstallsApi.md#phone_home) | **POST** /v1/installs/{install_id}/phone-home/{phone_home_id} | phone home for an install
[**reprovision_install**](InstallsApi.md#reprovision_install) | **POST** /v1/installs/{install_id}/reprovision | reprovision an install
[**reprovision_install_sandbox**](InstallsApi.md#reprovision_install_sandbox) | **POST** /v1/installs/{install_id}/reprovision-sandbox | reprovision an install sandbox
[**retry_owner_workflow_by_id**](InstallsApi.md#retry_owner_workflow_by_id) | **POST** /v1/workflows/{workflow_id}/retry | rerun the workflow steps starting from input step id, can be used to retry a failed step
[**retry_workflow**](InstallsApi.md#retry_workflow) | **POST** /v1/installs/{install_id}/retry-workflow | rerun the workflow steps starting from input step id, can be used to retry a failed step
[**sync_secrets**](InstallsApi.md#sync_secrets) | **POST** /v1/installs/{install_id}/sync-secrets | sync secrets install
[**teardown_install_component**](InstallsApi.md#teardown_install_component) | **POST** /v1/installs/{install_id}/components/{component_id}/teardown | teardown an install component
[**teardown_install_components**](InstallsApi.md#teardown_install_components) | **POST** /v1/installs/{install_id}/components/teardown-all | teardown an install&#39;s components
[**update_install**](InstallsApi.md#update_install) | **PATCH** /v1/installs/{install_id} | update an install
[**update_install_config**](InstallsApi.md#update_install_config) | **PATCH** /v1/installs/{install_id}/configs/{config_id} | create an install config
[**update_install_inputs**](InstallsApi.md#update_install_inputs) | **PATCH** /v1/installs/{install_id}/inputs | Updates install input config for app
[**update_install_workflow**](InstallsApi.md#update_install_workflow) | **PATCH** /v1/install-workflows/{install_workflow_id} | update an install workflow
[**update_workflow**](InstallsApi.md#update_workflow) | **PATCH** /v1/workflows/{workflow_id} | update a workflow


# **cancel_install_workflow**
> bool cancel_install_workflow(install_workflow_id)

cancel an ongoing install workflow

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
    api_instance = nuon.InstallsApi(api_client)
    install_workflow_id = 'install_workflow_id_example' # str | install workflow ID

    try:
        # cancel an ongoing install workflow
        api_response = api_instance.cancel_install_workflow(install_workflow_id)
        print("The response of InstallsApi->cancel_install_workflow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->cancel_install_workflow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_workflow_id** | **str**| install workflow ID | 

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
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_workflow**
> bool cancel_workflow(workflow_id)

cancel an ongoing workflow

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
    api_instance = nuon.InstallsApi(api_client)
    workflow_id = 'workflow_id_example' # str | workflow ID

    try:
        # cancel an ongoing workflow
        api_response = api_instance.cancel_workflow(workflow_id)
        print("The response of InstallsApi->cancel_workflow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->cancel_workflow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **str**| workflow ID | 

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
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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

# **create_install_config**
> AppInstallConfig create_install_config(install_id, service_create_install_config_request)

create an install config

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_install_config import AppInstallConfig
from nuon.models.service_create_install_config_request import ServiceCreateInstallConfigRequest
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
    api_instance = nuon.InstallsApi(api_client)
    install_id = 'install_id_example' # str | install ID
    service_create_install_config_request = nuon.ServiceCreateInstallConfigRequest() # ServiceCreateInstallConfigRequest | Input

    try:
        # create an install config
        api_response = api_instance.create_install_config(install_id, service_create_install_config_request)
        print("The response of InstallsApi->create_install_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->create_install_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **str**| install ID | 
 **service_create_install_config_request** | [**ServiceCreateInstallConfigRequest**](ServiceCreateInstallConfigRequest.md)| Input | 

### Return type

[**AppInstallConfig**](AppInstallConfig.md)

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

# **create_install_workflow_step_approval_response**
> AppWorkflowStepApprovalResponse create_install_workflow_step_approval_response(install_workflow_id, install_workflow_step_id, approval_id, service_create_workflow_step_approval_response_request)

deploy a build to an install

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_workflow_step_approval_response import AppWorkflowStepApprovalResponse
from nuon.models.service_create_workflow_step_approval_response_request import ServiceCreateWorkflowStepApprovalResponseRequest
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
    api_instance = nuon.InstallsApi(api_client)
    install_workflow_id = 'install_workflow_id_example' # str | workflow id
    install_workflow_step_id = 'install_workflow_step_id_example' # str | step id
    approval_id = 'approval_id_example' # str | approval id
    service_create_workflow_step_approval_response_request = nuon.ServiceCreateWorkflowStepApprovalResponseRequest() # ServiceCreateWorkflowStepApprovalResponseRequest | Input

    try:
        # deploy a build to an install
        api_response = api_instance.create_install_workflow_step_approval_response(install_workflow_id, install_workflow_step_id, approval_id, service_create_workflow_step_approval_response_request)
        print("The response of InstallsApi->create_install_workflow_step_approval_response:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->create_install_workflow_step_approval_response: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_workflow_id** | **str**| workflow id | 
 **install_workflow_step_id** | **str**| step id | 
 **approval_id** | **str**| approval id | 
 **service_create_workflow_step_approval_response_request** | [**ServiceCreateWorkflowStepApprovalResponseRequest**](ServiceCreateWorkflowStepApprovalResponseRequest.md)| Input | 

### Return type

[**AppWorkflowStepApprovalResponse**](AppWorkflowStepApprovalResponse.md)

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

# **create_workflow_step_approval_response**
> AppWorkflowStepApprovalResponse create_workflow_step_approval_response(workflow_id, workflow_step_id, approval_id, service_create_workflow_step_approval_response_request)

deploy a build to an install

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_workflow_step_approval_response import AppWorkflowStepApprovalResponse
from nuon.models.service_create_workflow_step_approval_response_request import ServiceCreateWorkflowStepApprovalResponseRequest
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
    api_instance = nuon.InstallsApi(api_client)
    workflow_id = 'workflow_id_example' # str | workflow id
    workflow_step_id = 'workflow_step_id_example' # str | step id
    approval_id = 'approval_id_example' # str | approval id
    service_create_workflow_step_approval_response_request = nuon.ServiceCreateWorkflowStepApprovalResponseRequest() # ServiceCreateWorkflowStepApprovalResponseRequest | Input

    try:
        # deploy a build to an install
        api_response = api_instance.create_workflow_step_approval_response(workflow_id, workflow_step_id, approval_id, service_create_workflow_step_approval_response_request)
        print("The response of InstallsApi->create_workflow_step_approval_response:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->create_workflow_step_approval_response: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **str**| workflow id | 
 **workflow_step_id** | **str**| step id | 
 **approval_id** | **str**| approval id | 
 **service_create_workflow_step_approval_response_request** | [**ServiceCreateWorkflowStepApprovalResponseRequest**](ServiceCreateWorkflowStepApprovalResponseRequest.md)| Input | 

### Return type

[**AppWorkflowStepApprovalResponse**](AppWorkflowStepApprovalResponse.md)

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

# **deploy_install_components**
> str deploy_install_components(install_id, service_deploy_install_components_request=service_deploy_install_components_request)

deploy all components on an install

Deploy all components to an install.  This walks the graph order of the install's app, and will trigger a deploy for each on the specified install. 

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.service_deploy_install_components_request import ServiceDeployInstallComponentsRequest
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
    api_instance = nuon.InstallsApi(api_client)
    install_id = 'install_id_example' # str | install ID
    service_deploy_install_components_request = nuon.ServiceDeployInstallComponentsRequest() # ServiceDeployInstallComponentsRequest | Input (optional)

    try:
        # deploy all components on an install
        api_response = api_instance.deploy_install_components(install_id, service_deploy_install_components_request=service_deploy_install_components_request)
        print("The response of InstallsApi->deploy_install_components:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->deploy_install_components: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **str**| install ID | 
 **service_deploy_install_components_request** | [**ServiceDeployInstallComponentsRequest**](ServiceDeployInstallComponentsRequest.md)| Input | [optional] 

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

# **deprovision_install**
> str deprovision_install(install_id, service_deprovision_install_request)

deprovision an install

Deprovision an install sandbox. 

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.service_deprovision_install_request import ServiceDeprovisionInstallRequest
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
    api_instance = nuon.InstallsApi(api_client)
    install_id = 'install_id_example' # str | install ID
    service_deprovision_install_request = nuon.ServiceDeprovisionInstallRequest() # ServiceDeprovisionInstallRequest | Input

    try:
        # deprovision an install
        api_response = api_instance.deprovision_install(install_id, service_deprovision_install_request)
        print("The response of InstallsApi->deprovision_install:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->deprovision_install: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **str**| install ID | 
 **service_deprovision_install_request** | [**ServiceDeprovisionInstallRequest**](ServiceDeprovisionInstallRequest.md)| Input | 

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

# **deprovision_install_sandbox**
> str deprovision_install_sandbox(install_id, service_deprovision_install_sandbox_request)

deprovision an install

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.service_deprovision_install_sandbox_request import ServiceDeprovisionInstallSandboxRequest
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
    api_instance = nuon.InstallsApi(api_client)
    install_id = 'install_id_example' # str | install ID
    service_deprovision_install_sandbox_request = nuon.ServiceDeprovisionInstallSandboxRequest() # ServiceDeprovisionInstallSandboxRequest | Input

    try:
        # deprovision an install
        api_response = api_instance.deprovision_install_sandbox(install_id, service_deprovision_install_sandbox_request)
        print("The response of InstallsApi->deprovision_install_sandbox:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->deprovision_install_sandbox: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **str**| install ID | 
 **service_deprovision_install_sandbox_request** | [**ServiceDeprovisionInstallSandboxRequest**](ServiceDeprovisionInstallSandboxRequest.md)| Input | 

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

# **forget_install**
> bool forget_install(install_id, body)

forget an install

Forget an install that has been deleted outside of nuon.  This should only be used in cases where an install was broken in an unordinary way and needs to be manually deleted so the parent resources can be deleted. 

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
    api_instance = nuon.InstallsApi(api_client)
    install_id = 'install_id_example' # str | install ID
    body = None # object | Input

    try:
        # forget an install
        api_response = api_instance.forget_install(install_id, body)
        print("The response of InstallsApi->forget_install:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->forget_install: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **str**| install ID | 
 **body** | **object**| Input | 

### Return type

**bool**

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
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_installs**
> List[AppInstall] get_app_installs(app_id, q=q, offset=offset, limit=limit, page=page, x_nuon_pagination_enabled=x_nuon_pagination_enabled)

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
    api_instance = nuon.InstallsApi(api_client)
    app_id = 'app_id_example' # str | app ID
    q = 'q_example' # str | search query (optional)
    offset = 0 # int | offset of results to return (optional) (default to 0)
    limit = 10 # int | limit of results to return (optional) (default to 10)
    page = 0 # int | page number of results to return (optional) (default to 0)
    x_nuon_pagination_enabled = True # bool | Enable pagination (optional)

    try:
        # get all installs for an app
        api_response = api_instance.get_app_installs(app_id, q=q, offset=offset, limit=limit, page=page, x_nuon_pagination_enabled=x_nuon_pagination_enabled)
        print("The response of InstallsApi->get_app_installs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->get_app_installs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| app ID | 
 **q** | **str**| search query | [optional] 
 **offset** | **int**| offset of results to return | [optional] [default to 0]
 **limit** | **int**| limit of results to return | [optional] [default to 10]
 **page** | **int**| page number of results to return | [optional] [default to 0]
 **x_nuon_pagination_enabled** | **bool**| Enable pagination | [optional] 

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

Forget an install that has been deleted outside of nuon.  This should only be used in cases where an install was broken in an unordinary way and needs to be manually deleted so the parent resources can be deleted. 

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

# **get_install_action_workflow**
> AppInstallActionWorkflow get_install_action_workflow(install_id, action_workflow_id)

get an install action workflow

Get an install action workflow. 

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_install_action_workflow import AppInstallActionWorkflow
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
    api_instance = nuon.InstallsApi(api_client)
    install_id = 'install_id_example' # str | install ID
    action_workflow_id = 'action_workflow_id_example' # str | workflow ID

    try:
        # get an install action workflow
        api_response = api_instance.get_install_action_workflow(install_id, action_workflow_id)
        print("The response of InstallsApi->get_install_action_workflow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->get_install_action_workflow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **str**| install ID | 
 **action_workflow_id** | **str**| workflow ID | 

### Return type

[**AppInstallActionWorkflow**](AppInstallActionWorkflow.md)

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

# **get_install_action_workflows**
> List[AppInstallActionWorkflow] get_install_action_workflows(install_id, offset=offset, limit=limit, page=page, x_nuon_pagination_enabled=x_nuon_pagination_enabled)

get an installs action workflows

Get install action workflows. 

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_install_action_workflow import AppInstallActionWorkflow
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
    api_instance = nuon.InstallsApi(api_client)
    install_id = 'install_id_example' # str | install ID
    offset = 0 # int | offset of results to return (optional) (default to 0)
    limit = 10 # int | limit of results to return (optional) (default to 10)
    page = 0 # int | page number of results to return (optional) (default to 0)
    x_nuon_pagination_enabled = True # bool | Enable pagination (optional)

    try:
        # get an installs action workflows
        api_response = api_instance.get_install_action_workflows(install_id, offset=offset, limit=limit, page=page, x_nuon_pagination_enabled=x_nuon_pagination_enabled)
        print("The response of InstallsApi->get_install_action_workflows:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->get_install_action_workflows: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **str**| install ID | 
 **offset** | **int**| offset of results to return | [optional] [default to 0]
 **limit** | **int**| limit of results to return | [optional] [default to 10]
 **page** | **int**| page number of results to return | [optional] [default to 0]
 **x_nuon_pagination_enabled** | **bool**| Enable pagination | [optional] 

### Return type

[**List[AppInstallActionWorkflow]**](AppInstallActionWorkflow.md)

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

# **get_install_audit_logs**
> List[AppInstallAuditLog] get_install_audit_logs(install_id, start, end)

get install audit logs

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_install_audit_log import AppInstallAuditLog
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
    api_instance = nuon.InstallsApi(api_client)
    install_id = 'install_id_example' # str | install ID
    start = 'start_example' # str | start timestamp for audit log range
    end = 'end_example' # str | end timestamp for audit log range

    try:
        # get install audit logs
        api_response = api_instance.get_install_audit_logs(install_id, start, end)
        print("The response of InstallsApi->get_install_audit_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->get_install_audit_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **str**| install ID | 
 **start** | **str**| start timestamp for audit log range | 
 **end** | **str**| end timestamp for audit log range | 

### Return type

[**List[AppInstallAuditLog]**](AppInstallAuditLog.md)

### Authorization

[APIKey](../README.md#APIKey), [OrgID](../README.md#OrgID)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv

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
> List[AppInstallDeploy] get_install_component_deploys(install_id, component_id, offset=offset, limit=limit, page=page, x_nuon_pagination_enabled=x_nuon_pagination_enabled)

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
    api_instance = nuon.InstallsApi(api_client)
    install_id = 'install_id_example' # str | install ID
    component_id = 'component_id_example' # str | component ID
    offset = 0 # int | offset of results to return (optional) (default to 0)
    limit = 10 # int | limit of results to return (optional) (default to 10)
    page = 0 # int | page number of results to return (optional) (default to 0)
    x_nuon_pagination_enabled = True # bool | Enable pagination (optional)

    try:
        # get an install components deploys
        api_response = api_instance.get_install_component_deploys(install_id, component_id, offset=offset, limit=limit, page=page, x_nuon_pagination_enabled=x_nuon_pagination_enabled)
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
 **offset** | **int**| offset of results to return | [optional] [default to 0]
 **limit** | **int**| limit of results to return | [optional] [default to 10]
 **page** | **int**| page number of results to return | [optional] [default to 0]
 **x_nuon_pagination_enabled** | **bool**| Enable pagination | [optional] 

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

# **get_install_component_outputs**
> Dict[str, object] get_install_component_outputs(install_id, component_id)

get an install component outputs

Return the latest outputs for a component.  **NOTE** requires a valid install. 

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
    api_instance = nuon.InstallsApi(api_client)
    install_id = 'install_id_example' # str | install ID
    component_id = 'component_id_example' # str | component ID

    try:
        # get an install component outputs
        api_response = api_instance.get_install_component_outputs(install_id, component_id)
        print("The response of InstallsApi->get_install_component_outputs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->get_install_component_outputs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **str**| install ID | 
 **component_id** | **str**| component ID | 

### Return type

**Dict[str, object]**

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
> List[AppInstallComponent] get_install_components(install_id, offset=offset, limit=limit, x_nuon_pagination_enabled=x_nuon_pagination_enabled)

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
    api_instance = nuon.InstallsApi(api_client)
    install_id = 'install_id_example' # str | install ID
    offset = 0 # int | offset of results to return (optional) (default to 0)
    limit = 10 # int | limit of results to return (optional) (default to 10)
    x_nuon_pagination_enabled = True # bool | Enable pagination (optional)

    try:
        # get an installs components
        api_response = api_instance.get_install_components(install_id, offset=offset, limit=limit, x_nuon_pagination_enabled=x_nuon_pagination_enabled)
        print("The response of InstallsApi->get_install_components:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->get_install_components: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **str**| install ID | 
 **offset** | **int**| offset of results to return | [optional] [default to 0]
 **limit** | **int**| limit of results to return | [optional] [default to 10]
 **x_nuon_pagination_enabled** | **bool**| Enable pagination | [optional] 

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

# **get_install_components_summary**
> List[AppInstallComponentSummary] get_install_components_summary(install_id, types=types, offset=offset, limit=limit, page=page, q=q, x_nuon_pagination_enabled=x_nuon_pagination_enabled)

get an installs components summary

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_install_component_summary import AppInstallComponentSummary
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
    api_instance = nuon.InstallsApi(api_client)
    install_id = 'install_id_example' # str | install ID
    types = 'types_example' # str | component types to filter by (optional)
    offset = 0 # int | offset of results to return (optional) (default to 0)
    limit = 10 # int | limit of results to return (optional) (default to 10)
    page = 0 # int | page number of results to return (optional) (default to 0)
    q = 'q_example' # str | search query for component name (optional)
    x_nuon_pagination_enabled = True # bool | Enable pagination (optional)

    try:
        # get an installs components summary
        api_response = api_instance.get_install_components_summary(install_id, types=types, offset=offset, limit=limit, page=page, q=q, x_nuon_pagination_enabled=x_nuon_pagination_enabled)
        print("The response of InstallsApi->get_install_components_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->get_install_components_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **str**| install ID | 
 **types** | **str**| component types to filter by | [optional] 
 **offset** | **int**| offset of results to return | [optional] [default to 0]
 **limit** | **int**| limit of results to return | [optional] [default to 10]
 **page** | **int**| page number of results to return | [optional] [default to 0]
 **q** | **str**| search query for component name | [optional] 
 **x_nuon_pagination_enabled** | **bool**| Enable pagination | [optional] 

### Return type

[**List[AppInstallComponentSummary]**](AppInstallComponentSummary.md)

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

# **get_install_deploys**
> List[AppInstallDeploy] get_install_deploys(install_id, offset=offset, limit=limit, page=page, x_nuon_pagination_enabled=x_nuon_pagination_enabled)

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
    api_instance = nuon.InstallsApi(api_client)
    install_id = 'install_id_example' # str | install ID
    offset = 0 # int | offset of results to return (optional) (default to 0)
    limit = 10 # int | limit of results to return (optional) (default to 10)
    page = 0 # int | page number of results to return (optional) (default to 0)
    x_nuon_pagination_enabled = True # bool | Enable pagination (optional)

    try:
        # get all deploys to an install
        api_response = api_instance.get_install_deploys(install_id, offset=offset, limit=limit, page=page, x_nuon_pagination_enabled=x_nuon_pagination_enabled)
        print("The response of InstallsApi->get_install_deploys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->get_install_deploys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **str**| install ID | 
 **offset** | **int**| offset of results to return | [optional] [default to 0]
 **limit** | **int**| limit of results to return | [optional] [default to 10]
 **page** | **int**| page number of results to return | [optional] [default to 0]
 **x_nuon_pagination_enabled** | **bool**| Enable pagination | [optional] 

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
> List[AppInstallEvent] get_install_events(install_id, offset=offset, limit=limit, page=page, x_nuon_pagination_enabled=x_nuon_pagination_enabled)

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
    api_instance = nuon.InstallsApi(api_client)
    install_id = 'install_id_example' # str | install ID
    offset = 0 # int | offset of results to return (optional) (default to 0)
    limit = 10 # int | limit of results to return (optional) (default to 10)
    page = 0 # int | page number of results to return (optional) (default to 0)
    x_nuon_pagination_enabled = True # bool | Enable pagination (optional)

    try:
        # get events for an install
        api_response = api_instance.get_install_events(install_id, offset=offset, limit=limit, page=page, x_nuon_pagination_enabled=x_nuon_pagination_enabled)
        print("The response of InstallsApi->get_install_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->get_install_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **str**| install ID | 
 **offset** | **int**| offset of results to return | [optional] [default to 0]
 **limit** | **int**| limit of results to return | [optional] [default to 10]
 **page** | **int**| page number of results to return | [optional] [default to 0]
 **x_nuon_pagination_enabled** | **bool**| Enable pagination | [optional] 

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
> List[AppInstallInputs] get_install_inputs(install_id, offset=offset, limit=limit, page=page, x_nuon_pagination_enabled=x_nuon_pagination_enabled)

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
    api_instance = nuon.InstallsApi(api_client)
    install_id = 'install_id_example' # str | install ID
    offset = 0 # int | offset of results to return (optional) (default to 0)
    limit = 10 # int | limit of results to return (optional) (default to 10)
    page = 0 # int | page number of results to return (optional) (default to 0)
    x_nuon_pagination_enabled = True # bool | Enable pagination (optional)

    try:
        # get an installs inputs
        api_response = api_instance.get_install_inputs(install_id, offset=offset, limit=limit, page=page, x_nuon_pagination_enabled=x_nuon_pagination_enabled)
        print("The response of InstallsApi->get_install_inputs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->get_install_inputs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **str**| install ID | 
 **offset** | **int**| offset of results to return | [optional] [default to 0]
 **limit** | **int**| limit of results to return | [optional] [default to 10]
 **page** | **int**| page number of results to return | [optional] [default to 0]
 **x_nuon_pagination_enabled** | **bool**| Enable pagination | [optional] 

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

# **get_install_readme**
> ServiceReadme get_install_readme(install_id)

get install readme rendered with

Returns the `app.readme` markdown with the values interpolated from the install inputs and component outputs. 

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.service_readme import ServiceReadme
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
    api_instance = nuon.InstallsApi(api_client)
    install_id = 'install_id_example' # str | install ID

    try:
        # get install readme rendered with
        api_response = api_instance.get_install_readme(install_id)
        print("The response of InstallsApi->get_install_readme:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->get_install_readme: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **str**| install ID | 

### Return type

[**ServiceReadme**](ServiceReadme.md)

### Authorization

[APIKey](../README.md#APIKey), [OrgID](../README.md#OrgID)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**206** | Partial Content |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_install_runner_group**
> AppRunnerGroup get_install_runner_group(install_id)

Get an install's runner group

Return the runner group, including runners and settings for the provided install. 

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_runner_group import AppRunnerGroup
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
    api_instance = nuon.InstallsApi(api_client)
    install_id = 'install_id_example' # str | install ID

    try:
        # Get an install's runner group
        api_response = api_instance.get_install_runner_group(install_id)
        print("The response of InstallsApi->get_install_runner_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->get_install_runner_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **str**| install ID | 

### Return type

[**AppRunnerGroup**](AppRunnerGroup.md)

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

# **get_install_sandbox_run**
> AppInstallSandboxRun get_install_sandbox_run(run_id)

get an install sandbox run

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
    api_instance = nuon.InstallsApi(api_client)
    run_id = 'run_id_example' # str | run ID

    try:
        # get an install sandbox run
        api_response = api_instance.get_install_sandbox_run(run_id)
        print("The response of InstallsApi->get_install_sandbox_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->get_install_sandbox_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| run ID | 

### Return type

[**AppInstallSandboxRun**](AppInstallSandboxRun.md)

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
> List[AppInstallSandboxRun] get_install_sandbox_runs(install_id, offset=offset, limit=limit, page=page, x_nuon_pagination_enabled=x_nuon_pagination_enabled)

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
    api_instance = nuon.InstallsApi(api_client)
    install_id = 'install_id_example' # str | install ID
    offset = 0 # int | offset of results to return (optional) (default to 0)
    limit = 10 # int | limit of results to return (optional) (default to 10)
    page = 0 # int | page number of results to return (optional) (default to 0)
    x_nuon_pagination_enabled = True # bool | Enable pagination (optional)

    try:
        # get an installs sandbox runs
        api_response = api_instance.get_install_sandbox_runs(install_id, offset=offset, limit=limit, page=page, x_nuon_pagination_enabled=x_nuon_pagination_enabled)
        print("The response of InstallsApi->get_install_sandbox_runs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->get_install_sandbox_runs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **str**| install ID | 
 **offset** | **int**| offset of results to return | [optional] [default to 0]
 **limit** | **int**| limit of results to return | [optional] [default to 10]
 **page** | **int**| page number of results to return | [optional] [default to 0]
 **x_nuon_pagination_enabled** | **bool**| Enable pagination | [optional] 

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

# **get_install_stack**
> AppInstallStack get_install_stack(stack_id)

get an install stack by stack ID

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_install_stack import AppInstallStack
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
    api_instance = nuon.InstallsApi(api_client)
    stack_id = 'stack_id_example' # str | stack ID

    try:
        # get an install stack by stack ID
        api_response = api_instance.get_install_stack(stack_id)
        print("The response of InstallsApi->get_install_stack:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->get_install_stack: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_id** | **str**| stack ID | 

### Return type

[**AppInstallStack**](AppInstallStack.md)

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

# **get_install_stack_by_install_id**
> AppInstallStack get_install_stack_by_install_id(install_id)

get an install stack by install ID

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_install_stack import AppInstallStack
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
    api_instance = nuon.InstallsApi(api_client)
    install_id = 'install_id_example' # str | install ID

    try:
        # get an install stack by install ID
        api_response = api_instance.get_install_stack_by_install_id(install_id)
        print("The response of InstallsApi->get_install_stack_by_install_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->get_install_stack_by_install_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **str**| install ID | 

### Return type

[**AppInstallStack**](AppInstallStack.md)

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

# **get_install_stack_runs**
> AppInstallStackVersionRun get_install_stack_runs(install_id)

get an install's stack runs

get install stack runs

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_install_stack_version_run import AppInstallStackVersionRun
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
    api_instance = nuon.InstallsApi(api_client)
    install_id = 'install_id_example' # str | install ID

    try:
        # get an install's stack runs
        api_response = api_instance.get_install_stack_runs(install_id)
        print("The response of InstallsApi->get_install_stack_runs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->get_install_stack_runs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **str**| install ID | 

### Return type

[**AppInstallStackVersionRun**](AppInstallStackVersionRun.md)

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

# **get_install_state**
> GithubComPowertoolsdevMonoPkgTypesStateState get_install_state(install_id)

Get the current state of an install.

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.github_com_powertoolsdev_mono_pkg_types_state_state import GithubComPowertoolsdevMonoPkgTypesStateState
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
    api_instance = nuon.InstallsApi(api_client)
    install_id = 'install_id_example' # str | install ID

    try:
        # Get the current state of an install.
        api_response = api_instance.get_install_state(install_id)
        print("The response of InstallsApi->get_install_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->get_install_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **str**| install ID | 

### Return type

[**GithubComPowertoolsdevMonoPkgTypesStateState**](GithubComPowertoolsdevMonoPkgTypesStateState.md)

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

# **get_install_workflow**
> AppWorkflow get_install_workflow(install_workflow_id)

get an install workflow

Return a workflow. 

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_workflow import AppWorkflow
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
    api_instance = nuon.InstallsApi(api_client)
    install_workflow_id = 'install_workflow_id_example' # str | install workflow ID

    try:
        # get an install workflow
        api_response = api_instance.get_install_workflow(install_workflow_id)
        print("The response of InstallsApi->get_install_workflow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->get_install_workflow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_workflow_id** | **str**| install workflow ID | 

### Return type

[**AppWorkflow**](AppWorkflow.md)

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

# **get_install_workflow_step**
> AppWorkflowStep get_install_workflow_step(install_workflow_id, install_workflow_step_id)

get an install workflow step

Return a single workflow step. 

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_workflow_step import AppWorkflowStep
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
    api_instance = nuon.InstallsApi(api_client)
    install_workflow_id = 'install_workflow_id_example' # str | workflow id
    install_workflow_step_id = 'install_workflow_step_id_example' # str | step id

    try:
        # get an install workflow step
        api_response = api_instance.get_install_workflow_step(install_workflow_id, install_workflow_step_id)
        print("The response of InstallsApi->get_install_workflow_step:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->get_install_workflow_step: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_workflow_id** | **str**| workflow id | 
 **install_workflow_step_id** | **str**| step id | 

### Return type

[**AppWorkflowStep**](AppWorkflowStep.md)

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

# **get_install_workflow_step_approval**
> AppWorkflowStepApproval get_install_workflow_step_approval(install_workflow_id, install_workflow_step_id, approval_id)

get an install workflow step approval

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_workflow_step_approval import AppWorkflowStepApproval
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
    api_instance = nuon.InstallsApi(api_client)
    install_workflow_id = 'install_workflow_id_example' # str | workflow id
    install_workflow_step_id = 'install_workflow_step_id_example' # str | step id
    approval_id = 'approval_id_example' # str | approval id

    try:
        # get an install workflow step approval
        api_response = api_instance.get_install_workflow_step_approval(install_workflow_id, install_workflow_step_id, approval_id)
        print("The response of InstallsApi->get_install_workflow_step_approval:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->get_install_workflow_step_approval: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_workflow_id** | **str**| workflow id | 
 **install_workflow_step_id** | **str**| step id | 
 **approval_id** | **str**| approval id | 

### Return type

[**AppWorkflowStepApproval**](AppWorkflowStepApproval.md)

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

# **get_install_workflow_steps**
> List[AppWorkflowStep] get_install_workflow_steps(install_workflow_id)

get an install workflow step

Return all steps for a workflow. 

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_workflow_step import AppWorkflowStep
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
    api_instance = nuon.InstallsApi(api_client)
    install_workflow_id = 'install_workflow_id_example' # str | install workflow ID

    try:
        # get an install workflow step
        api_response = api_instance.get_install_workflow_steps(install_workflow_id)
        print("The response of InstallsApi->get_install_workflow_steps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->get_install_workflow_steps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_workflow_id** | **str**| install workflow ID | 

### Return type

[**List[AppWorkflowStep]**](AppWorkflowStep.md)

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
> List[AppInstall] get_org_installs(offset=offset, q=q, limit=limit, page=page, x_nuon_pagination_enabled=x_nuon_pagination_enabled)

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
    api_instance = nuon.InstallsApi(api_client)
    offset = 0 # int | offset of results to return (optional) (default to 0)
    q = 'q_example' # str | search query to filter installs by name (optional)
    limit = 10 # int | limit of results to return (optional) (default to 10)
    page = 0 # int | page number of results to return (optional) (default to 0)
    x_nuon_pagination_enabled = True # bool | Enable pagination (optional)

    try:
        # get all installs for an org
        api_response = api_instance.get_org_installs(offset=offset, q=q, limit=limit, page=page, x_nuon_pagination_enabled=x_nuon_pagination_enabled)
        print("The response of InstallsApi->get_org_installs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->get_org_installs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| offset of results to return | [optional] [default to 0]
 **q** | **str**| search query to filter installs by name | [optional] 
 **limit** | **int**| limit of results to return | [optional] [default to 10]
 **page** | **int**| page number of results to return | [optional] [default to 0]
 **x_nuon_pagination_enabled** | **bool**| Enable pagination | [optional] 

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

# **get_workflow**
> AppWorkflow get_workflow(workflow_id)

get a workflow

Return a workflow. 

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_workflow import AppWorkflow
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
    api_instance = nuon.InstallsApi(api_client)
    workflow_id = 'workflow_id_example' # str | workflow ID

    try:
        # get a workflow
        api_response = api_instance.get_workflow(workflow_id)
        print("The response of InstallsApi->get_workflow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->get_workflow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **str**| workflow ID | 

### Return type

[**AppWorkflow**](AppWorkflow.md)

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

# **get_workflow_step**
> AppWorkflowStep get_workflow_step(workflow_id, workflow_step_id)

get a workflow step

Return a single workflow step. 

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_workflow_step import AppWorkflowStep
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
    api_instance = nuon.InstallsApi(api_client)
    workflow_id = 'workflow_id_example' # str | workflow id
    workflow_step_id = 'workflow_step_id_example' # str | step id

    try:
        # get a workflow step
        api_response = api_instance.get_workflow_step(workflow_id, workflow_step_id)
        print("The response of InstallsApi->get_workflow_step:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->get_workflow_step: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **str**| workflow id | 
 **workflow_step_id** | **str**| step id | 

### Return type

[**AppWorkflowStep**](AppWorkflowStep.md)

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

# **get_workflow_step_approval**
> AppWorkflowStepApproval get_workflow_step_approval(workflow_id, workflow_step_id, approval_id)

get an workflow step approval

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_workflow_step_approval import AppWorkflowStepApproval
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
    api_instance = nuon.InstallsApi(api_client)
    workflow_id = 'workflow_id_example' # str | workflow id
    workflow_step_id = 'workflow_step_id_example' # str | step id
    approval_id = 'approval_id_example' # str | approval id

    try:
        # get an workflow step approval
        api_response = api_instance.get_workflow_step_approval(workflow_id, workflow_step_id, approval_id)
        print("The response of InstallsApi->get_workflow_step_approval:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->get_workflow_step_approval: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **str**| workflow id | 
 **workflow_step_id** | **str**| step id | 
 **approval_id** | **str**| approval id | 

### Return type

[**AppWorkflowStepApproval**](AppWorkflowStepApproval.md)

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

# **get_workflow_step_approval_contents**
> List[int] get_workflow_step_approval_contents(workflow_id, workflow_step_id, approval_id)

get a workflow step approval contents

Return the contents of a json plan for an approval (compressed). 

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
    api_instance = nuon.InstallsApi(api_client)
    workflow_id = 'workflow_id_example' # str | workflow id
    workflow_step_id = 'workflow_step_id_example' # str | step id
    approval_id = 'approval_id_example' # str | approval id

    try:
        # get a workflow step approval contents
        api_response = api_instance.get_workflow_step_approval_contents(workflow_id, workflow_step_id, approval_id)
        print("The response of InstallsApi->get_workflow_step_approval_contents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->get_workflow_step_approval_contents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **str**| workflow id | 
 **workflow_step_id** | **str**| step id | 
 **approval_id** | **str**| approval id | 

### Return type

**List[int]**

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

# **get_workflow_steps**
> List[AppWorkflowStep] get_workflow_steps(workflow_id)

get a workflow step

Return all steps for a workflow. 

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_workflow_step import AppWorkflowStep
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
    api_instance = nuon.InstallsApi(api_client)
    workflow_id = 'workflow_id_example' # str | workflow ID

    try:
        # get a workflow step
        api_response = api_instance.get_workflow_steps(workflow_id)
        print("The response of InstallsApi->get_workflow_steps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->get_workflow_steps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **str**| workflow ID | 

### Return type

[**List[AppWorkflowStep]**](AppWorkflowStep.md)

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

# **get_workflows**
> List[AppWorkflow] get_workflows(install_id, offset=offset, limit=limit, page=page, x_nuon_pagination_enabled=x_nuon_pagination_enabled)

get workflows

Return workflows for an install. 

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_workflow import AppWorkflow
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
    api_instance = nuon.InstallsApi(api_client)
    install_id = 'install_id_example' # str | install ID
    offset = 0 # int | offset of results to return (optional) (default to 0)
    limit = 10 # int | limit of results to return (optional) (default to 10)
    page = 0 # int | page number of results to return (optional) (default to 0)
    x_nuon_pagination_enabled = True # bool | Enable pagination (optional)

    try:
        # get workflows
        api_response = api_instance.get_workflows(install_id, offset=offset, limit=limit, page=page, x_nuon_pagination_enabled=x_nuon_pagination_enabled)
        print("The response of InstallsApi->get_workflows:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->get_workflows: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **str**| install ID | 
 **offset** | **int**| offset of results to return | [optional] [default to 0]
 **limit** | **int**| limit of results to return | [optional] [default to 10]
 **page** | **int**| page number of results to return | [optional] [default to 0]
 **x_nuon_pagination_enabled** | **bool**| Enable pagination | [optional] 

### Return type

[**List[AppWorkflow]**](AppWorkflow.md)

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

# **phone_home**
> str phone_home(install_id, phone_home_id, request_body)

phone home for an install

A public endpoint for phoning home from a runner AWS cloudformation stack upon successfully processing it. 

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
    api_instance = nuon.InstallsApi(api_client)
    install_id = 'install_id_example' # str | install ID
    phone_home_id = 'phone_home_id_example' # str | phone home ID
    request_body = None # Dict[str, object] | Input

    try:
        # phone home for an install
        api_response = api_instance.phone_home(install_id, phone_home_id, request_body)
        print("The response of InstallsApi->phone_home:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->phone_home: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **str**| install ID | 
 **phone_home_id** | **str**| phone home ID | 
 **request_body** | [**Dict[str, object]**](object.md)| Input | 

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

# **reprovision_install**
> str reprovision_install(install_id, service_reprovision_install_request=service_reprovision_install_request)

reprovision an install

Reprovision an install sandbox.  

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.service_reprovision_install_request import ServiceReprovisionInstallRequest
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
    api_instance = nuon.InstallsApi(api_client)
    install_id = 'install_id_example' # str | install ID
    service_reprovision_install_request = nuon.ServiceReprovisionInstallRequest() # ServiceReprovisionInstallRequest | Input (optional)

    try:
        # reprovision an install
        api_response = api_instance.reprovision_install(install_id, service_reprovision_install_request=service_reprovision_install_request)
        print("The response of InstallsApi->reprovision_install:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->reprovision_install: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **str**| install ID | 
 **service_reprovision_install_request** | [**ServiceReprovisionInstallRequest**](ServiceReprovisionInstallRequest.md)| Input | [optional] 

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

# **reprovision_install_sandbox**
> str reprovision_install_sandbox(install_id, service_reprovision_install_sandbox_request)

reprovision an install sandbox

Reprovision an install sandbox and redeploy all components on top. 

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.service_reprovision_install_sandbox_request import ServiceReprovisionInstallSandboxRequest
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
    api_instance = nuon.InstallsApi(api_client)
    install_id = 'install_id_example' # str | install ID
    service_reprovision_install_sandbox_request = nuon.ServiceReprovisionInstallSandboxRequest() # ServiceReprovisionInstallSandboxRequest | Input

    try:
        # reprovision an install sandbox
        api_response = api_instance.reprovision_install_sandbox(install_id, service_reprovision_install_sandbox_request)
        print("The response of InstallsApi->reprovision_install_sandbox:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->reprovision_install_sandbox: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **str**| install ID | 
 **service_reprovision_install_sandbox_request** | [**ServiceReprovisionInstallSandboxRequest**](ServiceReprovisionInstallSandboxRequest.md)| Input | 

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

# **retry_owner_workflow_by_id**
> ServiceRetryWorkflowByIDResponse retry_owner_workflow_by_id(workflow_id, service_retry_workflow_by_id_request)

rerun the workflow steps starting from input step id, can be used to retry a failed step

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.service_retry_workflow_by_id_request import ServiceRetryWorkflowByIDRequest
from nuon.models.service_retry_workflow_by_id_response import ServiceRetryWorkflowByIDResponse
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
    api_instance = nuon.InstallsApi(api_client)
    workflow_id = 'workflow_id_example' # str | workflow ID
    service_retry_workflow_by_id_request = nuon.ServiceRetryWorkflowByIDRequest() # ServiceRetryWorkflowByIDRequest | Input

    try:
        # rerun the workflow steps starting from input step id, can be used to retry a failed step
        api_response = api_instance.retry_owner_workflow_by_id(workflow_id, service_retry_workflow_by_id_request)
        print("The response of InstallsApi->retry_owner_workflow_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->retry_owner_workflow_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **str**| workflow ID | 
 **service_retry_workflow_by_id_request** | [**ServiceRetryWorkflowByIDRequest**](ServiceRetryWorkflowByIDRequest.md)| Input | 

### Return type

[**ServiceRetryWorkflowByIDResponse**](ServiceRetryWorkflowByIDResponse.md)

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

# **retry_workflow**
> ServiceRetryWorkflowResponse retry_workflow(install_id, service_retry_workflow_request)

rerun the workflow steps starting from input step id, can be used to retry a failed step

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.service_retry_workflow_request import ServiceRetryWorkflowRequest
from nuon.models.service_retry_workflow_response import ServiceRetryWorkflowResponse
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
    api_instance = nuon.InstallsApi(api_client)
    install_id = 'install_id_example' # str | install ID
    service_retry_workflow_request = nuon.ServiceRetryWorkflowRequest() # ServiceRetryWorkflowRequest | Input

    try:
        # rerun the workflow steps starting from input step id, can be used to retry a failed step
        api_response = api_instance.retry_workflow(install_id, service_retry_workflow_request)
        print("The response of InstallsApi->retry_workflow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->retry_workflow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **str**| install ID | 
 **service_retry_workflow_request** | [**ServiceRetryWorkflowRequest**](ServiceRetryWorkflowRequest.md)| Input | 

### Return type

[**ServiceRetryWorkflowResponse**](ServiceRetryWorkflowResponse.md)

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

# **sync_secrets**
> str sync_secrets(install_id, service_sync_secrets_request=service_sync_secrets_request)

sync secrets install

Execute the sync secrets workflow. 

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.service_sync_secrets_request import ServiceSyncSecretsRequest
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
    api_instance = nuon.InstallsApi(api_client)
    install_id = 'install_id_example' # str | install ID
    service_sync_secrets_request = nuon.ServiceSyncSecretsRequest() # ServiceSyncSecretsRequest | Input (optional)

    try:
        # sync secrets install
        api_response = api_instance.sync_secrets(install_id, service_sync_secrets_request=service_sync_secrets_request)
        print("The response of InstallsApi->sync_secrets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->sync_secrets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **str**| install ID | 
 **service_sync_secrets_request** | [**ServiceSyncSecretsRequest**](ServiceSyncSecretsRequest.md)| Input | [optional] 

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
> str teardown_install_component(install_id, component_id, service_teardown_install_component_request=service_teardown_install_component_request)

teardown an install component

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.service_teardown_install_component_request import ServiceTeardownInstallComponentRequest
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
    api_instance = nuon.InstallsApi(api_client)
    install_id = 'install_id_example' # str | install ID
    component_id = 'component_id_example' # str | component ID
    service_teardown_install_component_request = nuon.ServiceTeardownInstallComponentRequest() # ServiceTeardownInstallComponentRequest | Input (optional)

    try:
        # teardown an install component
        api_response = api_instance.teardown_install_component(install_id, component_id, service_teardown_install_component_request=service_teardown_install_component_request)
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
 **service_teardown_install_component_request** | [**ServiceTeardownInstallComponentRequest**](ServiceTeardownInstallComponentRequest.md)| Input | [optional] 

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

# **teardown_install_components**
> str teardown_install_components(install_id, service_teardown_install_components_request)

teardown an install's components

Teardown all components on an install. 

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.service_teardown_install_components_request import ServiceTeardownInstallComponentsRequest
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
    api_instance = nuon.InstallsApi(api_client)
    install_id = 'install_id_example' # str | install ID
    service_teardown_install_components_request = nuon.ServiceTeardownInstallComponentsRequest() # ServiceTeardownInstallComponentsRequest | Input

    try:
        # teardown an install's components
        api_response = api_instance.teardown_install_components(install_id, service_teardown_install_components_request)
        print("The response of InstallsApi->teardown_install_components:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->teardown_install_components: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **str**| install ID | 
 **service_teardown_install_components_request** | [**ServiceTeardownInstallComponentsRequest**](ServiceTeardownInstallComponentsRequest.md)| Input | 

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

# **update_install_config**
> AppInstallConfig update_install_config(install_id, config_id, service_update_install_config_request)

create an install config

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_install_config import AppInstallConfig
from nuon.models.service_update_install_config_request import ServiceUpdateInstallConfigRequest
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
    api_instance = nuon.InstallsApi(api_client)
    install_id = 'install_id_example' # str | install ID
    config_id = 'config_id_example' # str | config ID
    service_update_install_config_request = nuon.ServiceUpdateInstallConfigRequest() # ServiceUpdateInstallConfigRequest | Input

    try:
        # create an install config
        api_response = api_instance.update_install_config(install_id, config_id, service_update_install_config_request)
        print("The response of InstallsApi->update_install_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->update_install_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **str**| install ID | 
 **config_id** | **str**| config ID | 
 **service_update_install_config_request** | [**ServiceUpdateInstallConfigRequest**](ServiceUpdateInstallConfigRequest.md)| Input | 

### Return type

[**AppInstallConfig**](AppInstallConfig.md)

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

# **update_install_inputs**
> AppInstallInputs update_install_inputs(install_id, service_update_install_inputs_request)

Updates install input config for app

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_install_inputs import AppInstallInputs
from nuon.models.service_update_install_inputs_request import ServiceUpdateInstallInputsRequest
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
    api_instance = nuon.InstallsApi(api_client)
    install_id = 'install_id_example' # str | install ID
    service_update_install_inputs_request = nuon.ServiceUpdateInstallInputsRequest() # ServiceUpdateInstallInputsRequest | Input

    try:
        # Updates install input config for app
        api_response = api_instance.update_install_inputs(install_id, service_update_install_inputs_request)
        print("The response of InstallsApi->update_install_inputs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->update_install_inputs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **str**| install ID | 
 **service_update_install_inputs_request** | [**ServiceUpdateInstallInputsRequest**](ServiceUpdateInstallInputsRequest.md)| Input | 

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
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_install_workflow**
> AppWorkflow update_install_workflow(install_workflow_id, service_update_workflow_request)

update an install workflow

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_workflow import AppWorkflow
from nuon.models.service_update_workflow_request import ServiceUpdateWorkflowRequest
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
    api_instance = nuon.InstallsApi(api_client)
    install_workflow_id = 'install_workflow_id_example' # str | install workflow ID
    service_update_workflow_request = nuon.ServiceUpdateWorkflowRequest() # ServiceUpdateWorkflowRequest | Input

    try:
        # update an install workflow
        api_response = api_instance.update_install_workflow(install_workflow_id, service_update_workflow_request)
        print("The response of InstallsApi->update_install_workflow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->update_install_workflow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_workflow_id** | **str**| install workflow ID | 
 **service_update_workflow_request** | [**ServiceUpdateWorkflowRequest**](ServiceUpdateWorkflowRequest.md)| Input | 

### Return type

[**AppWorkflow**](AppWorkflow.md)

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

# **update_workflow**
> AppWorkflow update_workflow(workflow_id, service_update_workflow_request)

update a workflow

### Example

* Api Key Authentication (APIKey):
* Api Key Authentication (OrgID):

```python
import time
import os
import nuon
from nuon.models.app_workflow import AppWorkflow
from nuon.models.service_update_workflow_request import ServiceUpdateWorkflowRequest
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
    api_instance = nuon.InstallsApi(api_client)
    workflow_id = 'workflow_id_example' # str | workflow ID
    service_update_workflow_request = nuon.ServiceUpdateWorkflowRequest() # ServiceUpdateWorkflowRequest | Input

    try:
        # update a workflow
        api_response = api_instance.update_workflow(workflow_id, service_update_workflow_request)
        print("The response of InstallsApi->update_workflow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->update_workflow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **str**| workflow ID | 
 **service_update_workflow_request** | [**ServiceUpdateWorkflowRequest**](ServiceUpdateWorkflowRequest.md)| Input | 

### Return type

[**AppWorkflow**](AppWorkflow.md)

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

