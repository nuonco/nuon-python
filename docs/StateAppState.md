# StateAppState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**populated** | **bool** |  | [optional] 
**secrets** | **Dict[str, str]** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from nuon.models.state_app_state import StateAppState

# TODO update the JSON string below
json = "{}"
# create an instance of StateAppState from a JSON string
state_app_state_instance = StateAppState.from_json(json)
# print the JSON string representation of the object
print StateAppState.to_json()

# convert the object into a dict
state_app_state_dict = state_app_state_instance.to_dict()
# create an instance of StateAppState from a dict
state_app_state_form_dict = state_app_state.from_dict(state_app_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


