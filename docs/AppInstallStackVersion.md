# AppInstallStackVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_config_id** | **str** |  | [optional] 
**aws_bucket_key** | **str** |  | [optional] 
**aws_bucket_name** | **str** | aws configuration parameters | [optional] 
**checksum** | **str** |  | [optional] 
**composite_status** | [**AppCompositeStatus**](AppCompositeStatus.md) |  | [optional] 
**contents** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**install_id** | **str** |  | [optional] 
**install_stack_id** | **str** |  | [optional] 
**org_id** | **str** |  | [optional] 
**phone_home_id** | **str** |  | [optional] 
**phone_home_url** | **str** |  | [optional] 
**quick_link_url** | **str** |  | [optional] 
**runs** | [**List[AppInstallStackVersionRun]**](AppInstallStackVersionRun.md) |  | [optional] 
**template_url** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_install_stack_version import AppInstallStackVersion

# TODO update the JSON string below
json = "{}"
# create an instance of AppInstallStackVersion from a JSON string
app_install_stack_version_instance = AppInstallStackVersion.from_json(json)
# print the JSON string representation of the object
print AppInstallStackVersion.to_json()

# convert the object into a dict
app_install_stack_version_dict = app_install_stack_version_instance.to_dict()
# create an instance of AppInstallStackVersion from a dict
app_install_stack_version_form_dict = app_install_stack_version.from_dict(app_install_stack_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


