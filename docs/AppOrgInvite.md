# AppOrgInvite


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**created_by** | [**AppAccount**](AppAccount.md) |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**org_id** | **str** | parent relationship | [optional] 
**role_type** | [**AppRoleType**](AppRoleType.md) |  | [optional] 
**status** | [**AppOrgInviteStatus**](AppOrgInviteStatus.md) |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_org_invite import AppOrgInvite

# TODO update the JSON string below
json = "{}"
# create an instance of AppOrgInvite from a JSON string
app_org_invite_instance = AppOrgInvite.from_json(json)
# print the JSON string representation of the object
print AppOrgInvite.to_json()

# convert the object into a dict
app_org_invite_dict = app_org_invite_instance.to_dict()
# create an instance of AppOrgInvite from a dict
app_org_invite_form_dict = app_org_invite.from_dict(app_org_invite_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


