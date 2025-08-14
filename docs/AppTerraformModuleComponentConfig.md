# AppTerraformModuleComponentConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component_config_connection_id** | **str** | parent reference | [optional] 
**connected_github_vcs_config** | [**AppConnectedGithubVCSConfig**](AppConnectedGithubVCSConfig.md) |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**env_vars** | **Dict[str, str]** |  | [optional] 
**id** | **str** |  | [optional] 
**public_git_vcs_config** | [**AppPublicGitVCSConfig**](AppPublicGitVCSConfig.md) |  | [optional] 
**updated_at** | **str** |  | [optional] 
**variables** | **Dict[str, str]** |  | [optional] 
**variables_files** | **List[str]** |  | [optional] 
**version** | **str** | terraform configuration values | [optional] 

## Example

```python
from nuon.models.app_terraform_module_component_config import AppTerraformModuleComponentConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AppTerraformModuleComponentConfig from a JSON string
app_terraform_module_component_config_instance = AppTerraformModuleComponentConfig.from_json(json)
# print the JSON string representation of the object
print AppTerraformModuleComponentConfig.to_json()

# convert the object into a dict
app_terraform_module_component_config_dict = app_terraform_module_component_config_instance.to_dict()
# create an instance of AppTerraformModuleComponentConfig from a dict
app_terraform_module_component_config_form_dict = app_terraform_module_component_config.from_dict(app_terraform_module_component_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


