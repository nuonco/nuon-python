from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_app_sandbox_config_env_vars import AppAppSandboxConfigEnvVars
    from ..models.app_app_sandbox_config_variables import AppAppSandboxConfigVariables
    from ..models.app_connected_github_vcs_config import AppConnectedGithubVCSConfig
    from ..models.app_public_git_vcs_config import AppPublicGitVCSConfig
    from ..models.refs_ref import RefsRef


T = TypeVar("T", bound="AppAppSandboxConfig")


@_attrs_define
class AppAppSandboxConfig:
    """
    Attributes:
        app_config_id (str | Unset):
        app_id (str | Unset):
        aws_region_type (str | Unset): cloud specific fields
        cloud_platform (str | Unset): fields set via after query
        connected_github_vcs_config (AppConnectedGithubVCSConfig | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        drift_schedule (str | Unset):
        env_vars (AppAppSandboxConfigEnvVars | Unset):
        id (str | Unset):
        org_id (str | Unset):
        public_git_vcs_config (AppPublicGitVCSConfig | Unset):
        references (list[str] | Unset):
        refs (list[RefsRef] | Unset):
        terraform_version (str | Unset):
        updated_at (str | Unset):
        variables (AppAppSandboxConfigVariables | Unset):
        variables_files (list[str] | Unset):
    """

    app_config_id: str | Unset = UNSET
    app_id: str | Unset = UNSET
    aws_region_type: str | Unset = UNSET
    cloud_platform: str | Unset = UNSET
    connected_github_vcs_config: AppConnectedGithubVCSConfig | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    drift_schedule: str | Unset = UNSET
    env_vars: AppAppSandboxConfigEnvVars | Unset = UNSET
    id: str | Unset = UNSET
    org_id: str | Unset = UNSET
    public_git_vcs_config: AppPublicGitVCSConfig | Unset = UNSET
    references: list[str] | Unset = UNSET
    refs: list[RefsRef] | Unset = UNSET
    terraform_version: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    variables: AppAppSandboxConfigVariables | Unset = UNSET
    variables_files: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_config_id = self.app_config_id

        app_id = self.app_id

        aws_region_type = self.aws_region_type

        cloud_platform = self.cloud_platform

        connected_github_vcs_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.connected_github_vcs_config, Unset):
            connected_github_vcs_config = self.connected_github_vcs_config.to_dict()

        created_at = self.created_at

        created_by_id = self.created_by_id

        drift_schedule = self.drift_schedule

        env_vars: dict[str, Any] | Unset = UNSET
        if not isinstance(self.env_vars, Unset):
            env_vars = self.env_vars.to_dict()

        id = self.id

        org_id = self.org_id

        public_git_vcs_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.public_git_vcs_config, Unset):
            public_git_vcs_config = self.public_git_vcs_config.to_dict()

        references: list[str] | Unset = UNSET
        if not isinstance(self.references, Unset):
            references = self.references

        refs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.refs, Unset):
            refs = []
            for refs_item_data in self.refs:
                refs_item = refs_item_data.to_dict()
                refs.append(refs_item)

        terraform_version = self.terraform_version

        updated_at = self.updated_at

        variables: dict[str, Any] | Unset = UNSET
        if not isinstance(self.variables, Unset):
            variables = self.variables.to_dict()

        variables_files: list[str] | Unset = UNSET
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
        if references is not UNSET:
            field_dict["references"] = references
        if refs is not UNSET:
            field_dict["refs"] = refs
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
        from ..models.refs_ref import RefsRef

        d = dict(src_dict)
        app_config_id = d.pop("app_config_id", UNSET)

        app_id = d.pop("app_id", UNSET)

        aws_region_type = d.pop("aws_region_type", UNSET)

        cloud_platform = d.pop("cloud_platform", UNSET)

        _connected_github_vcs_config = d.pop("connected_github_vcs_config", UNSET)
        connected_github_vcs_config: AppConnectedGithubVCSConfig | Unset
        if isinstance(_connected_github_vcs_config, Unset):
            connected_github_vcs_config = UNSET
        else:
            connected_github_vcs_config = AppConnectedGithubVCSConfig.from_dict(_connected_github_vcs_config)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        drift_schedule = d.pop("drift_schedule", UNSET)

        _env_vars = d.pop("env_vars", UNSET)
        env_vars: AppAppSandboxConfigEnvVars | Unset
        if isinstance(_env_vars, Unset):
            env_vars = UNSET
        else:
            env_vars = AppAppSandboxConfigEnvVars.from_dict(_env_vars)

        id = d.pop("id", UNSET)

        org_id = d.pop("org_id", UNSET)

        _public_git_vcs_config = d.pop("public_git_vcs_config", UNSET)
        public_git_vcs_config: AppPublicGitVCSConfig | Unset
        if isinstance(_public_git_vcs_config, Unset):
            public_git_vcs_config = UNSET
        else:
            public_git_vcs_config = AppPublicGitVCSConfig.from_dict(_public_git_vcs_config)

        references = cast(list[str], d.pop("references", UNSET))

        refs = []
        _refs = d.pop("refs", UNSET)
        for refs_item_data in _refs or []:
            refs_item = RefsRef.from_dict(refs_item_data)

            refs.append(refs_item)

        terraform_version = d.pop("terraform_version", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        _variables = d.pop("variables", UNSET)
        variables: AppAppSandboxConfigVariables | Unset
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
            references=references,
            refs=refs,
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
