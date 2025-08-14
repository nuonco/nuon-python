# ServiceRemoveOrgUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | [optional] 

## Example

```python
from nuon.models.service_remove_org_user_request import ServiceRemoveOrgUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceRemoveOrgUserRequest from a JSON string
service_remove_org_user_request_instance = ServiceRemoveOrgUserRequest.from_json(json)
# print the JSON string representation of the object
print ServiceRemoveOrgUserRequest.to_json()

# convert the object into a dict
service_remove_org_user_request_dict = service_remove_org_user_request_instance.to_dict()
# create an instance of ServiceRemoveOrgUserRequest from a dict
service_remove_org_user_request_form_dict = service_remove_org_user_request.from_dict(service_remove_org_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


