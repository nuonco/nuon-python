# AppAWSAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**iam_role_arn** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**region** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.app_aws_account import AppAWSAccount

# TODO update the JSON string below
json = "{}"
# create an instance of AppAWSAccount from a JSON string
app_aws_account_instance = AppAWSAccount.from_json(json)
# print the JSON string representation of the object
print AppAWSAccount.to_json()

# convert the object into a dict
app_aws_account_dict = app_aws_account_instance.to_dict()
# create an instance of AppAWSAccount from a dict
app_aws_account_form_dict = app_aws_account.from_dict(app_aws_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


