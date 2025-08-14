# ServiceComponentChildren


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**children** | [**List[AppComponent]**](AppComponent.md) |  | [optional] 

## Example

```python
from nuon.models.service_component_children import ServiceComponentChildren

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceComponentChildren from a JSON string
service_component_children_instance = ServiceComponentChildren.from_json(json)
# print the JSON string representation of the object
print ServiceComponentChildren.to_json()

# convert the object into a dict
service_component_children_dict = service_component_children_instance.to_dict()
# create an instance of ServiceComponentChildren from a dict
service_component_children_form_dict = service_component_children.from_dict(service_component_children_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


