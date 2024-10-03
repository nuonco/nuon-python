# AppRunner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**created_by** | [**AppAccount**](AppAccount.md) |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**jobs** | [**List[AppRunnerJob]**](AppRunnerJob.md) |  | [optional] 
**name** | **str** |  | [optional] 
**org** | [**AppOrg**](AppOrg.md) |  | [optional] 
**org_id** | **str** |  | [optional] 
**runner_id** | **str** |  | [optional] 
**runner_job** | [**AppRunnerJob**](AppRunnerJob.md) |  | [optional] 
**status** | **str** |  | [optional] 
**status_description** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_runner import AppRunner

# TODO update the JSON string below
json = "{}"
# create an instance of AppRunner from a JSON string
app_runner_instance = AppRunner.from_json(json)
# print the JSON string representation of the object
print AppRunner.to_json()

# convert the object into a dict
app_runner_dict = app_runner_instance.to_dict()
# create an instance of AppRunner from a dict
app_runner_form_dict = app_runner.from_dict(app_runner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


