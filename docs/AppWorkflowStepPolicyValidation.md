# AppWorkflowStepPolicyValidation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**install_workflow_step_id** | **str** | install workflow step is the install step that this was performed within | [optional] 
**response** | **str** | response is the kyverno response | [optional] 
**runner_job_id** | **str** | runnerJobID is the runner job that this was performed within | [optional] 
**status** | [**AppCompositeStatus**](AppCompositeStatus.md) | status denotes whether this passed, or whether it failed the job. | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_workflow_step_policy_validation import AppWorkflowStepPolicyValidation

# TODO update the JSON string below
json = "{}"
# create an instance of AppWorkflowStepPolicyValidation from a JSON string
app_workflow_step_policy_validation_instance = AppWorkflowStepPolicyValidation.from_json(json)
# print the JSON string representation of the object
print AppWorkflowStepPolicyValidation.to_json()

# convert the object into a dict
app_workflow_step_policy_validation_dict = app_workflow_step_policy_validation_instance.to_dict()
# create an instance of AppWorkflowStepPolicyValidation from a dict
app_workflow_step_policy_validation_form_dict = app_workflow_step_policy_validation.from_dict(app_workflow_step_policy_validation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


