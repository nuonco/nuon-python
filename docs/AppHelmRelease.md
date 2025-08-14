# AppHelmRelease


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | The rspb.Release body, as a base64-encoded string | [optional] 
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**helm_chart** | [**AppHelmChart**](AppHelmChart.md) |  | [optional] 
**helm_chart_id** | **str** |  | [optional] 
**key** | **str** |  | [optional] 
**labels** | **Dict[str, str]** |  | [optional] 
**name** | **str** | Release \&quot;labels\&quot; that can be used as filters in the storage.Query(labels map[string]string) we implemented. Note that allowing Helm users to filter against new dimensions will require a new migration to be added, and the Create and/or update functions to be updated accordingly. | [optional] 
**namespace** | **str** |  | [optional] 
**org_id** | **str** |  | [optional] 
**owner** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**type** | **str** | See https://github.com/helm/helm/blob/c9fe3d118caec699eb2565df9838673af379ce12/pkg/storage/driver/secrets.go#L231 | [optional] 
**updated_at** | **str** |  | [optional] 
**version** | **int** |  | [optional] 

## Example

```python
from nuon.models.app_helm_release import AppHelmRelease

# TODO update the JSON string below
json = "{}"
# create an instance of AppHelmRelease from a JSON string
app_helm_release_instance = AppHelmRelease.from_json(json)
# print the JSON string representation of the object
print AppHelmRelease.to_json()

# convert the object into a dict
app_helm_release_dict = app_helm_release_instance.to_dict()
# create an instance of AppHelmRelease from a dict
app_helm_release_form_dict = app_helm_release.from_dict(app_helm_release_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


