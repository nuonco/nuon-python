from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_connected_github_vcs_config import AppConnectedGithubVCSConfig
    from ..models.app_docker_build_component_config_env_vars import AppDockerBuildComponentConfigEnvVars
    from ..models.app_public_git_vcs_config import AppPublicGitVCSConfig


T = TypeVar("T", bound="AppDockerBuildComponentConfig")


@_attrs_define
class AppDockerBuildComponentConfig:
    """
    Attributes:
        build_args (list[str] | Unset):
        component_config_connection_id (str | Unset): value
        connected_github_vcs_config (AppConnectedGithubVCSConfig | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        dockerfile (str | Unset):
        env_vars (AppDockerBuildComponentConfigEnvVars | Unset):
        id (str | Unset):
        public_git_vcs_config (AppPublicGitVCSConfig | Unset):
        target (str | Unset):
        updated_at (str | Unset):
    """

    build_args: list[str] | Unset = UNSET
    component_config_connection_id: str | Unset = UNSET
    connected_github_vcs_config: AppConnectedGithubVCSConfig | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    dockerfile: str | Unset = UNSET
    env_vars: AppDockerBuildComponentConfigEnvVars | Unset = UNSET
    id: str | Unset = UNSET
    public_git_vcs_config: AppPublicGitVCSConfig | Unset = UNSET
    target: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        build_args: list[str] | Unset = UNSET
        if not isinstance(self.build_args, Unset):
            build_args = self.build_args

        component_config_connection_id = self.component_config_connection_id

        connected_github_vcs_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.connected_github_vcs_config, Unset):
            connected_github_vcs_config = self.connected_github_vcs_config.to_dict()

        created_at = self.created_at

        created_by_id = self.created_by_id

        dockerfile = self.dockerfile

        env_vars: dict[str, Any] | Unset = UNSET
        if not isinstance(self.env_vars, Unset):
            env_vars = self.env_vars.to_dict()

        id = self.id

        public_git_vcs_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.public_git_vcs_config, Unset):
            public_git_vcs_config = self.public_git_vcs_config.to_dict()

        target = self.target

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if build_args is not UNSET:
            field_dict["build_args"] = build_args
        if component_config_connection_id is not UNSET:
            field_dict["component_config_connection_id"] = component_config_connection_id
        if connected_github_vcs_config is not UNSET:
            field_dict["connected_github_vcs_config"] = connected_github_vcs_config
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if dockerfile is not UNSET:
            field_dict["dockerfile"] = dockerfile
        if env_vars is not UNSET:
            field_dict["env_vars"] = env_vars
        if id is not UNSET:
            field_dict["id"] = id
        if public_git_vcs_config is not UNSET:
            field_dict["public_git_vcs_config"] = public_git_vcs_config
        if target is not UNSET:
            field_dict["target"] = target
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_connected_github_vcs_config import AppConnectedGithubVCSConfig
        from ..models.app_docker_build_component_config_env_vars import AppDockerBuildComponentConfigEnvVars
        from ..models.app_public_git_vcs_config import AppPublicGitVCSConfig

        d = dict(src_dict)
        build_args = cast(list[str], d.pop("build_args", UNSET))

        component_config_connection_id = d.pop("component_config_connection_id", UNSET)

        _connected_github_vcs_config = d.pop("connected_github_vcs_config", UNSET)
        connected_github_vcs_config: AppConnectedGithubVCSConfig | Unset
        if isinstance(_connected_github_vcs_config, Unset):
            connected_github_vcs_config = UNSET
        else:
            connected_github_vcs_config = AppConnectedGithubVCSConfig.from_dict(_connected_github_vcs_config)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        dockerfile = d.pop("dockerfile", UNSET)

        _env_vars = d.pop("env_vars", UNSET)
        env_vars: AppDockerBuildComponentConfigEnvVars | Unset
        if isinstance(_env_vars, Unset):
            env_vars = UNSET
        else:
            env_vars = AppDockerBuildComponentConfigEnvVars.from_dict(_env_vars)

        id = d.pop("id", UNSET)

        _public_git_vcs_config = d.pop("public_git_vcs_config", UNSET)
        public_git_vcs_config: AppPublicGitVCSConfig | Unset
        if isinstance(_public_git_vcs_config, Unset):
            public_git_vcs_config = UNSET
        else:
            public_git_vcs_config = AppPublicGitVCSConfig.from_dict(_public_git_vcs_config)

        target = d.pop("target", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        app_docker_build_component_config = cls(
            build_args=build_args,
            component_config_connection_id=component_config_connection_id,
            connected_github_vcs_config=connected_github_vcs_config,
            created_at=created_at,
            created_by_id=created_by_id,
            dockerfile=dockerfile,
            env_vars=env_vars,
            id=id,
            public_git_vcs_config=public_git_vcs_config,
            target=target,
            updated_at=updated_at,
        )

        app_docker_build_component_config.additional_properties = d
        return app_docker_build_component_config

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
