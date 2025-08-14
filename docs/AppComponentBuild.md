# AppComponentBuild


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checksum** | **str** | checksum of our intermediate component config | [optional] 
**component_config_connection** | [**AppComponentConfigConnection**](AppComponentConfigConnection.md) |  | [optional] 
**component_config_connection_id** | **str** | DEPRECATED: will retain the field to connect against the last component config connection that set this build | [optional] 
**component_config_version** | **int** |  | [optional] 
**component_id** | **str** | Read-only fields set on the object to de-nest data | [optional] 
**component_name** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by** | [**AppAccount**](AppAccount.md) |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**git_ref** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**install_deploys** | [**List[AppInstallDeploy]**](AppInstallDeploy.md) |  | [optional] 
**log_stream** | [**AppLogStream**](AppLogStream.md) |  | [optional] 
**releases** | [**List[AppComponentRelease]**](AppComponentRelease.md) |  | [optional] 
**runner_job** | [**AppRunnerJob**](AppRunnerJob.md) | runner details | [optional] 
**status** | **str** |  | [optional] 
**status_description** | **str** |  | [optional] 
**status_v2** | [**AppCompositeStatus**](AppCompositeStatus.md) |  | [optional] 
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


