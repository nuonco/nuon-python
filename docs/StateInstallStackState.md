# StateInstallStackState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checksum** | **str** |  | [optional] 
**outputs** | **Dict[str, str]** |  | [optional] 
**populated** | **bool** |  | [optional] 
**quick_link_url** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**template_json** | **str** |  | [optional] 
**template_url** | **str** |  | [optional] 

## Example

```python
from nuon.models.state_install_stack_state import StateInstallStackState

# TODO update the JSON string below
json = "{}"
# create an instance of StateInstallStackState from a JSON string
state_install_stack_state_instance = StateInstallStackState.from_json(json)
# print the JSON string representation of the object
print StateInstallStackState.to_json()

# convert the object into a dict
state_install_stack_state_dict = state_install_stack_state_instance.to_dict()
# create an instance of StateInstallStackState from a dict
state_install_stack_state_form_dict = state_install_stack_state.from_dict(state_install_stack_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


