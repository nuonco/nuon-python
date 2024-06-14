# AppDockerBuildComponentConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**build_args** | **List[str]** |  | [optional] 
**component_config_connection_id** | **str** | value | [optional] 
**connected_github_vcs_config** | [**AppConnectedGithubVCSConfig**](AppConnectedGithubVCSConfig.md) |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by** | [**AppAccount**](AppAccount.md) |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**dockerfile** | **str** |  | [optional] 
**env_vars** | **Dict[str, str]** |  | [optional] 
**id** | **str** |  | [optional] 
**public_git_vcs_config** | [**AppPublicGitVCSConfig**](AppPublicGitVCSConfig.md) |  | [optional] 
**target** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_docker_build_component_config import AppDockerBuildComponentConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AppDockerBuildComponentConfig from a JSON string
app_docker_build_component_config_instance = AppDockerBuildComponentConfig.from_json(json)
# print the JSON string representation of the object
print AppDockerBuildComponentConfig.to_json()

# convert the object into a dict
app_docker_build_component_config_dict = app_docker_build_component_config_instance.to_dict()
# create an instance of AppDockerBuildComponentConfig from a dict
app_docker_build_component_config_form_dict = app_docker_build_component_config.from_dict(app_docker_build_component_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


