# AppTerraformWorkspaceLock


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**lock** | [**AppTerraformLock**](AppTerraformLock.md) |  | [optional] 
**runner_job** | [**AppRunnerJob**](AppRunnerJob.md) |  | [optional] 
**runner_job_id** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**workspace_id** | **str** | Foreign key to TerraformWorkspace with unique constraint to prevent multiple active locks | [optional] 

## Example

```python
from nuon.models.app_terraform_workspace_lock import AppTerraformWorkspaceLock

# TODO update the JSON string below
json = "{}"
# create an instance of AppTerraformWorkspaceLock from a JSON string
app_terraform_workspace_lock_instance = AppTerraformWorkspaceLock.from_json(json)
# print the JSON string representation of the object
print AppTerraformWorkspaceLock.to_json()

# convert the object into a dict
app_terraform_workspace_lock_dict = app_terraform_workspace_lock_instance.to_dict()
# create an instance of AppTerraformWorkspaceLock from a dict
app_terraform_workspace_lock_form_dict = app_terraform_workspace_lock.from_dict(app_terraform_workspace_lock_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


