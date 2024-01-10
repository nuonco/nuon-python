# StderrErrResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**error** | **str** |  | [optional] 
**user_error** | **bool** |  | [optional] 

## Example

```python
from nuon.models.stderr_err_response import StderrErrResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StderrErrResponse from a JSON string
stderr_err_response_instance = StderrErrResponse.from_json(json)
# print the JSON string representation of the object
print StderrErrResponse.to_json()

# convert the object into a dict
stderr_err_response_dict = stderr_err_response_instance.to_dict()
# create an instance of StderrErrResponse from a dict
stderr_err_response_form_dict = stderr_err_response.from_dict(stderr_err_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


