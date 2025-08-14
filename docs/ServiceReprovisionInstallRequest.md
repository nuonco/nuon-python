# ServiceReprovisionInstallRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_only** | **bool** |  | [optional] 

## Example

```python
from nuon.models.service_reprovision_install_request import ServiceReprovisionInstallRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceReprovisionInstallRequest from a JSON string
service_reprovision_install_request_instance = ServiceReprovisionInstallRequest.from_json(json)
# print the JSON string representation of the object
print ServiceReprovisionInstallRequest.to_json()

# convert the object into a dict
service_reprovision_install_request_dict = service_reprovision_install_request_instance.to_dict()
# create an instance of ServiceReprovisionInstallRequest from a dict
service_reprovision_install_request_form_dict = service_reprovision_install_request.from_dict(service_reprovision_install_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


