# AppRunnerJobExecution


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**created_by** | [**AppAccount**](AppAccount.md) |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**org** | [**AppOrg**](AppOrg.md) |  | [optional] 
**org_id** | **str** |  | [optional] 
**result** | [**AppRunnerJobExecutionResult**](AppRunnerJobExecutionResult.md) |  | [optional] 
**runner_job_id** | **str** |  | [optional] 
**status** | [**AppRunnerJobExecutionStatus**](AppRunnerJobExecutionStatus.md) |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_runner_job_execution import AppRunnerJobExecution

# TODO update the JSON string below
json = "{}"
# create an instance of AppRunnerJobExecution from a JSON string
app_runner_job_execution_instance = AppRunnerJobExecution.from_json(json)
# print the JSON string representation of the object
print AppRunnerJobExecution.to_json()

# convert the object into a dict
app_runner_job_execution_dict = app_runner_job_execution_instance.to_dict()
# create an instance of AppRunnerJobExecution from a dict
app_runner_job_execution_form_dict = app_runner_job_execution.from_dict(app_runner_job_execution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


