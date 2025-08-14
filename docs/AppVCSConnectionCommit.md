# AppVCSConnectionCommit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author_email** | **str** |  | [optional] 
**author_name** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**sha** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**vcs_connection_id** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_vcs_connection_commit import AppVCSConnectionCommit

# TODO update the JSON string below
json = "{}"
# create an instance of AppVCSConnectionCommit from a JSON string
app_vcs_connection_commit_instance = AppVCSConnectionCommit.from_json(json)
# print the JSON string representation of the object
print AppVCSConnectionCommit.to_json()

# convert the object into a dict
app_vcs_connection_commit_dict = app_vcs_connection_commit_instance.to_dict()
# create an instance of AppVCSConnectionCommit from a dict
app_vcs_connection_commit_form_dict = app_vcs_connection_commit.from_dict(app_vcs_connection_commit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


