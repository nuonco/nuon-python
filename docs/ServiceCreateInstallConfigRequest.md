# ServiceCreateInstallConfigRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approval_option** | [**AppInstallApprovalOption**](AppInstallApprovalOption.md) |  | [optional] 

## Example

```python
from nuon.models.service_create_install_config_request import ServiceCreateInstallConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCreateInstallConfigRequest from a JSON string
service_create_install_config_request_instance = ServiceCreateInstallConfigRequest.from_json(json)
# print the JSON string representation of the object
print ServiceCreateInstallConfigRequest.to_json()

# convert the object into a dict
service_create_install_config_request_dict = service_create_install_config_request_instance.to_dict()
# create an instance of ServiceCreateInstallConfigRequest from a dict
service_create_install_config_request_form_dict = service_create_install_config_request.from_dict(service_create_install_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


