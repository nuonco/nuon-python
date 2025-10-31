from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceRunnerConnectionStatus")


@_attrs_define
class ServiceRunnerConnectionStatus:
    """
    Attributes:
        connected (bool | Unset):
        latest_heartbeat_timestamp (int | Unset):
    """

    connected: bool | Unset = UNSET
    latest_heartbeat_timestamp: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connected = self.connected

        latest_heartbeat_timestamp = self.latest_heartbeat_timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if connected is not UNSET:
            field_dict["connected"] = connected
        if latest_heartbeat_timestamp is not UNSET:
            field_dict["latest_heartbeat_timestamp"] = latest_heartbeat_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        connected = d.pop("connected", UNSET)

        latest_heartbeat_timestamp = d.pop("latest_heartbeat_timestamp", UNSET)

        service_runner_connection_status = cls(
            connected=connected,
            latest_heartbeat_timestamp=latest_heartbeat_timestamp,
        )

        service_runner_connection_status.additional_properties = d
        return service_runner_connection_status

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
