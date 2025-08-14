# ServiceTeardownInstallComponentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_behavior** | **str** |  | [optional] 
**plan_only** | **bool** |  | [optional] 

## Example

```python
from nuon.models.service_teardown_install_component_request import ServiceTeardownInstallComponentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceTeardownInstallComponentRequest from a JSON string
service_teardown_install_component_request_instance = ServiceTeardownInstallComponentRequest.from_json(json)
# print the JSON string representation of the object
print ServiceTeardownInstallComponentRequest.to_json()

# convert the object into a dict
service_teardown_install_component_request_dict = service_teardown_install_component_request_instance.to_dict()
# create an instance of ServiceTeardownInstallComponentRequest from a dict
service_teardown_install_component_request_form_dict = service_teardown_install_component_request.from_dict(service_teardown_install_component_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


