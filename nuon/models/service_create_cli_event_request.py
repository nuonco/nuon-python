from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceCreateCLIEventRequest")


@_attrs_define
class ServiceCreateCLIEventRequest:
    """
    Attributes:
        cli_version (str):
        command (str):
        agent (str | Unset):
        duration_ms (int | Unset):
        os (str | Unset):
        success (bool | Unset):
    """

    cli_version: str
    command: str
    agent: str | Unset = UNSET
    duration_ms: int | Unset = UNSET
    os: str | Unset = UNSET
    success: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cli_version = self.cli_version

        command = self.command

        agent = self.agent

        duration_ms = self.duration_ms

        os = self.os

        success = self.success

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cli_version": cli_version,
                "command": command,
            }
        )
        if agent is not UNSET:
            field_dict["agent"] = agent
        if duration_ms is not UNSET:
            field_dict["duration_ms"] = duration_ms
        if os is not UNSET:
            field_dict["os"] = os
        if success is not UNSET:
            field_dict["success"] = success

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cli_version = d.pop("cli_version")

        command = d.pop("command")

        agent = d.pop("agent", UNSET)

        duration_ms = d.pop("duration_ms", UNSET)

        os = d.pop("os", UNSET)

        success = d.pop("success", UNSET)

        service_create_cli_event_request = cls(
            cli_version=cli_version,
            command=command,
            agent=agent,
            duration_ms=duration_ms,
            os=os,
            success=success,
        )

        service_create_cli_event_request.additional_properties = d
        return service_create_cli_event_request

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
