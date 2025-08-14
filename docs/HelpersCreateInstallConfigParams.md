# HelpersCreateInstallConfigParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approval_option** | [**AppInstallApprovalOption**](AppInstallApprovalOption.md) |  | [optional] 

## Example

```python
from nuon.models.helpers_create_install_config_params import HelpersCreateInstallConfigParams

# TODO update the JSON string below
json = "{}"
# create an instance of HelpersCreateInstallConfigParams from a JSON string
helpers_create_install_config_params_instance = HelpersCreateInstallConfigParams.from_json(json)
# print the JSON string representation of the object
print HelpersCreateInstallConfigParams.to_json()

# convert the object into a dict
helpers_create_install_config_params_dict = helpers_create_install_config_params_instance.to_dict()
# create an instance of HelpersCreateInstallConfigParams from a dict
helpers_create_install_config_params_form_dict = helpers_create_install_config_params.from_dict(helpers_create_install_config_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


