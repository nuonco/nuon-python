# StateInputsState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inputs** | **Dict[str, str]** |  | [optional] 
**populated** | **bool** |  | [optional] 

## Example

```python
from nuon.models.state_inputs_state import StateInputsState

# TODO update the JSON string below
json = "{}"
# create an instance of StateInputsState from a JSON string
state_inputs_state_instance = StateInputsState.from_json(json)
# print the JSON string representation of the object
print StateInputsState.to_json()

# convert the object into a dict
state_inputs_state_dict = state_inputs_state_instance.to_dict()
# create an instance of StateInputsState from a dict
state_inputs_state_form_dict = state_inputs_state.from_dict(state_inputs_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


