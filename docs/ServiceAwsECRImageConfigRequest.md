# ServiceAwsECRImageConfigRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_region** | **str** |  | [optional] 
**iam_role_arn** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.service_aws_ecr_image_config_request import ServiceAwsECRImageConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceAwsECRImageConfigRequest from a JSON string
service_aws_ecr_image_config_request_instance = ServiceAwsECRImageConfigRequest.from_json(json)
# print the JSON string representation of the object
print ServiceAwsECRImageConfigRequest.to_json()

# convert the object into a dict
service_aws_ecr_image_config_request_dict = service_aws_ecr_image_config_request_instance.to_dict()
# create an instance of ServiceAwsECRImageConfigRequest from a dict
service_aws_ecr_image_config_request_form_dict = service_aws_ecr_image_config_request.from_dict(service_aws_ecr_image_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


