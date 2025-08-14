# AppAppConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_workflow_configs** | [**List[AppActionWorkflowConfig]**](AppActionWorkflowConfig.md) |  | [optional] 
**app_branch** | [**AppAppBranch**](AppAppBranch.md) |  | [optional] 
**app_branch_id** | **str** |  | [optional] 
**app_id** | **str** |  | [optional] 
**break_glass** | [**AppAppBreakGlassConfig**](AppAppBreakGlassConfig.md) |  | [optional] 
**checksum** | **str** |  | [optional] 
**cli_version** | **str** |  | [optional] 
**component_config_connections** | [**List[AppComponentConfigConnection]**](AppComponentConfigConnection.md) |  | [optional] 
**component_ids** | **List[str]** |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**input** | [**AppAppInputConfig**](AppAppInputConfig.md) |  | [optional] 
**org_id** | **str** |  | [optional] 
**permissions** | [**AppAppPermissionsConfig**](AppAppPermissionsConfig.md) |  | [optional] 
**policies** | [**AppAppPoliciesConfig**](AppAppPoliciesConfig.md) |  | [optional] 
**readme** | **str** |  | [optional] 
**runner** | [**AppAppRunnerConfig**](AppAppRunnerConfig.md) |  | [optional] 
**sandbox** | [**AppAppSandboxConfig**](AppAppSandboxConfig.md) |  | [optional] 
**secrets** | [**AppAppSecretsConfig**](AppAppSecretsConfig.md) |  | [optional] 
**stack** | [**AppAppStackConfig**](AppAppStackConfig.md) |  | [optional] 
**state** | **str** |  | [optional] 
**status** | [**AppAppConfigStatus**](AppAppConfigStatus.md) |  | [optional] 
**status_description** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**vcs_connection_commit** | [**AppVCSConnectionCommit**](AppVCSConnectionCommit.md) |  | [optional] 
**version** | **int** | fields that are filled in via after query or views | [optional] 

## Example

```python
from nuon.models.app_app_config import AppAppConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AppAppConfig from a JSON string
app_app_config_instance = AppAppConfig.from_json(json)
# print the JSON string representation of the object
print AppAppConfig.to_json()

# convert the object into a dict
app_app_config_dict = app_app_config_instance.to_dict()
# create an instance of AppAppConfig from a dict
app_app_config_form_dict = app_app_config.from_dict(app_app_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


