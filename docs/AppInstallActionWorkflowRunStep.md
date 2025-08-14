# AppInstallActionWorkflowRunStep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**execution_duration** | **int** |  | [optional] 
**id** | **str** |  | [optional] 
**install_action_workflow_run_id** | **str** |  | [optional] 
**status** | [**AppInstallActionWorkflowRunStepStatus**](AppInstallActionWorkflowRunStepStatus.md) |  | [optional] 
**step_id** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_install_action_workflow_run_step import AppInstallActionWorkflowRunStep

# TODO update the JSON string below
json = "{}"
# create an instance of AppInstallActionWorkflowRunStep from a JSON string
app_install_action_workflow_run_step_instance = AppInstallActionWorkflowRunStep.from_json(json)
# print the JSON string representation of the object
print AppInstallActionWorkflowRunStep.to_json()

# convert the object into a dict
app_install_action_workflow_run_step_dict = app_install_action_workflow_run_step_instance.to_dict()
# create an instance of AppInstallActionWorkflowRunStep from a dict
app_install_action_workflow_run_step_form_dict = app_install_action_workflow_run_step.from_dict(app_install_action_workflow_run_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


