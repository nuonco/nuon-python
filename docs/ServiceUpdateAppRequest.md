# ServiceUpdateAppRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 

## Example

```python
from nuon.models.service_update_app_request import ServiceUpdateAppRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceUpdateAppRequest from a JSON string
service_update_app_request_instance = ServiceUpdateAppRequest.from_json(json)
# print the JSON string representation of the object
print ServiceUpdateAppRequest.to_json()

# convert the object into a dict
service_update_app_request_dict = service_update_app_request_instance.to_dict()
# create an instance of ServiceUpdateAppRequest from a dict
service_update_app_request_form_dict = service_update_app_request.from_dict(service_update_app_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


