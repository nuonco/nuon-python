from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.diff_diff_key import DiffDiffKey


T = TypeVar("T", bound="DiffDiff")


@_attrs_define
class DiffDiff:
    """
    Attributes:
        children (list[DiffDiff] | Unset):
        diff (DiffDiffKey | Unset):
        key (str | Unset):
    """

    children: list[DiffDiff] | Unset = UNSET
    diff: DiffDiffKey | Unset = UNSET
    key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        children: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.children, Unset):
            children = []
            for children_item_data in self.children:
                children_item = children_item_data.to_dict()
                children.append(children_item)

        diff: dict[str, Any] | Unset = UNSET
        if not isinstance(self.diff, Unset):
            diff = self.diff.to_dict()

        key = self.key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if children is not UNSET:
            field_dict["children"] = children
        if diff is not UNSET:
            field_dict["diff"] = diff
        if key is not UNSET:
            field_dict["key"] = key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.diff_diff_key import DiffDiffKey

        d = dict(src_dict)
        _children = d.pop("children", UNSET)
        children: list[DiffDiff] | Unset = UNSET
        if _children is not UNSET:
            children = []
            for children_item_data in _children:
                children_item = DiffDiff.from_dict(children_item_data)

                children.append(children_item)

        _diff = d.pop("diff", UNSET)
        diff: DiffDiffKey | Unset
        if isinstance(_diff, Unset):
            diff = UNSET
        else:
            diff = DiffDiffKey.from_dict(_diff)

        key = d.pop("key", UNSET)

        diff_diff = cls(
            children=children,
            diff=diff,
            key=key,
        )

        diff_diff.additional_properties = d
        return diff_diff

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
