from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_connected_github_vcs_sandbox_config_request import (
        ServiceConnectedGithubVCSSandboxConfigRequest,
    )
    from ..models.service_create_app_sandbox_config_request_env_vars import ServiceCreateAppSandboxConfigRequestEnvVars
    from ..models.service_create_app_sandbox_config_request_variables import (
        ServiceCreateAppSandboxConfigRequestVariables,
    )
    from ..models.service_public_git_vcs_sandbox_config_request import ServicePublicGitVCSSandboxConfigRequest


T = TypeVar("T", bound="ServiceCreateAppSandboxConfigRequest")


@_attrs_define
class ServiceCreateAppSandboxConfigRequest:
    """
    Attributes:
        env_vars (ServiceCreateAppSandboxConfigRequestEnvVars):
        terraform_version (str):
        variables (ServiceCreateAppSandboxConfigRequestVariables):
        app_config_id (str | Unset):
        connected_github_vcs_config (ServiceConnectedGithubVCSSandboxConfigRequest | Unset):
        drift_schedule (str | Unset):
        public_git_vcs_config (ServicePublicGitVCSSandboxConfigRequest | Unset):
        references (list[str] | Unset):
        variables_files (list[str] | Unset):
    """

    env_vars: ServiceCreateAppSandboxConfigRequestEnvVars
    terraform_version: str
    variables: ServiceCreateAppSandboxConfigRequestVariables
    app_config_id: str | Unset = UNSET
    connected_github_vcs_config: ServiceConnectedGithubVCSSandboxConfigRequest | Unset = UNSET
    drift_schedule: str | Unset = UNSET
    public_git_vcs_config: ServicePublicGitVCSSandboxConfigRequest | Unset = UNSET
    references: list[str] | Unset = UNSET
    variables_files: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        env_vars = self.env_vars.to_dict()

        terraform_version = self.terraform_version

        variables = self.variables.to_dict()

        app_config_id = self.app_config_id

        connected_github_vcs_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.connected_github_vcs_config, Unset):
            connected_github_vcs_config = self.connected_github_vcs_config.to_dict()

        drift_schedule = self.drift_schedule

        public_git_vcs_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.public_git_vcs_config, Unset):
            public_git_vcs_config = self.public_git_vcs_config.to_dict()

        references: list[str] | Unset = UNSET
        if not isinstance(self.references, Unset):
            references = self.references

        variables_files: list[str] | Unset = UNSET
        if not isinstance(self.variables_files, Unset):
            variables_files = self.variables_files

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "env_vars": env_vars,
                "terraform_version": terraform_version,
                "variables": variables,
            }
        )
        if app_config_id is not UNSET:
            field_dict["app_config_id"] = app_config_id
        if connected_github_vcs_config is not UNSET:
            field_dict["connected_github_vcs_config"] = connected_github_vcs_config
        if drift_schedule is not UNSET:
            field_dict["drift_schedule"] = drift_schedule
        if public_git_vcs_config is not UNSET:
            field_dict["public_git_vcs_config"] = public_git_vcs_config
        if references is not UNSET:
            field_dict["references"] = references
        if variables_files is not UNSET:
            field_dict["variables_files"] = variables_files

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_connected_github_vcs_sandbox_config_request import (
            ServiceConnectedGithubVCSSandboxConfigRequest,
        )
        from ..models.service_create_app_sandbox_config_request_env_vars import (
            ServiceCreateAppSandboxConfigRequestEnvVars,
        )
        from ..models.service_create_app_sandbox_config_request_variables import (
            ServiceCreateAppSandboxConfigRequestVariables,
        )
        from ..models.service_public_git_vcs_sandbox_config_request import ServicePublicGitVCSSandboxConfigRequest

        d = dict(src_dict)
        env_vars = ServiceCreateAppSandboxConfigRequestEnvVars.from_dict(d.pop("env_vars"))

        terraform_version = d.pop("terraform_version")

        variables = ServiceCreateAppSandboxConfigRequestVariables.from_dict(d.pop("variables"))

        app_config_id = d.pop("app_config_id", UNSET)

        _connected_github_vcs_config = d.pop("connected_github_vcs_config", UNSET)
        connected_github_vcs_config: ServiceConnectedGithubVCSSandboxConfigRequest | Unset
        if isinstance(_connected_github_vcs_config, Unset):
            connected_github_vcs_config = UNSET
        else:
            connected_github_vcs_config = ServiceConnectedGithubVCSSandboxConfigRequest.from_dict(
                _connected_github_vcs_config
            )

        drift_schedule = d.pop("drift_schedule", UNSET)

        _public_git_vcs_config = d.pop("public_git_vcs_config", UNSET)
        public_git_vcs_config: ServicePublicGitVCSSandboxConfigRequest | Unset
        if isinstance(_public_git_vcs_config, Unset):
            public_git_vcs_config = UNSET
        else:
            public_git_vcs_config = ServicePublicGitVCSSandboxConfigRequest.from_dict(_public_git_vcs_config)

        references = cast(list[str], d.pop("references", UNSET))

        variables_files = cast(list[str], d.pop("variables_files", UNSET))

        service_create_app_sandbox_config_request = cls(
            env_vars=env_vars,
            terraform_version=terraform_version,
            variables=variables,
            app_config_id=app_config_id,
            connected_github_vcs_config=connected_github_vcs_config,
            drift_schedule=drift_schedule,
            public_git_vcs_config=public_git_vcs_config,
            references=references,
            variables_files=variables_files,
        )

        service_create_app_sandbox_config_request.additional_properties = d
        return service_create_app_sandbox_config_request

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
