# ServiceRetryWorkflowByIDRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | **str** | Retry indicates whether to retry the current step or not | [optional] 
**step_id** | **str** | StepID is the ID of the step to start the retry from | [optional] 

## Example

```python
from nuon.models.service_retry_workflow_by_id_request import ServiceRetryWorkflowByIDRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceRetryWorkflowByIDRequest from a JSON string
service_retry_workflow_by_id_request_instance = ServiceRetryWorkflowByIDRequest.from_json(json)
# print the JSON string representation of the object
print ServiceRetryWorkflowByIDRequest.to_json()

# convert the object into a dict
service_retry_workflow_by_id_request_dict = service_retry_workflow_by_id_request_instance.to_dict()
# create an instance of ServiceRetryWorkflowByIDRequest from a dict
service_retry_workflow_by_id_request_form_dict = service_retry_workflow_by_id_request.from_dict(service_retry_workflow_by_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


