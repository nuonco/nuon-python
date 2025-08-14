# AppAppAWSIAMPolicyConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_aws_iam_role_config_id** | **str** |  | [optional] 
**app_config_id** | **str** |  | [optional] 
**cloudformation_stack_name** | **str** |  | [optional] 
**contents** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**managed_policy_name** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**org_id** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_app_awsiam_policy_config import AppAppAWSIAMPolicyConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AppAppAWSIAMPolicyConfig from a JSON string
app_app_awsiam_policy_config_instance = AppAppAWSIAMPolicyConfig.from_json(json)
# print the JSON string representation of the object
print AppAppAWSIAMPolicyConfig.to_json()

# convert the object into a dict
app_app_awsiam_policy_config_dict = app_app_awsiam_policy_config_instance.to_dict()
# create an instance of AppAppAWSIAMPolicyConfig from a dict
app_app_awsiam_policy_config_form_dict = app_app_awsiam_policy_config.from_dict(app_app_awsiam_policy_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


