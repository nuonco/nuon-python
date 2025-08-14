# AppLogStream


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attrs** | **Dict[str, str]** |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**open** | **bool** |  | [optional] 
**org_id** | **str** |  | [optional] 
**owner_id** | **str** |  | [optional] 
**owner_type** | **str** |  | [optional] 
**runner_api_url** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**write_token** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_log_stream import AppLogStream

# TODO update the JSON string below
json = "{}"
# create an instance of AppLogStream from a JSON string
app_log_stream_instance = AppLogStream.from_json(json)
# print the JSON string representation of the object
print AppLogStream.to_json()

# convert the object into a dict
app_log_stream_dict = app_log_stream_instance.to_dict()
# create an instance of AppLogStream from a dict
app_log_stream_form_dict = app_log_stream.from_dict(app_log_stream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


