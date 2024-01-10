# MetricsIncr


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**value** | **int** |  | [optional] 

## Example

```python
from nuon.models.metrics_incr import MetricsIncr

# TODO update the JSON string below
json = "{}"
# create an instance of MetricsIncr from a JSON string
metrics_incr_instance = MetricsIncr.from_json(json)
# print the JSON string representation of the object
print MetricsIncr.to_json()

# convert the object into a dict
metrics_incr_dict = metrics_incr_instance.to_dict()
# create an instance of MetricsIncr from a dict
metrics_incr_form_dict = metrics_incr.from_dict(metrics_incr_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


