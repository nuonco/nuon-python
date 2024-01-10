# ServiceCreateInstallInputsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inputs** | **Dict[str, str]** |  | 

## Example

```python
from openapi_client.models.service_create_install_inputs_request import ServiceCreateInstallInputsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCreateInstallInputsRequest from a JSON string
service_create_install_inputs_request_instance = ServiceCreateInstallInputsRequest.from_json(json)
# print the JSON string representation of the object
print ServiceCreateInstallInputsRequest.to_json()

# convert the object into a dict
service_create_install_inputs_request_dict = service_create_install_inputs_request_instance.to_dict()
# create an instance of ServiceCreateInstallInputsRequest from a dict
service_create_install_inputs_request_form_dict = service_create_install_inputs_request.from_dict(service_create_install_inputs_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


