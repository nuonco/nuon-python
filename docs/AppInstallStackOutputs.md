# AppInstallStackOutputs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws** | [**AppAWSStackOutputs**](AppAWSStackOutputs.md) |  | [optional] 
**azure** | [**AppAzureStackOutputs**](AppAzureStackOutputs.md) |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**data** | **Dict[str, str]** |  | [optional] 
**id** | **str** |  | [optional] 
**install_stack_id** | **str** |  | [optional] 
**install_version_run_id** | **str** |  | [optional] 
**org_id** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_install_stack_outputs import AppInstallStackOutputs

# TODO update the JSON string below
json = "{}"
# create an instance of AppInstallStackOutputs from a JSON string
app_install_stack_outputs_instance = AppInstallStackOutputs.from_json(json)
# print the JSON string representation of the object
print AppInstallStackOutputs.to_json()

# convert the object into a dict
app_install_stack_outputs_dict = app_install_stack_outputs_instance.to_dict()
# create an instance of AppInstallStackOutputs from a dict
app_install_stack_outputs_form_dict = app_install_stack_outputs.from_dict(app_install_stack_outputs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


