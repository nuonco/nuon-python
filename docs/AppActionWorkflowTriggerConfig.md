# AppActionWorkflowTriggerConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_workflow_config_id** | **str** |  | [optional] 
**app_config_id** | **str** | this belongs to an app config id | [optional] 
**app_id** | **str** |  | [optional] 
**component** | [**AppComponent**](AppComponent.md) |  | [optional] 
**component_id** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**cron_schedule** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_action_workflow_trigger_config import AppActionWorkflowTriggerConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AppActionWorkflowTriggerConfig from a JSON string
app_action_workflow_trigger_config_instance = AppActionWorkflowTriggerConfig.from_json(json)
# print the JSON string representation of the object
print AppActionWorkflowTriggerConfig.to_json()

# convert the object into a dict
app_action_workflow_trigger_config_dict = app_action_workflow_trigger_config_instance.to_dict()
# create an instance of AppActionWorkflowTriggerConfig from a dict
app_action_workflow_trigger_config_form_dict = app_action_workflow_trigger_config.from_dict(app_action_workflow_trigger_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


