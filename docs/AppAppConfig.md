# AppAppConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** |  | [optional] 
**content** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by** | [**AppUserToken**](AppUserToken.md) |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**format** | [**AppAppConfigFmt**](AppAppConfigFmt.md) |  | [optional] 
**generated_terraform** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**org_id** | **str** |  | [optional] 
**status** | [**AppAppConfigStatus**](AppAppConfigStatus.md) |  | [optional] 
**status_description** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_app_config import AppAppConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AppAppConfig from a JSON string
app_app_config_instance = AppAppConfig.from_json(json)
# print the JSON string representation of the object
print AppAppConfig.to_json()

# convert the object into a dict
app_app_config_dict = app_app_config_instance.to_dict()
# create an instance of AppAppConfig from a dict
app_app_config_form_dict = app_app_config.from_dict(app_app_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


