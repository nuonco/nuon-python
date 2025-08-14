# ServiceCreateActionWorkflowConfigStepRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**command** | **str** |  | [optional] 
**connected_github_vcs_config** | [**ServiceConnectedGithubVCSActionWorkflowConfigRequest**](ServiceConnectedGithubVCSActionWorkflowConfigRequest.md) |  | [optional] 
**env_vars** | **Dict[str, str]** |  | [optional] 
**inline_contents** | **str** |  | [optional] 
**name** | **str** |  | 
**public_git_vcs_config** | [**ServicePublicGitVCSActionWorkflowConfigRequest**](ServicePublicGitVCSActionWorkflowConfigRequest.md) |  | [optional] 
**references** | **List[str]** |  | [optional] 

## Example

```python
from nuon.models.service_create_action_workflow_config_step_request import ServiceCreateActionWorkflowConfigStepRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCreateActionWorkflowConfigStepRequest from a JSON string
service_create_action_workflow_config_step_request_instance = ServiceCreateActionWorkflowConfigStepRequest.from_json(json)
# print the JSON string representation of the object
print ServiceCreateActionWorkflowConfigStepRequest.to_json()

# convert the object into a dict
service_create_action_workflow_config_step_request_dict = service_create_action_workflow_config_step_request_instance.to_dict()
# create an instance of ServiceCreateActionWorkflowConfigStepRequest from a dict
service_create_action_workflow_config_step_request_form_dict = service_create_action_workflow_config_step_request.from_dict(service_create_action_workflow_config_step_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


