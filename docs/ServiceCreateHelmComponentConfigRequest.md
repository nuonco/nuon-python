# ServiceCreateHelmComponentConfigRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chart_name** | **str** |  | 
**connected_github_vcs_config** | [**ServiceConnectedGithubVCSConfigRequest**](ServiceConnectedGithubVCSConfigRequest.md) |  | [optional] 
**public_git_vcs_config** | [**ServicePublicGitVCSConfigRequest**](ServicePublicGitVCSConfigRequest.md) |  | [optional] 
**values** | **Dict[str, str]** |  | 

## Example

```python
from nuon.models.service_create_helm_component_config_request import ServiceCreateHelmComponentConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCreateHelmComponentConfigRequest from a JSON string
service_create_helm_component_config_request_instance = ServiceCreateHelmComponentConfigRequest.from_json(json)
# print the JSON string representation of the object
print ServiceCreateHelmComponentConfigRequest.to_json()

# convert the object into a dict
service_create_helm_component_config_request_dict = service_create_helm_component_config_request_instance.to_dict()
# create an instance of ServiceCreateHelmComponentConfigRequest from a dict
service_create_helm_component_config_request_form_dict = service_create_helm_component_config_request.from_dict(service_create_helm_component_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


