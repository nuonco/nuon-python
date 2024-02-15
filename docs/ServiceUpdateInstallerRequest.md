# ServiceUpdateInstallerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**links** | [**ServiceUpdateInstallerRequestLinks**](ServiceUpdateInstallerRequestLinks.md) |  | [optional] 
**name** | **str** |  | 
**post_install_markdown** | **str** |  | [optional] 

## Example

```python
from nuon.models.service_update_installer_request import ServiceUpdateInstallerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceUpdateInstallerRequest from a JSON string
service_update_installer_request_instance = ServiceUpdateInstallerRequest.from_json(json)
# print the JSON string representation of the object
print ServiceUpdateInstallerRequest.to_json()

# convert the object into a dict
service_update_installer_request_dict = service_update_installer_request_instance.to_dict()
# create an instance of ServiceUpdateInstallerRequest from a dict
service_update_installer_request_form_dict = service_update_installer_request.from_dict(service_update_installer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


