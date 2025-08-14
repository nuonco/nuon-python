# AppTerraformStateInstance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | **Dict[str, object]** |  | [optional] 
**schema_version** | **int** |  | [optional] 
**sensitive_attributes** | **List[object]** |  | [optional] 

## Example

```python
from nuon.models.app_terraform_state_instance import AppTerraformStateInstance

# TODO update the JSON string below
json = "{}"
# create an instance of AppTerraformStateInstance from a JSON string
app_terraform_state_instance_instance = AppTerraformStateInstance.from_json(json)
# print the JSON string representation of the object
print AppTerraformStateInstance.to_json()

# convert the object into a dict
app_terraform_state_instance_dict = app_terraform_state_instance_instance.to_dict()
# create an instance of AppTerraformStateInstance from a dict
app_terraform_state_instance_form_dict = app_terraform_state_instance.from_dict(app_terraform_state_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


