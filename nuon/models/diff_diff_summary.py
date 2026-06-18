from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DiffDiffSummary")


@_attrs_define
class DiffDiffSummary:
    """
    Attributes:
        added (int | Unset):
        changed (int | Unset):
        has_changed (bool | Unset):
        removed (int | Unset):
        unchanged (int | Unset):
    """

    added: int | Unset = UNSET
    changed: int | Unset = UNSET
    has_changed: bool | Unset = UNSET
    removed: int | Unset = UNSET
    unchanged: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        added = self.added

        changed = self.changed

        has_changed = self.has_changed

        removed = self.removed

        unchanged = self.unchanged

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if added is not UNSET:
            field_dict["added"] = added
        if changed is not UNSET:
            field_dict["changed"] = changed
        if has_changed is not UNSET:
            field_dict["has_changed"] = has_changed
        if removed is not UNSET:
            field_dict["removed"] = removed
        if unchanged is not UNSET:
            field_dict["unchanged"] = unchanged

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        added = d.pop("added", UNSET)

        changed = d.pop("changed", UNSET)

        has_changed = d.pop("has_changed", UNSET)

        removed = d.pop("removed", UNSET)

        unchanged = d.pop("unchanged", UNSET)

        diff_diff_summary = cls(
            added=added,
            changed=changed,
            has_changed=has_changed,
            removed=removed,
            unchanged=unchanged,
        )

        diff_diff_summary.additional_properties = d
        return diff_diff_summary

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
