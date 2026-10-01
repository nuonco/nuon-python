from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceUpdateOrgTelemetryRequest")


@_attrs_define
class ServiceUpdateOrgTelemetryRequest:
    """
    Attributes:
        enabled (bool | None | Unset):
        relay_endpoint (None | str | Unset):
    """

    enabled: bool | None | Unset = UNSET
    relay_endpoint: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled: bool | None | Unset
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

        relay_endpoint: None | str | Unset
        if isinstance(self.relay_endpoint, Unset):
            relay_endpoint = UNSET
        else:
            relay_endpoint = self.relay_endpoint

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if relay_endpoint is not UNSET:
            field_dict["relay_endpoint"] = relay_endpoint

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))

        def _parse_relay_endpoint(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        relay_endpoint = _parse_relay_endpoint(d.pop("relay_endpoint", UNSET))

        service_update_org_telemetry_request = cls(
            enabled=enabled,
            relay_endpoint=relay_endpoint,
        )

        service_update_org_telemetry_request.additional_properties = d
        return service_update_org_telemetry_request

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
