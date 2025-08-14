# AppRunnerGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**org_id** | **str** |  | [optional] 
**owner_id** | **str** | parent can org, install or in the future, builtin runner group | [optional] 
**owner_type** | **str** |  | [optional] 
**platform** | [**AppAppRunnerType**](AppAppRunnerType.md) |  | [optional] 
**runners** | [**List[AppRunner]**](AppRunner.md) |  | [optional] 
**settings** | [**AppRunnerGroupSettings**](AppRunnerGroupSettings.md) |  | [optional] 
**type** | [**AppRunnerGroupType**](AppRunnerGroupType.md) |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_runner_group import AppRunnerGroup

# TODO update the JSON string below
json = "{}"
# create an instance of AppRunnerGroup from a JSON string
app_runner_group_instance = AppRunnerGroup.from_json(json)
# print the JSON string representation of the object
print AppRunnerGroup.to_json()

# convert the object into a dict
app_runner_group_dict = app_runner_group_instance.to_dict()
# create an instance of AppRunnerGroup from a dict
app_runner_group_form_dict = app_runner_group.from_dict(app_runner_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


