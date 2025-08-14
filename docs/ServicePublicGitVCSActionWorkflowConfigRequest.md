# ServicePublicGitVCSActionWorkflowConfigRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch** | **str** |  | 
**directory** | **str** |  | 
**repo** | **str** |  | 

## Example

```python
from nuon.models.service_public_git_vcs_action_workflow_config_request import ServicePublicGitVCSActionWorkflowConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServicePublicGitVCSActionWorkflowConfigRequest from a JSON string
service_public_git_vcs_action_workflow_config_request_instance = ServicePublicGitVCSActionWorkflowConfigRequest.from_json(json)
# print the JSON string representation of the object
print ServicePublicGitVCSActionWorkflowConfigRequest.to_json()

# convert the object into a dict
service_public_git_vcs_action_workflow_config_request_dict = service_public_git_vcs_action_workflow_config_request_instance.to_dict()
# create an instance of ServicePublicGitVCSActionWorkflowConfigRequest from a dict
service_public_git_vcs_action_workflow_config_request_form_dict = service_public_git_vcs_action_workflow_config_request.from_dict(service_public_git_vcs_action_workflow_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


