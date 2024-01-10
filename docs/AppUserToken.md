# AppUserToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**expires_at** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**issued_at** | **str** |  | [optional] 
**issuer** | **str** |  | [optional] 
**subject** | **str** | claim data | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_user_token import AppUserToken

# TODO update the JSON string below
json = "{}"
# create an instance of AppUserToken from a JSON string
app_user_token_instance = AppUserToken.from_json(json)
# print the JSON string representation of the object
print AppUserToken.to_json()

# convert the object into a dict
app_user_token_dict = app_user_token_instance.to_dict()
# create an instance of AppUserToken from a dict
app_user_token_form_dict = app_user_token.from_dict(app_user_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


