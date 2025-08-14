# ServiceCreateJobComponentConfigRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_config_id** | **str** |  | [optional] 
**args** | **List[str]** |  | [optional] 
**checksum** | **str** |  | [optional] 
**cmd** | **List[str]** |  | [optional] 
**env_vars** | **Dict[str, str]** |  | [optional] 
**image_url** | **str** |  | 
**references** | **List[str]** |  | [optional] 
**tag** | **str** |  | 

## Example

```python
from nuon.models.service_create_job_component_config_request import ServiceCreateJobComponentConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCreateJobComponentConfigRequest from a JSON string
service_create_job_component_config_request_instance = ServiceCreateJobComponentConfigRequest.from_json(json)
# print the JSON string representation of the object
print ServiceCreateJobComponentConfigRequest.to_json()

# convert the object into a dict
service_create_job_component_config_request_dict = service_create_job_component_config_request_instance.to_dict()
# create an instance of ServiceCreateJobComponentConfigRequest from a dict
service_create_job_component_config_request_form_dict = service_create_job_component_config_request.from_dict(service_create_job_component_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


