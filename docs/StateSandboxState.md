# StateSandboxState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**outputs** | **Dict[str, object]** |  | [optional] 
**populated** | **bool** |  | [optional] 
**recent_runs** | [**List[StateSandboxState]**](StateSandboxState.md) |  | [optional] 
**status** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from nuon.models.state_sandbox_state import StateSandboxState

# TODO update the JSON string below
json = "{}"
# create an instance of StateSandboxState from a JSON string
state_sandbox_state_instance = StateSandboxState.from_json(json)
# print the JSON string representation of the object
print StateSandboxState.to_json()

# convert the object into a dict
state_sandbox_state_dict = state_sandbox_state_instance.to_dict()
# create an instance of StateSandboxState from a dict
state_sandbox_state_form_dict = state_sandbox_state.from_dict(state_sandbox_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


