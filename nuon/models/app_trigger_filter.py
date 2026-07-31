from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_trigger_filter_type import AppTriggerFilterType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AppTriggerFilter")


@_attrs_define
class AppTriggerFilter:
    """
    Attributes:
        from_ (str | Unset):
        op (AppTriggerFilterType | Unset):
        path (str | Unset):
        value (Any | Unset):
    """

    from_: str | Unset = UNSET
    op: AppTriggerFilterType | Unset = UNSET
    path: str | Unset = UNSET
    value: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_ = self.from_

        op: str | Unset = UNSET
        if not isinstance(self.op, Unset):
            op = self.op.value

        path = self.path

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if from_ is not UNSET:
            field_dict["from"] = from_
        if op is not UNSET:
            field_dict["op"] = op
        if path is not UNSET:
            field_dict["path"] = path
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        from_ = d.pop("from", UNSET)

        _op = d.pop("op", UNSET)
        op: AppTriggerFilterType | Unset
        if isinstance(_op, Unset):
            op = UNSET
        else:
            op = AppTriggerFilterType(_op)

        path = d.pop("path", UNSET)

        value = d.pop("value", UNSET)

        app_trigger_filter = cls(
            from_=from_,
            op=op,
            path=path,
            value=value,
        )

        app_trigger_filter.additional_properties = d
        return app_trigger_filter

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
