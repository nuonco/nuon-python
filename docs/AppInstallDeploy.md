# AppInstallDeploy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_workflow_runs** | [**List[AppInstallActionWorkflowRun]**](AppInstallActionWorkflowRun.md) |  | [optional] 
**build_id** | **str** |  | [optional] 
**component_build** | [**AppComponentBuild**](AppComponentBuild.md) |  | [optional] 
**component_config_version** | **int** |  | [optional] 
**component_id** | **str** |  | [optional] 
**component_name** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by** | [**AppAccount**](AppAccount.md) |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**install_component_id** | **str** |  | [optional] 
**install_deploy_type** | [**AppInstallDeployType**](AppInstallDeployType.md) |  | [optional] 
**install_id** | **str** | Fields that are de-nested at read time using AfterQuery | [optional] 
**install_workflow_id** | **str** | DEPRECATED: use WorkflowID | [optional] 
**log_stream** | [**AppLogStream**](AppLogStream.md) |  | [optional] 
**oci_artifact** | [**AppOCIArtifact**](AppOCIArtifact.md) |  | [optional] 
**outputs** | **Dict[str, object]** |  | [optional] 
**release_id** | **str** |  | [optional] 
**runner_jobs** | [**List[AppRunnerJob]**](AppRunnerJob.md) | runner details | [optional] 
**status** | **str** |  | [optional] 
**status_description** | **str** |  | [optional] 
**status_v2** | [**AppCompositeStatus**](AppCompositeStatus.md) |  | [optional] 
**updated_at** | **str** |  | [optional] 
**workflow** | [**AppWorkflow**](AppWorkflow.md) |  | [optional] 
**workflow_id** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_install_deploy import AppInstallDeploy

# TODO update the JSON string below
json = "{}"
# create an instance of AppInstallDeploy from a JSON string
app_install_deploy_instance = AppInstallDeploy.from_json(json)
# print the JSON string representation of the object
print AppInstallDeploy.to_json()

# convert the object into a dict
app_install_deploy_dict = app_install_deploy_instance.to_dict()
# create an instance of AppInstallDeploy from a dict
app_install_deploy_form_dict = app_install_deploy.from_dict(app_install_deploy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


