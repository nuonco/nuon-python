from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_connected_github_vcs_config_request import ServiceConnectedGithubVCSConfigRequest
    from ..models.service_create_docker_build_component_config_request_env_vars import (
        ServiceCreateDockerBuildComponentConfigRequestEnvVars,
    )
    from ..models.service_public_git_vcs_config_request import ServicePublicGitVCSConfigRequest


T = TypeVar("T", bound="ServiceCreateDockerBuildComponentConfigRequest")


@_attrs_define
class ServiceCreateDockerBuildComponentConfigRequest:
    """
    Attributes:
        dockerfile (str):
        app_config_id (str | Unset):
        build_args (list[str] | Unset):
        build_timeout (str | Unset): Duration string for build operations (e.g., "30m", "1h")
        checksum (str | Unset):
        connected_github_vcs_config (ServiceConnectedGithubVCSConfigRequest | Unset):
        dependencies (list[str] | Unset):
        deploy_timeout (str | Unset): Duration string for deploy operations (e.g., "30m", "1h")
        env_vars (ServiceCreateDockerBuildComponentConfigRequestEnvVars | Unset):
        public_git_vcs_config (ServicePublicGitVCSConfigRequest | Unset):
        references (list[str] | Unset):
        target (str | Unset):
    """

    dockerfile: str
    app_config_id: str | Unset = UNSET
    build_args: list[str] | Unset = UNSET
    build_timeout: str | Unset = UNSET
    checksum: str | Unset = UNSET
    connected_github_vcs_config: ServiceConnectedGithubVCSConfigRequest | Unset = UNSET
    dependencies: list[str] | Unset = UNSET
    deploy_timeout: str | Unset = UNSET
    env_vars: ServiceCreateDockerBuildComponentConfigRequestEnvVars | Unset = UNSET
    public_git_vcs_config: ServicePublicGitVCSConfigRequest | Unset = UNSET
    references: list[str] | Unset = UNSET
    target: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dockerfile = self.dockerfile

        app_config_id = self.app_config_id

        build_args: list[str] | Unset = UNSET
        if not isinstance(self.build_args, Unset):
            build_args = self.build_args

        build_timeout = self.build_timeout

        checksum = self.checksum

        connected_github_vcs_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.connected_github_vcs_config, Unset):
            connected_github_vcs_config = self.connected_github_vcs_config.to_dict()

        dependencies: list[str] | Unset = UNSET
        if not isinstance(self.dependencies, Unset):
            dependencies = self.dependencies

        deploy_timeout = self.deploy_timeout

        env_vars: dict[str, Any] | Unset = UNSET
        if not isinstance(self.env_vars, Unset):
            env_vars = self.env_vars.to_dict()

        public_git_vcs_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.public_git_vcs_config, Unset):
            public_git_vcs_config = self.public_git_vcs_config.to_dict()

        references: list[str] | Unset = UNSET
        if not isinstance(self.references, Unset):
            references = self.references

        target = self.target

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dockerfile": dockerfile,
            }
        )
        if app_config_id is not UNSET:
            field_dict["app_config_id"] = app_config_id
        if build_args is not UNSET:
            field_dict["build_args"] = build_args
        if build_timeout is not UNSET:
            field_dict["build_timeout"] = build_timeout
        if checksum is not UNSET:
            field_dict["checksum"] = checksum
        if connected_github_vcs_config is not UNSET:
            field_dict["connected_github_vcs_config"] = connected_github_vcs_config
        if dependencies is not UNSET:
            field_dict["dependencies"] = dependencies
        if deploy_timeout is not UNSET:
            field_dict["deploy_timeout"] = deploy_timeout
        if env_vars is not UNSET:
            field_dict["env_vars"] = env_vars
        if public_git_vcs_config is not UNSET:
            field_dict["public_git_vcs_config"] = public_git_vcs_config
        if references is not UNSET:
            field_dict["references"] = references
        if target is not UNSET:
            field_dict["target"] = target

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_connected_github_vcs_config_request import ServiceConnectedGithubVCSConfigRequest
        from ..models.service_create_docker_build_component_config_request_env_vars import (
            ServiceCreateDockerBuildComponentConfigRequestEnvVars,
        )
        from ..models.service_public_git_vcs_config_request import ServicePublicGitVCSConfigRequest

        d = dict(src_dict)
        dockerfile = d.pop("dockerfile")

        app_config_id = d.pop("app_config_id", UNSET)

        build_args = cast(list[str], d.pop("build_args", UNSET))

        build_timeout = d.pop("build_timeout", UNSET)

        checksum = d.pop("checksum", UNSET)

        _connected_github_vcs_config = d.pop("connected_github_vcs_config", UNSET)
        connected_github_vcs_config: ServiceConnectedGithubVCSConfigRequest | Unset
        if isinstance(_connected_github_vcs_config, Unset):
            connected_github_vcs_config = UNSET
        else:
            connected_github_vcs_config = ServiceConnectedGithubVCSConfigRequest.from_dict(_connected_github_vcs_config)

        dependencies = cast(list[str], d.pop("dependencies", UNSET))

        deploy_timeout = d.pop("deploy_timeout", UNSET)

        _env_vars = d.pop("env_vars", UNSET)
        env_vars: ServiceCreateDockerBuildComponentConfigRequestEnvVars | Unset
        if isinstance(_env_vars, Unset):
            env_vars = UNSET
        else:
            env_vars = ServiceCreateDockerBuildComponentConfigRequestEnvVars.from_dict(_env_vars)

        _public_git_vcs_config = d.pop("public_git_vcs_config", UNSET)
        public_git_vcs_config: ServicePublicGitVCSConfigRequest | Unset
        if isinstance(_public_git_vcs_config, Unset):
            public_git_vcs_config = UNSET
        else:
            public_git_vcs_config = ServicePublicGitVCSConfigRequest.from_dict(_public_git_vcs_config)

        references = cast(list[str], d.pop("references", UNSET))

        target = d.pop("target", UNSET)

        service_create_docker_build_component_config_request = cls(
            dockerfile=dockerfile,
            app_config_id=app_config_id,
            build_args=build_args,
            build_timeout=build_timeout,
            checksum=checksum,
            connected_github_vcs_config=connected_github_vcs_config,
            dependencies=dependencies,
            deploy_timeout=deploy_timeout,
            env_vars=env_vars,
            public_git_vcs_config=public_git_vcs_config,
            references=references,
            target=target,
        )

        service_create_docker_build_component_config_request.additional_properties = d
        return service_create_docker_build_component_config_request

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
