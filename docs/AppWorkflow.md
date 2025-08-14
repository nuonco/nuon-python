# AppWorkflow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approval_option** | [**AppInstallApprovalOption**](AppInstallApprovalOption.md) |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by** | [**AppAccount**](AppAccount.md) |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**execution_time** | **int** |  | [optional] 
**finished** | **bool** |  | [optional] 
**finished_at** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**install_action_workflow_runs** | [**List[AppInstallActionWorkflowRun]**](AppInstallActionWorkflowRun.md) |  | [optional] 
**install_deploys** | [**List[AppInstallDeploy]**](AppInstallDeploy.md) |  | [optional] 
**install_sandbox_runs** | [**List[AppInstallSandboxRun]**](AppInstallSandboxRun.md) |  | [optional] 
**links** | **Dict[str, object]** |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**name** | **str** |  | [optional] 
**owner_id** | **str** |  | [optional] 
**owner_type** | **str** |  | [optional] 
**plan_only** | **bool** |  | [optional] 
**started_at** | **str** |  | [optional] 
**status** | [**AppCompositeStatus**](AppCompositeStatus.md) |  | [optional] 
**step_error_behavior** | [**AppStepErrorBehavior**](AppStepErrorBehavior.md) |  | [optional] 
**steps** | [**List[AppWorkflowStep]**](AppWorkflowStep.md) | steps represent each piece of the workflow | [optional] 
**type** | [**AppWorkflowType**](AppWorkflowType.md) |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_workflow import AppWorkflow

# TODO update the JSON string below
json = "{}"
# create an instance of AppWorkflow from a JSON string
app_workflow_instance = AppWorkflow.from_json(json)
# print the JSON string representation of the object
print AppWorkflow.to_json()

# convert the object into a dict
app_workflow_dict = app_workflow_instance.to_dict()
# create an instance of AppWorkflow from a dict
app_workflow_form_dict = app_workflow.from_dict(app_workflow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


