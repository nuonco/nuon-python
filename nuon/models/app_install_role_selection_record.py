from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppInstallRoleSelectionRecord")


@_attrs_define
class AppInstallRoleSelectionRecord:
    """
    Attributes:
        available (bool | Unset):
        role_id (str | Unset):
        role_name (str | Unset):
        role_source (str | Unset):
        selected (bool | Unset):
    """

    available: bool | Unset = UNSET
    role_id: str | Unset = UNSET
    role_name: str | Unset = UNSET
    role_source: str | Unset = UNSET
    selected: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        available = self.available

        role_id = self.role_id

        role_name = self.role_name

        role_source = self.role_source

        selected = self.selected

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if available is not UNSET:
            field_dict["available"] = available
        if role_id is not UNSET:
            field_dict["role_id"] = role_id
        if role_name is not UNSET:
            field_dict["role_name"] = role_name
        if role_source is not UNSET:
            field_dict["role_source"] = role_source
        if selected is not UNSET:
            field_dict["selected"] = selected

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        available = d.pop("available", UNSET)

        role_id = d.pop("role_id", UNSET)

        role_name = d.pop("role_name", UNSET)

        role_source = d.pop("role_source", UNSET)

        selected = d.pop("selected", UNSET)

        app_install_role_selection_record = cls(
            available=available,
            role_id=role_id,
            role_name=role_name,
            role_source=role_source,
            selected=selected,
        )

        app_install_role_selection_record.additional_properties = d
        return app_install_role_selection_record

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
