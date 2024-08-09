# ServiceCreateAppRunnerConfigRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**env_vars** | **Dict[str, str]** |  | [optional] 
**type** | [**AppAppRunnerType**](AppAppRunnerType.md) |  | 

## Example

```python
from nuon.models.service_create_app_runner_config_request import ServiceCreateAppRunnerConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCreateAppRunnerConfigRequest from a JSON string
service_create_app_runner_config_request_instance = ServiceCreateAppRunnerConfigRequest.from_json(json)
# print the JSON string representation of the object
print ServiceCreateAppRunnerConfigRequest.to_json()

# convert the object into a dict
service_create_app_runner_config_request_dict = service_create_app_runner_config_request_instance.to_dict()
# create an instance of ServiceCreateAppRunnerConfigRequest from a dict
service_create_app_runner_config_request_form_dict = service_create_app_runner_config_request.from_dict(service_create_app_runner_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


