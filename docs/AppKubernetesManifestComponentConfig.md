# AppKubernetesManifestComponentConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component_config_connection_id** | **str** | value | [optional] 
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**manifest** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_kubernetes_manifest_component_config import AppKubernetesManifestComponentConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AppKubernetesManifestComponentConfig from a JSON string
app_kubernetes_manifest_component_config_instance = AppKubernetesManifestComponentConfig.from_json(json)
# print the JSON string representation of the object
print AppKubernetesManifestComponentConfig.to_json()

# convert the object into a dict
app_kubernetes_manifest_component_config_dict = app_kubernetes_manifest_component_config_instance.to_dict()
# create an instance of AppKubernetesManifestComponentConfig from a dict
app_kubernetes_manifest_component_config_form_dict = app_kubernetes_manifest_component_config.from_dict(app_kubernetes_manifest_component_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


