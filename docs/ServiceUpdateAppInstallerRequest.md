# ServiceUpdateAppInstallerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**links** | [**ServiceUpdateAppInstallerRequestLinks**](ServiceUpdateAppInstallerRequestLinks.md) |  | [optional] 
**name** | **str** |  | 

## Example

```python
from openapi_client.models.service_update_app_installer_request import ServiceUpdateAppInstallerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceUpdateAppInstallerRequest from a JSON string
service_update_app_installer_request_instance = ServiceUpdateAppInstallerRequest.from_json(json)
# print the JSON string representation of the object
print ServiceUpdateAppInstallerRequest.to_json()

# convert the object into a dict
service_update_app_installer_request_dict = service_update_app_installer_request_instance.to_dict()
# create an instance of ServiceUpdateAppInstallerRequest from a dict
service_update_app_installer_request_form_dict = service_update_app_installer_request.from_dict(service_update_app_installer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


