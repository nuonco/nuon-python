# RefsRef


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | [**RefsRefType**](RefsRefType.md) |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from nuon.models.refs_ref import RefsRef

# TODO update the JSON string below
json = "{}"
# create an instance of RefsRef from a JSON string
refs_ref_instance = RefsRef.from_json(json)
# print the JSON string representation of the object
print RefsRef.to_json()

# convert the object into a dict
refs_ref_dict = refs_ref_instance.to_dict()
# create an instance of RefsRef from a dict
refs_ref_form_dict = refs_ref.from_dict(refs_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


