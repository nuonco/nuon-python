# AppJobComponentConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**args** | **List[str]** |  | [optional] 
**cmd** | **List[str]** |  | [optional] 
**component_config_connection_id** | **str** | value | [optional] 
**created_at** | **str** |  | [optional] 
**created_by** | [**AppAccount**](AppAccount.md) |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**env_vars** | **Dict[str, str]** |  | [optional] 
**id** | **str** |  | [optional] 
**image_url** | **str** | Image attributes, copied from a docker_buid or external_image component. | [optional] 
**tag** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_job_component_config import AppJobComponentConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AppJobComponentConfig from a JSON string
app_job_component_config_instance = AppJobComponentConfig.from_json(json)
# print the JSON string representation of the object
print AppJobComponentConfig.to_json()

# convert the object into a dict
app_job_component_config_dict = app_job_component_config_instance.to_dict()
# create an instance of AppJobComponentConfig from a dict
app_job_component_config_form_dict = app_job_component_config.from_dict(app_job_component_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


