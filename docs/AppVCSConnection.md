# AppVCSConnection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**created_by** | [**AppUserToken**](AppUserToken.md) |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**github_install_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**vcs_connection_commit** | [**List[AppVCSConnectionCommit]**](AppVCSConnectionCommit.md) |  | [optional] 

## Example

```python
from nuon.models.app_vcs_connection import AppVCSConnection

# TODO update the JSON string below
json = "{}"
# create an instance of AppVCSConnection from a JSON string
app_vcs_connection_instance = AppVCSConnection.from_json(json)
# print the JSON string representation of the object
print AppVCSConnection.to_json()

# convert the object into a dict
app_vcs_connection_dict = app_vcs_connection_instance.to_dict()
# create an instance of AppVCSConnection from a dict
app_vcs_connection_form_dict = app_vcs_connection.from_dict(app_vcs_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


