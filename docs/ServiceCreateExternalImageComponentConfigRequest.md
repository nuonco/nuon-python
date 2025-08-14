# ServiceCreateExternalImageComponentConfigRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_config_id** | **str** |  | [optional] 
**aws_ecr_image_config** | [**ServiceAwsECRImageConfigRequest**](ServiceAwsECRImageConfigRequest.md) |  | [optional] 
**checksum** | **str** |  | [optional] 
**dependencies** | **List[str]** |  | [optional] 
**image_url** | **str** |  | 
**references** | **List[str]** |  | [optional] 
**tag** | **str** |  | 

## Example

```python
from nuon.models.service_create_external_image_component_config_request import ServiceCreateExternalImageComponentConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCreateExternalImageComponentConfigRequest from a JSON string
service_create_external_image_component_config_request_instance = ServiceCreateExternalImageComponentConfigRequest.from_json(json)
# print the JSON string representation of the object
print ServiceCreateExternalImageComponentConfigRequest.to_json()

# convert the object into a dict
service_create_external_image_component_config_request_dict = service_create_external_image_component_config_request_instance.to_dict()
# create an instance of ServiceCreateExternalImageComponentConfigRequest from a dict
service_create_external_image_component_config_request_form_dict = service_create_external_image_component_config_request.from_dict(service_create_external_image_component_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


