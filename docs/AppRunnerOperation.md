# AppRunnerOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**log_stream** | [**AppLogStream**](AppLogStream.md) | job details | [optional] 
**operation_type** | [**AppRunnerOperationType**](AppRunnerOperationType.md) |  | [optional] 
**runner_id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**status_description** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_runner_operation import AppRunnerOperation

# TODO update the JSON string below
json = "{}"
# create an instance of AppRunnerOperation from a JSON string
app_runner_operation_instance = AppRunnerOperation.from_json(json)
# print the JSON string representation of the object
print AppRunnerOperation.to_json()

# convert the object into a dict
app_runner_operation_dict = app_runner_operation_instance.to_dict()
# create an instance of AppRunnerOperation from a dict
app_runner_operation_form_dict = app_runner_operation.from_dict(app_runner_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


