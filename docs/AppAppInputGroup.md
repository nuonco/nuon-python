# AppAppInputGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_input_id** | **str** |  | [optional] 
**app_inputs** | [**List[AppAppInput]**](AppAppInput.md) |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by** | [**AppUserToken**](AppUserToken.md) |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**org_id** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_app_input_group import AppAppInputGroup

# TODO update the JSON string below
json = "{}"
# create an instance of AppAppInputGroup from a JSON string
app_app_input_group_instance = AppAppInputGroup.from_json(json)
# print the JSON string representation of the object
print AppAppInputGroup.to_json()

# convert the object into a dict
app_app_input_group_dict = app_app_input_group_instance.to_dict()
# create an instance of AppAppInputGroup from a dict
app_app_input_group_form_dict = app_app_input_group.from_dict(app_app_input_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


