# ServiceUpdateInstallerRequestMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**community_url** | **str** |  | 
**copyright_markdown** | **str** |  | [optional] 
**demo_url** | **str** |  | [optional] 
**description** | **str** |  | 
**documentation_url** | **str** |  | 
**favicon_url** | **str** |  | [optional] 
**footer_markdown** | **str** |  | [optional] 
**github_url** | **str** |  | 
**homepage_url** | **str** |  | 
**logo_url** | **str** |  | 
**og_image_url** | **str** |  | [optional] 
**post_install_markdown** | **str** |  | [optional] 

## Example

```python
from nuon.models.service_update_installer_request_metadata import ServiceUpdateInstallerRequestMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceUpdateInstallerRequestMetadata from a JSON string
service_update_installer_request_metadata_instance = ServiceUpdateInstallerRequestMetadata.from_json(json)
# print the JSON string representation of the object
print ServiceUpdateInstallerRequestMetadata.to_json()

# convert the object into a dict
service_update_installer_request_metadata_dict = service_update_installer_request_metadata_instance.to_dict()
# create an instance of ServiceUpdateInstallerRequestMetadata from a dict
service_update_installer_request_metadata_form_dict = service_update_installer_request_metadata.from_dict(service_update_installer_request_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


