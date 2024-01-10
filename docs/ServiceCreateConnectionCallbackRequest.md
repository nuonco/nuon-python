# ServiceCreateConnectionCallbackRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**github_install_id** | **str** |  | 
**org_id** | **str** |  | 

## Example

```python
from openapi_client.models.service_create_connection_callback_request import ServiceCreateConnectionCallbackRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCreateConnectionCallbackRequest from a JSON string
service_create_connection_callback_request_instance = ServiceCreateConnectionCallbackRequest.from_json(json)
# print the JSON string representation of the object
print ServiceCreateConnectionCallbackRequest.to_json()

# convert the object into a dict
service_create_connection_callback_request_dict = service_create_connection_callback_request_instance.to_dict()
# create an instance of ServiceCreateConnectionCallbackRequest from a dict
service_create_connection_callback_request_form_dict = service_create_connection_callback_request.from_dict(service_create_connection_callback_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


