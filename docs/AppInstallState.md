# AppInstallState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contents** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**install_id** | **str** |  | [optional] 
**triggered_by_id** | **str** |  | [optional] 
**triggered_by_type** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**version** | **int** |  | [optional] 

## Example

```python
from nuon.models.app_install_state import AppInstallState

# TODO update the JSON string below
json = "{}"
# create an instance of AppInstallState from a JSON string
app_install_state_instance = AppInstallState.from_json(json)
# print the JSON string representation of the object
print AppInstallState.to_json()

# convert the object into a dict
app_install_state_dict = app_install_state_instance.to_dict()
# create an instance of AppInstallState from a dict
app_install_state_form_dict = app_install_state.from_dict(app_install_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


