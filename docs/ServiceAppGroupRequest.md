# ServiceAppGroupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**display_name** | **str** |  | 
**index** | **int** |  | 

## Example

```python
from nuon.models.service_app_group_request import ServiceAppGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceAppGroupRequest from a JSON string
service_app_group_request_instance = ServiceAppGroupRequest.from_json(json)
# print the JSON string representation of the object
print ServiceAppGroupRequest.to_json()

# convert the object into a dict
service_app_group_request_dict = service_app_group_request_instance.to_dict()
# create an instance of ServiceAppGroupRequest from a dict
service_app_group_request_form_dict = service_app_group_request.from_dict(service_app_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


