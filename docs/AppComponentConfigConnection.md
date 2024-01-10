# AppComponentConfigConnection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component_id** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**docker_build** | [**AppDockerBuildComponentConfig**](AppDockerBuildComponentConfig.md) |  | [optional] 
**external_image** | [**AppExternalImageComponentConfig**](AppExternalImageComponentConfig.md) |  | [optional] 
**helm** | [**AppHelmComponentConfig**](AppHelmComponentConfig.md) |  | [optional] 
**id** | **str** |  | [optional] 
**job** | [**AppJobComponentConfig**](AppJobComponentConfig.md) |  | [optional] 
**terraform_module** | [**AppTerraformModuleComponentConfig**](AppTerraformModuleComponentConfig.md) |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.app_component_config_connection import AppComponentConfigConnection

# TODO update the JSON string below
json = "{}"
# create an instance of AppComponentConfigConnection from a JSON string
app_component_config_connection_instance = AppComponentConfigConnection.from_json(json)
# print the JSON string representation of the object
print AppComponentConfigConnection.to_json()

# convert the object into a dict
app_component_config_connection_dict = app_component_config_connection_instance.to_dict()
# create an instance of AppComponentConfigConnection from a dict
app_component_config_connection_form_dict = app_component_config_connection.from_dict(app_component_config_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


