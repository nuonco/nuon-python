# AppSandboxRelease


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**created_by** | [**AppUserToken**](AppUserToken.md) |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**deprovision_policy_url** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**one_click_role_template_url** | **str** |  | [optional] 
**provision_policy_url** | **str** |  | [optional] 
**trust_policy_url** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_sandbox_release import AppSandboxRelease

# TODO update the JSON string below
json = "{}"
# create an instance of AppSandboxRelease from a JSON string
app_sandbox_release_instance = AppSandboxRelease.from_json(json)
# print the JSON string representation of the object
print AppSandboxRelease.to_json()

# convert the object into a dict
app_sandbox_release_dict = app_sandbox_release_instance.to_dict()
# create an instance of AppSandboxRelease from a dict
app_sandbox_release_form_dict = app_sandbox_release.from_dict(app_sandbox_release_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


