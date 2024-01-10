# ServiceConnectedGithubVCSSandboxConfigRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch** | **str** |  | [optional] 
**directory** | **str** |  | 
**git_ref** | **str** |  | [optional] 
**repo** | **str** |  | 

## Example

```python
from nuon.models.service_connected_github_vcs_sandbox_config_request import ServiceConnectedGithubVCSSandboxConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceConnectedGithubVCSSandboxConfigRequest from a JSON string
service_connected_github_vcs_sandbox_config_request_instance = ServiceConnectedGithubVCSSandboxConfigRequest.from_json(json)
# print the JSON string representation of the object
print ServiceConnectedGithubVCSSandboxConfigRequest.to_json()

# convert the object into a dict
service_connected_github_vcs_sandbox_config_request_dict = service_connected_github_vcs_sandbox_config_request_instance.to_dict()
# create an instance of ServiceConnectedGithubVCSSandboxConfigRequest from a dict
service_connected_github_vcs_sandbox_config_request_form_dict = service_connected_github_vcs_sandbox_config_request.from_dict(service_connected_github_vcs_sandbox_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


