# ServiceCreateAppBreakGlassConfigRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_config_id** | **str** |  | 
**roles** | [**List[ServiceAppAWSIAMRoleConfig]**](ServiceAppAWSIAMRoleConfig.md) |  | 

## Example

```python
from nuon.models.service_create_app_break_glass_config_request import ServiceCreateAppBreakGlassConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCreateAppBreakGlassConfigRequest from a JSON string
service_create_app_break_glass_config_request_instance = ServiceCreateAppBreakGlassConfigRequest.from_json(json)
# print the JSON string representation of the object
print ServiceCreateAppBreakGlassConfigRequest.to_json()

# convert the object into a dict
service_create_app_break_glass_config_request_dict = service_create_app_break_glass_config_request_instance.to_dict()
# create an instance of ServiceCreateAppBreakGlassConfigRequest from a dict
service_create_app_break_glass_config_request_form_dict = service_create_app_break_glass_config_request.from_dict(service_create_app_break_glass_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


