from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.helpers_connected_github_vcs_config_request import HelpersConnectedGithubVCSConfigRequest
    from ..models.helpers_public_git_vcs_config_request import HelpersPublicGitVCSConfigRequest
    from ..models.service_create_app_sandbox_config_request_env_vars import ServiceCreateAppSandboxConfigRequestEnvVars
    from ..models.service_create_app_sandbox_config_request_operation_roles import (
        ServiceCreateAppSandboxConfigRequestOperationRoles,
    )
    from ..models.service_create_app_sandbox_config_request_pulumi_config import (
        ServiceCreateAppSandboxConfigRequestPulumiConfig,
    )
    from ..models.service_create_app_sandbox_config_request_variables import (
        ServiceCreateAppSandboxConfigRequestVariables,
    )


T = TypeVar("T", bound="ServiceCreateAppSandboxConfigRequest")


@_attrs_define
class ServiceCreateAppSandboxConfigRequest:
    """
    Attributes:
        env_vars (ServiceCreateAppSandboxConfigRequestEnvVars):
        variables (ServiceCreateAppSandboxConfigRequestVariables):
        app_config_id (str | Unset):
        auto_approve_on_policies_passing (bool | Unset):
        connected_github_vcs_config (HelpersConnectedGithubVCSConfigRequest | Unset):
        drift_schedule (str | Unset):
        max_auto_retries (int | Unset):
        operation_roles (ServiceCreateAppSandboxConfigRequestOperationRoles | Unset):
        public_git_vcs_config (HelpersPublicGitVCSConfigRequest | Unset):
        pulumi_config (ServiceCreateAppSandboxConfigRequestPulumiConfig | Unset):
        pulumi_version (str | Unset):
        references (list[str] | Unset):
        runtime (str | Unset):
        skip_noops (bool | Unset):
        terraform_version (str | Unset):
        type_ (str | Unset):
        variables_files (list[str] | Unset):
    """

    env_vars: ServiceCreateAppSandboxConfigRequestEnvVars
    variables: ServiceCreateAppSandboxConfigRequestVariables
    app_config_id: str | Unset = UNSET
    auto_approve_on_policies_passing: bool | Unset = UNSET
    connected_github_vcs_config: HelpersConnectedGithubVCSConfigRequest | Unset = UNSET
    drift_schedule: str | Unset = UNSET
    max_auto_retries: int | Unset = UNSET
    operation_roles: ServiceCreateAppSandboxConfigRequestOperationRoles | Unset = UNSET
    public_git_vcs_config: HelpersPublicGitVCSConfigRequest | Unset = UNSET
    pulumi_config: ServiceCreateAppSandboxConfigRequestPulumiConfig | Unset = UNSET
    pulumi_version: str | Unset = UNSET
    references: list[str] | Unset = UNSET
    runtime: str | Unset = UNSET
    skip_noops: bool | Unset = UNSET
    terraform_version: str | Unset = UNSET
    type_: str | Unset = UNSET
    variables_files: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        env_vars = self.env_vars.to_dict()

        variables = self.variables.to_dict()

        app_config_id = self.app_config_id

        auto_approve_on_policies_passing = self.auto_approve_on_policies_passing

        connected_github_vcs_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.connected_github_vcs_config, Unset):
            connected_github_vcs_config = self.connected_github_vcs_config.to_dict()

        drift_schedule = self.drift_schedule

        max_auto_retries = self.max_auto_retries

        operation_roles: dict[str, Any] | Unset = UNSET
        if not isinstance(self.operation_roles, Unset):
            operation_roles = self.operation_roles.to_dict()

        public_git_vcs_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.public_git_vcs_config, Unset):
            public_git_vcs_config = self.public_git_vcs_config.to_dict()

        pulumi_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pulumi_config, Unset):
            pulumi_config = self.pulumi_config.to_dict()

        pulumi_version = self.pulumi_version

        references: list[str] | Unset = UNSET
        if not isinstance(self.references, Unset):
            references = self.references

        runtime = self.runtime

        skip_noops = self.skip_noops

        terraform_version = self.terraform_version

        type_ = self.type_

        variables_files: list[str] | Unset = UNSET
        if not isinstance(self.variables_files, Unset):
            variables_files = self.variables_files

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
        if auto_approve_on_policies_passing is not UNSET:
            field_dict["auto_approve_on_policies_passing"] = auto_approve_on_policies_passing
        if connected_github_vcs_config is not UNSET:
            field_dict["connected_github_vcs_config"] = connected_github_vcs_config
        if drift_schedule is not UNSET:
            field_dict["drift_schedule"] = drift_schedule
        if max_auto_retries is not UNSET:
            field_dict["max_auto_retries"] = max_auto_retries
        if operation_roles is not UNSET:
            field_dict["operation_roles"] = operation_roles
        if public_git_vcs_config is not UNSET:
            field_dict["public_git_vcs_config"] = public_git_vcs_config
        if pulumi_config is not UNSET:
            field_dict["pulumi_config"] = pulumi_config
        if pulumi_version is not UNSET:
            field_dict["pulumi_version"] = pulumi_version
        if references is not UNSET:
            field_dict["references"] = references
        if runtime is not UNSET:
            field_dict["runtime"] = runtime
        if skip_noops is not UNSET:
            field_dict["skip_noops"] = skip_noops
        if terraform_version is not UNSET:
            field_dict["terraform_version"] = terraform_version
        if type_ is not UNSET:
            field_dict["type"] = type_
        if variables_files is not UNSET:
            field_dict["variables_files"] = variables_files

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.helpers_connected_github_vcs_config_request import HelpersConnectedGithubVCSConfigRequest
        from ..models.helpers_public_git_vcs_config_request import HelpersPublicGitVCSConfigRequest
        from ..models.service_create_app_sandbox_config_request_env_vars import (
            ServiceCreateAppSandboxConfigRequestEnvVars,
        )
        from ..models.service_create_app_sandbox_config_request_operation_roles import (
            ServiceCreateAppSandboxConfigRequestOperationRoles,
        )
        from ..models.service_create_app_sandbox_config_request_pulumi_config import (
            ServiceCreateAppSandboxConfigRequestPulumiConfig,
        )
        from ..models.service_create_app_sandbox_config_request_variables import (
            ServiceCreateAppSandboxConfigRequestVariables,
        )

        d = dict(src_dict)
        env_vars = ServiceCreateAppSandboxConfigRequestEnvVars.from_dict(d.pop("env_vars"))

        variables = ServiceCreateAppSandboxConfigRequestVariables.from_dict(d.pop("variables"))

        app_config_id = d.pop("app_config_id", UNSET)

        auto_approve_on_policies_passing = d.pop("auto_approve_on_policies_passing", UNSET)

        _connected_github_vcs_config = d.pop("connected_github_vcs_config", UNSET)
        connected_github_vcs_config: HelpersConnectedGithubVCSConfigRequest | Unset
        if isinstance(_connected_github_vcs_config, Unset):
            connected_github_vcs_config = UNSET
        else:
            connected_github_vcs_config = HelpersConnectedGithubVCSConfigRequest.from_dict(_connected_github_vcs_config)

        drift_schedule = d.pop("drift_schedule", UNSET)

        max_auto_retries = d.pop("max_auto_retries", UNSET)

        _operation_roles = d.pop("operation_roles", UNSET)
        operation_roles: ServiceCreateAppSandboxConfigRequestOperationRoles | Unset
        if isinstance(_operation_roles, Unset):
            operation_roles = UNSET
        else:
            operation_roles = ServiceCreateAppSandboxConfigRequestOperationRoles.from_dict(_operation_roles)

        _public_git_vcs_config = d.pop("public_git_vcs_config", UNSET)
        public_git_vcs_config: HelpersPublicGitVCSConfigRequest | Unset
        if isinstance(_public_git_vcs_config, Unset):
            public_git_vcs_config = UNSET
        else:
            public_git_vcs_config = HelpersPublicGitVCSConfigRequest.from_dict(_public_git_vcs_config)

        _pulumi_config = d.pop("pulumi_config", UNSET)
        pulumi_config: ServiceCreateAppSandboxConfigRequestPulumiConfig | Unset
        if isinstance(_pulumi_config, Unset):
            pulumi_config = UNSET
        else:
            pulumi_config = ServiceCreateAppSandboxConfigRequestPulumiConfig.from_dict(_pulumi_config)

        pulumi_version = d.pop("pulumi_version", UNSET)

        references = cast(list[str], d.pop("references", UNSET))

        runtime = d.pop("runtime", UNSET)

        skip_noops = d.pop("skip_noops", UNSET)

        terraform_version = d.pop("terraform_version", UNSET)

        type_ = d.pop("type", UNSET)

        variables_files = cast(list[str], d.pop("variables_files", UNSET))

        service_create_app_sandbox_config_request = cls(
            env_vars=env_vars,
            variables=variables,
            app_config_id=app_config_id,
            auto_approve_on_policies_passing=auto_approve_on_policies_passing,
            connected_github_vcs_config=connected_github_vcs_config,
            drift_schedule=drift_schedule,
            max_auto_retries=max_auto_retries,
            operation_roles=operation_roles,
            public_git_vcs_config=public_git_vcs_config,
            pulumi_config=pulumi_config,
            pulumi_version=pulumi_version,
            references=references,
            runtime=runtime,
            skip_noops=skip_noops,
            terraform_version=terraform_version,
            type_=type_,
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
