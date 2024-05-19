# ServiceCreateComponentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dependencies** | **List[str]** |  | [optional] 
**name** | **str** |  | 
**var_name** | **str** |  | [optional] 

## Example

```python
from nuon.models.service_create_component_request import ServiceCreateComponentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCreateComponentRequest from a JSON string
service_create_component_request_instance = ServiceCreateComponentRequest.from_json(json)
# print the JSON string representation of the object
print ServiceCreateComponentRequest.to_json()

# convert the object into a dict
service_create_component_request_dict = service_create_component_request_instance.to_dict()
# create an instance of ServiceCreateComponentRequest from a dict
service_create_component_request_form_dict = service_create_component_request.from_dict(service_create_component_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


