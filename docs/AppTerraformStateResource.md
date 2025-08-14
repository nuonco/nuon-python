# AppTerraformStateResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instances** | [**List[AppTerraformStateInstance]**](AppTerraformStateInstance.md) |  | [optional] 
**mode** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**provider** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_terraform_state_resource import AppTerraformStateResource

# TODO update the JSON string below
json = "{}"
# create an instance of AppTerraformStateResource from a JSON string
app_terraform_state_resource_instance = AppTerraformStateResource.from_json(json)
# print the JSON string representation of the object
print AppTerraformStateResource.to_json()

# convert the object into a dict
app_terraform_state_resource_dict = app_terraform_state_resource_instance.to_dict()
# create an instance of AppTerraformStateResource from a dict
app_terraform_state_resource_form_dict = app_terraform_state_resource.from_dict(app_terraform_state_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


