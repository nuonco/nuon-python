# AppRunnerJobExecutionResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contents** | **str** |  | [optional] 
**contents_display** | **str** |  | [optional] 
**contents_display_gzip** | **str** |  | [optional] 
**contents_gzip** | **str** | columns for storage of gzipped contents and plans | [optional] 
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**error_code** | **int** |  | [optional] 
**error_metadata** | **Dict[str, str]** |  | [optional] 
**id** | **str** |  | [optional] 
**org_id** | **str** |  | [optional] 
**runner_job_execution_id** | **str** |  | [optional] 
**success** | **bool** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_runner_job_execution_result import AppRunnerJobExecutionResult

# TODO update the JSON string below
json = "{}"
# create an instance of AppRunnerJobExecutionResult from a JSON string
app_runner_job_execution_result_instance = AppRunnerJobExecutionResult.from_json(json)
# print the JSON string representation of the object
print AppRunnerJobExecutionResult.to_json()

# convert the object into a dict
app_runner_job_execution_result_dict = app_runner_job_execution_result_instance.to_dict()
# create an instance of AppRunnerJobExecutionResult from a dict
app_runner_job_execution_result_form_dict = app_runner_job_execution_result.from_dict(app_runner_job_execution_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


