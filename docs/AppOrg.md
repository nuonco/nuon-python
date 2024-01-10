# AppOrg


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**custom_cert** | **bool** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**sandbox_mode** | **bool** | These fields are used to control the behaviour of the org NOTE: these are starting as nullable, so we can update stage/prod before resetting locally. | [optional] 
**status** | **str** |  | [optional] 
**status_description** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**users** | [**List[AppUserOrg]**](AppUserOrg.md) |  | [optional] 
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


