# AppHelmComponentConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chart_name** | **str** | Helm specific configurations | [optional] 
**component_config_connection_id** | **str** | parent reference | [optional] 
**connected_github_vcs_config** | [**AppConnectedGithubVCSConfig**](AppConnectedGithubVCSConfig.md) |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by** | [**AppUserToken**](AppUserToken.md) |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**public_git_vcs_config** | [**AppPublicGitVCSConfig**](AppPublicGitVCSConfig.md) |  | [optional] 
**updated_at** | **str** |  | [optional] 
**values** | **Dict[str, str]** |  | [optional] 

## Example

```python
from nuon.models.app_helm_component_config import AppHelmComponentConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AppHelmComponentConfig from a JSON string
app_helm_component_config_instance = AppHelmComponentConfig.from_json(json)
# print the JSON string representation of the object
print AppHelmComponentConfig.to_json()

# convert the object into a dict
app_helm_component_config_dict = app_helm_component_config_instance.to_dict()
# create an instance of AppHelmComponentConfig from a dict
app_helm_component_config_form_dict = app_helm_component_config.from_dict(app_helm_component_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


