# AppAppRunnerConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** |  | [optional] 
**app_runner_type** | [**AppAppRunnerType**](AppAppRunnerType.md) |  | [optional] 
**cloud_platform** | [**AppCloudPlatform**](AppCloudPlatform.md) |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by** | [**AppAccount**](AppAccount.md) |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**env_vars** | **Dict[str, str]** |  | [optional] 
**id** | **str** |  | [optional] 
**org_id** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_app_runner_config import AppAppRunnerConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AppAppRunnerConfig from a JSON string
app_app_runner_config_instance = AppAppRunnerConfig.from_json(json)
# print the JSON string representation of the object
print AppAppRunnerConfig.to_json()

# convert the object into a dict
app_app_runner_config_dict = app_app_runner_config_instance.to_dict()
# create an instance of AppAppRunnerConfig from a dict
app_app_runner_config_form_dict = app_app_runner_config.from_dict(app_app_runner_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


