# AppAzureAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**created_by** | [**AppAccount**](AppAccount.md) |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**install** | [**AppInstall**](AppInstall.md) |  | [optional] 
**location** | **str** |  | [optional] 
**service_principal_app_id** | **str** |  | [optional] 
**service_principal_password** | **str** |  | [optional] 
**subscription_id** | **str** |  | [optional] 
**subscription_tenant_id** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_azure_account import AppAzureAccount

# TODO update the JSON string below
json = "{}"
# create an instance of AppAzureAccount from a JSON string
app_azure_account_instance = AppAzureAccount.from_json(json)
# print the JSON string representation of the object
print AppAzureAccount.to_json()

# convert the object into a dict
app_azure_account_dict = app_azure_account_instance.to_dict()
# create an instance of AppAzureAccount from a dict
app_azure_account_form_dict = app_azure_account.from_dict(app_azure_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


