# AppHelmConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chart_name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 
**storage_driver** | **str** |  | [optional] 
**take_ownership** | **bool** | Newer fields that we don&#39;t need to store as columns in the database | [optional] 
**values** | **Dict[str, str]** |  | [optional] 
**values_files** | **List[str]** |  | [optional] 

## Example

```python
from nuon.models.app_helm_config import AppHelmConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AppHelmConfig from a JSON string
app_helm_config_instance = AppHelmConfig.from_json(json)
# print the JSON string representation of the object
print AppHelmConfig.to_json()

# convert the object into a dict
app_helm_config_dict = app_helm_config_instance.to_dict()
# create an instance of AppHelmConfig from a dict
app_helm_config_form_dict = app_helm_config.from_dict(app_helm_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


