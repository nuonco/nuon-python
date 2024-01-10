# ServiceCreateAppInstallerRequestLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**community** | **str** |  | 
**demo** | **str** |  | [optional] 
**documentation** | **str** |  | 
**github** | **str** |  | 
**homepage** | **str** |  | 
**logo** | **str** |  | 

## Example

```python
from nuon.models.service_create_app_installer_request_links import ServiceCreateAppInstallerRequestLinks

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCreateAppInstallerRequestLinks from a JSON string
service_create_app_installer_request_links_instance = ServiceCreateAppInstallerRequestLinks.from_json(json)
# print the JSON string representation of the object
print ServiceCreateAppInstallerRequestLinks.to_json()

# convert the object into a dict
service_create_app_installer_request_links_dict = service_create_app_installer_request_links_instance.to_dict()
# create an instance of ServiceCreateAppInstallerRequestLinks from a dict
service_create_app_installer_request_links_form_dict = service_create_app_installer_request_links.from_dict(service_create_app_installer_request_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


