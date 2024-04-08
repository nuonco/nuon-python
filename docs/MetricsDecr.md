# MetricsDecr


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 

## Example

```python
from nuon.models.metrics_decr import MetricsDecr

# TODO update the JSON string below
json = "{}"
# create an instance of MetricsDecr from a JSON string
metrics_decr_instance = MetricsDecr.from_json(json)
# print the JSON string representation of the object
print MetricsDecr.to_json()

# convert the object into a dict
metrics_decr_dict = metrics_decr_instance.to_dict()
# create an instance of MetricsDecr from a dict
metrics_decr_form_dict = metrics_decr.from_dict(metrics_decr_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


