from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceAppFleetSummary")


@_attrs_define
class ServiceAppFleetSummary:
    """
    Attributes:
        applied (int | Unset):
        behind (int | Unset):
        matched (int | Unset):
        runner_not_active (int | Unset):
        total (int | Unset):
        unknown (int | Unset):
    """

    applied: int | Unset = UNSET
    behind: int | Unset = UNSET
    matched: int | Unset = UNSET
    runner_not_active: int | Unset = UNSET
    total: int | Unset = UNSET
    unknown: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        applied = self.applied

        behind = self.behind

        matched = self.matched

        runner_not_active = self.runner_not_active

        total = self.total

        unknown = self.unknown

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if applied is not UNSET:
            field_dict["applied"] = applied
        if behind is not UNSET:
            field_dict["behind"] = behind
        if matched is not UNSET:
            field_dict["matched"] = matched
        if runner_not_active is not UNSET:
            field_dict["runner_not_active"] = runner_not_active
        if total is not UNSET:
            field_dict["total"] = total
        if unknown is not UNSET:
            field_dict["unknown"] = unknown

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        applied = d.pop("applied", UNSET)

        behind = d.pop("behind", UNSET)

        matched = d.pop("matched", UNSET)

        runner_not_active = d.pop("runner_not_active", UNSET)

        total = d.pop("total", UNSET)

        unknown = d.pop("unknown", UNSET)

        service_app_fleet_summary = cls(
            applied=applied,
            behind=behind,
            matched=matched,
            runner_not_active=runner_not_active,
            total=total,
            unknown=unknown,
        )

        service_app_fleet_summary.additional_properties = d
        return service_app_fleet_summary

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
