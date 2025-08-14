# GithubComPowertoolsdevMonoPkgTypesStateState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**StateActionsState**](StateActionsState.md) |  | [optional] 
**app** | [**StateAppState**](StateAppState.md) |  | [optional] 
**cloud_account** | [**StateCloudAccount**](StateCloudAccount.md) |  | [optional] 
**components** | **Dict[str, object]** |  | [optional] 
**domain** | [**StateDomainState**](StateDomainState.md) |  | [optional] 
**id** | **str** |  | [optional] 
**inputs** | [**StateInputsState**](StateInputsState.md) |  | [optional] 
**install** | [**StateInstallState**](StateInstallState.md) | NOTE: for backwards compatibility, these are remaining in place. | [optional] 
**install_stack** | [**StateInstallStackState**](StateInstallStackState.md) |  | [optional] 
**name** | **str** |  | [optional] 
**org** | [**StateOrgState**](StateOrgState.md) |  | [optional] 
**runner** | [**StateRunnerState**](StateRunnerState.md) |  | [optional] 
**sandbox** | [**StateSandboxState**](StateSandboxState.md) |  | [optional] 
**secrets** | [**Dict[str, OutputsSecretSyncOutput]**](OutputsSecretSyncOutput.md) |  | [optional] 

## Example

```python
from nuon.models.github_com_powertoolsdev_mono_pkg_types_state_state import GithubComPowertoolsdevMonoPkgTypesStateState

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComPowertoolsdevMonoPkgTypesStateState from a JSON string
github_com_powertoolsdev_mono_pkg_types_state_state_instance = GithubComPowertoolsdevMonoPkgTypesStateState.from_json(json)
# print the JSON string representation of the object
print GithubComPowertoolsdevMonoPkgTypesStateState.to_json()

# convert the object into a dict
github_com_powertoolsdev_mono_pkg_types_state_state_dict = github_com_powertoolsdev_mono_pkg_types_state_state_instance.to_dict()
# create an instance of GithubComPowertoolsdevMonoPkgTypesStateState from a dict
github_com_powertoolsdev_mono_pkg_types_state_state_form_dict = github_com_powertoolsdev_mono_pkg_types_state_state.from_dict(github_com_powertoolsdev_mono_pkg_types_state_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


