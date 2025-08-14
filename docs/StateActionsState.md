# StateActionsState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**populated** | **bool** |  | [optional] 
**workflows** | [**Dict[str, StateActionWorkflowState]**](StateActionWorkflowState.md) |  | [optional] 

## Example

```python
from nuon.models.state_actions_state import StateActionsState

# TODO update the JSON string below
json = "{}"
# create an instance of StateActionsState from a JSON string
state_actions_state_instance = StateActionsState.from_json(json)
# print the JSON string representation of the object
print StateActionsState.to_json()

# convert the object into a dict
state_actions_state_dict = state_actions_state_instance.to_dict()
# create an instance of StateActionsState from a dict
state_actions_state_form_dict = state_actions_state.from_dict(state_actions_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


