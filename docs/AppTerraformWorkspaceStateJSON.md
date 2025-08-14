# AppTerraformWorkspaceStateJSON


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contents** | **List[int]** |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**runner_job** | [**AppRunnerJob**](AppRunnerJob.md) |  | [optional] 
**runner_job_id** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**workspace_id** | **str** | Foreign key to TerraformWorkspace with unique constraint to prevent conflicting states for a workspace | [optional] 

## Example

```python
from nuon.models.app_terraform_workspace_state_json import AppTerraformWorkspaceStateJSON

# TODO update the JSON string below
json = "{}"
# create an instance of AppTerraformWorkspaceStateJSON from a JSON string
app_terraform_workspace_state_json_instance = AppTerraformWorkspaceStateJSON.from_json(json)
# print the JSON string representation of the object
print AppTerraformWorkspaceStateJSON.to_json()

# convert the object into a dict
app_terraform_workspace_state_json_dict = app_terraform_workspace_state_json_instance.to_dict()
# create an instance of AppTerraformWorkspaceStateJSON from a dict
app_terraform_workspace_state_json_form_dict = app_terraform_workspace_state_json.from_dict(app_terraform_workspace_state_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


