# AppAWSECRImageConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_region** | **str** |  | [optional] 
**component_config_id** | **str** | connection to parent model | [optional] 
**component_config_type** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by** | [**AppAccount**](AppAccount.md) |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**iam_role_arn** | **str** | actual configuration | [optional] 
**id** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nuon.models.app_awsecr_image_config import AppAWSECRImageConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AppAWSECRImageConfig from a JSON string
app_awsecr_image_config_instance = AppAWSECRImageConfig.from_json(json)
# print the JSON string representation of the object
print AppAWSECRImageConfig.to_json()

# convert the object into a dict
app_awsecr_image_config_dict = app_awsecr_image_config_instance.to_dict()
# create an instance of AppAWSECRImageConfig from a dict
app_awsecr_image_config_form_dict = app_awsecr_image_config.from_dict(app_awsecr_image_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


