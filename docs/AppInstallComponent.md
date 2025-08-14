# AppInstallComponent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | [**AppComponent**](AppComponent.md) |  | [optional] 
**component_id** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**helm_chart** | [**AppHelmChart**](AppHelmChart.md) |  | [optional] 
**id** | **str** |  | [optional] 
**install_deploys** | [**List[AppInstallDeploy]**](AppInstallDeploy.md) |  | [optional] 
**install_id** | **str** |  | [optional] 
**links** | **Dict[str, object]** |  | [optional] 
**status** | **str** |  | [optional] 
**status_description** | **str** |  | [optional] 
**status_v2** | [**AppCompositeStatus**](AppCompositeStatus.md) |  | [optional] 
**terraform_workspace** | [**AppTerraformWorkspace**](AppTerraformWorkspace.md) |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_install_component import AppInstallComponent

# TODO update the JSON string below
json = "{}"
# create an instance of AppInstallComponent from a JSON string
app_install_component_instance = AppInstallComponent.from_json(json)
# print the JSON string representation of the object
print AppInstallComponent.to_json()

# convert the object into a dict
app_install_component_dict = app_install_component_instance.to_dict()
# create an instance of AppInstallComponent from a dict
app_install_component_form_dict = app_install_component.from_dict(app_install_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


