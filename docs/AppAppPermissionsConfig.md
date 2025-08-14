# AppAppPermissionsConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_config_id** | **str** |  | [optional] 
**app_id** | **str** |  | [optional] 
**aws_iam_roles** | [**List[AppAppAWSIAMRoleConfig]**](AppAppAWSIAMRoleConfig.md) |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**deprovision_aws_iam_role** | [**AppAppAWSIAMRoleConfig**](AppAppAWSIAMRoleConfig.md) |  | [optional] 
**id** | **str** |  | [optional] 
**maintenance_aws_iam_role** | [**AppAppAWSIAMRoleConfig**](AppAppAWSIAMRoleConfig.md) |  | [optional] 
**org_id** | **str** |  | [optional] 
**provision_aws_iam_role** | [**AppAppAWSIAMRoleConfig**](AppAppAWSIAMRoleConfig.md) | loaded via an after query | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_app_permissions_config import AppAppPermissionsConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AppAppPermissionsConfig from a JSON string
app_app_permissions_config_instance = AppAppPermissionsConfig.from_json(json)
# print the JSON string representation of the object
print AppAppPermissionsConfig.to_json()

# convert the object into a dict
app_app_permissions_config_dict = app_app_permissions_config_instance.to_dict()
# create an instance of AppAppPermissionsConfig from a dict
app_app_permissions_config_form_dict = app_app_permissions_config.from_dict(app_app_permissions_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


