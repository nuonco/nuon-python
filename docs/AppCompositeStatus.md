# AppCompositeStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at_ts** | **int** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**history** | [**List[AppCompositeStatus]**](AppCompositeStatus.md) |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 
**status** | [**AppStatus**](AppStatus.md) |  | [optional] 
**status_human_description** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_composite_status import AppCompositeStatus

# TODO update the JSON string below
json = "{}"
# create an instance of AppCompositeStatus from a JSON string
app_composite_status_instance = AppCompositeStatus.from_json(json)
# print the JSON string representation of the object
print AppCompositeStatus.to_json()

# convert the object into a dict
app_composite_status_dict = app_composite_status_instance.to_dict()
# create an instance of AppCompositeStatus from a dict
app_composite_status_form_dict = app_composite_status.from_dict(app_composite_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


