# ServiceDeployInstallComponentsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_only** | **bool** |  | [optional] 

## Example

```python
from nuon.models.service_deploy_install_components_request import ServiceDeployInstallComponentsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceDeployInstallComponentsRequest from a JSON string
service_deploy_install_components_request_instance = ServiceDeployInstallComponentsRequest.from_json(json)
# print the JSON string representation of the object
print ServiceDeployInstallComponentsRequest.to_json()

# convert the object into a dict
service_deploy_install_components_request_dict = service_deploy_install_components_request_instance.to_dict()
# create an instance of ServiceDeployInstallComponentsRequest from a dict
service_deploy_install_components_request_form_dict = service_deploy_install_components_request.from_dict(service_deploy_install_components_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


