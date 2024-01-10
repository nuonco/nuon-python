# ServiceAppInputRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **str** |  | [optional] 
**description** | **str** |  | 
**required** | **bool** |  | [optional] 

## Example

```python
from nuon.models.service_app_input_request import ServiceAppInputRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceAppInputRequest from a JSON string
service_app_input_request_instance = ServiceAppInputRequest.from_json(json)
# print the JSON string representation of the object
print ServiceAppInputRequest.to_json()

# convert the object into a dict
service_app_input_request_dict = service_app_input_request_instance.to_dict()
# create an instance of ServiceAppInputRequest from a dict
service_app_input_request_form_dict = service_app_input_request.from_dict(service_app_input_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


