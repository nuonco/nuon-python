# ServiceWaitlistRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_name** | **str** |  | 

## Example

```python
from nuon.models.service_waitlist_request import ServiceWaitlistRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceWaitlistRequest from a JSON string
service_waitlist_request_instance = ServiceWaitlistRequest.from_json(json)
# print the JSON string representation of the object
print ServiceWaitlistRequest.to_json()

# convert the object into a dict
service_waitlist_request_dict = service_waitlist_request_instance.to_dict()
# create an instance of ServiceWaitlistRequest from a dict
service_waitlist_request_form_dict = service_waitlist_request.from_dict(service_waitlist_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


