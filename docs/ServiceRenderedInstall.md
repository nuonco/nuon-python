# ServiceRenderedInstall


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**install** | [**AppInstall**](AppInstall.md) |  | [optional] 
**installer** | [**ServiceRenderedInstaller**](ServiceRenderedInstaller.md) |  | [optional] 
**installer_content** | **str** |  | [optional] 

## Example

```python
from nuon.models.service_rendered_install import ServiceRenderedInstall

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceRenderedInstall from a JSON string
service_rendered_install_instance = ServiceRenderedInstall.from_json(json)
# print the JSON string representation of the object
print ServiceRenderedInstall.to_json()

# convert the object into a dict
service_rendered_install_dict = service_rendered_install_instance.to_dict()
# create an instance of ServiceRenderedInstall from a dict
service_rendered_install_form_dict = service_rendered_install.from_dict(service_rendered_install_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


