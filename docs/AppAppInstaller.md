# AppAppInstaller


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app** | [**AppApp**](AppApp.md) |  | [optional] 
**app_id** | **str** |  | [optional] 
**app_installer_metadata** | [**AppAppInstallerMetadata**](AppAppInstallerMetadata.md) |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by** | [**AppUserToken**](AppUserToken.md) |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**installer_url** | **str** | filled in via after query | [optional] 
**org_id** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_app_installer import AppAppInstaller

# TODO update the JSON string below
json = "{}"
# create an instance of AppAppInstaller from a JSON string
app_app_installer_instance = AppAppInstaller.from_json(json)
# print the JSON string representation of the object
print AppAppInstaller.to_json()

# convert the object into a dict
app_app_installer_dict = app_app_installer_instance.to_dict()
# create an instance of AppAppInstaller from a dict
app_app_installer_form_dict = app_app_installer.from_dict(app_app_installer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


