# AppTerraformWorkspaceState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contents** | **List[int]** |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**org_id** | **str** |  | [optional] 
**revision** | **int** |  | [optional] 
**runner_job** | [**AppRunnerJob**](AppRunnerJob.md) |  | [optional] 
**runner_job_id** | **str** |  | [optional] 
**terraform_workspace** | [**AppTerraformWorkspace**](AppTerraformWorkspace.md) |  | [optional] 
**terraform_workspace_id** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_terraform_workspace_state import AppTerraformWorkspaceState

# TODO update the JSON string below
json = "{}"
# create an instance of AppTerraformWorkspaceState from a JSON string
app_terraform_workspace_state_instance = AppTerraformWorkspaceState.from_json(json)
# print the JSON string representation of the object
print AppTerraformWorkspaceState.to_json()

# convert the object into a dict
app_terraform_workspace_state_dict = app_terraform_workspace_state_instance.to_dict()
# create an instance of AppTerraformWorkspaceState from a dict
app_terraform_workspace_state_form_dict = app_terraform_workspace_state.from_dict(app_terraform_workspace_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


