# AppInstallerMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**community_url** | **str** |  | [optional] 
**copyright_markdown** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by** | [**AppAccount**](AppAccount.md) |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**demo_url** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**documentation_url** | **str** |  | [optional] 
**favicon_url** | **str** |  | [optional] 
**footer_markdown** | **str** |  | [optional] 
**formatted_demo_url** | **str** |  | [optional] 
**github_url** | **str** |  | [optional] 
**homepage_url** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**installer_id** | **str** |  | [optional] 
**logo_url** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**og_image_url** | **str** |  | [optional] 
**post_install_markdown** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_installer_metadata import AppInstallerMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of AppInstallerMetadata from a JSON string
app_installer_metadata_instance = AppInstallerMetadata.from_json(json)
# print the JSON string representation of the object
print AppInstallerMetadata.to_json()

# convert the object into a dict
app_installer_metadata_dict = app_installer_metadata_instance.to_dict()
# create an instance of AppInstallerMetadata from a dict
app_installer_metadata_form_dict = app_installer_metadata.from_dict(app_installer_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


