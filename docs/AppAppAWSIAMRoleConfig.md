# AppAppAWSIAMRoleConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_config_id** | **str** |  | [optional] 
**cloudformation_param_name** | **str** |  | [optional] 
**cloudformation_stack_name** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**org_id** | **str** |  | [optional] 
**owner_id** | **str** |  | [optional] 
**owner_type** | **str** |  | [optional] 
**permissions_boundary** | **str** |  | [optional] 
**policies** | [**List[AppAppAWSIAMPolicyConfig]**](AppAppAWSIAMPolicyConfig.md) |  | [optional] 
**type** | [**AppAWSIAMRoleType**](AppAWSIAMRoleType.md) |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_app_awsiam_role_config import AppAppAWSIAMRoleConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AppAppAWSIAMRoleConfig from a JSON string
app_app_awsiam_role_config_instance = AppAppAWSIAMRoleConfig.from_json(json)
# print the JSON string representation of the object
print AppAppAWSIAMRoleConfig.to_json()

# convert the object into a dict
app_app_awsiam_role_config_dict = app_app_awsiam_role_config_instance.to_dict()
# create an instance of AppAppAWSIAMRoleConfig from a dict
app_app_awsiam_role_config_form_dict = app_app_awsiam_role_config.from_dict(app_app_awsiam_role_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


