from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceInstallTelemetrySettings")


@_attrs_define
class ServiceInstallTelemetrySettings:
    """
    Attributes:
        enabled (bool | Unset):
        org_default (bool | Unset):
        override (bool | None | Unset):
        relay_configured (bool | Unset):
    """

    enabled: bool | Unset = UNSET
    org_default: bool | Unset = UNSET
    override: bool | None | Unset = UNSET
    relay_configured: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        org_default = self.org_default

        override: bool | None | Unset
        if isinstance(self.override, Unset):
            override = UNSET
        else:
            override = self.override

        relay_configured = self.relay_configured

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if org_default is not UNSET:
            field_dict["org_default"] = org_default
        if override is not UNSET:
            field_dict["override"] = override
        if relay_configured is not UNSET:
            field_dict["relay_configured"] = relay_configured

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        org_default = d.pop("org_default", UNSET)

        def _parse_override(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        override = _parse_override(d.pop("override", UNSET))

        relay_configured = d.pop("relay_configured", UNSET)

        service_install_telemetry_settings = cls(
            enabled=enabled,
            org_default=org_default,
            override=override,
            relay_configured=relay_configured,
        )

        service_install_telemetry_settings.additional_properties = d
        return service_install_telemetry_settings

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
