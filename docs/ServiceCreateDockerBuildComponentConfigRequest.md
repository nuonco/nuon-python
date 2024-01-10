# ServiceCreateDockerBuildComponentConfigRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**build_args** | **List[str]** |  | [optional] 
**connected_github_vcs_config** | [**ServiceConnectedGithubVCSConfigRequest**](ServiceConnectedGithubVCSConfigRequest.md) |  | [optional] 
**dockerfile** | **str** |  | 
**env_vars** | **Dict[str, str]** |  | [optional] 
**public_git_vcs_config** | [**ServicePublicGitVCSConfigRequest**](ServicePublicGitVCSConfigRequest.md) |  | [optional] 
**target** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.service_create_docker_build_component_config_request import ServiceCreateDockerBuildComponentConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCreateDockerBuildComponentConfigRequest from a JSON string
service_create_docker_build_component_config_request_instance = ServiceCreateDockerBuildComponentConfigRequest.from_json(json)
# print the JSON string representation of the object
print ServiceCreateDockerBuildComponentConfigRequest.to_json()

# convert the object into a dict
service_create_docker_build_component_config_request_dict = service_create_docker_build_component_config_request_instance.to_dict()
# create an instance of ServiceCreateDockerBuildComponentConfigRequest from a dict
service_create_docker_build_component_config_request_form_dict = service_create_docker_build_component_config_request.from_dict(service_create_docker_build_component_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


