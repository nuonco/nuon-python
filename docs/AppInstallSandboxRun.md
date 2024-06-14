# AppInstallSandboxRun


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_sandbox_config** | [**AppAppSandboxConfig**](AppAppSandboxConfig.md) |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by** | [**AppAccount**](AppAccount.md) |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**install_id** | **str** |  | [optional] 
**run_type** | [**AppSandboxRunType**](AppSandboxRunType.md) |  | [optional] 
**status** | **str** |  | [optional] 
**status_description** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_install_sandbox_run import AppInstallSandboxRun

# TODO update the JSON string below
json = "{}"
# create an instance of AppInstallSandboxRun from a JSON string
app_install_sandbox_run_instance = AppInstallSandboxRun.from_json(json)
# print the JSON string representation of the object
print AppInstallSandboxRun.to_json()

# convert the object into a dict
app_install_sandbox_run_dict = app_install_sandbox_run_instance.to_dict()
# create an instance of AppInstallSandboxRun from a dict
app_install_sandbox_run_form_dict = app_install_sandbox_run.from_dict(app_install_sandbox_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


