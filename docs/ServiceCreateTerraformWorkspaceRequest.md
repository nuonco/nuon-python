# ServiceCreateTerraformWorkspaceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner_id** | **str** |  | 
**owner_type** | **str** |  | 

## Example

```python
from nuon.models.service_create_terraform_workspace_request import ServiceCreateTerraformWorkspaceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCreateTerraformWorkspaceRequest from a JSON string
service_create_terraform_workspace_request_instance = ServiceCreateTerraformWorkspaceRequest.from_json(json)
# print the JSON string representation of the object
print ServiceCreateTerraformWorkspaceRequest.to_json()

# convert the object into a dict
service_create_terraform_workspace_request_dict = service_create_terraform_workspace_request_instance.to_dict()
# create an instance of ServiceCreateTerraformWorkspaceRequest from a dict
service_create_terraform_workspace_request_form_dict = service_create_terraform_workspace_request.from_dict(service_create_terraform_workspace_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


