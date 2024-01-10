# ServiceCreateTerraformModuleComponentConfigRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connected_github_vcs_config** | [**ServiceConnectedGithubVCSConfigRequest**](ServiceConnectedGithubVCSConfigRequest.md) |  | [optional] 
**env_vars** | **Dict[str, str]** |  | 
**public_git_vcs_config** | [**ServicePublicGitVCSConfigRequest**](ServicePublicGitVCSConfigRequest.md) |  | [optional] 
**variables** | **Dict[str, str]** |  | 
**version** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.service_create_terraform_module_component_config_request import ServiceCreateTerraformModuleComponentConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCreateTerraformModuleComponentConfigRequest from a JSON string
service_create_terraform_module_component_config_request_instance = ServiceCreateTerraformModuleComponentConfigRequest.from_json(json)
# print the JSON string representation of the object
print ServiceCreateTerraformModuleComponentConfigRequest.to_json()

# convert the object into a dict
service_create_terraform_module_component_config_request_dict = service_create_terraform_module_component_config_request_instance.to_dict()
# create an instance of ServiceCreateTerraformModuleComponentConfigRequest from a dict
service_create_terraform_module_component_config_request_form_dict = service_create_terraform_module_component_config_request.from_dict(service_create_terraform_module_component_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


