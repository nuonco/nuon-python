# ServiceCreateAppInputConfigRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | [**Dict[str, ServiceAppGroupRequest]**](ServiceAppGroupRequest.md) |  | 
**inputs** | [**Dict[str, ServiceAppInputRequest]**](ServiceAppInputRequest.md) |  | 

## Example

```python
from nuon.models.service_create_app_input_config_request import ServiceCreateAppInputConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCreateAppInputConfigRequest from a JSON string
service_create_app_input_config_request_instance = ServiceCreateAppInputConfigRequest.from_json(json)
# print the JSON string representation of the object
print ServiceCreateAppInputConfigRequest.to_json()

# convert the object into a dict
service_create_app_input_config_request_dict = service_create_app_input_config_request_instance.to_dict()
# create an instance of ServiceCreateAppInputConfigRequest from a dict
service_create_app_input_config_request_form_dict = service_create_app_input_config_request.from_dict(service_create_app_input_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


