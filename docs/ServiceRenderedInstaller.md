# ServiceRenderedInstaller


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apps** | [**List[AppApp]**](AppApp.md) |  | [optional] 
**metadata** | [**AppInstallerMetadata**](AppInstallerMetadata.md) |  | [optional] 
**sandbox_mode** | **bool** |  | [optional] 

## Example

```python
from nuon.models.service_rendered_installer import ServiceRenderedInstaller

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceRenderedInstaller from a JSON string
service_rendered_installer_instance = ServiceRenderedInstaller.from_json(json)
# print the JSON string representation of the object
print ServiceRenderedInstaller.to_json()

# convert the object into a dict
service_rendered_installer_dict = service_rendered_installer_instance.to_dict()
# create an instance of ServiceRenderedInstaller from a dict
service_rendered_installer_form_dict = service_rendered_installer.from_dict(service_rendered_installer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


