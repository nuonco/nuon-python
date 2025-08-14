# ServiceAppAWSIAMRoleConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**display_name** | **str** |  | 
**name** | **str** |  | 
**permissions_boundary** | **str** |  | [optional] 
**policies** | [**List[ServiceAppAWSIAMPolicyConfig]**](ServiceAppAWSIAMPolicyConfig.md) |  | [optional] 

## Example

```python
from nuon.models.service_app_awsiam_role_config import ServiceAppAWSIAMRoleConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceAppAWSIAMRoleConfig from a JSON string
service_app_awsiam_role_config_instance = ServiceAppAWSIAMRoleConfig.from_json(json)
# print the JSON string representation of the object
print ServiceAppAWSIAMRoleConfig.to_json()

# convert the object into a dict
service_app_awsiam_role_config_dict = service_app_awsiam_role_config_instance.to_dict()
# create an instance of ServiceAppAWSIAMRoleConfig from a dict
service_app_awsiam_role_config_form_dict = service_app_awsiam_role_config.from_dict(service_app_awsiam_role_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


