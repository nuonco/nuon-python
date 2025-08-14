# AppInstallComponentSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**build_status** | [**AppComponentBuildStatus**](AppComponentBuildStatus.md) |  | [optional] 
**build_status_description** | **str** |  | [optional] 
**component_config** | [**AppComponentConfigConnection**](AppComponentConfigConnection.md) |  | [optional] 
**component_id** | **str** |  | [optional] 
**component_name** | **str** |  | [optional] 
**dependencies** | [**List[AppComponent]**](AppComponent.md) |  | [optional] 
**deploy_status** | [**AppInstallDeployStatus**](AppInstallDeployStatus.md) |  | [optional] 
**deploy_status_description** | **str** |  | [optional] 
**id** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_install_component_summary import AppInstallComponentSummary

# TODO update the JSON string below
json = "{}"
# create an instance of AppInstallComponentSummary from a JSON string
app_install_component_summary_instance = AppInstallComponentSummary.from_json(json)
# print the JSON string representation of the object
print AppInstallComponentSummary.to_json()

# convert the object into a dict
app_install_component_summary_dict = app_install_component_summary_instance.to_dict()
# create an instance of AppInstallComponentSummary from a dict
app_install_component_summary_form_dict = app_install_component_summary.from_dict(app_install_component_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


