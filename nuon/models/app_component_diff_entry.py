from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppComponentDiffEntry")


@_attrs_define
class AppComponentDiffEntry:
    """
    Attributes:
        build_changed (bool | Unset):
        component_id (str | Unset):
        component_name (str | Unset):
        component_type (str | Unset):
        new_build_id (str | Unset):
        new_checksum (str | Unset):
        old_build_id (str | Unset):
        old_checksum (str | Unset):
    """

    build_changed: bool | Unset = UNSET
    component_id: str | Unset = UNSET
    component_name: str | Unset = UNSET
    component_type: str | Unset = UNSET
    new_build_id: str | Unset = UNSET
    new_checksum: str | Unset = UNSET
    old_build_id: str | Unset = UNSET
    old_checksum: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        build_changed = self.build_changed

        component_id = self.component_id

        component_name = self.component_name

        component_type = self.component_type

        new_build_id = self.new_build_id

        new_checksum = self.new_checksum

        old_build_id = self.old_build_id

        old_checksum = self.old_checksum

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if build_changed is not UNSET:
            field_dict["build_changed"] = build_changed
        if component_id is not UNSET:
            field_dict["component_id"] = component_id
        if component_name is not UNSET:
            field_dict["component_name"] = component_name
        if component_type is not UNSET:
            field_dict["component_type"] = component_type
        if new_build_id is not UNSET:
            field_dict["new_build_id"] = new_build_id
        if new_checksum is not UNSET:
            field_dict["new_checksum"] = new_checksum
        if old_build_id is not UNSET:
            field_dict["old_build_id"] = old_build_id
        if old_checksum is not UNSET:
            field_dict["old_checksum"] = old_checksum

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        build_changed = d.pop("build_changed", UNSET)

        component_id = d.pop("component_id", UNSET)

        component_name = d.pop("component_name", UNSET)

        component_type = d.pop("component_type", UNSET)

        new_build_id = d.pop("new_build_id", UNSET)

        new_checksum = d.pop("new_checksum", UNSET)

        old_build_id = d.pop("old_build_id", UNSET)

        old_checksum = d.pop("old_checksum", UNSET)

        app_component_diff_entry = cls(
            build_changed=build_changed,
            component_id=component_id,
            component_name=component_name,
            component_type=component_type,
            new_build_id=new_build_id,
            new_checksum=new_checksum,
            old_build_id=old_build_id,
            old_checksum=old_checksum,
        )

        app_component_diff_entry.additional_properties = d
        return app_component_diff_entry

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
