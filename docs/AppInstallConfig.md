# AppInstallConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approval_option** | [**AppInstallApprovalOption**](AppInstallApprovalOption.md) |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**install_id** | **str** |  | [optional] 
**org_id** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_install_config import AppInstallConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AppInstallConfig from a JSON string
app_install_config_instance = AppInstallConfig.from_json(json)
# print the JSON string representation of the object
print AppInstallConfig.to_json()

# convert the object into a dict
app_install_config_dict = app_install_config_instance.to_dict()
# create an instance of AppInstallConfig from a dict
app_install_config_form_dict = app_install_config.from_dict(app_install_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


