# MetricsTiming


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**value** | **int** |  | [optional] 

## Example

```python
from nuon.models.metrics_timing import MetricsTiming

# TODO update the JSON string below
json = "{}"
# create an instance of MetricsTiming from a JSON string
metrics_timing_instance = MetricsTiming.from_json(json)
# print the JSON string representation of the object
print MetricsTiming.to_json()

# convert the object into a dict
metrics_timing_dict = metrics_timing_instance.to_dict()
# create an instance of MetricsTiming from a dict
metrics_timing_form_dict = metrics_timing.from_dict(metrics_timing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


