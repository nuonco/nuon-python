# AppTerraformWorkspace


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**org_id** | **str** |  | [optional] 
**owner_id** | **str** |  | [optional] 
**owner_type** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_terraform_workspace import AppTerraformWorkspace

# TODO update the JSON string below
json = "{}"
# create an instance of AppTerraformWorkspace from a JSON string
app_terraform_workspace_instance = AppTerraformWorkspace.from_json(json)
# print the JSON string representation of the object
print AppTerraformWorkspace.to_json()

# convert the object into a dict
app_terraform_workspace_dict = app_terraform_workspace_instance.to_dict()
# create an instance of AppTerraformWorkspace from a dict
app_terraform_workspace_form_dict = app_terraform_workspace.from_dict(app_terraform_workspace_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


