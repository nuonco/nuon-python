# ServiceAppInstaller


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app** | [**AppApp**](AppApp.md) |  | [optional] 
**app_inputs** | [**AppAppInputConfig**](AppAppInputConfig.md) |  | [optional] 
**app_sandbox** | [**AppAppSandboxConfig**](AppAppSandboxConfig.md) |  | [optional] 
**metadata** | [**AppAppInstallerMetadata**](AppAppInstallerMetadata.md) |  | [optional] 
**sandbox_mode** | **bool** |  | [optional] 

## Example

```python
from nuon.models.service_app_installer import ServiceAppInstaller

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceAppInstaller from a JSON string
service_app_installer_instance = ServiceAppInstaller.from_json(json)
# print the JSON string representation of the object
print ServiceAppInstaller.to_json()

# convert the object into a dict
service_app_installer_dict = service_app_installer_instance.to_dict()
# create an instance of ServiceAppInstaller from a dict
service_app_installer_form_dict = service_app_installer.from_dict(service_app_installer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


