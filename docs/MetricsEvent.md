# MetricsEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | [**StatsdEvent**](StatsdEvent.md) |  | [optional] 

## Example

```python
from openapi_client.models.metrics_event import MetricsEvent

# TODO update the JSON string below
json = "{}"
# create an instance of MetricsEvent from a JSON string
metrics_event_instance = MetricsEvent.from_json(json)
# print the JSON string representation of the object
print MetricsEvent.to_json()

# convert the object into a dict
metrics_event_dict = metrics_event_instance.to_dict()
# create an instance of MetricsEvent from a dict
metrics_event_form_dict = metrics_event.from_dict(metrics_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


