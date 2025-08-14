# AppAppBranch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** |  | [optional] 
**connected_github_vcs_config_id** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**org_id** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**workflows** | [**List[AppWorkflow]**](AppWorkflow.md) |  | [optional] 

## Example

```python
from nuon.models.app_app_branch import AppAppBranch

# TODO update the JSON string below
json = "{}"
# create an instance of AppAppBranch from a JSON string
app_app_branch_instance = AppAppBranch.from_json(json)
# print the JSON string representation of the object
print AppAppBranch.to_json()

# convert the object into a dict
app_app_branch_dict = app_app_branch_instance.to_dict()
# create an instance of AppAppBranch from a dict
app_app_branch_form_dict = app_app_branch.from_dict(app_app_branch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


