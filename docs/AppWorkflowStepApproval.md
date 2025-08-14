# AppWorkflowStepApproval


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**install_workflow_step** | [**AppWorkflowStep**](AppWorkflowStep.md) |  | [optional] 
**install_workflow_step_id** | **str** | the step that this approval belongs too | [optional] 
**owner_id** | **str** |  | [optional] 
**owner_type** | **str** |  | [optional] 
**response** | [**AppWorkflowStepApprovalResponse**](AppWorkflowStepApprovalResponse.md) | the response object must be created by the user in the UI or CLI | [optional] 
**runner_job** | [**AppRunnerJob**](AppRunnerJob.md) |  | [optional] 
**runner_job_id** | **str** | the runner job where this approval was created | [optional] 
**type** | [**AppWorkflowStepApprovalType**](AppWorkflowStepApprovalType.md) |  | [optional] 
**updated_at** | **str** |  | [optional] 
**workflow_step** | [**AppWorkflowStep**](AppWorkflowStep.md) |  | [optional] 
**workflow_step_id** | **str** | afterquery | [optional] 

## Example

```python
from nuon.models.app_workflow_step_approval import AppWorkflowStepApproval

# TODO update the JSON string below
json = "{}"
# create an instance of AppWorkflowStepApproval from a JSON string
app_workflow_step_approval_instance = AppWorkflowStepApproval.from_json(json)
# print the JSON string representation of the object
print AppWorkflowStepApproval.to_json()

# convert the object into a dict
app_workflow_step_approval_dict = app_workflow_step_approval_instance.to_dict()
# create an instance of AppWorkflowStepApproval from a dict
app_workflow_step_approval_form_dict = app_workflow_step_approval.from_dict(app_workflow_step_approval_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


