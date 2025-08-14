# AppInstallActionWorkflowRun


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_workflow_config_id** | **str** |  | [optional] 
**config** | [**AppActionWorkflowConfig**](AppActionWorkflowConfig.md) |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by** | [**AppAccount**](AppAccount.md) |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**execution_time** | **int** | after query | [optional] 
**id** | **str** |  | [optional] 
**install_action_workflow** | [**AppInstallActionWorkflow**](AppInstallActionWorkflow.md) |  | [optional] 
**install_action_workflow_id** | **str** |  | [optional] 
**install_id** | **str** |  | [optional] 
**install_workflow_id** | **str** |  | [optional] 
**log_stream** | [**AppLogStream**](AppLogStream.md) |  | [optional] 
**outputs** | **Dict[str, object]** |  | [optional] 
**run_env_vars** | **Dict[str, str]** |  | [optional] 
**runner_job** | [**AppRunnerJob**](AppRunnerJob.md) |  | [optional] 
**status** | **str** |  | [optional] 
**status_description** | **str** |  | [optional] 
**status_v2** | [**AppCompositeStatus**](AppCompositeStatus.md) |  | [optional] 
**steps** | [**List[AppInstallActionWorkflowRunStep]**](AppInstallActionWorkflowRunStep.md) |  | [optional] 
**trigger_type** | [**AppActionWorkflowTriggerType**](AppActionWorkflowTriggerType.md) |  | [optional] 
**triggered_by_id** | **str** |  | [optional] 
**triggered_by_type** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**workflow** | [**AppWorkflow**](AppWorkflow.md) |  | [optional] 
**workflow_id** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_install_action_workflow_run import AppInstallActionWorkflowRun

# TODO update the JSON string below
json = "{}"
# create an instance of AppInstallActionWorkflowRun from a JSON string
app_install_action_workflow_run_instance = AppInstallActionWorkflowRun.from_json(json)
# print the JSON string representation of the object
print AppInstallActionWorkflowRun.to_json()

# convert the object into a dict
app_install_action_workflow_run_dict = app_install_action_workflow_run_instance.to_dict()
# create an instance of AppInstallActionWorkflowRun from a dict
app_install_action_workflow_run_form_dict = app_install_action_workflow_run.from_dict(app_install_action_workflow_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


