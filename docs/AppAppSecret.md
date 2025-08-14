# AppAppSecret


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**length** | **int** | after query fields | [optional] 
**name** | **str** |  | [optional] 
**org_id** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_app_secret import AppAppSecret

# TODO update the JSON string below
json = "{}"
# create an instance of AppAppSecret from a JSON string
app_app_secret_instance = AppAppSecret.from_json(json)
# print the JSON string representation of the object
print AppAppSecret.to_json()

# convert the object into a dict
app_app_secret_dict = app_app_secret_instance.to_dict()
# create an instance of AppAppSecret from a dict
app_app_secret_form_dict = app_app_secret.from_dict(app_app_secret_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


