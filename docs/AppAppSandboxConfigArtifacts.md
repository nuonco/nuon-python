# AppAppSandboxConfigArtifacts

Links are dynamically loaded using an after query

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloudformation_stack_template** | **str** |  | [optional] 
**deprovision_policy** | **str** |  | [optional] 
**provision_policy** | **str** |  | [optional] 
**trust_policy** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_app_sandbox_config_artifacts import AppAppSandboxConfigArtifacts

# TODO update the JSON string below
json = "{}"
# create an instance of AppAppSandboxConfigArtifacts from a JSON string
app_app_sandbox_config_artifacts_instance = AppAppSandboxConfigArtifacts.from_json(json)
# print the JSON string representation of the object
print AppAppSandboxConfigArtifacts.to_json()

# convert the object into a dict
app_app_sandbox_config_artifacts_dict = app_app_sandbox_config_artifacts_instance.to_dict()
# create an instance of AppAppSandboxConfigArtifacts from a dict
app_app_sandbox_config_artifacts_form_dict = app_app_sandbox_config_artifacts.from_dict(app_app_sandbox_config_artifacts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


