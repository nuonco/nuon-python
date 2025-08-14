# ServiceAppAWSIAMPolicyConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contents** | **str** |  | [optional] 
**managed_policy_name** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from nuon.models.service_app_awsiam_policy_config import ServiceAppAWSIAMPolicyConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceAppAWSIAMPolicyConfig from a JSON string
service_app_awsiam_policy_config_instance = ServiceAppAWSIAMPolicyConfig.from_json(json)
# print the JSON string representation of the object
print ServiceAppAWSIAMPolicyConfig.to_json()

# convert the object into a dict
service_app_awsiam_policy_config_dict = service_app_awsiam_policy_config_instance.to_dict()
# create an instance of ServiceAppAWSIAMPolicyConfig from a dict
service_app_awsiam_policy_config_form_dict = service_app_awsiam_policy_config.from_dict(service_app_awsiam_policy_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


