# AppRunnerJobExecutionOutputs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**org_id** | **str** |  | [optional] 
**outputs** | **Dict[str, object]** |  | [optional] 
**outputs_json** | **str** |  | [optional] 
**runner_job_execution_id** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_runner_job_execution_outputs import AppRunnerJobExecutionOutputs

# TODO update the JSON string below
json = "{}"
# create an instance of AppRunnerJobExecutionOutputs from a JSON string
app_runner_job_execution_outputs_instance = AppRunnerJobExecutionOutputs.from_json(json)
# print the JSON string representation of the object
print AppRunnerJobExecutionOutputs.to_json()

# convert the object into a dict
app_runner_job_execution_outputs_dict = app_runner_job_execution_outputs_instance.to_dict()
# create an instance of AppRunnerJobExecutionOutputs from a dict
app_runner_job_execution_outputs_form_dict = app_runner_job_execution_outputs.from_dict(app_runner_job_execution_outputs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


