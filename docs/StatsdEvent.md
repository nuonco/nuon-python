# StatsdEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregation_key** | **str** | AggregationKey groups this event with others of the same key. | [optional] 
**alert_type** | [**StatsdEventAlertType**](StatsdEventAlertType.md) | AlertType can be statsd.Info, statsd.Error, statsd.Warning, or statsd.Success.
If absent, the default value applied by the dogstatsd server is Info. | [optional] 
**hostname** | **str** | Hostname for the event. | [optional] 
**priority** | [**StatsdEventPriority**](StatsdEventPriority.md) | Priority of the event.  Can be statsd.Low or statsd.Normal. | [optional] 
**source_type_name** | **str** | SourceTypeName is a source type for the event. | [optional] 
**tags** | **List[str]** | Tags for the event. | [optional] 
**text** | **str** | Text is the description of the event. | [optional] 
**timestamp** | **str** | Timestamp is a timestamp for the event.  If not provided, the dogstatsd server will set this to the current time. | [optional] 
**title** | **str** | Title of the event.  Required. | [optional] 

## Example

```python
from nuon.models.statsd_event import StatsdEvent

# TODO update the JSON string below
json = "{}"
# create an instance of StatsdEvent from a JSON string
statsd_event_instance = StatsdEvent.from_json(json)
# print the JSON string representation of the object
print StatsdEvent.to_json()

# convert the object into a dict
statsd_event_dict = statsd_event_instance.to_dict()
# create an instance of StatsdEvent from a dict
statsd_event_form_dict = statsd_event.from_dict(statsd_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


