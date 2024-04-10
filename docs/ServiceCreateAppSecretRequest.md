# ServiceCreateAppSecretRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from nuon.models.service_create_app_secret_request import ServiceCreateAppSecretRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCreateAppSecretRequest from a JSON string
service_create_app_secret_request_instance = ServiceCreateAppSecretRequest.from_json(json)
# print the JSON string representation of the object
print ServiceCreateAppSecretRequest.to_json()

# convert the object into a dict
service_create_app_secret_request_dict = service_create_app_secret_request_instance.to_dict()
# create an instance of ServiceCreateAppSecretRequest from a dict
service_create_app_secret_request_form_dict = service_create_app_secret_request.from_dict(service_create_app_secret_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


