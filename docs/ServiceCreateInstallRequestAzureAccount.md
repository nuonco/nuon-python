# ServiceCreateInstallRequestAzureAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | **str** |  | [optional] 
**service_principal_app_id** | **str** |  | [optional] 
**service_principal_password** | **str** |  | [optional] 
**subscription_id** | **str** |  | [optional] 
**subscription_tenant_id** | **str** |  | [optional] 

## Example

```python
from nuon.models.service_create_install_request_azure_account import ServiceCreateInstallRequestAzureAccount

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCreateInstallRequestAzureAccount from a JSON string
service_create_install_request_azure_account_instance = ServiceCreateInstallRequestAzureAccount.from_json(json)
# print the JSON string representation of the object
print ServiceCreateInstallRequestAzureAccount.to_json()

# convert the object into a dict
service_create_install_request_azure_account_dict = service_create_install_request_azure_account_instance.to_dict()
# create an instance of ServiceCreateInstallRequestAzureAccount from a dict
service_create_install_request_azure_account_form_dict = service_create_install_request_azure_account.from_dict(service_create_install_request_azure_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


