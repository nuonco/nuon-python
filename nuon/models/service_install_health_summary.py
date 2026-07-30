from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceInstallHealthSummary")


@_attrs_define
class ServiceInstallHealthSummary:
    """
    Attributes:
        app_id (str | Unset):
        degraded_components (int | Unset):
        health (str | Unset):
        health_description (str | Unset):
        install_id (str | Unset):
        install_name (str | Unset):
        unhealthy_components (int | Unset):
    """

    app_id: str | Unset = UNSET
    degraded_components: int | Unset = UNSET
    health: str | Unset = UNSET
    health_description: str | Unset = UNSET
    install_id: str | Unset = UNSET
    install_name: str | Unset = UNSET
    unhealthy_components: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_id = self.app_id

        degraded_components = self.degraded_components

        health = self.health

        health_description = self.health_description

        install_id = self.install_id

        install_name = self.install_name

        unhealthy_components = self.unhealthy_components

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_id is not UNSET:
            field_dict["app_id"] = app_id
        if degraded_components is not UNSET:
            field_dict["degraded_components"] = degraded_components
        if health is not UNSET:
            field_dict["health"] = health
        if health_description is not UNSET:
            field_dict["health_description"] = health_description
        if install_id is not UNSET:
            field_dict["install_id"] = install_id
        if install_name is not UNSET:
            field_dict["install_name"] = install_name
        if unhealthy_components is not UNSET:
            field_dict["unhealthy_components"] = unhealthy_components

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        app_id = d.pop("app_id", UNSET)

        degraded_components = d.pop("degraded_components", UNSET)

        health = d.pop("health", UNSET)

        health_description = d.pop("health_description", UNSET)

        install_id = d.pop("install_id", UNSET)

        install_name = d.pop("install_name", UNSET)

        unhealthy_components = d.pop("unhealthy_components", UNSET)

        service_install_health_summary = cls(
            app_id=app_id,
            degraded_components=degraded_components,
            health=health,
            health_description=health_description,
            install_id=install_id,
            install_name=install_name,
            unhealthy_components=unhealthy_components,
        )

        service_install_health_summary.additional_properties = d
        return service_install_health_summary

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
