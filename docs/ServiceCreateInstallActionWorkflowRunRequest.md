# ServiceCreateInstallActionWorkflowRunRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_workflow_config_id** | **str** |  | [optional] 
**run_env_vars** | **Dict[str, str]** |  | [optional] 

## Example

```python
from nuon.models.service_create_install_action_workflow_run_request import ServiceCreateInstallActionWorkflowRunRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCreateInstallActionWorkflowRunRequest from a JSON string
service_create_install_action_workflow_run_request_instance = ServiceCreateInstallActionWorkflowRunRequest.from_json(json)
# print the JSON string representation of the object
print ServiceCreateInstallActionWorkflowRunRequest.to_json()

# convert the object into a dict
service_create_install_action_workflow_run_request_dict = service_create_install_action_workflow_run_request_instance.to_dict()
# create an instance of ServiceCreateInstallActionWorkflowRunRequest from a dict
service_create_install_action_workflow_run_request_form_dict = service_create_install_action_workflow_run_request.from_dict(service_create_install_action_workflow_run_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


