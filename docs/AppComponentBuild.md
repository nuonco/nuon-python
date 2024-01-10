# AppComponentBuild


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component_config_connection_id** | **str** |  | [optional] 
**component_id** | **str** | Read-only fields set on the object to de-nest data | [optional] 
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**git_ref** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**install_deploys** | [**List[AppInstallDeploy]**](AppInstallDeploy.md) |  | [optional] 
**releases** | [**List[AppComponentRelease]**](AppComponentRelease.md) |  | [optional] 
**status** | **str** |  | [optional] 
**status_description** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**vcs_connection_commit** | [**AppVCSConnectionCommit**](AppVCSConnectionCommit.md) |  | [optional] 

## Example

```python
from nuon.models.app_component_build import AppComponentBuild

# TODO update the JSON string below
json = "{}"
# create an instance of AppComponentBuild from a JSON string
app_component_build_instance = AppComponentBuild.from_json(json)
# print the JSON string representation of the object
print AppComponentBuild.to_json()

# convert the object into a dict
app_component_build_dict = app_component_build_instance.to_dict()
# create an instance of AppComponentBuild from a dict
app_component_build_form_dict = app_component_build.from_dict(app_component_build_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


