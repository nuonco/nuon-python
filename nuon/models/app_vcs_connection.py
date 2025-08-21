from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_vcs_connection_commit import AppVCSConnectionCommit


T = TypeVar("T", bound="AppVCSConnection")


@_attrs_define
class AppVCSConnection:
    """
    Attributes:
        created_at (Union[Unset, str]):
        created_by_id (Union[Unset, str]):
        github_install_id (Union[Unset, str]):
        id (Union[Unset, str]):
        updated_at (Union[Unset, str]):
        vcs_connection_commit (Union[Unset, list['AppVCSConnectionCommit']]):
    """

    created_at: Union[Unset, str] = UNSET
    created_by_id: Union[Unset, str] = UNSET
    github_install_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    vcs_connection_commit: Union[Unset, list["AppVCSConnectionCommit"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        created_by_id = self.created_by_id

        github_install_id = self.github_install_id

        id = self.id

        updated_at = self.updated_at

        vcs_connection_commit: Union[Unset, list[dict[str, Any]]] = UNSET
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
        if github_install_id is not UNSET:
            field_dict["github_install_id"] = github_install_id
        if id is not UNSET:
            field_dict["id"] = id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if vcs_connection_commit is not UNSET:
            field_dict["vcs_connection_commit"] = vcs_connection_commit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_vcs_connection_commit import AppVCSConnectionCommit

        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        github_install_id = d.pop("github_install_id", UNSET)

        id = d.pop("id", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        vcs_connection_commit = []
        _vcs_connection_commit = d.pop("vcs_connection_commit", UNSET)
        for vcs_connection_commit_item_data in _vcs_connection_commit or []:
            vcs_connection_commit_item = AppVCSConnectionCommit.from_dict(vcs_connection_commit_item_data)

            vcs_connection_commit.append(vcs_connection_commit_item)

        app_vcs_connection = cls(
            created_at=created_at,
            created_by_id=created_by_id,
            github_install_id=github_install_id,
            id=id,
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
