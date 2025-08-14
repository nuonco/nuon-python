# AppOrg


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**features** | **Dict[str, bool]** |  | [optional] 
**id** | **str** |  | [optional] 
**links** | **Dict[str, object]** |  | [optional] 
**logo_url** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**notifications_config** | [**AppNotificationsConfig**](AppNotificationsConfig.md) |  | [optional] 
**runner_group** | [**AppRunnerGroup**](AppRunnerGroup.md) |  | [optional] 
**sandbox_mode** | **bool** |  | [optional] 
**status** | **str** |  | [optional] 
**status_description** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**vcs_connections** | [**List[AppVCSConnection]**](AppVCSConnection.md) |  | [optional] 

## Example

```python
from nuon.models.app_org import AppOrg

# TODO update the JSON string below
json = "{}"
# create an instance of AppOrg from a JSON string
app_org_instance = AppOrg.from_json(json)
# print the JSON string representation of the object
print AppOrg.to_json()

# convert the object into a dict
app_org_dict = app_org_instance.to_dict()
# create an instance of AppOrg from a dict
app_org_form_dict = app_org.from_dict(app_org_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


