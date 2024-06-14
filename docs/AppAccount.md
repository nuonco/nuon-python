# AppAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_type** | [**AppAccountType**](AppAccountType.md) |  | [optional] 
**created_at** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**org_ids** | **List[str]** | ReadOnly Fields | [optional] 
**orgs** | [**List[AppOrg]**](AppOrg.md) |  | [optional] 
**permissions** | [**Dict[str, PermissionsPermission]**](PermissionsPermission.md) |  | [optional] 
**roles** | [**List[AppRole]**](AppRole.md) |  | [optional] 
**subject** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_account import AppAccount

# TODO update the JSON string below
json = "{}"
# create an instance of AppAccount from a JSON string
app_account_instance = AppAccount.from_json(json)
# print the JSON string representation of the object
print AppAccount.to_json()

# convert the object into a dict
app_account_dict = app_account_instance.to_dict()
# create an instance of AppAccount from a dict
app_account_form_dict = app_account.from_dict(app_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


