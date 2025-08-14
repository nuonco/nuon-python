# ServiceRunnerConnectionStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connected** | **bool** |  | [optional] 
**latest_heartbeat_timestamp** | **int** |  | [optional] 

## Example

```python
from nuon.models.service_runner_connection_status import ServiceRunnerConnectionStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceRunnerConnectionStatus from a JSON string
service_runner_connection_status_instance = ServiceRunnerConnectionStatus.from_json(json)
# print the JSON string representation of the object
print ServiceRunnerConnectionStatus.to_json()

# convert the object into a dict
service_runner_connection_status_dict = service_runner_connection_status_instance.to_dict()
# create an instance of ServiceRunnerConnectionStatus from a dict
service_runner_connection_status_form_dict = service_runner_connection_status.from_dict(service_runner_connection_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


