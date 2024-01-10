# ServiceRepository


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clone_url** | **str** |  | 
**default_branch** | **str** |  | 
**full_name** | **str** |  | 
**git_url** | **str** |  | 
**github_install_id** | **str** |  | 
**name** | **str** |  | 
**user_name** | **str** |  | 

## Example

```python
from nuon.models.service_repository import ServiceRepository

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceRepository from a JSON string
service_repository_instance = ServiceRepository.from_json(json)
# print the JSON string representation of the object
print ServiceRepository.to_json()

# convert the object into a dict
service_repository_dict = service_repository_instance.to_dict()
# create an instance of ServiceRepository from a dict
service_repository_form_dict = service_repository.from_dict(service_repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


