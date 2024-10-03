# AppOtelLogRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**log_attributes** | **Dict[str, str]** |  | [optional] 
**resource_attributes** | **Dict[str, str]** |  | [optional] 
**resource_schema_url** | **str** |  | [optional] 
**runner_group_id** | **str** |  | [optional] 
**runner_id** | **str** | internal attributes | [optional] 
**runner_job_execution_id** | **str** |  | [optional] 
**runner_job_id** | **str** |  | [optional] 
**scope_attributes** | **Dict[str, str]** |  | [optional] 
**scope_name** | **str** |  | [optional] 
**scope_schema_url** | **str** |  | [optional] 
**scope_version** | **str** |  | [optional] 
**service_name** | **str** |  | [optional] 
**severity_number** | **int** |  | [optional] 
**severity_text** | **str** |  | [optional] 
**span_id** | **str** |  | [optional] 
**timestamp** | **str** | OTEL log message attributes | [optional] 
**timestamp_date** | **str** |  | [optional] 
**timestamp_time** | **str** |  | [optional] 
**trace_flags** | **int** |  | [optional] 
**trace_id** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_otel_log_record import AppOtelLogRecord

# TODO update the JSON string below
json = "{}"
# create an instance of AppOtelLogRecord from a JSON string
app_otel_log_record_instance = AppOtelLogRecord.from_json(json)
# print the JSON string representation of the object
print AppOtelLogRecord.to_json()

# convert the object into a dict
app_otel_log_record_dict = app_otel_log_record_instance.to_dict()
# create an instance of AppOtelLogRecord from a dict
app_otel_log_record_form_dict = app_otel_log_record.from_dict(app_otel_log_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


