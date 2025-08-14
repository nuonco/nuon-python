# StateActionWorkflowState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**outputs** | **Dict[str, object]** |  | [optional] 
**populated** | **bool** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from nuon.models.state_action_workflow_state import StateActionWorkflowState

# TODO update the JSON string below
json = "{}"
# create an instance of StateActionWorkflowState from a JSON string
state_action_workflow_state_instance = StateActionWorkflowState.from_json(json)
# print the JSON string representation of the object
print StateActionWorkflowState.to_json()

# convert the object into a dict
state_action_workflow_state_dict = state_action_workflow_state_instance.to_dict()
# create an instance of StateActionWorkflowState from a dict
state_action_workflow_state_form_dict = state_action_workflow_state.from_dict(state_action_workflow_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


