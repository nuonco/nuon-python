# AppAzureStackOutputs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_vault_id** | **str** |  | [optional] 
**key_vault_name** | **str** |  | [optional] 
**network_id** | **str** |  | [optional] 
**network_name** | **str** |  | [optional] 
**private_subnet_ids** | **List[str]** |  | [optional] 
**private_subnet_names** | **List[str]** |  | [optional] 
**public_subnet_ids** | **List[str]** |  | [optional] 
**public_subnet_names** | **List[str]** |  | [optional] 
**resource_group_id** | **str** |  | [optional] 
**resource_group_location** | **str** |  | [optional] 
**resource_group_name** | **str** |  | [optional] 
**subscription_id** | **str** |  | [optional] 
**subscription_tenant_id** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_azure_stack_outputs import AppAzureStackOutputs

# TODO update the JSON string below
json = "{}"
# create an instance of AppAzureStackOutputs from a JSON string
app_azure_stack_outputs_instance = AppAzureStackOutputs.from_json(json)
# print the JSON string representation of the object
print AppAzureStackOutputs.to_json()

# convert the object into a dict
app_azure_stack_outputs_dict = app_azure_stack_outputs_instance.to_dict()
# create an instance of AppAzureStackOutputs from a dict
app_azure_stack_outputs_form_dict = app_azure_stack_outputs.from_dict(app_azure_stack_outputs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


