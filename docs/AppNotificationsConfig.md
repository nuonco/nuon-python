# AppNotificationsConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**org_id** | **str** |  | [optional] 
**owner_id** | **str** |  | [optional] 
**owner_type** | **str** |  | [optional] 
**slack_webhook_url** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_notifications_config import AppNotificationsConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AppNotificationsConfig from a JSON string
app_notifications_config_instance = AppNotificationsConfig.from_json(json)
# print the JSON string representation of the object
print AppNotificationsConfig.to_json()

# convert the object into a dict
app_notifications_config_dict = app_notifications_config_instance.to_dict()
# create an instance of AppNotificationsConfig from a dict
app_notifications_config_form_dict = app_notifications_config.from_dict(app_notifications_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


