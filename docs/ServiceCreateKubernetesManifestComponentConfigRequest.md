# ServiceCreateKubernetesManifestComponentConfigRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_config_id** | **str** |  | [optional] 
**checksum** | **str** |  | [optional] 
**dependencies** | **List[str]** |  | [optional] 
**manifest** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 

## Example

```python
from nuon.models.service_create_kubernetes_manifest_component_config_request import ServiceCreateKubernetesManifestComponentConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCreateKubernetesManifestComponentConfigRequest from a JSON string
service_create_kubernetes_manifest_component_config_request_instance = ServiceCreateKubernetesManifestComponentConfigRequest.from_json(json)
# print the JSON string representation of the object
print ServiceCreateKubernetesManifestComponentConfigRequest.to_json()

# convert the object into a dict
service_create_kubernetes_manifest_component_config_request_dict = service_create_kubernetes_manifest_component_config_request_instance.to_dict()
# create an instance of ServiceCreateKubernetesManifestComponentConfigRequest from a dict
service_create_kubernetes_manifest_component_config_request_form_dict = service_create_kubernetes_manifest_component_config_request.from_dict(service_create_kubernetes_manifest_component_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


