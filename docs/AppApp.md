# AppApp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_platform** | [**AppCloudPlatform**](AppCloudPlatform.md) |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by** | [**AppUserToken**](AppUserToken.md) |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**input_config** | [**AppAppInputConfig**](AppAppInputConfig.md) | fields set via after query | [optional] 
**name** | **str** |  | [optional] 
**notifications_config** | [**AppNotificationsConfig**](AppNotificationsConfig.md) |  | [optional] 
**org_id** | **str** |  | [optional] 
**runner_config** | [**AppAppRunnerConfig**](AppAppRunnerConfig.md) |  | [optional] 
**sandbox_config** | [**AppAppSandboxConfig**](AppAppSandboxConfig.md) |  | [optional] 
**slack_webhook_url** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**status_description** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_app import AppApp

# TODO update the JSON string below
json = "{}"
# create an instance of AppApp from a JSON string
app_app_instance = AppApp.from_json(json)
# print the JSON string representation of the object
print AppApp.to_json()

# convert the object into a dict
app_app_dict = app_app_instance.to_dict()
# create an instance of AppApp from a dict
app_app_form_dict = app_app.from_dict(app_app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


