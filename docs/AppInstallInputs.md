# AppInstallInputs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_input_config_id** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**install_id** | **str** |  | [optional] 
**org_id** | **str** |  | [optional] 
**redacted_values** | **Dict[str, str]** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**values** | **Dict[str, str]** |  | [optional] 

## Example

```python
from nuon.models.app_install_inputs import AppInstallInputs

# TODO update the JSON string below
json = "{}"
# create an instance of AppInstallInputs from a JSON string
app_install_inputs_instance = AppInstallInputs.from_json(json)
# print the JSON string representation of the object
print AppInstallInputs.to_json()

# convert the object into a dict
app_install_inputs_dict = app_install_inputs_instance.to_dict()
# create an instance of AppInstallInputs from a dict
app_install_inputs_form_dict = app_install_inputs.from_dict(app_install_inputs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


