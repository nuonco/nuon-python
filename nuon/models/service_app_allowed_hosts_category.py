from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceAppAllowedHostsCategory")


@_attrs_define
class ServiceAppAllowedHostsCategory:
    """
    Attributes:
        entries (list[str] | Unset):
        restricted (bool | Unset):
    """

    entries: list[str] | Unset = UNSET
    restricted: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entries: list[str] | Unset = UNSET
        if not isinstance(self.entries, Unset):
            entries = self.entries

        restricted = self.restricted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entries is not UNSET:
            field_dict["entries"] = entries
        if restricted is not UNSET:
            field_dict["restricted"] = restricted

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        entries = cast(list[str], d.pop("entries", UNSET))

        restricted = d.pop("restricted", UNSET)

        service_app_allowed_hosts_category = cls(
            entries=entries,
            restricted=restricted,
        )

        service_app_allowed_hosts_category.additional_properties = d
        return service_app_allowed_hosts_category

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
