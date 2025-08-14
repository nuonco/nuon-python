# ServiceDeprovisionInstallSandboxRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_behavior** | **str** |  | [optional] 
**plan_only** | **bool** |  | [optional] 

## Example

```python
from nuon.models.service_deprovision_install_sandbox_request import ServiceDeprovisionInstallSandboxRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceDeprovisionInstallSandboxRequest from a JSON string
service_deprovision_install_sandbox_request_instance = ServiceDeprovisionInstallSandboxRequest.from_json(json)
# print the JSON string representation of the object
print ServiceDeprovisionInstallSandboxRequest.to_json()

# convert the object into a dict
service_deprovision_install_sandbox_request_dict = service_deprovision_install_sandbox_request_instance.to_dict()
# create an instance of ServiceDeprovisionInstallSandboxRequest from a dict
service_deprovision_install_sandbox_request_form_dict = service_deprovision_install_sandbox_request.from_dict(service_deprovision_install_sandbox_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


