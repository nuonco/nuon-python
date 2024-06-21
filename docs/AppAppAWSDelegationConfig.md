# AppAppAWSDelegationConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key_id** | **str** | static credentials for long lived cross account access. NOTE: this is not recommended for long-term usage, just to be used for short term access before gov-cloud support is fully spun up. | [optional] 
**app_sandbox_config_id** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by** | [**AppAccount**](AppAccount.md) |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**iam_role_arn** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**org_id** | **str** |  | [optional] 
**secret_access_key** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_app_aws_delegation_config import AppAppAWSDelegationConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AppAppAWSDelegationConfig from a JSON string
app_app_aws_delegation_config_instance = AppAppAWSDelegationConfig.from_json(json)
# print the JSON string representation of the object
print AppAppAWSDelegationConfig.to_json()

# convert the object into a dict
app_app_aws_delegation_config_dict = app_app_aws_delegation_config_instance.to_dict()
# create an instance of AppAppAWSDelegationConfig from a dict
app_app_aws_delegation_config_form_dict = app_app_aws_delegation_config.from_dict(app_app_aws_delegation_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


