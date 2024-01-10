# ServiceCreateComponentBuildRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**git_ref** | **str** |  | [optional] 
**use_latest** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.service_create_component_build_request import ServiceCreateComponentBuildRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCreateComponentBuildRequest from a JSON string
service_create_component_build_request_instance = ServiceCreateComponentBuildRequest.from_json(json)
# print the JSON string representation of the object
print ServiceCreateComponentBuildRequest.to_json()

# convert the object into a dict
service_create_component_build_request_dict = service_create_component_build_request_instance.to_dict()
# create an instance of ServiceCreateComponentBuildRequest from a dict
service_create_component_build_request_form_dict = service_create_component_build_request.from_dict(service_create_component_build_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


