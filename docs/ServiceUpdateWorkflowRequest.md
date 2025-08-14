# ServiceUpdateWorkflowRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approval_option** | [**AppInstallApprovalOption**](AppInstallApprovalOption.md) |  | 

## Example

```python
from nuon.models.service_update_workflow_request import ServiceUpdateWorkflowRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceUpdateWorkflowRequest from a JSON string
service_update_workflow_request_instance = ServiceUpdateWorkflowRequest.from_json(json)
# print the JSON string representation of the object
print ServiceUpdateWorkflowRequest.to_json()

# convert the object into a dict
service_update_workflow_request_dict = service_update_workflow_request_instance.to_dict()
# create an instance of ServiceUpdateWorkflowRequest from a dict
service_update_workflow_request_form_dict = service_update_workflow_request.from_dict(service_update_workflow_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


