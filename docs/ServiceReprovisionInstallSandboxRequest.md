# ServiceReprovisionInstallSandboxRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_only** | **bool** |  | [optional] 

## Example

```python
from nuon.models.service_reprovision_install_sandbox_request import ServiceReprovisionInstallSandboxRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceReprovisionInstallSandboxRequest from a JSON string
service_reprovision_install_sandbox_request_instance = ServiceReprovisionInstallSandboxRequest.from_json(json)
# print the JSON string representation of the object
print ServiceReprovisionInstallSandboxRequest.to_json()

# convert the object into a dict
service_reprovision_install_sandbox_request_dict = service_reprovision_install_sandbox_request_instance.to_dict()
# create an instance of ServiceReprovisionInstallSandboxRequest from a dict
service_reprovision_install_sandbox_request_form_dict = service_reprovision_install_sandbox_request.from_dict(service_reprovision_install_sandbox_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


