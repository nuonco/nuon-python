# AppOCIArtifact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **Dict[str, str]** |  | [optional] 
**architecture** | **str** |  | [optional] 
**artifact_type** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**digest** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**media_type** | **str** |  | [optional] 
**org_id** | **str** |  | [optional] 
**os** | **str** | Platform fields | [optional] 
**os_features** | **List[str]** |  | [optional] 
**os_version** | **str** |  | [optional] 
**owner_id** | **str** |  | [optional] 
**owner_type** | **str** |  | [optional] 
**repository** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**tag** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**urls** | **List[str]** |  | [optional] 
**variant** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_oci_artifact import AppOCIArtifact

# TODO update the JSON string below
json = "{}"
# create an instance of AppOCIArtifact from a JSON string
app_oci_artifact_instance = AppOCIArtifact.from_json(json)
# print the JSON string representation of the object
print AppOCIArtifact.to_json()

# convert the object into a dict
app_oci_artifact_dict = app_oci_artifact_instance.to_dict()
# create an instance of AppOCIArtifact from a dict
app_oci_artifact_form_dict = app_oci_artifact.from_dict(app_oci_artifact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


