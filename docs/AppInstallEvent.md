# AppInstallEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**install_id** | **str** |  | [optional] 
**operation** | **str** |  | [optional] 
**operation_name** | **str** |  | [optional] 
**operation_status** | [**AppOperationStatus**](AppOperationStatus.md) |  | [optional] 
**org_id** | **str** |  | [optional] 
**payload** | **Dict[str, str]** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_install_event import AppInstallEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AppInstallEvent from a JSON string
app_install_event_instance = AppInstallEvent.from_json(json)
# print the JSON string representation of the object
print AppInstallEvent.to_json()

# convert the object into a dict
app_install_event_dict = app_install_event_instance.to_dict()
# create an instance of AppInstallEvent from a dict
app_install_event_form_dict = app_install_event.from_dict(app_install_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


