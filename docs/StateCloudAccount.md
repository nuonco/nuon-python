# StateCloudAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws** | [**StateAWSCloudAccount**](StateAWSCloudAccount.md) |  | [optional] 
**azure** | [**StateAzureCloudAccount**](StateAzureCloudAccount.md) |  | [optional] 

## Example

```python
from nuon.models.state_cloud_account import StateCloudAccount

# TODO update the JSON string below
json = "{}"
# create an instance of StateCloudAccount from a JSON string
state_cloud_account_instance = StateCloudAccount.from_json(json)
# print the JSON string representation of the object
print StateCloudAccount.to_json()

# convert the object into a dict
state_cloud_account_dict = state_cloud_account_instance.to_dict()
# create an instance of StateCloudAccount from a dict
state_cloud_account_form_dict = state_cloud_account.from_dict(state_cloud_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


