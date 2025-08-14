# ServiceAppSecretConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_generate** | **bool** |  | [optional] 
**default** | **str** |  | [optional] 
**description** | **str** |  | 
**display_name** | **str** |  | 
**format** | **str** |  | [optional] 
**kubernetes_secret_name** | **str** |  | [optional] 
**kubernetes_secret_namespace** | **str** |  | [optional] 
**kubernetes_sync** | **bool** |  | [optional] 
**name** | **str** |  | 
**required** | **bool** |  | [optional] 

## Example

```python
from nuon.models.service_app_secret_config import ServiceAppSecretConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceAppSecretConfig from a JSON string
service_app_secret_config_instance = ServiceAppSecretConfig.from_json(json)
# print the JSON string representation of the object
print ServiceAppSecretConfig.to_json()

# convert the object into a dict
service_app_secret_config_dict = service_app_secret_config_instance.to_dict()
# create an instance of ServiceAppSecretConfig from a dict
service_app_secret_config_form_dict = service_app_secret_config.from_dict(service_app_secret_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


