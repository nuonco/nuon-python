# StateRunnerState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**populated** | **bool** |  | [optional] 
**runner_group_id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from nuon.models.state_runner_state import StateRunnerState

# TODO update the JSON string below
json = "{}"
# create an instance of StateRunnerState from a JSON string
state_runner_state_instance = StateRunnerState.from_json(json)
# print the JSON string representation of the object
print StateRunnerState.to_json()

# convert the object into a dict
state_runner_state_dict = state_runner_state_instance.to_dict()
# create an instance of StateRunnerState from a dict
state_runner_state_form_dict = state_runner_state.from_dict(state_runner_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


