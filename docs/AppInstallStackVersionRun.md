# AppInstallStackVersionRun


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**data** | **Dict[str, str]** |  | [optional] 
**id** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_install_stack_version_run import AppInstallStackVersionRun

# TODO update the JSON string below
json = "{}"
# create an instance of AppInstallStackVersionRun from a JSON string
app_install_stack_version_run_instance = AppInstallStackVersionRun.from_json(json)
# print the JSON string representation of the object
print AppInstallStackVersionRun.to_json()

# convert the object into a dict
app_install_stack_version_run_dict = app_install_stack_version_run_instance.to_dict()
# create an instance of AppInstallStackVersionRun from a dict
app_install_stack_version_run_form_dict = app_install_stack_version_run.from_dict(app_install_stack_version_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


