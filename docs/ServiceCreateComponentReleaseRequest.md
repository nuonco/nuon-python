# ServiceCreateComponentReleaseRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_build** | **bool** |  | [optional] 
**build_id** | **str** |  | [optional] 
**strategy** | [**ServiceCreateComponentReleaseRequestStrategy**](ServiceCreateComponentReleaseRequestStrategy.md) |  | [optional] 

## Example

```python
from openapi_client.models.service_create_component_release_request import ServiceCreateComponentReleaseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCreateComponentReleaseRequest from a JSON string
service_create_component_release_request_instance = ServiceCreateComponentReleaseRequest.from_json(json)
# print the JSON string representation of the object
print ServiceCreateComponentReleaseRequest.to_json()

# convert the object into a dict
service_create_component_release_request_dict = service_create_component_release_request_instance.to_dict()
# create an instance of ServiceCreateComponentReleaseRequest from a dict
service_create_component_release_request_form_dict = service_create_component_release_request.from_dict(service_create_component_release_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


