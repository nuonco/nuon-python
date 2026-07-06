from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceAppLabelKeySummary")


@_attrs_define
class ServiceAppLabelKeySummary:
    """
    Attributes:
        color (str | Unset):
        default_color (str | Unset):
        entity_types (list[str] | Unset):
        is_override (bool | Unset):
        key (str | Unset):
        usage_count (int | Unset):
        values (list[str] | Unset):
    """

    color: str | Unset = UNSET
    default_color: str | Unset = UNSET
    entity_types: list[str] | Unset = UNSET
    is_override: bool | Unset = UNSET
    key: str | Unset = UNSET
    usage_count: int | Unset = UNSET
    values: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        color = self.color

        default_color = self.default_color

        entity_types: list[str] | Unset = UNSET
        if not isinstance(self.entity_types, Unset):
            entity_types = self.entity_types

        is_override = self.is_override

        key = self.key

        usage_count = self.usage_count

        values: list[str] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = self.values

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if color is not UNSET:
            field_dict["color"] = color
        if default_color is not UNSET:
            field_dict["default_color"] = default_color
        if entity_types is not UNSET:
            field_dict["entity_types"] = entity_types
        if is_override is not UNSET:
            field_dict["is_override"] = is_override
        if key is not UNSET:
            field_dict["key"] = key
        if usage_count is not UNSET:
            field_dict["usage_count"] = usage_count
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        color = d.pop("color", UNSET)

        default_color = d.pop("default_color", UNSET)

        entity_types = cast(list[str], d.pop("entity_types", UNSET))

        is_override = d.pop("is_override", UNSET)

        key = d.pop("key", UNSET)

        usage_count = d.pop("usage_count", UNSET)

        values = cast(list[str], d.pop("values", UNSET))

        service_app_label_key_summary = cls(
            color=color,
            default_color=default_color,
            entity_types=entity_types,
            is_override=is_override,
            key=key,
            usage_count=usage_count,
            values=values,
        )

        service_app_label_key_summary.additional_properties = d
        return service_app_label_key_summary

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
