# ServiceCreateInstallDeployRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**build_id** | **str** |  | [optional] 

## Example

```python
from nuon.models.service_create_install_deploy_request import ServiceCreateInstallDeployRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCreateInstallDeployRequest from a JSON string
service_create_install_deploy_request_instance = ServiceCreateInstallDeployRequest.from_json(json)
# print the JSON string representation of the object
print ServiceCreateInstallDeployRequest.to_json()

# convert the object into a dict
service_create_install_deploy_request_dict = service_create_install_deploy_request_instance.to_dict()
# create an instance of ServiceCreateInstallDeployRequest from a dict
service_create_install_deploy_request_form_dict = service_create_install_deploy_request.from_dict(service_create_install_deploy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


