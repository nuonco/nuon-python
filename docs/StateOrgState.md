# StateOrgState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**populated** | **bool** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from nuon.models.state_org_state import StateOrgState

# TODO update the JSON string below
json = "{}"
# create an instance of StateOrgState from a JSON string
state_org_state_instance = StateOrgState.from_json(json)
# print the JSON string representation of the object
print StateOrgState.to_json()

# convert the object into a dict
state_org_state_dict = state_org_state_instance.to_dict()
# create an instance of StateOrgState from a dict
state_org_state_form_dict = state_org_state.from_dict(state_org_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


