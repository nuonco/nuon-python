# AppAWSStackOutputs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | [optional] 
**deprovision_iam_role_arn** | **str** |  | [optional] 
**maintenance_iam_role_arn** | **str** |  | [optional] 
**private_subnets** | **List[str]** |  | [optional] 
**provision_iam_role_arn** | **str** |  | [optional] 
**public_subnets** | **List[str]** |  | [optional] 
**region** | **str** |  | [optional] 
**runner_iam_role_arn** | **str** |  | [optional] 
**runner_subnet** | **str** |  | [optional] 
**vpc_id** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_aws_stack_outputs import AppAWSStackOutputs

# TODO update the JSON string below
json = "{}"
# create an instance of AppAWSStackOutputs from a JSON string
app_aws_stack_outputs_instance = AppAWSStackOutputs.from_json(json)
# print the JSON string representation of the object
print AppAWSStackOutputs.to_json()

# convert the object into a dict
app_aws_stack_outputs_dict = app_aws_stack_outputs_instance.to_dict()
# create an instance of AppAWSStackOutputs from a dict
app_aws_stack_outputs_form_dict = app_aws_stack_outputs.from_dict(app_aws_stack_outputs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


