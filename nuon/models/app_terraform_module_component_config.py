from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_connected_github_vcs_config import AppConnectedGithubVCSConfig
    from ..models.app_public_git_vcs_config import AppPublicGitVCSConfig
    from ..models.app_terraform_module_component_config_env_vars import AppTerraformModuleComponentConfigEnvVars
    from ..models.app_terraform_module_component_config_variables import AppTerraformModuleComponentConfigVariables


T = TypeVar("T", bound="AppTerraformModuleComponentConfig")


@_attrs_define
class AppTerraformModuleComponentConfig:
    """
    Attributes:
        component_config_connection_id (Union[Unset, str]): parent reference
        connected_github_vcs_config (Union[Unset, AppConnectedGithubVCSConfig]):
        created_at (Union[Unset, str]):
        created_by_id (Union[Unset, str]):
        env_vars (Union[Unset, AppTerraformModuleComponentConfigEnvVars]):
        id (Union[Unset, str]):
        public_git_vcs_config (Union[Unset, AppPublicGitVCSConfig]):
        updated_at (Union[Unset, str]):
        variables (Union[Unset, AppTerraformModuleComponentConfigVariables]):
        variables_files (Union[Unset, list[str]]):
        version (Union[Unset, str]): terraform configuration values
    """

    component_config_connection_id: Union[Unset, str] = UNSET
    connected_github_vcs_config: Union[Unset, "AppConnectedGithubVCSConfig"] = UNSET
    created_at: Union[Unset, str] = UNSET
    created_by_id: Union[Unset, str] = UNSET
    env_vars: Union[Unset, "AppTerraformModuleComponentConfigEnvVars"] = UNSET
    id: Union[Unset, str] = UNSET
    public_git_vcs_config: Union[Unset, "AppPublicGitVCSConfig"] = UNSET
    updated_at: Union[Unset, str] = UNSET
    variables: Union[Unset, "AppTerraformModuleComponentConfigVariables"] = UNSET
    variables_files: Union[Unset, list[str]] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        component_config_connection_id = self.component_config_connection_id

        connected_github_vcs_config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.connected_github_vcs_config, Unset):
            connected_github_vcs_config = self.connected_github_vcs_config.to_dict()

        created_at = self.created_at

        created_by_id = self.created_by_id

        env_vars: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.env_vars, Unset):
            env_vars = self.env_vars.to_dict()

        id = self.id

        public_git_vcs_config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.public_git_vcs_config, Unset):
            public_git_vcs_config = self.public_git_vcs_config.to_dict()

        updated_at = self.updated_at

        variables: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.variables, Unset):
            variables = self.variables.to_dict()

        variables_files: Union[Unset, list[str]] = UNSET
        if not isinstance(self.variables_files, Unset):
            variables_files = self.variables_files

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if component_config_connection_id is not UNSET:
            field_dict["component_config_connection_id"] = component_config_connection_id
        if connected_github_vcs_config is not UNSET:
            field_dict["connected_github_vcs_config"] = connected_github_vcs_config
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if env_vars is not UNSET:
            field_dict["env_vars"] = env_vars
        if id is not UNSET:
            field_dict["id"] = id
        if public_git_vcs_config is not UNSET:
            field_dict["public_git_vcs_config"] = public_git_vcs_config
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if variables is not UNSET:
            field_dict["variables"] = variables
        if variables_files is not UNSET:
            field_dict["variables_files"] = variables_files
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_connected_github_vcs_config import AppConnectedGithubVCSConfig
        from ..models.app_public_git_vcs_config import AppPublicGitVCSConfig
        from ..models.app_terraform_module_component_config_env_vars import AppTerraformModuleComponentConfigEnvVars
        from ..models.app_terraform_module_component_config_variables import AppTerraformModuleComponentConfigVariables

        d = dict(src_dict)
        component_config_connection_id = d.pop("component_config_connection_id", UNSET)

        _connected_github_vcs_config = d.pop("connected_github_vcs_config", UNSET)
        connected_github_vcs_config: Union[Unset, AppConnectedGithubVCSConfig]
        if isinstance(_connected_github_vcs_config, Unset):
            connected_github_vcs_config = UNSET
        else:
            connected_github_vcs_config = AppConnectedGithubVCSConfig.from_dict(_connected_github_vcs_config)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        _env_vars = d.pop("env_vars", UNSET)
        env_vars: Union[Unset, AppTerraformModuleComponentConfigEnvVars]
        if isinstance(_env_vars, Unset):
            env_vars = UNSET
        else:
            env_vars = AppTerraformModuleComponentConfigEnvVars.from_dict(_env_vars)

        id = d.pop("id", UNSET)

        _public_git_vcs_config = d.pop("public_git_vcs_config", UNSET)
        public_git_vcs_config: Union[Unset, AppPublicGitVCSConfig]
        if isinstance(_public_git_vcs_config, Unset):
            public_git_vcs_config = UNSET
        else:
            public_git_vcs_config = AppPublicGitVCSConfig.from_dict(_public_git_vcs_config)

        updated_at = d.pop("updated_at", UNSET)

        _variables = d.pop("variables", UNSET)
        variables: Union[Unset, AppTerraformModuleComponentConfigVariables]
        if isinstance(_variables, Unset):
            variables = UNSET
        else:
            variables = AppTerraformModuleComponentConfigVariables.from_dict(_variables)

        variables_files = cast(list[str], d.pop("variables_files", UNSET))

        version = d.pop("version", UNSET)

        app_terraform_module_component_config = cls(
            component_config_connection_id=component_config_connection_id,
            connected_github_vcs_config=connected_github_vcs_config,
            created_at=created_at,
            created_by_id=created_by_id,
            env_vars=env_vars,
            id=id,
            public_git_vcs_config=public_git_vcs_config,
            updated_at=updated_at,
            variables=variables,
            variables_files=variables_files,
            version=version,
        )

        app_terraform_module_component_config.additional_properties = d
        return app_terraform_module_component_config

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
