from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceAvailableRole")


@_attrs_define
class ServiceAvailableRole:
    """
    Attributes:
        arn (str | Unset):
        name (str | Unset):
        role_type (str | Unset):
    """

    arn: str | Unset = UNSET
    name: str | Unset = UNSET
    role_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        arn = self.arn

        name = self.name

        role_type = self.role_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if arn is not UNSET:
            field_dict["arn"] = arn
        if name is not UNSET:
            field_dict["name"] = name
        if role_type is not UNSET:
            field_dict["role_type"] = role_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        arn = d.pop("arn", UNSET)

        name = d.pop("name", UNSET)

        role_type = d.pop("role_type", UNSET)

        service_available_role = cls(
            arn=arn,
            name=name,
            role_type=role_type,
        )

        service_available_role.additional_properties = d
        return service_available_role

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
