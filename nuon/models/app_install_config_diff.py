from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_component_diff_entry import AppComponentDiffEntry


T = TypeVar("T", bound="AppInstallConfigDiff")


@_attrs_define
class AppInstallConfigDiff:
    """
    Attributes:
        added (list[AppComponentDiffEntry] | Unset):
        changed (list[AppComponentDiffEntry] | Unset):
        removed (list[AppComponentDiffEntry] | Unset):
        sandbox_changed (bool | Unset):
        sandbox_new_id (str | Unset):
        sandbox_old_id (str | Unset):
        stack_changed (bool | Unset):
        stack_new_id (str | Unset):
        stack_old_id (str | Unset):
        unchanged (list[AppComponentDiffEntry] | Unset):
    """

    added: list[AppComponentDiffEntry] | Unset = UNSET
    changed: list[AppComponentDiffEntry] | Unset = UNSET
    removed: list[AppComponentDiffEntry] | Unset = UNSET
    sandbox_changed: bool | Unset = UNSET
    sandbox_new_id: str | Unset = UNSET
    sandbox_old_id: str | Unset = UNSET
    stack_changed: bool | Unset = UNSET
    stack_new_id: str | Unset = UNSET
    stack_old_id: str | Unset = UNSET
    unchanged: list[AppComponentDiffEntry] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        added: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.added, Unset):
            added = []
            for added_item_data in self.added:
                added_item = added_item_data.to_dict()
                added.append(added_item)

        changed: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.changed, Unset):
            changed = []
            for changed_item_data in self.changed:
                changed_item = changed_item_data.to_dict()
                changed.append(changed_item)

        removed: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.removed, Unset):
            removed = []
            for removed_item_data in self.removed:
                removed_item = removed_item_data.to_dict()
                removed.append(removed_item)

        sandbox_changed = self.sandbox_changed

        sandbox_new_id = self.sandbox_new_id

        sandbox_old_id = self.sandbox_old_id

        stack_changed = self.stack_changed

        stack_new_id = self.stack_new_id

        stack_old_id = self.stack_old_id

        unchanged: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.unchanged, Unset):
            unchanged = []
            for unchanged_item_data in self.unchanged:
                unchanged_item = unchanged_item_data.to_dict()
                unchanged.append(unchanged_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if added is not UNSET:
            field_dict["added"] = added
        if changed is not UNSET:
            field_dict["changed"] = changed
        if removed is not UNSET:
            field_dict["removed"] = removed
        if sandbox_changed is not UNSET:
            field_dict["sandbox_changed"] = sandbox_changed
        if sandbox_new_id is not UNSET:
            field_dict["sandbox_new_id"] = sandbox_new_id
        if sandbox_old_id is not UNSET:
            field_dict["sandbox_old_id"] = sandbox_old_id
        if stack_changed is not UNSET:
            field_dict["stack_changed"] = stack_changed
        if stack_new_id is not UNSET:
            field_dict["stack_new_id"] = stack_new_id
        if stack_old_id is not UNSET:
            field_dict["stack_old_id"] = stack_old_id
        if unchanged is not UNSET:
            field_dict["unchanged"] = unchanged

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_component_diff_entry import AppComponentDiffEntry

        d = dict(src_dict)
        _added = d.pop("added", UNSET)
        added: list[AppComponentDiffEntry] | Unset = UNSET
        if _added is not UNSET:
            added = []
            for added_item_data in _added:
                added_item = AppComponentDiffEntry.from_dict(added_item_data)

                added.append(added_item)

        _changed = d.pop("changed", UNSET)
        changed: list[AppComponentDiffEntry] | Unset = UNSET
        if _changed is not UNSET:
            changed = []
            for changed_item_data in _changed:
                changed_item = AppComponentDiffEntry.from_dict(changed_item_data)

                changed.append(changed_item)

        _removed = d.pop("removed", UNSET)
        removed: list[AppComponentDiffEntry] | Unset = UNSET
        if _removed is not UNSET:
            removed = []
            for removed_item_data in _removed:
                removed_item = AppComponentDiffEntry.from_dict(removed_item_data)

                removed.append(removed_item)

        sandbox_changed = d.pop("sandbox_changed", UNSET)

        sandbox_new_id = d.pop("sandbox_new_id", UNSET)

        sandbox_old_id = d.pop("sandbox_old_id", UNSET)

        stack_changed = d.pop("stack_changed", UNSET)

        stack_new_id = d.pop("stack_new_id", UNSET)

        stack_old_id = d.pop("stack_old_id", UNSET)

        _unchanged = d.pop("unchanged", UNSET)
        unchanged: list[AppComponentDiffEntry] | Unset = UNSET
        if _unchanged is not UNSET:
            unchanged = []
            for unchanged_item_data in _unchanged:
                unchanged_item = AppComponentDiffEntry.from_dict(unchanged_item_data)

                unchanged.append(unchanged_item)

        app_install_config_diff = cls(
            added=added,
            changed=changed,
            removed=removed,
            sandbox_changed=sandbox_changed,
            sandbox_new_id=sandbox_new_id,
            sandbox_old_id=sandbox_old_id,
            stack_changed=stack_changed,
            stack_new_id=stack_new_id,
            stack_old_id=stack_old_id,
            unchanged=unchanged,
        )

        app_install_config_diff.additional_properties = d
        return app_install_config_diff

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
