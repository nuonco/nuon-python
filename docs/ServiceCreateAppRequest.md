# ServiceCreateAppRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**name** | **str** |  | 
**slack_webhook_url** | **str** |  | [optional] 

## Example

```python
from nuon.models.service_create_app_request import ServiceCreateAppRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCreateAppRequest from a JSON string
service_create_app_request_instance = ServiceCreateAppRequest.from_json(json)
# print the JSON string representation of the object
print ServiceCreateAppRequest.to_json()

# convert the object into a dict
service_create_app_request_dict = service_create_app_request_instance.to_dict()
# create an instance of ServiceCreateAppRequest from a dict
service_create_app_request_form_dict = service_create_app_request.from_dict(service_create_app_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


