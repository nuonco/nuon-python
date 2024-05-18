# ServiceCreateInstallerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_ids** | **List[str]** |  | 
**metadata** | [**ServiceCreateInstallerRequestMetadata**](ServiceCreateInstallerRequestMetadata.md) |  | [optional] 
**name** | **str** |  | 

## Example

```python
from nuon.models.service_create_installer_request import ServiceCreateInstallerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCreateInstallerRequest from a JSON string
service_create_installer_request_instance = ServiceCreateInstallerRequest.from_json(json)
# print the JSON string representation of the object
print ServiceCreateInstallerRequest.to_json()

# convert the object into a dict
service_create_installer_request_dict = service_create_installer_request_instance.to_dict()
# create an instance of ServiceCreateInstallerRequest from a dict
service_create_installer_request_form_dict = service_create_installer_request.from_dict(service_create_installer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


