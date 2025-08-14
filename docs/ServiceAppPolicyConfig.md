# ServiceAppPolicyConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contents** | **str** |  | 
**type** | [**ConfigAppPolicyType**](ConfigAppPolicyType.md) |  | 

## Example

```python
from nuon.models.service_app_policy_config import ServiceAppPolicyConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceAppPolicyConfig from a JSON string
service_app_policy_config_instance = ServiceAppPolicyConfig.from_json(json)
# print the JSON string representation of the object
print ServiceAppPolicyConfig.to_json()

# convert the object into a dict
service_app_policy_config_dict = service_app_policy_config_instance.to_dict()
# create an instance of ServiceAppPolicyConfig from a dict
service_app_policy_config_form_dict = service_app_policy_config.from_dict(service_app_policy_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


