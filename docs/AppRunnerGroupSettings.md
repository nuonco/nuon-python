# AppRunnerGroupSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_cloudformation_stack_type** | **str** |  | [optional] 
**aws_instance_type** | **str** | aws runner specifics runner-v2 | [optional] 
**aws_max_instance_lifetime** | **int** | Default: 7 days | [optional] 
**aws_tags** | **Dict[str, str]** |  | [optional] 
**container_image_tag** | **str** |  | [optional] 
**container_image_url** | **str** | configuration for deploying the runner | [optional] 
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**enable_logging** | **bool** |  | [optional] 
**enable_metrics** | **bool** |  | [optional] 
**enable_sentry** | **bool** |  | [optional] 
**groups** | **List[str]** | the job loop groups the runner should poll for | [optional] 
**heart_beat_timeout** | **int** | Various settings for the runner to handle internally | [optional] 
**id** | **str** |  | [optional] 
**local_aws_iam_role_arn** | **str** |  | [optional] 
**logging_level** | **str** |  | [optional] 
**metadata** | **Dict[str, str]** | Metadata is used as both log and metric tags/attributes in the runner when emitting data | [optional] 
**org_aws_iam_role_arn** | **str** | org runner specifics | [optional] 
**org_id** | **str** |  | [optional] 
**org_k8s_service_account_name** | **str** |  | [optional] 
**otel_collector_config** | **str** |  | [optional] 
**platform** | **str** | platform variable for use in the runner | [optional] 
**runner_api_url** | **str** |  | [optional] 
**runner_group_id** | **str** |  | [optional] 
**sandbox_mode** | **bool** | configuration for managing the runner server side | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_runner_group_settings import AppRunnerGroupSettings

# TODO update the JSON string below
json = "{}"
# create an instance of AppRunnerGroupSettings from a JSON string
app_runner_group_settings_instance = AppRunnerGroupSettings.from_json(json)
# print the JSON string representation of the object
print AppRunnerGroupSettings.to_json()

# convert the object into a dict
app_runner_group_settings_dict = app_runner_group_settings_instance.to_dict()
# create an instance of AppRunnerGroupSettings from a dict
app_runner_group_settings_form_dict = app_runner_group_settings.from_dict(app_runner_group_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


