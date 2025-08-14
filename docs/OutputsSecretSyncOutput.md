# OutputsSecretSyncOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arn** | **str** |  | [optional] 
**exists** | **bool** |  | [optional] 
**kubernetes_key** | **str** |  | [optional] 
**kubernetes_name** | **str** |  | [optional] 
**kubernetes_namespace** | **str** |  | [optional] 
**length** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**timestamp** | **str** |  | [optional] 

## Example

```python
from nuon.models.outputs_secret_sync_output import OutputsSecretSyncOutput

# TODO update the JSON string below
json = "{}"
# create an instance of OutputsSecretSyncOutput from a JSON string
outputs_secret_sync_output_instance = OutputsSecretSyncOutput.from_json(json)
# print the JSON string representation of the object
print OutputsSecretSyncOutput.to_json()

# convert the object into a dict
outputs_secret_sync_output_dict = outputs_secret_sync_output_instance.to_dict()
# create an instance of OutputsSecretSyncOutput from a dict
outputs_secret_sync_output_form_dict = outputs_secret_sync_output.from_dict(outputs_secret_sync_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


