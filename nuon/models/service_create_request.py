from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_cloud_connection_preset import AppCloudConnectionPreset
from ..models.service_create_request_platform import ServiceCreateRequestPlatform
from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceCreateRequest")


@_attrs_define
class ServiceCreateRequest:
    """
    Attributes:
        default_region (str | Unset):
        name (str | Unset):
        platform (ServiceCreateRequestPlatform | Unset):
        preset (AppCloudConnectionPreset | Unset):
        principal (str | Unset):
        target_id (str | Unset):
    """

    default_region: str | Unset = UNSET
    name: str | Unset = UNSET
    platform: ServiceCreateRequestPlatform | Unset = UNSET
    preset: AppCloudConnectionPreset | Unset = UNSET
    principal: str | Unset = UNSET
    target_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default_region = self.default_region

        name = self.name

        platform: str | Unset = UNSET
        if not isinstance(self.platform, Unset):
            platform = self.platform.value

        preset: str | Unset = UNSET
        if not isinstance(self.preset, Unset):
            preset = self.preset.value

        principal = self.principal

        target_id = self.target_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_region is not UNSET:
            field_dict["default_region"] = default_region
        if name is not UNSET:
            field_dict["name"] = name
        if platform is not UNSET:
            field_dict["platform"] = platform
        if preset is not UNSET:
            field_dict["preset"] = preset
        if principal is not UNSET:
            field_dict["principal"] = principal
        if target_id is not UNSET:
            field_dict["target_id"] = target_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        default_region = d.pop("default_region", UNSET)

        name = d.pop("name", UNSET)

        _platform = d.pop("platform", UNSET)
        platform: ServiceCreateRequestPlatform | Unset
        if isinstance(_platform, Unset):
            platform = UNSET
        else:
            platform = ServiceCreateRequestPlatform(_platform)

        _preset = d.pop("preset", UNSET)
        preset: AppCloudConnectionPreset | Unset
        if isinstance(_preset, Unset):
            preset = UNSET
        else:
            preset = AppCloudConnectionPreset(_preset)

        principal = d.pop("principal", UNSET)

        target_id = d.pop("target_id", UNSET)

        service_create_request = cls(
            default_region=default_region,
            name=name,
            platform=platform,
            preset=preset,
            principal=principal,
            target_id=target_id,
        )

        service_create_request.additional_properties = d
        return service_create_request

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
