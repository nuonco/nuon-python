# AppInstall


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** |  | [optional] 
**app_runner_config** | [**AppAppRunnerConfig**](AppAppRunnerConfig.md) |  | [optional] 
**app_sandbox_config** | [**AppAppSandboxConfig**](AppAppSandboxConfig.md) |  | [optional] 
**aws_account** | [**AppAWSAccount**](AppAWSAccount.md) |  | [optional] 
**azure_account** | [**AppAzureAccount**](AppAzureAccount.md) |  | [optional] 
**component_statuses** | **Dict[str, str]** |  | [optional] 
**composite_component_status** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by** | [**AppAccount**](AppAccount.md) |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**install_components** | [**List[AppInstallComponent]**](AppInstallComponent.md) |  | [optional] 
**install_events** | [**List[AppInstallEvent]**](AppInstallEvent.md) |  | [optional] 
**install_inputs** | [**List[AppInstallInputs]**](AppInstallInputs.md) |  | [optional] 
**install_number** | **int** |  | [optional] 
**install_sandbox_runs** | [**List[AppInstallSandboxRun]**](AppInstallSandboxRun.md) |  | [optional] 
**name** | **str** |  | [optional] 
**runner_status** | **str** |  | [optional] 
**sandbox_status** | **str** |  | [optional] 
**status** | **str** | TODO(jm): deprecate these fields once the terraform provider has been updated | [optional] 
**status_description** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_install import AppInstall

# TODO update the JSON string below
json = "{}"
# create an instance of AppInstall from a JSON string
app_install_instance = AppInstall.from_json(json)
# print the JSON string representation of the object
print AppInstall.to_json()

# convert the object into a dict
app_install_dict = app_install_instance.to_dict()
# create an instance of AppInstall from a dict
app_install_form_dict = app_install.from_dict(app_install_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


