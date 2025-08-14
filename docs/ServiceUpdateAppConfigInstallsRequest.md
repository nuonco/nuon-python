# ServiceUpdateAppConfigInstallsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**install_ids** | **List[str]** |  | [optional] 
**update_all** | **bool** |  | [optional] 

## Example

```python
from nuon.models.service_update_app_config_installs_request import ServiceUpdateAppConfigInstallsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceUpdateAppConfigInstallsRequest from a JSON string
service_update_app_config_installs_request_instance = ServiceUpdateAppConfigInstallsRequest.from_json(json)
# print the JSON string representation of the object
print ServiceUpdateAppConfigInstallsRequest.to_json()

# convert the object into a dict
service_update_app_config_installs_request_dict = service_update_app_config_installs_request_instance.to_dict()
# create an instance of ServiceUpdateAppConfigInstallsRequest from a dict
service_update_app_config_installs_request_form_dict = service_update_app_config_installs_request.from_dict(service_update_app_config_installs_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


