# ServiceCLIConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_audience** | **str** |  | [optional] 
**auth_client_id** | **str** |  | [optional] 
**auth_domain** | **str** |  | [optional] 

## Example

```python
from nuon.models.service_cli_config import ServiceCLIConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCLIConfig from a JSON string
service_cli_config_instance = ServiceCLIConfig.from_json(json)
# print the JSON string representation of the object
print ServiceCLIConfig.to_json()

# convert the object into a dict
service_cli_config_dict = service_cli_config_instance.to_dict()
# create an instance of ServiceCLIConfig from a dict
service_cli_config_form_dict = service_cli_config.from_dict(service_cli_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


