# StateDomainState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**internal_domain** | **str** |  | [optional] 
**populated** | **bool** |  | [optional] 
**public_domain** | **str** |  | [optional] 

## Example

```python
from nuon.models.state_domain_state import StateDomainState

# TODO update the JSON string below
json = "{}"
# create an instance of StateDomainState from a JSON string
state_domain_state_instance = StateDomainState.from_json(json)
# print the JSON string representation of the object
print StateDomainState.to_json()

# convert the object into a dict
state_domain_state_dict = state_domain_state_instance.to_dict()
# create an instance of StateDomainState from a dict
state_domain_state_form_dict = state_domain_state.from_dict(state_domain_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


