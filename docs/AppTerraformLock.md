# AppTerraformLock


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**info** | **str** |  | [optional] 
**operation** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**version** | **object** |  | [optional] 
**who** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_terraform_lock import AppTerraformLock

# TODO update the JSON string below
json = "{}"
# create an instance of AppTerraformLock from a JSON string
app_terraform_lock_instance = AppTerraformLock.from_json(json)
# print the JSON string representation of the object
print AppTerraformLock.to_json()

# convert the object into a dict
app_terraform_lock_dict = app_terraform_lock_instance.to_dict()
# create an instance of AppTerraformLock from a dict
app_terraform_lock_form_dict = app_terraform_lock.from_dict(app_terraform_lock_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


