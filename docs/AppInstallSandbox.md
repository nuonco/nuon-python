# AppInstallSandbox


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**install_id** | **str** |  | [optional] 
**install_sandbox_runs** | [**List[AppInstallSandboxRun]**](AppInstallSandboxRun.md) |  | [optional] 
**status** | **str** |  | [optional] 
**status_description** | **str** |  | [optional] 
**status_v2** | [**AppCompositeStatus**](AppCompositeStatus.md) |  | [optional] 
**terraform_workspace** | [**AppTerraformWorkspace**](AppTerraformWorkspace.md) |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_install_sandbox import AppInstallSandbox

# TODO update the JSON string below
json = "{}"
# create an instance of AppInstallSandbox from a JSON string
app_install_sandbox_instance = AppInstallSandbox.from_json(json)
# print the JSON string representation of the object
print AppInstallSandbox.to_json()

# convert the object into a dict
app_install_sandbox_dict = app_install_sandbox_instance.to_dict()
# create an instance of AppInstallSandbox from a dict
app_install_sandbox_form_dict = app_install_sandbox.from_dict(app_install_sandbox_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


