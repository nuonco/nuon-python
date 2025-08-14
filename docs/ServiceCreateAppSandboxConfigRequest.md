# ServiceCreateAppSandboxConfigRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_config_id** | **str** |  | [optional] 
**connected_github_vcs_config** | [**ServiceConnectedGithubVCSSandboxConfigRequest**](ServiceConnectedGithubVCSSandboxConfigRequest.md) |  | [optional] 
**env_vars** | **Dict[str, str]** |  | 
**public_git_vcs_config** | [**ServicePublicGitVCSSandboxConfigRequest**](ServicePublicGitVCSSandboxConfigRequest.md) |  | [optional] 
**terraform_version** | **str** |  | 
**variables** | **Dict[str, str]** |  | 
**variables_files** | **List[str]** |  | [optional] 

## Example

```python
from nuon.models.service_create_app_sandbox_config_request import ServiceCreateAppSandboxConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCreateAppSandboxConfigRequest from a JSON string
service_create_app_sandbox_config_request_instance = ServiceCreateAppSandboxConfigRequest.from_json(json)
# print the JSON string representation of the object
print ServiceCreateAppSandboxConfigRequest.to_json()

# convert the object into a dict
service_create_app_sandbox_config_request_dict = service_create_app_sandbox_config_request_instance.to_dict()
# create an instance of ServiceCreateAppSandboxConfigRequest from a dict
service_create_app_sandbox_config_request_form_dict = service_create_app_sandbox_config_request.from_dict(service_create_app_sandbox_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


