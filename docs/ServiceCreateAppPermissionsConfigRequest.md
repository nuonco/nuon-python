# ServiceCreateAppPermissionsConfigRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_config_id** | **str** |  | 
**deprovision_role** | [**ServiceAppAWSIAMRoleConfig**](ServiceAppAWSIAMRoleConfig.md) |  | 
**maintenance_role** | [**ServiceAppAWSIAMRoleConfig**](ServiceAppAWSIAMRoleConfig.md) |  | 
**provision_role** | [**ServiceAppAWSIAMRoleConfig**](ServiceAppAWSIAMRoleConfig.md) |  | 

## Example

```python
from nuon.models.service_create_app_permissions_config_request import ServiceCreateAppPermissionsConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCreateAppPermissionsConfigRequest from a JSON string
service_create_app_permissions_config_request_instance = ServiceCreateAppPermissionsConfigRequest.from_json(json)
# print the JSON string representation of the object
print ServiceCreateAppPermissionsConfigRequest.to_json()

# convert the object into a dict
service_create_app_permissions_config_request_dict = service_create_app_permissions_config_request_instance.to_dict()
# create an instance of ServiceCreateAppPermissionsConfigRequest from a dict
service_create_app_permissions_config_request_form_dict = service_create_app_permissions_config_request.from_dict(service_create_app_permissions_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


