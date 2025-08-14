# AppAppBreakGlassConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_config_id** | **str** |  | [optional] 
**app_id** | **str** |  | [optional] 
**aws_iam_roles** | [**List[AppAppAWSIAMRoleConfig]**](AppAppAWSIAMRoleConfig.md) |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**org_id** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_app_break_glass_config import AppAppBreakGlassConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AppAppBreakGlassConfig from a JSON string
app_app_break_glass_config_instance = AppAppBreakGlassConfig.from_json(json)
# print the JSON string representation of the object
print AppAppBreakGlassConfig.to_json()

# convert the object into a dict
app_app_break_glass_config_dict = app_app_break_glass_config_instance.to_dict()
# create an instance of AppAppBreakGlassConfig from a dict
app_app_break_glass_config_form_dict = app_app_break_glass_config.from_dict(app_app_break_glass_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


