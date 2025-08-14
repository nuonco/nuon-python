# AppInstallSandboxRun


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_workflow_runs** | [**List[AppInstallActionWorkflowRun]**](AppInstallActionWorkflowRun.md) |  | [optional] 
**app_sandbox_config** | [**AppAppSandboxConfig**](AppAppSandboxConfig.md) |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by** | [**AppAccount**](AppAccount.md) |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**install_id** | **str** |  | [optional] 
**install_sandbox_id** | **str** | TODO: once we run a backfill we can make this non pointer | [optional] 
**install_workflow_id** | **str** |  | [optional] 
**log_stream** | [**AppLogStream**](AppLogStream.md) |  | [optional] 
**outputs** | **Dict[str, object]** |  | [optional] 
**run_type** | [**AppSandboxRunType**](AppSandboxRunType.md) |  | [optional] 
**runner_jobs** | [**List[AppRunnerJob]**](AppRunnerJob.md) | runner details | [optional] 
**status** | **str** |  | [optional] 
**status_description** | **str** |  | [optional] 
**status_v2** | [**AppCompositeStatus**](AppCompositeStatus.md) |  | [optional] 
**updated_at** | **str** |  | [optional] 
**workflow** | [**AppWorkflow**](AppWorkflow.md) |  | [optional] 
**workflow_id** | **str** | Fields that are de-nested at read time using AfterQuery | [optional] 

## Example

```python
from nuon.models.app_install_sandbox_run import AppInstallSandboxRun

# TODO update the JSON string below
json = "{}"
# create an instance of AppInstallSandboxRun from a JSON string
app_install_sandbox_run_instance = AppInstallSandboxRun.from_json(json)
# print the JSON string representation of the object
print AppInstallSandboxRun.to_json()

# convert the object into a dict
app_install_sandbox_run_dict = app_install_sandbox_run_instance.to_dict()
# create an instance of AppInstallSandboxRun from a dict
app_install_sandbox_run_form_dict = app_install_sandbox_run.from_dict(app_install_sandbox_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


