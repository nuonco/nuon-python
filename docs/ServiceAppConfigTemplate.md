# ServiceAppConfigTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | [optional] 
**filename** | **str** |  | [optional] 
**format** | [**AppAppConfigFmt**](AppAppConfigFmt.md) |  | [optional] 
**type** | [**ServiceAppConfigTemplateType**](ServiceAppConfigTemplateType.md) |  | [optional] 

## Example

```python
from nuon.models.service_app_config_template import ServiceAppConfigTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceAppConfigTemplate from a JSON string
service_app_config_template_instance = ServiceAppConfigTemplate.from_json(json)
# print the JSON string representation of the object
print ServiceAppConfigTemplate.to_json()

# convert the object into a dict
service_app_config_template_dict = service_app_config_template_instance.to_dict()
# create an instance of ServiceAppConfigTemplate from a dict
service_app_config_template_form_dict = service_app_config_template.from_dict(service_app_config_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


