# AppAppInputConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_config_id** | **str** |  | [optional] 
**app_id** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**input_groups** | [**List[AppAppInputGroup]**](AppAppInputGroup.md) |  | [optional] 
**inputs** | [**List[AppAppInput]**](AppAppInput.md) |  | [optional] 
**install_inputs** | [**List[AppInstallInputs]**](AppInstallInputs.md) |  | [optional] 
**org_id** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_app_input_config import AppAppInputConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AppAppInputConfig from a JSON string
app_app_input_config_instance = AppAppInputConfig.from_json(json)
# print the JSON string representation of the object
print AppAppInputConfig.to_json()

# convert the object into a dict
app_app_input_config_dict = app_app_input_config_instance.to_dict()
# create an instance of AppAppInputConfig from a dict
app_app_input_config_form_dict = app_app_input_config.from_dict(app_app_input_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


