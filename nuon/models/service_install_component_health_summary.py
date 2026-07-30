from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceInstallComponentHealthSummary")


@_attrs_define
class ServiceInstallComponentHealthSummary:
    """
    Attributes:
        component_id (str | Unset): ComponentID is what dashboard component routes are keyed by — a link
            built from the install-component id instead dead-ends on an empty page.
        component_name (str | Unset):
        current_health (str | Unset):
        install_component_id (str | Unset):
        uptime_percent (float | Unset):
    """

    component_id: str | Unset = UNSET
    component_name: str | Unset = UNSET
    current_health: str | Unset = UNSET
    install_component_id: str | Unset = UNSET
    uptime_percent: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        component_id = self.component_id

        component_name = self.component_name

        current_health = self.current_health

        install_component_id = self.install_component_id

        uptime_percent = self.uptime_percent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if component_id is not UNSET:
            field_dict["component_id"] = component_id
        if component_name is not UNSET:
            field_dict["component_name"] = component_name
        if current_health is not UNSET:
            field_dict["current_health"] = current_health
        if install_component_id is not UNSET:
            field_dict["install_component_id"] = install_component_id
        if uptime_percent is not UNSET:
            field_dict["uptime_percent"] = uptime_percent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        component_id = d.pop("component_id", UNSET)

        component_name = d.pop("component_name", UNSET)

        current_health = d.pop("current_health", UNSET)

        install_component_id = d.pop("install_component_id", UNSET)

        uptime_percent = d.pop("uptime_percent", UNSET)

        service_install_component_health_summary = cls(
            component_id=component_id,
            component_name=component_name,
            current_health=current_health,
            install_component_id=install_component_id,
            uptime_percent=uptime_percent,
        )

        service_install_component_health_summary.additional_properties = d
        return service_install_component_health_summary

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
