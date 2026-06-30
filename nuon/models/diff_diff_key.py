from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.diff_op import DiffOp
from ..types import UNSET, Unset

T = TypeVar("T", bound="DiffDiffKey")


@_attrs_define
class DiffDiffKey:
    """
    Attributes:
        after (str | Unset):
        before (str | Unset):
        diff (str | Unset):
        op (DiffOp | Unset):
    """

    after: str | Unset = UNSET
    before: str | Unset = UNSET
    diff: str | Unset = UNSET
    op: DiffOp | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        after = self.after

        before = self.before

        diff = self.diff

        op: str | Unset = UNSET
        if not isinstance(self.op, Unset):
            op = self.op.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if after is not UNSET:
            field_dict["after"] = after
        if before is not UNSET:
            field_dict["before"] = before
        if diff is not UNSET:
            field_dict["diff"] = diff
        if op is not UNSET:
            field_dict["op"] = op

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        after = d.pop("after", UNSET)

        before = d.pop("before", UNSET)

        diff = d.pop("diff", UNSET)

        _op = d.pop("op", UNSET)
        op: DiffOp | Unset
        if isinstance(_op, Unset):
            op = UNSET
        else:
            op = DiffOp(_op)

        diff_diff_key = cls(
            after=after,
            before=before,
            diff=diff,
            op=op,
        )

        diff_diff_key.additional_properties = d
        return diff_diff_key

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
