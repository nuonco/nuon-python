from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppVCSConnectionCommit")


@_attrs_define
class AppVCSConnectionCommit:
    """
    Attributes:
        author_email (str | Unset):
        author_name (str | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        id (str | Unset):
        message (str | Unset):
        sha (str | Unset):
        updated_at (str | Unset):
        vcs_connection_id (str | Unset):
    """

    author_email: str | Unset = UNSET
    author_name: str | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    id: str | Unset = UNSET
    message: str | Unset = UNSET
    sha: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    vcs_connection_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        author_email = self.author_email

        author_name = self.author_name

        created_at = self.created_at

        created_by_id = self.created_by_id

        id = self.id

        message = self.message

        sha = self.sha

        updated_at = self.updated_at

        vcs_connection_id = self.vcs_connection_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if author_email is not UNSET:
            field_dict["author_email"] = author_email
        if author_name is not UNSET:
            field_dict["author_name"] = author_name
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if id is not UNSET:
            field_dict["id"] = id
        if message is not UNSET:
            field_dict["message"] = message
        if sha is not UNSET:
            field_dict["sha"] = sha
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if vcs_connection_id is not UNSET:
            field_dict["vcs_connection_id"] = vcs_connection_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        author_email = d.pop("author_email", UNSET)

        author_name = d.pop("author_name", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        id = d.pop("id", UNSET)

        message = d.pop("message", UNSET)

        sha = d.pop("sha", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        vcs_connection_id = d.pop("vcs_connection_id", UNSET)

        app_vcs_connection_commit = cls(
            author_email=author_email,
            author_name=author_name,
            created_at=created_at,
            created_by_id=created_by_id,
            id=id,
            message=message,
            sha=sha,
            updated_at=updated_at,
            vcs_connection_id=vcs_connection_id,
        )

        app_vcs_connection_commit.additional_properties = d
        return app_vcs_connection_commit

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
