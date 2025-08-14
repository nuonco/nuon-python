# ServiceCreateAppBranchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connected_github_vcs_config_id** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from nuon.models.service_create_app_branch_request import ServiceCreateAppBranchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCreateAppBranchRequest from a JSON string
service_create_app_branch_request_instance = ServiceCreateAppBranchRequest.from_json(json)
# print the JSON string representation of the object
print ServiceCreateAppBranchRequest.to_json()

# convert the object into a dict
service_create_app_branch_request_dict = service_create_app_branch_request_instance.to_dict()
# create an instance of ServiceCreateAppBranchRequest from a dict
service_create_app_branch_request_form_dict = service_create_app_branch_request.from_dict(service_create_app_branch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


