from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_connected_github_vcs_config_request import ServiceConnectedGithubVCSConfigRequest
    from ..models.service_create_pulumi_component_config_request_config import (
        ServiceCreatePulumiComponentConfigRequestConfig,
    )
    from ..models.service_create_pulumi_component_config_request_env_vars import (
        ServiceCreatePulumiComponentConfigRequestEnvVars,
    )
    from ..models.service_create_pulumi_component_config_request_operation_roles import (
        ServiceCreatePulumiComponentConfigRequestOperationRoles,
    )
    from ..models.service_public_git_vcs_config_request import ServicePublicGitVCSConfigRequest


T = TypeVar("T", bound="ServiceCreatePulumiComponentConfigRequest")


@_attrs_define
class ServiceCreatePulumiComponentConfigRequest:
    """
    Attributes:
        config (ServiceCreatePulumiComponentConfigRequestConfig):
        env_vars (ServiceCreatePulumiComponentConfigRequestEnvVars):
        runtime (str):
        app_config_id (str | Unset):
        auto_approve_on_policies_passing (bool | Unset):
        build_timeout (str | Unset):
        checksum (str | Unset):
        connected_github_vcs_config (ServiceConnectedGithubVCSConfigRequest | Unset):
        default_enabled (bool | Unset):
        dependencies (list[str] | Unset):
        deploy_timeout (str | Unset):
        drift_schedule (str | Unset):
        kubernetes_context (str | Unset):
        max_auto_retries (int | Unset):
        operation_roles (ServiceCreatePulumiComponentConfigRequestOperationRoles | Unset):
        public_git_vcs_config (ServicePublicGitVCSConfigRequest | Unset):
        references (list[str] | Unset):
        skip_noops (bool | Unset):
        toggleable (bool | Unset):
        version (str | Unset):
    """

    config: ServiceCreatePulumiComponentConfigRequestConfig
    env_vars: ServiceCreatePulumiComponentConfigRequestEnvVars
    runtime: str
    app_config_id: str | Unset = UNSET
    auto_approve_on_policies_passing: bool | Unset = UNSET
    build_timeout: str | Unset = UNSET
    checksum: str | Unset = UNSET
    connected_github_vcs_config: ServiceConnectedGithubVCSConfigRequest | Unset = UNSET
    default_enabled: bool | Unset = UNSET
    dependencies: list[str] | Unset = UNSET
    deploy_timeout: str | Unset = UNSET
    drift_schedule: str | Unset = UNSET
    kubernetes_context: str | Unset = UNSET
    max_auto_retries: int | Unset = UNSET
    operation_roles: ServiceCreatePulumiComponentConfigRequestOperationRoles | Unset = UNSET
    public_git_vcs_config: ServicePublicGitVCSConfigRequest | Unset = UNSET
    references: list[str] | Unset = UNSET
    skip_noops: bool | Unset = UNSET
    toggleable: bool | Unset = UNSET
    version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        config = self.config.to_dict()

        env_vars = self.env_vars.to_dict()

        runtime = self.runtime

        app_config_id = self.app_config_id

        auto_approve_on_policies_passing = self.auto_approve_on_policies_passing

        build_timeout = self.build_timeout

        checksum = self.checksum

        connected_github_vcs_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.connected_github_vcs_config, Unset):
            connected_github_vcs_config = self.connected_github_vcs_config.to_dict()

        default_enabled = self.default_enabled

        dependencies: list[str] | Unset = UNSET
        if not isinstance(self.dependencies, Unset):
            dependencies = self.dependencies

        deploy_timeout = self.deploy_timeout

        drift_schedule = self.drift_schedule

        kubernetes_context = self.kubernetes_context

        max_auto_retries = self.max_auto_retries

        operation_roles: dict[str, Any] | Unset = UNSET
        if not isinstance(self.operation_roles, Unset):
            operation_roles = self.operation_roles.to_dict()

        public_git_vcs_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.public_git_vcs_config, Unset):
            public_git_vcs_config = self.public_git_vcs_config.to_dict()

        references: list[str] | Unset = UNSET
        if not isinstance(self.references, Unset):
            references = self.references

        skip_noops = self.skip_noops

        toggleable = self.toggleable

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "config": config,
                "env_vars": env_vars,
                "runtime": runtime,
            }
        )
        if app_config_id is not UNSET:
            field_dict["app_config_id"] = app_config_id
        if auto_approve_on_policies_passing is not UNSET:
            field_dict["auto_approve_on_policies_passing"] = auto_approve_on_policies_passing
        if build_timeout is not UNSET:
            field_dict["build_timeout"] = build_timeout
        if checksum is not UNSET:
            field_dict["checksum"] = checksum
        if connected_github_vcs_config is not UNSET:
            field_dict["connected_github_vcs_config"] = connected_github_vcs_config
        if default_enabled is not UNSET:
            field_dict["default_enabled"] = default_enabled
        if dependencies is not UNSET:
            field_dict["dependencies"] = dependencies
        if deploy_timeout is not UNSET:
            field_dict["deploy_timeout"] = deploy_timeout
        if drift_schedule is not UNSET:
            field_dict["drift_schedule"] = drift_schedule
        if kubernetes_context is not UNSET:
            field_dict["kubernetes_context"] = kubernetes_context
        if max_auto_retries is not UNSET:
            field_dict["max_auto_retries"] = max_auto_retries
        if operation_roles is not UNSET:
            field_dict["operation_roles"] = operation_roles
        if public_git_vcs_config is not UNSET:
            field_dict["public_git_vcs_config"] = public_git_vcs_config
        if references is not UNSET:
            field_dict["references"] = references
        if skip_noops is not UNSET:
            field_dict["skip_noops"] = skip_noops
        if toggleable is not UNSET:
            field_dict["toggleable"] = toggleable
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_connected_github_vcs_config_request import ServiceConnectedGithubVCSConfigRequest
        from ..models.service_create_pulumi_component_config_request_config import (
            ServiceCreatePulumiComponentConfigRequestConfig,
        )
        from ..models.service_create_pulumi_component_config_request_env_vars import (
            ServiceCreatePulumiComponentConfigRequestEnvVars,
        )
        from ..models.service_create_pulumi_component_config_request_operation_roles import (
            ServiceCreatePulumiComponentConfigRequestOperationRoles,
        )
        from ..models.service_public_git_vcs_config_request import ServicePublicGitVCSConfigRequest

        d = dict(src_dict)
        config = ServiceCreatePulumiComponentConfigRequestConfig.from_dict(d.pop("config"))

        env_vars = ServiceCreatePulumiComponentConfigRequestEnvVars.from_dict(d.pop("env_vars"))

        runtime = d.pop("runtime")

        app_config_id = d.pop("app_config_id", UNSET)

        auto_approve_on_policies_passing = d.pop("auto_approve_on_policies_passing", UNSET)

        build_timeout = d.pop("build_timeout", UNSET)

        checksum = d.pop("checksum", UNSET)

        _connected_github_vcs_config = d.pop("connected_github_vcs_config", UNSET)
        connected_github_vcs_config: ServiceConnectedGithubVCSConfigRequest | Unset
        if isinstance(_connected_github_vcs_config, Unset):
            connected_github_vcs_config = UNSET
        else:
            connected_github_vcs_config = ServiceConnectedGithubVCSConfigRequest.from_dict(_connected_github_vcs_config)

        default_enabled = d.pop("default_enabled", UNSET)

        dependencies = cast(list[str], d.pop("dependencies", UNSET))

        deploy_timeout = d.pop("deploy_timeout", UNSET)

        drift_schedule = d.pop("drift_schedule", UNSET)

        kubernetes_context = d.pop("kubernetes_context", UNSET)

        max_auto_retries = d.pop("max_auto_retries", UNSET)

        _operation_roles = d.pop("operation_roles", UNSET)
        operation_roles: ServiceCreatePulumiComponentConfigRequestOperationRoles | Unset
        if isinstance(_operation_roles, Unset):
            operation_roles = UNSET
        else:
            operation_roles = ServiceCreatePulumiComponentConfigRequestOperationRoles.from_dict(_operation_roles)

        _public_git_vcs_config = d.pop("public_git_vcs_config", UNSET)
        public_git_vcs_config: ServicePublicGitVCSConfigRequest | Unset
        if isinstance(_public_git_vcs_config, Unset):
            public_git_vcs_config = UNSET
        else:
            public_git_vcs_config = ServicePublicGitVCSConfigRequest.from_dict(_public_git_vcs_config)

        references = cast(list[str], d.pop("references", UNSET))

        skip_noops = d.pop("skip_noops", UNSET)

        toggleable = d.pop("toggleable", UNSET)

        version = d.pop("version", UNSET)

        service_create_pulumi_component_config_request = cls(
            config=config,
            env_vars=env_vars,
            runtime=runtime,
            app_config_id=app_config_id,
            auto_approve_on_policies_passing=auto_approve_on_policies_passing,
            build_timeout=build_timeout,
            checksum=checksum,
            connected_github_vcs_config=connected_github_vcs_config,
            default_enabled=default_enabled,
            dependencies=dependencies,
            deploy_timeout=deploy_timeout,
            drift_schedule=drift_schedule,
            kubernetes_context=kubernetes_context,
            max_auto_retries=max_auto_retries,
            operation_roles=operation_roles,
            public_git_vcs_config=public_git_vcs_config,
            references=references,
            skip_noops=skip_noops,
            toggleable=toggleable,
            version=version,
        )

        service_create_pulumi_component_config_request.additional_properties = d
        return service_create_pulumi_component_config_request

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
