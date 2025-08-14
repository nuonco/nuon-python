# ServiceCreateAppPoliciesConfigRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_config_id** | **str** |  | 
**policies** | [**List[ServiceAppPolicyConfig]**](ServiceAppPolicyConfig.md) |  | [optional] 

## Example

```python
from nuon.models.service_create_app_policies_config_request import ServiceCreateAppPoliciesConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCreateAppPoliciesConfigRequest from a JSON string
service_create_app_policies_config_request_instance = ServiceCreateAppPoliciesConfigRequest.from_json(json)
# print the JSON string representation of the object
print ServiceCreateAppPoliciesConfigRequest.to_json()

# convert the object into a dict
service_create_app_policies_config_request_dict = service_create_app_policies_config_request_instance.to_dict()
# create an instance of ServiceCreateAppPoliciesConfigRequest from a dict
service_create_app_policies_config_request_form_dict = service_create_app_policies_config_request.from_dict(service_create_app_policies_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


