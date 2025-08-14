# ServiceReadme


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original** | **str** |  | [optional] 
**readme** | **str** |  | [optional] 
**warnings** | **List[str]** |  | [optional] 

## Example

```python
from nuon.models.service_readme import ServiceReadme

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceReadme from a JSON string
service_readme_instance = ServiceReadme.from_json(json)
# print the JSON string representation of the object
print ServiceReadme.to_json()

# convert the object into a dict
service_readme_dict = service_readme_instance.to_dict()
# create an instance of ServiceReadme from a dict
service_readme_form_dict = service_readme.from_dict(service_readme_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


