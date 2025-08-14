# AppActionWorkflowStepConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_workflow_config_id** | **str** |  | [optional] 
**app_config_id** | **str** | this belongs to an app config id | [optional] 
**app_id** | **str** |  | [optional] 
**command** | **str** |  | [optional] 
**connected_github_vcs_config** | [**AppConnectedGithubVCSConfig**](AppConnectedGithubVCSConfig.md) |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**env_vars** | **Dict[str, str]** |  | [optional] 
**id** | **str** |  | [optional] 
**idx** | **int** |  | [optional] 
**inline_contents** | **str** |  | [optional] 
**name** | **str** | metadata | [optional] 
**previous_step_id** | **str** |  | [optional] 
**public_git_vcs_config** | [**AppPublicGitVCSConfig**](AppPublicGitVCSConfig.md) | all the details needed for a step | [optional] 
**references** | **List[str]** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_action_workflow_step_config import AppActionWorkflowStepConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AppActionWorkflowStepConfig from a JSON string
app_action_workflow_step_config_instance = AppActionWorkflowStepConfig.from_json(json)
# print the JSON string representation of the object
print AppActionWorkflowStepConfig.to_json()

# convert the object into a dict
app_action_workflow_step_config_dict = app_action_workflow_step_config_instance.to_dict()
# create an instance of AppActionWorkflowStepConfig from a dict
app_action_workflow_step_config_form_dict = app_action_workflow_step_config.from_dict(app_action_workflow_step_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


