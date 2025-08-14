# ServiceCreateAppActionWorkflowRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 

## Example

```python
from nuon.models.service_create_app_action_workflow_request import ServiceCreateAppActionWorkflowRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCreateAppActionWorkflowRequest from a JSON string
service_create_app_action_workflow_request_instance = ServiceCreateAppActionWorkflowRequest.from_json(json)
# print the JSON string representation of the object
print ServiceCreateAppActionWorkflowRequest.to_json()

# convert the object into a dict
service_create_app_action_workflow_request_dict = service_create_app_action_workflow_request_instance.to_dict()
# create an instance of ServiceCreateAppActionWorkflowRequest from a dict
service_create_app_action_workflow_request_form_dict = service_create_app_action_workflow_request.from_dict(service_create_app_action_workflow_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


