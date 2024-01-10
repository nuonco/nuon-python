# ServiceConnectedGithubVCSConfigRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch** | **str** |  | [optional] 
**directory** | **str** |  | 
**git_ref** | **str** |  | [optional] 
**repo** | **str** |  | 

## Example

```python
from nuon.models.service_connected_github_vcs_config_request import ServiceConnectedGithubVCSConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceConnectedGithubVCSConfigRequest from a JSON string
service_connected_github_vcs_config_request_instance = ServiceConnectedGithubVCSConfigRequest.from_json(json)
# print the JSON string representation of the object
print ServiceConnectedGithubVCSConfigRequest.to_json()

# convert the object into a dict
service_connected_github_vcs_config_request_dict = service_connected_github_vcs_config_request_instance.to_dict()
# create an instance of ServiceConnectedGithubVCSConfigRequest from a dict
service_connected_github_vcs_config_request_form_dict = service_connected_github_vcs_config_request.from_dict(service_connected_github_vcs_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


