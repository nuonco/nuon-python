from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceVCSConnectionRepo")


@_attrs_define
class ServiceVCSConnectionRepo:
    """
    Attributes:
        default_branch (str | Unset):
        description (str | Unset):
        fork (bool | Unset):
        full_name (str | Unset):
        html_url (str | Unset):
        id (int | Unset):
        name (str | Unset):
        private (bool | Unset):
        updated_at (str | Unset):
    """

    default_branch: str | Unset = UNSET
    description: str | Unset = UNSET
    fork: bool | Unset = UNSET
    full_name: str | Unset = UNSET
    html_url: str | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    private: bool | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default_branch = self.default_branch

        description = self.description

        fork = self.fork

        full_name = self.full_name

        html_url = self.html_url

        id = self.id

        name = self.name

        private = self.private

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_branch is not UNSET:
            field_dict["default_branch"] = default_branch
        if description is not UNSET:
            field_dict["description"] = description
        if fork is not UNSET:
            field_dict["fork"] = fork
        if full_name is not UNSET:
            field_dict["full_name"] = full_name
        if html_url is not UNSET:
            field_dict["html_url"] = html_url
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if private is not UNSET:
            field_dict["private"] = private
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        default_branch = d.pop("default_branch", UNSET)

        description = d.pop("description", UNSET)

        fork = d.pop("fork", UNSET)

        full_name = d.pop("full_name", UNSET)

        html_url = d.pop("html_url", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        private = d.pop("private", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        service_vcs_connection_repo = cls(
            default_branch=default_branch,
            description=description,
            fork=fork,
            full_name=full_name,
            html_url=html_url,
            id=id,
            name=name,
            private=private,
            updated_at=updated_at,
        )

        service_vcs_connection_repo.additional_properties = d
        return service_vcs_connection_repo

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
