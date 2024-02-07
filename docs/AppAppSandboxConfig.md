# AppAppSandboxConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** | TODO(jm): add this back, once we have migrated all existing app sandbox configs &#x60;gorm:\&quot;not null;default null\&quot;&#x60; | [optional] 
**artifacts** | [**AppAppSandboxConfigArtifacts**](AppAppSandboxConfigArtifacts.md) |  | [optional] 
**connected_github_vcs_config** | [**AppConnectedGithubVCSConfig**](AppConnectedGithubVCSConfig.md) |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**org_id** | **str** |  | [optional] 
**public_git_vcs_config** | [**AppPublicGitVCSConfig**](AppPublicGitVCSConfig.md) |  | [optional] 
**sandbox_release** | [**AppSandboxRelease**](AppSandboxRelease.md) |  | [optional] 
**sandbox_release_id** | **str** |  | [optional] 
**terraform_version** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**variables** | **Dict[str, str]** |  | [optional] 

## Example

```python
from nuon.models.app_app_sandbox_config import AppAppSandboxConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AppAppSandboxConfig from a JSON string
app_app_sandbox_config_instance = AppAppSandboxConfig.from_json(json)
# print the JSON string representation of the object
print AppAppSandboxConfig.to_json()

# convert the object into a dict
app_app_sandbox_config_dict = app_app_sandbox_config_instance.to_dict()
# create an instance of AppAppSandboxConfig from a dict
app_app_sandbox_config_form_dict = app_app_sandbox_config.from_dict(app_app_sandbox_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


