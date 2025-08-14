# AppPolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | [**AppPolicyName**](AppPolicyName.md) |  | [optional] 
**permissions** | **Dict[str, str]** | Permissions are used to track granular permissions for each domain | [optional] 
**role_id** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_policy import AppPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of AppPolicy from a JSON string
app_policy_instance = AppPolicy.from_json(json)
# print the JSON string representation of the object
print AppPolicy.to_json()

# convert the object into a dict
app_policy_dict = app_policy_instance.to_dict()
# create an instance of AppPolicy from a dict
app_policy_form_dict = app_policy.from_dict(app_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


