from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_connected_github_vcs_config_request import ServiceConnectedGithubVCSConfigRequest
    from ..models.service_create_terraform_module_component_config_request_env_vars import (
        ServiceCreateTerraformModuleComponentConfigRequestEnvVars,
    )
    from ..models.service_create_terraform_module_component_config_request_variables import (
        ServiceCreateTerraformModuleComponentConfigRequestVariables,
    )
    from ..models.service_public_git_vcs_config_request import ServicePublicGitVCSConfigRequest


T = TypeVar("T", bound="ServiceCreateTerraformModuleComponentConfigRequest")


@_attrs_define
class ServiceCreateTerraformModuleComponentConfigRequest:
    """
    Attributes:
        env_vars (ServiceCreateTerraformModuleComponentConfigRequestEnvVars):
        variables (ServiceCreateTerraformModuleComponentConfigRequestVariables):
        app_config_id (str | Unset):
        checksum (str | Unset):
        connected_github_vcs_config (ServiceConnectedGithubVCSConfigRequest | Unset):
        dependencies (list[str] | Unset):
        drift_schedule (str | Unset):
        public_git_vcs_config (ServicePublicGitVCSConfigRequest | Unset):
        references (list[str] | Unset):
        variables_files (list[str] | Unset):
        version (str | Unset):
    """

    env_vars: ServiceCreateTerraformModuleComponentConfigRequestEnvVars
    variables: ServiceCreateTerraformModuleComponentConfigRequestVariables
    app_config_id: str | Unset = UNSET
    checksum: str | Unset = UNSET
    connected_github_vcs_config: ServiceConnectedGithubVCSConfigRequest | Unset = UNSET
    dependencies: list[str] | Unset = UNSET
    drift_schedule: str | Unset = UNSET
    public_git_vcs_config: ServicePublicGitVCSConfigRequest | Unset = UNSET
    references: list[str] | Unset = UNSET
    variables_files: list[str] | Unset = UNSET
    version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        env_vars = self.env_vars.to_dict()

        variables = self.variables.to_dict()

        app_config_id = self.app_config_id

        checksum = self.checksum

        connected_github_vcs_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.connected_github_vcs_config, Unset):
            connected_github_vcs_config = self.connected_github_vcs_config.to_dict()

        dependencies: list[str] | Unset = UNSET
        if not isinstance(self.dependencies, Unset):
            dependencies = self.dependencies

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

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "env_vars": env_vars,
                "variables": variables,
            }
        )
        if app_config_id is not UNSET:
            field_dict["app_config_id"] = app_config_id
        if checksum is not UNSET:
            field_dict["checksum"] = checksum
        if connected_github_vcs_config is not UNSET:
            field_dict["connected_github_vcs_config"] = connected_github_vcs_config
        if dependencies is not UNSET:
            field_dict["dependencies"] = dependencies
        if drift_schedule is not UNSET:
            field_dict["drift_schedule"] = drift_schedule
        if public_git_vcs_config is not UNSET:
            field_dict["public_git_vcs_config"] = public_git_vcs_config
        if references is not UNSET:
            field_dict["references"] = references
        if variables_files is not UNSET:
            field_dict["variables_files"] = variables_files
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_connected_github_vcs_config_request import ServiceConnectedGithubVCSConfigRequest
        from ..models.service_create_terraform_module_component_config_request_env_vars import (
            ServiceCreateTerraformModuleComponentConfigRequestEnvVars,
        )
        from ..models.service_create_terraform_module_component_config_request_variables import (
            ServiceCreateTerraformModuleComponentConfigRequestVariables,
        )
        from ..models.service_public_git_vcs_config_request import ServicePublicGitVCSConfigRequest

        d = dict(src_dict)
        env_vars = ServiceCreateTerraformModuleComponentConfigRequestEnvVars.from_dict(d.pop("env_vars"))

        variables = ServiceCreateTerraformModuleComponentConfigRequestVariables.from_dict(d.pop("variables"))

        app_config_id = d.pop("app_config_id", UNSET)

        checksum = d.pop("checksum", UNSET)

        _connected_github_vcs_config = d.pop("connected_github_vcs_config", UNSET)
        connected_github_vcs_config: ServiceConnectedGithubVCSConfigRequest | Unset
        if isinstance(_connected_github_vcs_config, Unset):
            connected_github_vcs_config = UNSET
        else:
            connected_github_vcs_config = ServiceConnectedGithubVCSConfigRequest.from_dict(_connected_github_vcs_config)

        dependencies = cast(list[str], d.pop("dependencies", UNSET))

        drift_schedule = d.pop("drift_schedule", UNSET)

        _public_git_vcs_config = d.pop("public_git_vcs_config", UNSET)
        public_git_vcs_config: ServicePublicGitVCSConfigRequest | Unset
        if isinstance(_public_git_vcs_config, Unset):
            public_git_vcs_config = UNSET
        else:
            public_git_vcs_config = ServicePublicGitVCSConfigRequest.from_dict(_public_git_vcs_config)

        references = cast(list[str], d.pop("references", UNSET))

        variables_files = cast(list[str], d.pop("variables_files", UNSET))

        version = d.pop("version", UNSET)

        service_create_terraform_module_component_config_request = cls(
            env_vars=env_vars,
            variables=variables,
            app_config_id=app_config_id,
            checksum=checksum,
            connected_github_vcs_config=connected_github_vcs_config,
            dependencies=dependencies,
            drift_schedule=drift_schedule,
            public_git_vcs_config=public_git_vcs_config,
            references=references,
            variables_files=variables_files,
            version=version,
        )

        service_create_terraform_module_component_config_request.additional_properties = d
        return service_create_terraform_module_component_config_request

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
