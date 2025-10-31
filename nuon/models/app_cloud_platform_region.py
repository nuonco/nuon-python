from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppCloudPlatformRegion")


@_attrs_define
class AppCloudPlatformRegion:
    """
    Attributes:
        display_name (str | Unset):
        icon (str | Unset):
        name (str | Unset):
        value (str | Unset):
    """

    display_name: str | Unset = UNSET
    icon: str | Unset = UNSET
    name: str | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        icon = self.icon

        name = self.name

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if icon is not UNSET:
            field_dict["icon"] = icon
        if name is not UNSET:
            field_dict["name"] = name
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        display_name = d.pop("display_name", UNSET)

        icon = d.pop("icon", UNSET)

        name = d.pop("name", UNSET)

        value = d.pop("value", UNSET)

        app_cloud_platform_region = cls(
            display_name=display_name,
            icon=icon,
            name=name,
            value=value,
        )

        app_cloud_platform_region.additional_properties = d
        return app_cloud_platform_region

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
