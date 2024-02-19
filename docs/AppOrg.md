# AppOrg


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**awsecrimage_configs** | [**List[AppAWSECRImageConfig]**](AppAWSECRImageConfig.md) |  | [optional] 
**connected_github_vcs_configs** | [**List[AppConnectedGithubVCSConfig]**](AppConnectedGithubVCSConfig.md) |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by** | [**AppUserToken**](AppUserToken.md) |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**custom_cert** | **bool** |  | [optional] 
**health_checks** | [**List[AppOrgHealthCheck]**](AppOrgHealthCheck.md) |  | [optional] 
**id** | **str** |  | [optional] 
**latest_health_check** | [**AppOrgHealthCheck**](AppOrgHealthCheck.md) | Filled in at read time | [optional] 
**name** | **str** |  | [optional] 
**public_git_vcs_configs** | [**List[AppPublicGitVCSConfig]**](AppPublicGitVCSConfig.md) | NOTE(jm): with GORM, these cascades are not getting created properly. For now, we just add them here, but eventually we should be able to remove these and add them directly. | [optional] 
**sandbox_mode** | **bool** | These fields are used to control the behaviour of the org NOTE: these are starting as nullable, so we can update stage/prod before resetting locally. | [optional] 
**status** | **str** |  | [optional] 
**status_description** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**users** | [**List[AppUserOrg]**](AppUserOrg.md) |  | [optional] 
**vcs_connections** | [**List[AppVCSConnection]**](AppVCSConnection.md) |  | [optional] 

## Example

```python
from nuon.models.app_org import AppOrg

# TODO update the JSON string below
json = "{}"
# create an instance of AppOrg from a JSON string
app_org_instance = AppOrg.from_json(json)
# print the JSON string representation of the object
print AppOrg.to_json()

# convert the object into a dict
app_org_dict = app_org_instance.to_dict()
# create an instance of AppOrg from a dict
app_org_form_dict = app_org.from_dict(app_org_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


