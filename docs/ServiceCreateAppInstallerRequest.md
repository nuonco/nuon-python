# ServiceCreateAppInstallerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**links** | [**ServiceCreateAppInstallerRequestLinks**](ServiceCreateAppInstallerRequestLinks.md) |  | [optional] 
**name** | **str** |  | 
**slug** | **str** |  | 

## Example

```python
from nuon.models.service_create_app_installer_request import ServiceCreateAppInstallerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCreateAppInstallerRequest from a JSON string
service_create_app_installer_request_instance = ServiceCreateAppInstallerRequest.from_json(json)
# print the JSON string representation of the object
print ServiceCreateAppInstallerRequest.to_json()

# convert the object into a dict
service_create_app_installer_request_dict = service_create_app_installer_request_instance.to_dict()
# create an instance of ServiceCreateAppInstallerRequest from a dict
service_create_app_installer_request_form_dict = service_create_app_installer_request.from_dict(service_create_app_installer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


