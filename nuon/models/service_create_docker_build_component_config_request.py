from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

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
        app_config_id (Union[Unset, str]):
        build_args (Union[Unset, list[str]]):
        checksum (Union[Unset, str]):
        connected_github_vcs_config (Union[Unset, ServiceConnectedGithubVCSConfigRequest]):
        dependencies (Union[Unset, list[str]]):
        env_vars (Union[Unset, ServiceCreateDockerBuildComponentConfigRequestEnvVars]):
        public_git_vcs_config (Union[Unset, ServicePublicGitVCSConfigRequest]):
        references (Union[Unset, list[str]]):
        target (Union[Unset, str]):
    """

    dockerfile: str
    app_config_id: Union[Unset, str] = UNSET
    build_args: Union[Unset, list[str]] = UNSET
    checksum: Union[Unset, str] = UNSET
    connected_github_vcs_config: Union[Unset, "ServiceConnectedGithubVCSConfigRequest"] = UNSET
    dependencies: Union[Unset, list[str]] = UNSET
    env_vars: Union[Unset, "ServiceCreateDockerBuildComponentConfigRequestEnvVars"] = UNSET
    public_git_vcs_config: Union[Unset, "ServicePublicGitVCSConfigRequest"] = UNSET
    references: Union[Unset, list[str]] = UNSET
    target: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dockerfile = self.dockerfile

        app_config_id = self.app_config_id

        build_args: Union[Unset, list[str]] = UNSET
        if not isinstance(self.build_args, Unset):
            build_args = self.build_args

        checksum = self.checksum

        connected_github_vcs_config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.connected_github_vcs_config, Unset):
            connected_github_vcs_config = self.connected_github_vcs_config.to_dict()

        dependencies: Union[Unset, list[str]] = UNSET
        if not isinstance(self.dependencies, Unset):
            dependencies = self.dependencies

        env_vars: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.env_vars, Unset):
            env_vars = self.env_vars.to_dict()

        public_git_vcs_config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.public_git_vcs_config, Unset):
            public_git_vcs_config = self.public_git_vcs_config.to_dict()

        references: Union[Unset, list[str]] = UNSET
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
        if checksum is not UNSET:
            field_dict["checksum"] = checksum
        if connected_github_vcs_config is not UNSET:
            field_dict["connected_github_vcs_config"] = connected_github_vcs_config
        if dependencies is not UNSET:
            field_dict["dependencies"] = dependencies
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

        checksum = d.pop("checksum", UNSET)

        _connected_github_vcs_config = d.pop("connected_github_vcs_config", UNSET)
        connected_github_vcs_config: Union[Unset, ServiceConnectedGithubVCSConfigRequest]
        if isinstance(_connected_github_vcs_config, Unset):
            connected_github_vcs_config = UNSET
        else:
            connected_github_vcs_config = ServiceConnectedGithubVCSConfigRequest.from_dict(_connected_github_vcs_config)

        dependencies = cast(list[str], d.pop("dependencies", UNSET))

        _env_vars = d.pop("env_vars", UNSET)
        env_vars: Union[Unset, ServiceCreateDockerBuildComponentConfigRequestEnvVars]
        if isinstance(_env_vars, Unset):
            env_vars = UNSET
        else:
            env_vars = ServiceCreateDockerBuildComponentConfigRequestEnvVars.from_dict(_env_vars)

        _public_git_vcs_config = d.pop("public_git_vcs_config", UNSET)
        public_git_vcs_config: Union[Unset, ServicePublicGitVCSConfigRequest]
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
            checksum=checksum,
            connected_github_vcs_config=connected_github_vcs_config,
            dependencies=dependencies,
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
