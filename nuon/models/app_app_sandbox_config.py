from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_app_sandbox_config_env_vars import AppAppSandboxConfigEnvVars
    from ..models.app_app_sandbox_config_variables import AppAppSandboxConfigVariables
    from ..models.app_connected_github_vcs_config import AppConnectedGithubVCSConfig
    from ..models.app_public_git_vcs_config import AppPublicGitVCSConfig


T = TypeVar("T", bound="AppAppSandboxConfig")


@_attrs_define
class AppAppSandboxConfig:
    """
    Attributes:
        app_config_id (Union[Unset, str]):
        app_id (Union[Unset, str]):
        aws_region_type (Union[Unset, str]): cloud specific fields
        cloud_platform (Union[Unset, str]): fields set via after query
        connected_github_vcs_config (Union[Unset, AppConnectedGithubVCSConfig]):
        created_at (Union[Unset, str]):
        created_by_id (Union[Unset, str]):
        drift_schedule (Union[Unset, str]):
        env_vars (Union[Unset, AppAppSandboxConfigEnvVars]):
        id (Union[Unset, str]):
        org_id (Union[Unset, str]):
        public_git_vcs_config (Union[Unset, AppPublicGitVCSConfig]):
        terraform_version (Union[Unset, str]):
        updated_at (Union[Unset, str]):
        variables (Union[Unset, AppAppSandboxConfigVariables]):
        variables_files (Union[Unset, list[str]]):
    """

    app_config_id: Union[Unset, str] = UNSET
    app_id: Union[Unset, str] = UNSET
    aws_region_type: Union[Unset, str] = UNSET
    cloud_platform: Union[Unset, str] = UNSET
    connected_github_vcs_config: Union[Unset, "AppConnectedGithubVCSConfig"] = UNSET
    created_at: Union[Unset, str] = UNSET
    created_by_id: Union[Unset, str] = UNSET
    drift_schedule: Union[Unset, str] = UNSET
    env_vars: Union[Unset, "AppAppSandboxConfigEnvVars"] = UNSET
    id: Union[Unset, str] = UNSET
    org_id: Union[Unset, str] = UNSET
    public_git_vcs_config: Union[Unset, "AppPublicGitVCSConfig"] = UNSET
    terraform_version: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    variables: Union[Unset, "AppAppSandboxConfigVariables"] = UNSET
    variables_files: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_config_id = self.app_config_id

        app_id = self.app_id

        aws_region_type = self.aws_region_type

        cloud_platform = self.cloud_platform

        connected_github_vcs_config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.connected_github_vcs_config, Unset):
            connected_github_vcs_config = self.connected_github_vcs_config.to_dict()

        created_at = self.created_at

        created_by_id = self.created_by_id

        drift_schedule = self.drift_schedule

        env_vars: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.env_vars, Unset):
            env_vars = self.env_vars.to_dict()

        id = self.id

        org_id = self.org_id

        public_git_vcs_config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.public_git_vcs_config, Unset):
            public_git_vcs_config = self.public_git_vcs_config.to_dict()

        terraform_version = self.terraform_version

        updated_at = self.updated_at

        variables: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.variables, Unset):
            variables = self.variables.to_dict()

        variables_files: Union[Unset, list[str]] = UNSET
        if not isinstance(self.variables_files, Unset):
            variables_files = self.variables_files

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_config_id is not UNSET:
            field_dict["app_config_id"] = app_config_id
        if app_id is not UNSET:
            field_dict["app_id"] = app_id
        if aws_region_type is not UNSET:
            field_dict["aws_region_type"] = aws_region_type
        if cloud_platform is not UNSET:
            field_dict["cloud_platform"] = cloud_platform
        if connected_github_vcs_config is not UNSET:
            field_dict["connected_github_vcs_config"] = connected_github_vcs_config
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if drift_schedule is not UNSET:
            field_dict["drift_schedule"] = drift_schedule
        if env_vars is not UNSET:
            field_dict["env_vars"] = env_vars
        if id is not UNSET:
            field_dict["id"] = id
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if public_git_vcs_config is not UNSET:
            field_dict["public_git_vcs_config"] = public_git_vcs_config
        if terraform_version is not UNSET:
            field_dict["terraform_version"] = terraform_version
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if variables is not UNSET:
            field_dict["variables"] = variables
        if variables_files is not UNSET:
            field_dict["variables_files"] = variables_files

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_app_sandbox_config_env_vars import AppAppSandboxConfigEnvVars
        from ..models.app_app_sandbox_config_variables import AppAppSandboxConfigVariables
        from ..models.app_connected_github_vcs_config import AppConnectedGithubVCSConfig
        from ..models.app_public_git_vcs_config import AppPublicGitVCSConfig

        d = dict(src_dict)
        app_config_id = d.pop("app_config_id", UNSET)

        app_id = d.pop("app_id", UNSET)

        aws_region_type = d.pop("aws_region_type", UNSET)

        cloud_platform = d.pop("cloud_platform", UNSET)

        _connected_github_vcs_config = d.pop("connected_github_vcs_config", UNSET)
        connected_github_vcs_config: Union[Unset, AppConnectedGithubVCSConfig]
        if isinstance(_connected_github_vcs_config, Unset):
            connected_github_vcs_config = UNSET
        else:
            connected_github_vcs_config = AppConnectedGithubVCSConfig.from_dict(_connected_github_vcs_config)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        drift_schedule = d.pop("drift_schedule", UNSET)

        _env_vars = d.pop("env_vars", UNSET)
        env_vars: Union[Unset, AppAppSandboxConfigEnvVars]
        if isinstance(_env_vars, Unset):
            env_vars = UNSET
        else:
            env_vars = AppAppSandboxConfigEnvVars.from_dict(_env_vars)

        id = d.pop("id", UNSET)

        org_id = d.pop("org_id", UNSET)

        _public_git_vcs_config = d.pop("public_git_vcs_config", UNSET)
        public_git_vcs_config: Union[Unset, AppPublicGitVCSConfig]
        if isinstance(_public_git_vcs_config, Unset):
            public_git_vcs_config = UNSET
        else:
            public_git_vcs_config = AppPublicGitVCSConfig.from_dict(_public_git_vcs_config)

        terraform_version = d.pop("terraform_version", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        _variables = d.pop("variables", UNSET)
        variables: Union[Unset, AppAppSandboxConfigVariables]
        if isinstance(_variables, Unset):
            variables = UNSET
        else:
            variables = AppAppSandboxConfigVariables.from_dict(_variables)

        variables_files = cast(list[str], d.pop("variables_files", UNSET))

        app_app_sandbox_config = cls(
            app_config_id=app_config_id,
            app_id=app_id,
            aws_region_type=aws_region_type,
            cloud_platform=cloud_platform,
            connected_github_vcs_config=connected_github_vcs_config,
            created_at=created_at,
            created_by_id=created_by_id,
            drift_schedule=drift_schedule,
            env_vars=env_vars,
            id=id,
            org_id=org_id,
            public_git_vcs_config=public_git_vcs_config,
            terraform_version=terraform_version,
            updated_at=updated_at,
            variables=variables,
            variables_files=variables_files,
        )

        app_app_sandbox_config.additional_properties = d
        return app_app_sandbox_config

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
