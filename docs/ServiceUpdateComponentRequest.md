# ServiceUpdateComponentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dependencies** | **List[str]** |  | [optional] 
**name** | **str** |  | 
**var_name** | **str** |  | [optional] 

## Example

```python
from nuon.models.service_update_component_request import ServiceUpdateComponentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceUpdateComponentRequest from a JSON string
service_update_component_request_instance = ServiceUpdateComponentRequest.from_json(json)
# print the JSON string representation of the object
print ServiceUpdateComponentRequest.to_json()

# convert the object into a dict
service_update_component_request_dict = service_update_component_request_instance.to_dict()
# create an instance of ServiceUpdateComponentRequest from a dict
service_update_component_request_form_dict = service_update_component_request.from_dict(service_update_component_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


