# AppAppSecretConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_config_id** | **str** |  | [optional] 
**app_id** | **str** |  | [optional] 
**app_secrets_config_id** | **str** |  | [optional] 
**auto_generate** | **bool** |  | [optional] 
**cloudformation_param_name** | **str** |  | [optional] 
**cloudformation_stack_name** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**default** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**format** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**kubernetes_secret_name** | **str** |  | [optional] 
**kubernetes_secret_namespace** | **str** |  | [optional] 
**kubernetes_sync** | **bool** | for syncing into kubernetes | [optional] 
**name** | **str** |  | [optional] 
**org_id** | **str** |  | [optional] 
**required** | **bool** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_app_secret_config import AppAppSecretConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AppAppSecretConfig from a JSON string
app_app_secret_config_instance = AppAppSecretConfig.from_json(json)
# print the JSON string representation of the object
print AppAppSecretConfig.to_json()

# convert the object into a dict
app_app_secret_config_dict = app_app_secret_config_instance.to_dict()
# create an instance of AppAppSecretConfig from a dict
app_app_secret_config_form_dict = app_app_secret_config.from_dict(app_app_secret_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


