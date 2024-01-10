# ServicePublishMetricInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**decr** | [**MetricsDecr**](MetricsDecr.md) |  | [optional] 
**event** | [**MetricsEvent**](MetricsEvent.md) |  | [optional] 
**incr** | [**MetricsIncr**](MetricsIncr.md) |  | [optional] 
**timing** | [**MetricsTiming**](MetricsTiming.md) |  | [optional] 

## Example

```python
from openapi_client.models.service_publish_metric_input import ServicePublishMetricInput

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


