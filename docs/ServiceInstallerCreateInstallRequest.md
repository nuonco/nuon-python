# ServiceInstallerCreateInstallRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_account** | [**ServiceCreateInstallRequestAwsAccount**](ServiceCreateInstallRequestAwsAccount.md) |  | 
**name** | **str** |  | 

## Example

```python
from nuon.models.service_installer_create_install_request import ServiceInstallerCreateInstallRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceInstallerCreateInstallRequest from a JSON string
service_installer_create_install_request_instance = ServiceInstallerCreateInstallRequest.from_json(json)
# print the JSON string representation of the object
print ServiceInstallerCreateInstallRequest.to_json()

# convert the object into a dict
service_installer_create_install_request_dict = service_installer_create_install_request_instance.to_dict()
# create an instance of ServiceInstallerCreateInstallRequest from a dict
service_installer_create_install_request_form_dict = service_installer_create_install_request.from_dict(service_installer_create_install_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


