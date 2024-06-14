# AppComponentReleaseStep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component_release_id** | **str** | parent release ID | [optional] 
**created_at** | **str** |  | [optional] 
**created_by** | [**AppAccount**](AppAccount.md) |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**delay** | **str** | fields to control the delay of the individual step, as this is set based on the parent strategy | [optional] 
**id** | **str** |  | [optional] 
**install_deploys** | [**List[AppInstallDeploy]**](AppInstallDeploy.md) |  | [optional] 
**requested_install_ids** | **List[str]** | When a step is created, a set of installs are targeted. However, by the time the release step goes out, the install might have been setup in any order of ways. | [optional] 
**status** | **str** |  | [optional] 
**status_description** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_component_release_step import AppComponentReleaseStep

# TODO update the JSON string below
json = "{}"
# create an instance of AppComponentReleaseStep from a JSON string
app_component_release_step_instance = AppComponentReleaseStep.from_json(json)
# print the JSON string representation of the object
print AppComponentReleaseStep.to_json()

# convert the object into a dict
app_component_release_step_dict = app_component_release_step_instance.to_dict()
# create an instance of AppComponentReleaseStep from a dict
app_component_release_step_form_dict = app_component_release_step.from_dict(app_component_release_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


