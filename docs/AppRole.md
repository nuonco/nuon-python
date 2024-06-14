# AppRole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | [**AppAccount**](AppAccount.md) |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**policies** | [**List[AppPolicy]**](AppPolicy.md) |  | [optional] 
**role_type** | [**AppRoleType**](AppRoleType.md) |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_role import AppRole

# TODO update the JSON string below
json = "{}"
# create an instance of AppRole from a JSON string
app_role_instance = AppRole.from_json(json)
# print the JSON string representation of the object
print AppRole.to_json()

# convert the object into a dict
app_role_dict = app_role_instance.to_dict()
# create an instance of AppRole from a dict
app_role_form_dict = app_role.from_dict(app_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


