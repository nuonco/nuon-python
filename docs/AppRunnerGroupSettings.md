# AppRunnerGroupSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container_image_tag** | **str** |  | [optional] 
**container_image_url** | **str** | configuration for deploying the runner | [optional] 
**created_at** | **str** |  | [optional] 
**created_by** | [**AppAccount**](AppAccount.md) |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**env** | **str** | Never persisted, populated at runtime from the overall ctl-api settings | [optional] 
**heart_beat_timeout** | **int** | Various settings for the runner to handle internally | [optional] 
**id** | **str** |  | [optional] 
**org_id** | **str** |  | [optional] 
**otel_collector_config** | **str** |  | [optional] 
**runner_api_url** | **str** |  | [optional] 
**runner_group_id** | **str** |  | [optional] 
**settings_refresh_timeout** | **int** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_runner_group_settings import AppRunnerGroupSettings

# TODO update the JSON string below
json = "{}"
# create an instance of AppRunnerGroupSettings from a JSON string
app_runner_group_settings_instance = AppRunnerGroupSettings.from_json(json)
# print the JSON string representation of the object
print AppRunnerGroupSettings.to_json()

# convert the object into a dict
app_runner_group_settings_dict = app_runner_group_settings_instance.to_dict()
# create an instance of AppRunnerGroupSettings from a dict
app_runner_group_settings_form_dict = app_runner_group_settings.from_dict(app_runner_group_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


