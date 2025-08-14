# AppWorkflowStep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approval** | [**AppWorkflowStepApproval**](AppWorkflowStepApproval.md) | the step approval is built into each step at the runner level. | [optional] 
**created_at** | **str** |  | [optional] 
**created_by** | [**AppAccount**](AppAccount.md) |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**execution_time** | **int** |  | [optional] 
**execution_type** | [**AppWorkflowStepExecutionType**](AppWorkflowStepExecutionType.md) |  | [optional] 
**finished** | **bool** |  | [optional] 
**finished_at** | **str** |  | [optional] 
**group_idx** | **int** | to group steps which belong to same logical group, eg, plan/apply | [optional] 
**group_retry_idx** | **int** | counter for every retry attempted on a group | [optional] 
**id** | **str** |  | [optional] 
**idx** | **int** |  | [optional] 
**install_workflow_id** | **str** | DEPRECATED: this is the install workflow ID, which is now the workflow ID. | [optional] 
**links** | **Dict[str, object]** |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**name** | **str** |  | [optional] 
**owner_id** | **str** |  | [optional] 
**owner_type** | **str** |  | [optional] 
**policy_validation** | [**AppWorkflowStepPolicyValidation**](AppWorkflowStepPolicyValidation.md) |  | [optional] 
**retried** | **bool** |  | [optional] 
**retryable** | **bool** |  | [optional] 
**skippable** | **bool** |  | [optional] 
**started_at** | **str** |  | [optional] 
**status** | [**AppCompositeStatus**](AppCompositeStatus.md) | status | [optional] 
**step_target_id** | **str** | the following fields are set _once_ a step is in flight, and are orchestrated via the step&#39;s signal.  this is a polymorphic gorm relationship to one of the following objects:  install_cloudformation_stack install_sandbox_run install_runner_update install_deploy install_action_workflow_run (can be many of these) | [optional] 
**step_target_type** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**workflow_id** | **str** | Fields that are de-nested at read time using AfterQuery | [optional] 

## Example

```python
from nuon.models.app_workflow_step import AppWorkflowStep

# TODO update the JSON string below
json = "{}"
# create an instance of AppWorkflowStep from a JSON string
app_workflow_step_instance = AppWorkflowStep.from_json(json)
# print the JSON string representation of the object
print AppWorkflowStep.to_json()

# convert the object into a dict
app_workflow_step_dict = app_workflow_step_instance.to_dict()
# create an instance of AppWorkflowStep from a dict
app_workflow_step_form_dict = app_workflow_step.from_dict(app_workflow_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


