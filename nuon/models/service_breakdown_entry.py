from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceBreakdownEntry")


@_attrs_define
class ServiceBreakdownEntry:
    """
    Attributes:
        denies (int | Unset):
        evaluations (int | Unset):
        key (str | Unset):
        passes (int | Unset):
        warns (int | Unset):
    """

    denies: int | Unset = UNSET
    evaluations: int | Unset = UNSET
    key: str | Unset = UNSET
    passes: int | Unset = UNSET
    warns: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        denies = self.denies

        evaluations = self.evaluations

        key = self.key

        passes = self.passes

        warns = self.warns

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if denies is not UNSET:
            field_dict["denies"] = denies
        if evaluations is not UNSET:
            field_dict["evaluations"] = evaluations
        if key is not UNSET:
            field_dict["key"] = key
        if passes is not UNSET:
            field_dict["passes"] = passes
        if warns is not UNSET:
            field_dict["warns"] = warns

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        denies = d.pop("denies", UNSET)

        evaluations = d.pop("evaluations", UNSET)

        key = d.pop("key", UNSET)

        passes = d.pop("passes", UNSET)

        warns = d.pop("warns", UNSET)

        service_breakdown_entry = cls(
            denies=denies,
            evaluations=evaluations,
            key=key,
            passes=passes,
            warns=warns,
        )

        service_breakdown_entry.additional_properties = d
        return service_breakdown_entry

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
