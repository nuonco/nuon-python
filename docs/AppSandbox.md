# AppSandbox


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**releases** | [**List[AppSandboxRelease]**](AppSandboxRelease.md) |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_sandbox import AppSandbox

# TODO update the JSON string below
json = "{}"
# create an instance of AppSandbox from a JSON string
app_sandbox_instance = AppSandbox.from_json(json)
# print the JSON string representation of the object
print AppSandbox.to_json()

# convert the object into a dict
app_sandbox_dict = app_sandbox_instance.to_dict()
# create an instance of AppSandbox from a dict
app_sandbox_form_dict = app_sandbox.from_dict(app_sandbox_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


