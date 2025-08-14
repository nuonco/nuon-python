# ServiceCreateInstallRequestAwsAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iam_role_arn** | **str** |  | [optional] 
**region** | **str** |  | [optional] 

## Example

```python
from nuon.models.service_create_install_request_aws_account import ServiceCreateInstallRequestAwsAccount

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCreateInstallRequestAwsAccount from a JSON string
service_create_install_request_aws_account_instance = ServiceCreateInstallRequestAwsAccount.from_json(json)
# print the JSON string representation of the object
print ServiceCreateInstallRequestAwsAccount.to_json()

# convert the object into a dict
service_create_install_request_aws_account_dict = service_create_install_request_aws_account_instance.to_dict()
# create an instance of ServiceCreateInstallRequestAwsAccount from a dict
service_create_install_request_aws_account_form_dict = service_create_install_request_aws_account.from_dict(service_create_install_request_aws_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


