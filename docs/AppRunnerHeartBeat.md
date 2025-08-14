# AppRunnerHeartBeat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alive_time** | **int** |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**runner_id** | **str** |  | [optional] 
**started_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_runner_heart_beat import AppRunnerHeartBeat

# TODO update the JSON string below
json = "{}"
# create an instance of AppRunnerHeartBeat from a JSON string
app_runner_heart_beat_instance = AppRunnerHeartBeat.from_json(json)
# print the JSON string representation of the object
print AppRunnerHeartBeat.to_json()

# convert the object into a dict
app_runner_heart_beat_dict = app_runner_heart_beat_instance.to_dict()
# create an instance of AppRunnerHeartBeat from a dict
app_runner_heart_beat_form_dict = app_runner_heart_beat.from_dict(app_runner_heart_beat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


