from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceComponentTeardownRequest")


@_attrs_define
class ServiceComponentTeardownRequest:
    """
    Attributes:
        retain (list[str] | Unset): Resource or module addresses removed from state instead of destroyed on teardown.
    """

    retain: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        retain: list[str] | Unset = UNSET
        if not isinstance(self.retain, Unset):
            retain = self.retain

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if retain is not UNSET:
            field_dict["retain"] = retain

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        retain = cast(list[str], d.pop("retain", UNSET))

        service_component_teardown_request = cls(
            retain=retain,
        )

        service_component_teardown_request.additional_properties = d
        return service_component_teardown_request

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
