# ServicePublishMetricInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**decr** | [**MetricsDecr**](MetricsDecr.md) |  | [optional] 
**event** | [**MetricsEvent**](MetricsEvent.md) | TODO: remove this after test
Just making a non-functional change to create a promotion PR.
Generating the python SDK locally, with no changes, actually fixed the synax error.
This may be an edge case that only happens on the first generation, when it creates all the files from scratch.
If this doesn&#39;t fix it, I&#39;ll try moving this statsd stuff to the admin api. | [optional] 
**incr** | [**MetricsIncr**](MetricsIncr.md) |  | [optional] 
**timing** | [**MetricsTiming**](MetricsTiming.md) |  | [optional] 

## Example

```python
from nuon.models.service_publish_metric_input import ServicePublishMetricInput

# TODO update the JSON string below
json = "{}"
# create an instance of ServicePublishMetricInput from a JSON string
service_publish_metric_input_instance = ServicePublishMetricInput.from_json(json)
# print the JSON string representation of the object
print ServicePublishMetricInput.to_json()

# convert the object into a dict
service_publish_metric_input_dict = service_publish_metric_input_instance.to_dict()
# create an instance of ServicePublishMetricInput from a dict
service_publish_metric_input_form_dict = service_publish_metric_input.from_dict(service_publish_metric_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


