# AppWorkflowStepApprovalResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**install_workflow_step_approval_id** | **str** | the approval the response belongs to | [optional] 
**note** | **str** |  | [optional] 
**type** | [**AppWorkflowStepResponseType**](AppWorkflowStepResponseType.md) | the response type | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_workflow_step_approval_response import AppWorkflowStepApprovalResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AppWorkflowStepApprovalResponse from a JSON string
app_workflow_step_approval_response_instance = AppWorkflowStepApprovalResponse.from_json(json)
# print the JSON string representation of the object
print AppWorkflowStepApprovalResponse.to_json()

# convert the object into a dict
app_workflow_step_approval_response_dict = app_workflow_step_approval_response_instance.to_dict()
# create an instance of AppWorkflowStepApprovalResponse from a dict
app_workflow_step_approval_response_form_dict = app_workflow_step_approval_response.from_dict(app_workflow_step_approval_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


