from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_vcs_connection import AppVCSConnection


T = TypeVar("T", bound="AppConnectedGithubVCSConfig")


@_attrs_define
class AppConnectedGithubVCSConfig:
    """
    Attributes:
        branch (str | Unset):
        component_config_id (str | Unset): parent component
        component_config_type (str | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        directory (str | Unset):
        id (str | Unset):
        repo (str | Unset):
        repo_name (str | Unset):
        repo_owner (str | Unset):
        updated_at (str | Unset):
        vcs_connection (AppVCSConnection | Unset):
        vcs_connection_id (str | Unset):
    """

    branch: str | Unset = UNSET
    component_config_id: str | Unset = UNSET
    component_config_type: str | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    directory: str | Unset = UNSET
    id: str | Unset = UNSET
    repo: str | Unset = UNSET
    repo_name: str | Unset = UNSET
    repo_owner: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    vcs_connection: AppVCSConnection | Unset = UNSET
    vcs_connection_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        branch = self.branch

        component_config_id = self.component_config_id

        component_config_type = self.component_config_type

        created_at = self.created_at

        created_by_id = self.created_by_id

        directory = self.directory

        id = self.id

        repo = self.repo

        repo_name = self.repo_name

        repo_owner = self.repo_owner

        updated_at = self.updated_at

        vcs_connection: dict[str, Any] | Unset = UNSET
        if not isinstance(self.vcs_connection, Unset):
            vcs_connection = self.vcs_connection.to_dict()

        vcs_connection_id = self.vcs_connection_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if branch is not UNSET:
            field_dict["branch"] = branch
        if component_config_id is not UNSET:
            field_dict["component_config_id"] = component_config_id
        if component_config_type is not UNSET:
            field_dict["component_config_type"] = component_config_type
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if directory is not UNSET:
            field_dict["directory"] = directory
        if id is not UNSET:
            field_dict["id"] = id
        if repo is not UNSET:
            field_dict["repo"] = repo
        if repo_name is not UNSET:
            field_dict["repo_name"] = repo_name
        if repo_owner is not UNSET:
            field_dict["repo_owner"] = repo_owner
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if vcs_connection is not UNSET:
            field_dict["vcs_connection"] = vcs_connection
        if vcs_connection_id is not UNSET:
            field_dict["vcs_connection_id"] = vcs_connection_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_vcs_connection import AppVCSConnection

        d = dict(src_dict)
        branch = d.pop("branch", UNSET)

        component_config_id = d.pop("component_config_id", UNSET)

        component_config_type = d.pop("component_config_type", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        directory = d.pop("directory", UNSET)

        id = d.pop("id", UNSET)

        repo = d.pop("repo", UNSET)

        repo_name = d.pop("repo_name", UNSET)

        repo_owner = d.pop("repo_owner", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        _vcs_connection = d.pop("vcs_connection", UNSET)
        vcs_connection: AppVCSConnection | Unset
        if isinstance(_vcs_connection, Unset):
            vcs_connection = UNSET
        else:
            vcs_connection = AppVCSConnection.from_dict(_vcs_connection)

        vcs_connection_id = d.pop("vcs_connection_id", UNSET)

        app_connected_github_vcs_config = cls(
            branch=branch,
            component_config_id=component_config_id,
            component_config_type=component_config_type,
            created_at=created_at,
            created_by_id=created_by_id,
            directory=directory,
            id=id,
            repo=repo,
            repo_name=repo_name,
            repo_owner=repo_owner,
            updated_at=updated_at,
            vcs_connection=vcs_connection,
            vcs_connection_id=vcs_connection_id,
        )

        app_connected_github_vcs_config.additional_properties = d
        return app_connected_github_vcs_config

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
