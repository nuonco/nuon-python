# AppComponent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** |  | [optional] 
**config_versions** | **int** |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**dependencies** | **List[str]** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**status_description** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_component import AppComponent

# TODO update the JSON string below
json = "{}"
# create an instance of AppComponent from a JSON string
app_component_instance = AppComponent.from_json(json)
# print the JSON string representation of the object
print AppComponent.to_json()

# convert the object into a dict
app_component_dict = app_component_instance.to_dict()
# create an instance of AppComponent from a dict
app_component_form_dict = app_component.from_dict(app_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


