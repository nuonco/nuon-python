# AppInstallAuditLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**install_id** | **str** |  | [optional] 
**log_line** | **str** |  | [optional] 
**time_stamp** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_install_audit_log import AppInstallAuditLog

# TODO update the JSON string below
json = "{}"
# create an instance of AppInstallAuditLog from a JSON string
app_install_audit_log_instance = AppInstallAuditLog.from_json(json)
# print the JSON string representation of the object
print AppInstallAuditLog.to_json()

# convert the object into a dict
app_install_audit_log_dict = app_install_audit_log_instance.to_dict()
# create an instance of AppInstallAuditLog from a dict
app_install_audit_log_form_dict = app_install_audit_log.from_dict(app_install_audit_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


