# AppConnectedGithubVCSConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch** | **str** |  | [optional] 
**component_config_id** | **str** | parent component | [optional] 
**component_config_type** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**directory** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**repo** | **str** |  | [optional] 
**repo_name** | **str** |  | [optional] 
**repo_owner** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**vcs_connection** | [**AppVCSConnection**](AppVCSConnection.md) |  | [optional] 
**vcs_connection_id** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_connected_github_vcs_config import AppConnectedGithubVCSConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AppConnectedGithubVCSConfig from a JSON string
app_connected_github_vcs_config_instance = AppConnectedGithubVCSConfig.from_json(json)
# print the JSON string representation of the object
print AppConnectedGithubVCSConfig.to_json()

# convert the object into a dict
app_connected_github_vcs_config_dict = app_connected_github_vcs_config_instance.to_dict()
# create an instance of AppConnectedGithubVCSConfig from a dict
app_connected_github_vcs_config_form_dict = app_connected_github_vcs_config.from_dict(app_connected_github_vcs_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


