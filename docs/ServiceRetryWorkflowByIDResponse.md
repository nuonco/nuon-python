# ServiceRetryWorkflowByIDResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_id** | **str** |  | [optional] 

## Example

```python
from nuon.models.service_retry_workflow_by_id_response import ServiceRetryWorkflowByIDResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceRetryWorkflowByIDResponse from a JSON string
service_retry_workflow_by_id_response_instance = ServiceRetryWorkflowByIDResponse.from_json(json)
# print the JSON string representation of the object
print ServiceRetryWorkflowByIDResponse.to_json()

# convert the object into a dict
service_retry_workflow_by_id_response_dict = service_retry_workflow_by_id_response_instance.to_dict()
# create an instance of ServiceRetryWorkflowByIDResponse from a dict
service_retry_workflow_by_id_response_form_dict = service_retry_workflow_by_id_response.from_dict(service_retry_workflow_by_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


