# AppComponentRelease


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**build_id** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by** | [**AppUserToken**](AppUserToken.md) |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**release_steps** | [**List[AppComponentReleaseStep]**](AppComponentReleaseStep.md) |  | [optional] 
**status** | **str** |  | [optional] 
**status_description** | **str** |  | [optional] 
**total_release_steps** | **int** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_component_release import AppComponentRelease

# TODO update the JSON string below
json = "{}"
# create an instance of AppComponentRelease from a JSON string
app_component_release_instance = AppComponentRelease.from_json(json)
# print the JSON string representation of the object
print AppComponentRelease.to_json()

# convert the object into a dict
app_component_release_dict = app_component_release_instance.to_dict()
# create an instance of AppComponentRelease from a dict
app_component_release_form_dict = app_component_release.from_dict(app_component_release_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


