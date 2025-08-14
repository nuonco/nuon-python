# ServiceSyncSecretsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_only** | **bool** |  | [optional] 

## Example

```python
from nuon.models.service_sync_secrets_request import ServiceSyncSecretsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceSyncSecretsRequest from a JSON string
service_sync_secrets_request_instance = ServiceSyncSecretsRequest.from_json(json)
# print the JSON string representation of the object
print ServiceSyncSecretsRequest.to_json()

# convert the object into a dict
service_sync_secrets_request_dict = service_sync_secrets_request_instance.to_dict()
# create an instance of ServiceSyncSecretsRequest from a dict
service_sync_secrets_request_form_dict = service_sync_secrets_request.from_dict(service_sync_secrets_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


