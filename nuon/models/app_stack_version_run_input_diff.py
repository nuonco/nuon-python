from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppStackVersionRunInputDiff")


@_attrs_define
class AppStackVersionRunInputDiff:
    """
    Attributes:
        added (list[str] | Unset):
        changed (list[str] | Unset):
        removed (list[str] | Unset):
    """

    added: list[str] | Unset = UNSET
    changed: list[str] | Unset = UNSET
    removed: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        added: list[str] | Unset = UNSET
        if not isinstance(self.added, Unset):
            added = self.added

        changed: list[str] | Unset = UNSET
        if not isinstance(self.changed, Unset):
            changed = self.changed

        removed: list[str] | Unset = UNSET
        if not isinstance(self.removed, Unset):
            removed = self.removed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if added is not UNSET:
            field_dict["added"] = added
        if changed is not UNSET:
            field_dict["changed"] = changed
        if removed is not UNSET:
            field_dict["removed"] = removed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        added = cast(list[str], d.pop("added", UNSET))

        changed = cast(list[str], d.pop("changed", UNSET))

        removed = cast(list[str], d.pop("removed", UNSET))

        app_stack_version_run_input_diff = cls(
            added=added,
            changed=changed,
            removed=removed,
        )

        app_stack_version_run_input_diff.additional_properties = d
        return app_stack_version_run_input_diff

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
