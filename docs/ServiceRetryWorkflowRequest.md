# ServiceRetryWorkflowRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | **str** | Retry indicates whether to retry the current step or not | [optional] 
**step_id** | **str** | StepID is the ID of the step to start the retry from | [optional] 
**workflow_id** | **str** |  | [optional] 

## Example

```python
from nuon.models.service_retry_workflow_request import ServiceRetryWorkflowRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceRetryWorkflowRequest from a JSON string
service_retry_workflow_request_instance = ServiceRetryWorkflowRequest.from_json(json)
# print the JSON string representation of the object
print ServiceRetryWorkflowRequest.to_json()

# convert the object into a dict
service_retry_workflow_request_dict = service_retry_workflow_request_instance.to_dict()
# create an instance of ServiceRetryWorkflowRequest from a dict
service_retry_workflow_request_form_dict = service_retry_workflow_request.from_dict(service_retry_workflow_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


