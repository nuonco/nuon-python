from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.refs_ref_type import RefsRefType
from ..types import UNSET, Unset

T = TypeVar("T", bound="RefsRef")


@_attrs_define
class RefsRef:
    """
    Attributes:
        input_ (str | Unset):
        name (str | Unset):
        type_ (RefsRefType | Unset):
        value (str | Unset):
    """

    input_: str | Unset = UNSET
    name: str | Unset = UNSET
    type_: RefsRefType | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        input_ = self.input_

        name = self.name

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if input_ is not UNSET:
            field_dict["input"] = input_
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        input_ = d.pop("input", UNSET)

        name = d.pop("name", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: RefsRefType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RefsRefType(_type_)

        value = d.pop("value", UNSET)

        refs_ref = cls(
            input_=input_,
            name=name,
            type_=type_,
            value=value,
        )

        refs_ref.additional_properties = d
        return refs_ref

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
