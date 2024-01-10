# AppPublicGitVCSConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch** | **str** |  | [optional] 
**component_config_id** | **str** |  | [optional] 
**component_config_type** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**directory** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**repo** | **str** | actual configuration | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_public_git_vcs_config import AppPublicGitVCSConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AppPublicGitVCSConfig from a JSON string
app_public_git_vcs_config_instance = AppPublicGitVCSConfig.from_json(json)
# print the JSON string representation of the object
print AppPublicGitVCSConfig.to_json()

# convert the object into a dict
app_public_git_vcs_config_dict = app_public_git_vcs_config_instance.to_dict()
# create an instance of AppPublicGitVCSConfig from a dict
app_public_git_vcs_config_form_dict = app_public_git_vcs_config.from_dict(app_public_git_vcs_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


