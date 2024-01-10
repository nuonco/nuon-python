# AppAppInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_input_id** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**default** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**org_id** | **str** |  | [optional] 
**required** | **bool** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.app_app_input import AppAppInput

# TODO update the JSON string below
json = "{}"
# create an instance of AppAppInput from a JSON string
app_app_input_instance = AppAppInput.from_json(json)
# print the JSON string representation of the object
print AppAppInput.to_json()

# convert the object into a dict
app_app_input_dict = app_app_input_instance.to_dict()
# create an instance of AppAppInput from a dict
app_app_input_form_dict = app_app_input.from_dict(app_app_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


