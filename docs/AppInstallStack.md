# AppInstallStack


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**install_id** | **str** |  | [optional] 
**install_stack_outputs** | [**AppInstallStackOutputs**](AppInstallStackOutputs.md) |  | [optional] 
**org_id** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**versions** | [**List[AppInstallStackVersion]**](AppInstallStackVersion.md) |  | [optional] 

## Example

```python
from nuon.models.app_install_stack import AppInstallStack

# TODO update the JSON string below
json = "{}"
# create an instance of AppInstallStack from a JSON string
app_install_stack_instance = AppInstallStack.from_json(json)
# print the JSON string representation of the object
print AppInstallStack.to_json()

# convert the object into a dict
app_install_stack_dict = app_install_stack_instance.to_dict()
# create an instance of AppInstallStack from a dict
app_install_stack_form_dict = app_install_stack.from_dict(app_install_stack_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


