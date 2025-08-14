# ServiceUpdateAppConfigRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component_ids** | **List[str]** |  | [optional] 
**state** | **str** |  | [optional] 
**status** | [**AppAppConfigStatus**](AppAppConfigStatus.md) |  | [optional] 
**status_description** | **str** |  | [optional] 

## Example

```python
from nuon.models.service_update_app_config_request import ServiceUpdateAppConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceUpdateAppConfigRequest from a JSON string
service_update_app_config_request_instance = ServiceUpdateAppConfigRequest.from_json(json)
# print the JSON string representation of the object
print ServiceUpdateAppConfigRequest.to_json()

# convert the object into a dict
service_update_app_config_request_dict = service_update_app_config_request_instance.to_dict()
# create an instance of ServiceUpdateAppConfigRequest from a dict
service_update_app_config_request_form_dict = service_update_app_config_request.from_dict(service_update_app_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


