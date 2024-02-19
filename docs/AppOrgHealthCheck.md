# AppOrgHealthCheck


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**created_by** | [**AppUserToken**](AppUserToken.md) |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**org_id** | **str** |  | [optional] 
**status** | [**AppOrgHealthCheckStatus**](AppOrgHealthCheckStatus.md) |  | [optional] 
**status_description** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_org_health_check import AppOrgHealthCheck

# TODO update the JSON string below
json = "{}"
# create an instance of AppOrgHealthCheck from a JSON string
app_org_health_check_instance = AppOrgHealthCheck.from_json(json)
# print the JSON string representation of the object
print AppOrgHealthCheck.to_json()

# convert the object into a dict
app_org_health_check_dict = app_org_health_check_instance.to_dict()
# create an instance of AppOrgHealthCheck from a dict
app_org_health_check_form_dict = app_org_health_check.from_dict(app_org_health_check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


