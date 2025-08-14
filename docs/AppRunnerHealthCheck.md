# AppRunnerHealthCheck


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**minute_bucket** | **str** |  | [optional] 
**runner_id** | **str** |  | [optional] 
**runner_job** | [**AppRunnerJob**](AppRunnerJob.md) |  | [optional] 
**status** | [**AppRunnerStatus**](AppRunnerStatus.md) |  | [optional] 
**status_code** | **int** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_runner_health_check import AppRunnerHealthCheck

# TODO update the JSON string below
json = "{}"
# create an instance of AppRunnerHealthCheck from a JSON string
app_runner_health_check_instance = AppRunnerHealthCheck.from_json(json)
# print the JSON string representation of the object
print AppRunnerHealthCheck.to_json()

# convert the object into a dict
app_runner_health_check_dict = app_runner_health_check_instance.to_dict()
# create an instance of AppRunnerHealthCheck from a dict
app_runner_health_check_form_dict = app_runner_health_check.from_dict(app_runner_health_check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


