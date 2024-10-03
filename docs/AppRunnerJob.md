# AppRunnerJob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_timeout** | **int** | available timeout is how long a job can be marked as \&quot;available\&quot; before being requeued | [optional] 
**created_at** | **str** |  | [optional] 
**created_by** | [**AppAccount**](AppAccount.md) |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**execution_timeout** | **int** | execution timeout is how long a job can be marked as \&quot;exeucuting\&quot; before being requeued | [optional] 
**executions** | [**List[AppRunnerJobExecution]**](AppRunnerJobExecution.md) |  | [optional] 
**group** | [**AppRunnerJobGroup**](AppRunnerJobGroup.md) |  | [optional] 
**id** | **str** |  | [optional] 
**max_executions** | **int** |  | [optional] 
**operation** | [**AppRunnerJobOperationType**](AppRunnerJobOperationType.md) |  | [optional] 
**org** | [**AppOrg**](AppOrg.md) |  | [optional] 
**org_id** | **str** |  | [optional] 
**overall_timeout** | **int** | overall timeout is how long a job can be attempted, before being cancelled | [optional] 
**owner_id** | **str** |  | [optional] 
**owner_type** | **str** |  | [optional] 
**queue_timeout** | **int** | queue timeout is how long a job can be queued, before being made available | [optional] 
**runner_id** | **str** |  | [optional] 
**status** | [**AppRunnerJobStatus**](AppRunnerJobStatus.md) |  | [optional] 
**status_description** | **str** |  | [optional] 
**type** | [**AppRunnerJobType**](AppRunnerJobType.md) |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_runner_job import AppRunnerJob

# TODO update the JSON string below
json = "{}"
# create an instance of AppRunnerJob from a JSON string
app_runner_job_instance = AppRunnerJob.from_json(json)
# print the JSON string representation of the object
print AppRunnerJob.to_json()

# convert the object into a dict
app_runner_job_dict = app_runner_job_instance.to_dict()
# create an instance of AppRunnerJob from a dict
app_runner_job_form_dict = app_runner_job.from_dict(app_runner_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


