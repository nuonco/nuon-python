# AppActionWorkflowConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_workflow_id** | **str** |  | [optional] 
**app_config_id** | **str** |  | [optional] 
**app_id** | **str** |  | [optional] 
**component_dependency_ids** | **List[str]** |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**refs** | [**List[RefsRef]**](RefsRef.md) |  | [optional] 
**steps** | [**List[AppActionWorkflowStepConfig]**](AppActionWorkflowStepConfig.md) |  | [optional] 
**timeout** | **int** |  | [optional] 
**triggers** | [**List[AppActionWorkflowTriggerConfig]**](AppActionWorkflowTriggerConfig.md) | INFO: if adding new associations here, ensure they are added to the batch delete activity | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_action_workflow_config import AppActionWorkflowConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AppActionWorkflowConfig from a JSON string
app_action_workflow_config_instance = AppActionWorkflowConfig.from_json(json)
# print the JSON string representation of the object
print AppActionWorkflowConfig.to_json()

# convert the object into a dict
app_action_workflow_config_dict = app_action_workflow_config_instance.to_dict()
# create an instance of AppActionWorkflowConfig from a dict
app_action_workflow_config_form_dict = app_action_workflow_config.from_dict(app_action_workflow_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


