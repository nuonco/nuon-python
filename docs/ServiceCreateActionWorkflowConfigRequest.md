# ServiceCreateActionWorkflowConfigRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_config_id** | **str** |  | 
**dependencies** | **List[str]** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**steps** | [**List[ServiceCreateActionWorkflowConfigStepRequest]**](ServiceCreateActionWorkflowConfigStepRequest.md) |  | 
**timeout** | **int** |  | [optional] 
**triggers** | [**List[ServiceCreateActionWorkflowConfigTriggerRequest]**](ServiceCreateActionWorkflowConfigTriggerRequest.md) |  | 

## Example

```python
from nuon.models.service_create_action_workflow_config_request import ServiceCreateActionWorkflowConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCreateActionWorkflowConfigRequest from a JSON string
service_create_action_workflow_config_request_instance = ServiceCreateActionWorkflowConfigRequest.from_json(json)
# print the JSON string representation of the object
print ServiceCreateActionWorkflowConfigRequest.to_json()

# convert the object into a dict
service_create_action_workflow_config_request_dict = service_create_action_workflow_config_request_instance.to_dict()
# create an instance of ServiceCreateActionWorkflowConfigRequest from a dict
service_create_action_workflow_config_request_form_dict = service_create_action_workflow_config_request.from_dict(service_create_action_workflow_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


