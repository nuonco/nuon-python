# AppUserOrg


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**created_by** | [**AppUserToken**](AppUserToken.md) |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**org_id** | **str** | parent relationship | [optional] 
**updated_at** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_user_org import AppUserOrg

# TODO update the JSON string below
json = "{}"
# create an instance of AppUserOrg from a JSON string
app_user_org_instance = AppUserOrg.from_json(json)
# print the JSON string representation of the object
print AppUserOrg.to_json()

# convert the object into a dict
app_user_org_dict = app_user_org_instance.to_dict()
# create an instance of AppUserOrg from a dict
app_user_org_form_dict = app_user_org.from_dict(app_user_org_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


