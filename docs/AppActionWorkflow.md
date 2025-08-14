# AppActionWorkflow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** |  | [optional] 
**config_count** | **int** |  | [optional] 
**configs** | [**List[AppActionWorkflowConfig]**](AppActionWorkflowConfig.md) |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** | metadata | [optional] 
**status** | **str** | TODO: change to default null after migration &amp; after initial pr | [optional] 
**status_description** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_action_workflow import AppActionWorkflow

# TODO update the JSON string below
json = "{}"
# create an instance of AppActionWorkflow from a JSON string
app_action_workflow_instance = AppActionWorkflow.from_json(json)
# print the JSON string representation of the object
print AppActionWorkflow.to_json()

# convert the object into a dict
app_action_workflow_dict = app_action_workflow_instance.to_dict()
# create an instance of AppActionWorkflow from a dict
app_action_workflow_form_dict = app_action_workflow.from_dict(app_action_workflow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


