# ServiceCreateOrgRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**use_sandbox_mode** | **bool** | These fields are used to control the behaviour of the org. | [optional] 

## Example

```python
from nuon.models.service_create_org_request import ServiceCreateOrgRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCreateOrgRequest from a JSON string
service_create_org_request_instance = ServiceCreateOrgRequest.from_json(json)
# print the JSON string representation of the object
print ServiceCreateOrgRequest.to_json()

# convert the object into a dict
service_create_org_request_dict = service_create_org_request_instance.to_dict()
# create an instance of ServiceCreateOrgRequest from a dict
service_create_org_request_form_dict = service_create_org_request.from_dict(service_create_org_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


