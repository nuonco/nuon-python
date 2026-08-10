from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_connected_github_vcs_config import AppConnectedGithubVCSConfig
    from ..models.app_public_git_vcs_config import AppPublicGitVCSConfig


T = TypeVar("T", bound="AppAppInstallsConfig")


@_attrs_define
class AppAppInstallsConfig:
    """
    Attributes:
        app_id (str | Unset):
        branch (str | Unset):
        connected_github_vcs_config (AppConnectedGithubVCSConfig | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        directory (str | Unset):
        id (str | Unset):
        org_id (str | Unset):
        public_git_vcs_config (AppPublicGitVCSConfig | Unset):
        repo (str | Unset):
        source (str | Unset):
        updated_at (str | Unset):
        vcs_connection_id (str | Unset):
        vcs_type (str | Unset):
    """

    app_id: str | Unset = UNSET
    branch: str | Unset = UNSET
    connected_github_vcs_config: AppConnectedGithubVCSConfig | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    directory: str | Unset = UNSET
    id: str | Unset = UNSET
    org_id: str | Unset = UNSET
    public_git_vcs_config: AppPublicGitVCSConfig | Unset = UNSET
    repo: str | Unset = UNSET
    source: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    vcs_connection_id: str | Unset = UNSET
    vcs_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_id = self.app_id

        branch = self.branch

        connected_github_vcs_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.connected_github_vcs_config, Unset):
            connected_github_vcs_config = self.connected_github_vcs_config.to_dict()

        created_at = self.created_at

        created_by_id = self.created_by_id

        directory = self.directory

        id = self.id

        org_id = self.org_id

        public_git_vcs_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.public_git_vcs_config, Unset):
            public_git_vcs_config = self.public_git_vcs_config.to_dict()

        repo = self.repo

        source = self.source

        updated_at = self.updated_at

        vcs_connection_id = self.vcs_connection_id

        vcs_type = self.vcs_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_id is not UNSET:
            field_dict["app_id"] = app_id
        if branch is not UNSET:
            field_dict["branch"] = branch
        if connected_github_vcs_config is not UNSET:
            field_dict["connected_github_vcs_config"] = connected_github_vcs_config
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if directory is not UNSET:
            field_dict["directory"] = directory
        if id is not UNSET:
            field_dict["id"] = id
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if public_git_vcs_config is not UNSET:
            field_dict["public_git_vcs_config"] = public_git_vcs_config
        if repo is not UNSET:
            field_dict["repo"] = repo
        if source is not UNSET:
            field_dict["source"] = source
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if vcs_connection_id is not UNSET:
            field_dict["vcs_connection_id"] = vcs_connection_id
        if vcs_type is not UNSET:
            field_dict["vcs_type"] = vcs_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_connected_github_vcs_config import AppConnectedGithubVCSConfig
        from ..models.app_public_git_vcs_config import AppPublicGitVCSConfig

        d = dict(src_dict)
        app_id = d.pop("app_id", UNSET)

        branch = d.pop("branch", UNSET)

        _connected_github_vcs_config = d.pop("connected_github_vcs_config", UNSET)
        connected_github_vcs_config: AppConnectedGithubVCSConfig | Unset
        if isinstance(_connected_github_vcs_config, Unset):
            connected_github_vcs_config = UNSET
        else:
            connected_github_vcs_config = AppConnectedGithubVCSConfig.from_dict(_connected_github_vcs_config)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        directory = d.pop("directory", UNSET)

        id = d.pop("id", UNSET)

        org_id = d.pop("org_id", UNSET)

        _public_git_vcs_config = d.pop("public_git_vcs_config", UNSET)
        public_git_vcs_config: AppPublicGitVCSConfig | Unset
        if isinstance(_public_git_vcs_config, Unset):
            public_git_vcs_config = UNSET
        else:
            public_git_vcs_config = AppPublicGitVCSConfig.from_dict(_public_git_vcs_config)

        repo = d.pop("repo", UNSET)

        source = d.pop("source", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        vcs_connection_id = d.pop("vcs_connection_id", UNSET)

        vcs_type = d.pop("vcs_type", UNSET)

        app_app_installs_config = cls(
            app_id=app_id,
            branch=branch,
            connected_github_vcs_config=connected_github_vcs_config,
            created_at=created_at,
            created_by_id=created_by_id,
            directory=directory,
            id=id,
            org_id=org_id,
            public_git_vcs_config=public_git_vcs_config,
            repo=repo,
            source=source,
            updated_at=updated_at,
            vcs_connection_id=vcs_connection_id,
            vcs_type=vcs_type,
        )

        app_app_installs_config.additional_properties = d
        return app_app_installs_config

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
