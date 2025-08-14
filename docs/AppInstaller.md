# AppInstaller


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apps** | [**List[AppApp]**](AppApp.md) |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**metadata** | [**AppInstallerMetadata**](AppInstallerMetadata.md) |  | [optional] 
**org_id** | **str** |  | [optional] 
**type** | [**AppInstallerType**](AppInstallerType.md) |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_installer import AppInstaller

# TODO update the JSON string below
json = "{}"
# create an instance of AppInstaller from a JSON string
app_installer_instance = AppInstaller.from_json(json)
# print the JSON string representation of the object
print AppInstaller.to_json()

# convert the object into a dict
app_installer_dict = app_installer_instance.to_dict()
# create an instance of AppInstaller from a dict
app_installer_form_dict = app_installer.from_dict(app_installer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


