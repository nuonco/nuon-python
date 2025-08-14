# AppInstallActionWorkflow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_workflow** | [**AppActionWorkflow**](AppActionWorkflow.md) |  | [optional] 
**action_workflow_id** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**install_id** | **str** |  | [optional] 
**runs** | [**List[AppInstallActionWorkflowRun]**](AppInstallActionWorkflowRun.md) |  | [optional] 
**status** | **str** | after query fields filled in after querying | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_install_action_workflow import AppInstallActionWorkflow

# TODO update the JSON string below
json = "{}"
# create an instance of AppInstallActionWorkflow from a JSON string
app_install_action_workflow_instance = AppInstallActionWorkflow.from_json(json)
# print the JSON string representation of the object
print AppInstallActionWorkflow.to_json()

# convert the object into a dict
app_install_action_workflow_dict = app_install_action_workflow_instance.to_dict()
# create an instance of AppInstallActionWorkflow from a dict
app_install_action_workflow_form_dict = app_install_action_workflow.from_dict(app_install_action_workflow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


