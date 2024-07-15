# ServiceSetAppConfigStatusRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**AppAppConfigStatus**](AppAppConfigStatus.md) |  | [optional] 
**status_description** | **str** |  | [optional] 

## Example

```python
from nuon.models.service_set_app_config_status_request import ServiceSetAppConfigStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceSetAppConfigStatusRequest from a JSON string
service_set_app_config_status_request_instance = ServiceSetAppConfigStatusRequest.from_json(json)
# print the JSON string representation of the object
print ServiceSetAppConfigStatusRequest.to_json()

# convert the object into a dict
service_set_app_config_status_request_dict = service_set_app_config_status_request_instance.to_dict()
# create an instance of ServiceSetAppConfigStatusRequest from a dict
service_set_app_config_status_request_form_dict = service_set_app_config_status_request.from_dict(service_set_app_config_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


