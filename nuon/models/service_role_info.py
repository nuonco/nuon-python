from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_role_type import AppRoleType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceRoleInfo")


@_attrs_define
class ServiceRoleInfo:
    """
    Attributes:
        applies_to (list[str] | Unset):
        description (str | Unset):
        role_type (AppRoleType | Unset):
        title (str | Unset):
    """

    applies_to: list[str] | Unset = UNSET
    description: str | Unset = UNSET
    role_type: AppRoleType | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        applies_to: list[str] | Unset = UNSET
        if not isinstance(self.applies_to, Unset):
            applies_to = self.applies_to

        description = self.description

        role_type: str | Unset = UNSET
        if not isinstance(self.role_type, Unset):
            role_type = self.role_type.value

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if applies_to is not UNSET:
            field_dict["applies_to"] = applies_to
        if description is not UNSET:
            field_dict["description"] = description
        if role_type is not UNSET:
            field_dict["role_type"] = role_type
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        applies_to = cast(list[str], d.pop("applies_to", UNSET))

        description = d.pop("description", UNSET)

        _role_type = d.pop("role_type", UNSET)
        role_type: AppRoleType | Unset
        if isinstance(_role_type, Unset):
            role_type = UNSET
        else:
            role_type = AppRoleType(_role_type)

        title = d.pop("title", UNSET)

        service_role_info = cls(
            applies_to=applies_to,
            description=description,
            role_type=role_type,
            title=title,
        )

        service_role_info.additional_properties = d
        return service_role_info

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
