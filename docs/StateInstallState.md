# StateInstallState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**inputs** | **Dict[str, str]** |  | [optional] 
**internal_domain** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**populated** | **bool** |  | [optional] 
**public_domain** | **str** |  | [optional] 
**sandbox** | [**StateSandboxState**](StateSandboxState.md) |  | [optional] 

## Example

```python
from nuon.models.state_install_state import StateInstallState

# TODO update the JSON string below
json = "{}"
# create an instance of StateInstallState from a JSON string
state_install_state_instance = StateInstallState.from_json(json)
# print the JSON string representation of the object
print StateInstallState.to_json()

# convert the object into a dict
state_install_state_dict = state_install_state_instance.to_dict()
# create an instance of StateInstallState from a dict
state_install_state_form_dict = state_install_state.from_dict(state_install_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


