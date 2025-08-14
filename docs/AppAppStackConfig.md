# AppAppStackConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_config_id** | **str** |  | [optional] 
**app_id** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**org_id** | **str** |  | [optional] 
**runner_nested_template_url** | **str** |  | [optional] 
**type** | [**AppStackType**](AppStackType.md) |  | [optional] 
**updated_at** | **str** |  | [optional] 
**vpc_nested_template_url** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_app_stack_config import AppAppStackConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AppAppStackConfig from a JSON string
app_app_stack_config_instance = AppAppStackConfig.from_json(json)
# print the JSON string representation of the object
print AppAppStackConfig.to_json()

# convert the object into a dict
app_app_stack_config_dict = app_app_stack_config_instance.to_dict()
# create an instance of AppAppStackConfig from a dict
app_app_stack_config_form_dict = app_app_stack_config.from_dict(app_app_stack_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


