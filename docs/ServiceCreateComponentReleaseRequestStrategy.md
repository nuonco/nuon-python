# ServiceCreateComponentReleaseRequestStrategy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delay** | **str** |  | [optional] 
**installs_per_step** | **int** |  | [optional] 

## Example

```python
from nuon.models.service_create_component_release_request_strategy import ServiceCreateComponentReleaseRequestStrategy

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCreateComponentReleaseRequestStrategy from a JSON string
service_create_component_release_request_strategy_instance = ServiceCreateComponentReleaseRequestStrategy.from_json(json)
# print the JSON string representation of the object
print ServiceCreateComponentReleaseRequestStrategy.to_json()

# convert the object into a dict
service_create_component_release_request_strategy_dict = service_create_component_release_request_strategy_instance.to_dict()
# create an instance of ServiceCreateComponentReleaseRequestStrategy from a dict
service_create_component_release_request_strategy_form_dict = service_create_component_release_request_strategy.from_dict(service_create_component_release_request_strategy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


