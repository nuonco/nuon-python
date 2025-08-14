# AppHelmChart


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**helm_releases** | [**List[AppHelmRelease]**](AppHelmRelease.md) |  | [optional] 
**id** | **str** |  | [optional] 
**org_id** | **str** |  | [optional] 
**owner_id** | **str** |  | [optional] 
**owner_type** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_helm_chart import AppHelmChart

# TODO update the JSON string below
json = "{}"
# create an instance of AppHelmChart from a JSON string
app_helm_chart_instance = AppHelmChart.from_json(json)
# print the JSON string representation of the object
print AppHelmChart.to_json()

# convert the object into a dict
app_helm_chart_dict = app_helm_chart_instance.to_dict()
# create an instance of AppHelmChart from a dict
app_helm_chart_form_dict = app_helm_chart.from_dict(app_helm_chart_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


