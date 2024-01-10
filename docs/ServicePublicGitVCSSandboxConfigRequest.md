# ServicePublicGitVCSSandboxConfigRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch** | **str** |  | 
**directory** | **str** |  | 
**repo** | **str** |  | 

## Example

```python
from nuon.models.service_public_git_vcs_sandbox_config_request import ServicePublicGitVCSSandboxConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServicePublicGitVCSSandboxConfigRequest from a JSON string
service_public_git_vcs_sandbox_config_request_instance = ServicePublicGitVCSSandboxConfigRequest.from_json(json)
# print the JSON string representation of the object
print ServicePublicGitVCSSandboxConfigRequest.to_json()

# convert the object into a dict
service_public_git_vcs_sandbox_config_request_dict = service_public_git_vcs_sandbox_config_request_instance.to_dict()
# create an instance of ServicePublicGitVCSSandboxConfigRequest from a dict
service_public_git_vcs_sandbox_config_request_form_dict = service_public_git_vcs_sandbox_config_request.from_dict(service_public_git_vcs_sandbox_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


