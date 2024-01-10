# AppExternalImageComponentConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_ecr_image_config** | [**AppAWSECRImageConfig**](AppAWSECRImageConfig.md) |  | [optional] 
**component_config_connection_id** | **str** | value | [optional] 
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**tag** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.app_external_image_component_config import AppExternalImageComponentConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AppExternalImageComponentConfig from a JSON string
app_external_image_component_config_instance = AppExternalImageComponentConfig.from_json(json)
# print the JSON string representation of the object
print AppExternalImageComponentConfig.to_json()

# convert the object into a dict
app_external_image_component_config_dict = app_external_image_component_config_instance.to_dict()
# create an instance of AppExternalImageComponentConfig from a dict
app_external_image_component_config_form_dict = app_external_image_component_config.from_dict(app_external_image_component_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


