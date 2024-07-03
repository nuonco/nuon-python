# ServiceCreateOrgInviteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 

## Example

```python
from nuon.models.service_create_org_invite_request import ServiceCreateOrgInviteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCreateOrgInviteRequest from a JSON string
service_create_org_invite_request_instance = ServiceCreateOrgInviteRequest.from_json(json)
# print the JSON string representation of the object
print ServiceCreateOrgInviteRequest.to_json()

# convert the object into a dict
service_create_org_invite_request_dict = service_create_org_invite_request_instance.to_dict()
# create an instance of ServiceCreateOrgInviteRequest from a dict
service_create_org_invite_request_form_dict = service_create_org_invite_request.from_dict(service_create_org_invite_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


