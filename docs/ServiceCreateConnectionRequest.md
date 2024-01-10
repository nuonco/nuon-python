# ServiceCreateConnectionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**github_install_id** | **str** |  | 

## Example

```python
from nuon.models.service_create_connection_request import ServiceCreateConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCreateConnectionRequest from a JSON string
service_create_connection_request_instance = ServiceCreateConnectionRequest.from_json(json)
# print the JSON string representation of the object
print ServiceCreateConnectionRequest.to_json()

# convert the object into a dict
service_create_connection_request_dict = service_create_connection_request_instance.to_dict()
# create an instance of ServiceCreateConnectionRequest from a dict
service_create_connection_request_form_dict = service_create_connection_request.from_dict(service_create_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


