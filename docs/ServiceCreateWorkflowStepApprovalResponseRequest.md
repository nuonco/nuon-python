# ServiceCreateWorkflowStepApprovalResponseRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**note** | **str** |  | [optional] 
**response_type** | [**AppWorkflowStepResponseType**](AppWorkflowStepResponseType.md) |  | [optional] 

## Example

```python
from nuon.models.service_create_workflow_step_approval_response_request import ServiceCreateWorkflowStepApprovalResponseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCreateWorkflowStepApprovalResponseRequest from a JSON string
service_create_workflow_step_approval_response_request_instance = ServiceCreateWorkflowStepApprovalResponseRequest.from_json(json)
# print the JSON string representation of the object
print ServiceCreateWorkflowStepApprovalResponseRequest.to_json()

# convert the object into a dict
service_create_workflow_step_approval_response_request_dict = service_create_workflow_step_approval_response_request_instance.to_dict()
# create an instance of ServiceCreateWorkflowStepApprovalResponseRequest from a dict
service_create_workflow_step_approval_response_request_form_dict = service_create_workflow_step_approval_response_request.from_dict(service_create_workflow_step_approval_response_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


