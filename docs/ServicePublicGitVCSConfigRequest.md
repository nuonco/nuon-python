# ServicePublicGitVCSConfigRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch** | **str** |  | 
**directory** | **str** |  | 
**repo** | **str** |  | 

## Example

```python
from openapi_client.models.service_public_git_vcs_config_request import ServicePublicGitVCSConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServicePublicGitVCSConfigRequest from a JSON string
service_public_git_vcs_config_request_instance = ServicePublicGitVCSConfigRequest.from_json(json)
# print the JSON string representation of the object
print ServicePublicGitVCSConfigRequest.to_json()

# convert the object into a dict
service_public_git_vcs_config_request_dict = service_public_git_vcs_config_request_instance.to_dict()
# create an instance of ServicePublicGitVCSConfigRequest from a dict
service_public_git_vcs_config_request_form_dict = service_public_git_vcs_config_request.from_dict(service_public_git_vcs_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


