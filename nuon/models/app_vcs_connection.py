from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_composite_status import AppCompositeStatus
    from ..models.app_queue import AppQueue
    from ..models.app_vcs_connection_commit import AppVCSConnectionCommit


T = TypeVar("T", bound="AppVCSConnection")


@_attrs_define
class AppVCSConnection:
    """
    Attributes:
        created_at (str | Unset):
        created_by_id (str | Unset):
        github_account_id (str | Unset):
        github_account_name (str | Unset):
        github_install_id (str | Unset):
        id (str | Unset):
        queues (list[AppQueue] | Unset):
        status (AppCompositeStatus | Unset):
        updated_at (str | Unset):
        vcs_connection_commit (list[AppVCSConnectionCommit] | Unset):
    """

    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    github_account_id: str | Unset = UNSET
    github_account_name: str | Unset = UNSET
    github_install_id: str | Unset = UNSET
    id: str | Unset = UNSET
    queues: list[AppQueue] | Unset = UNSET
    status: AppCompositeStatus | Unset = UNSET
    updated_at: str | Unset = UNSET
    vcs_connection_commit: list[AppVCSConnectionCommit] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        created_by_id = self.created_by_id

        github_account_id = self.github_account_id

        github_account_name = self.github_account_name

        github_install_id = self.github_install_id

        id = self.id

        queues: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.queues, Unset):
            queues = []
            for queues_item_data in self.queues:
                queues_item = queues_item_data.to_dict()
                queues.append(queues_item)

        status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        updated_at = self.updated_at

        vcs_connection_commit: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.vcs_connection_commit, Unset):
            vcs_connection_commit = []
            for vcs_connection_commit_item_data in self.vcs_connection_commit:
                vcs_connection_commit_item = vcs_connection_commit_item_data.to_dict()
                vcs_connection_commit.append(vcs_connection_commit_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if github_account_id is not UNSET:
            field_dict["github_account_id"] = github_account_id
        if github_account_name is not UNSET:
            field_dict["github_account_name"] = github_account_name
        if github_install_id is not UNSET:
            field_dict["github_install_id"] = github_install_id
        if id is not UNSET:
            field_dict["id"] = id
        if queues is not UNSET:
            field_dict["queues"] = queues
        if status is not UNSET:
            field_dict["status"] = status
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if vcs_connection_commit is not UNSET:
            field_dict["vcs_connection_commit"] = vcs_connection_commit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_composite_status import AppCompositeStatus
        from ..models.app_queue import AppQueue
        from ..models.app_vcs_connection_commit import AppVCSConnectionCommit

        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        github_account_id = d.pop("github_account_id", UNSET)

        github_account_name = d.pop("github_account_name", UNSET)

        github_install_id = d.pop("github_install_id", UNSET)

        id = d.pop("id", UNSET)

        _queues = d.pop("queues", UNSET)
        queues: list[AppQueue] | Unset = UNSET
        if _queues is not UNSET:
            queues = []
            for queues_item_data in _queues:
                queues_item = AppQueue.from_dict(queues_item_data)

                queues.append(queues_item)

        _status = d.pop("status", UNSET)
        status: AppCompositeStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AppCompositeStatus.from_dict(_status)

        updated_at = d.pop("updated_at", UNSET)

        _vcs_connection_commit = d.pop("vcs_connection_commit", UNSET)
        vcs_connection_commit: list[AppVCSConnectionCommit] | Unset = UNSET
        if _vcs_connection_commit is not UNSET:
            vcs_connection_commit = []
            for vcs_connection_commit_item_data in _vcs_connection_commit:
                vcs_connection_commit_item = AppVCSConnectionCommit.from_dict(vcs_connection_commit_item_data)

                vcs_connection_commit.append(vcs_connection_commit_item)

        app_vcs_connection = cls(
            created_at=created_at,
            created_by_id=created_by_id,
            github_account_id=github_account_id,
            github_account_name=github_account_name,
            github_install_id=github_install_id,
            id=id,
            queues=queues,
            status=status,
            updated_at=updated_at,
            vcs_connection_commit=vcs_connection_commit,
        )

        app_vcs_connection.additional_properties = d
        return app_vcs_connection

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
