# AppWaitlist


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**org_name** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_waitlist import AppWaitlist

# TODO update the JSON string below
json = "{}"
# create an instance of AppWaitlist from a JSON string
app_waitlist_instance = AppWaitlist.from_json(json)
# print the JSON string representation of the object
print AppWaitlist.to_json()

# convert the object into a dict
app_waitlist_dict = app_waitlist_instance.to_dict()
# create an instance of AppWaitlist from a dict
app_waitlist_form_dict = app_waitlist.from_dict(app_waitlist_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


