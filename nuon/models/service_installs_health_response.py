from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_install_health_summary import ServiceInstallHealthSummary


T = TypeVar("T", bound="ServiceInstallsHealthResponse")


@_attrs_define
class ServiceInstallsHealthResponse:
    """
    Attributes:
        all_healthy (bool | Unset):
        degraded (int | Unset):
        healthy (int | Unset):
        installs (list[ServiceInstallHealthSummary] | Unset):
        total (int | Unset):
        unhealthy (int | Unset):
        unknown (int | Unset):
        unset (int | Unset):
    """

    all_healthy: bool | Unset = UNSET
    degraded: int | Unset = UNSET
    healthy: int | Unset = UNSET
    installs: list[ServiceInstallHealthSummary] | Unset = UNSET
    total: int | Unset = UNSET
    unhealthy: int | Unset = UNSET
    unknown: int | Unset = UNSET
    unset: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        all_healthy = self.all_healthy

        degraded = self.degraded

        healthy = self.healthy

        installs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.installs, Unset):
            installs = []
            for installs_item_data in self.installs:
                installs_item = installs_item_data.to_dict()
                installs.append(installs_item)

        total = self.total

        unhealthy = self.unhealthy

        unknown = self.unknown

        unset = self.unset

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if all_healthy is not UNSET:
            field_dict["all_healthy"] = all_healthy
        if degraded is not UNSET:
            field_dict["degraded"] = degraded
        if healthy is not UNSET:
            field_dict["healthy"] = healthy
        if installs is not UNSET:
            field_dict["installs"] = installs
        if total is not UNSET:
            field_dict["total"] = total
        if unhealthy is not UNSET:
            field_dict["unhealthy"] = unhealthy
        if unknown is not UNSET:
            field_dict["unknown"] = unknown
        if unset is not UNSET:
            field_dict["unset"] = unset

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_install_health_summary import ServiceInstallHealthSummary

        d = dict(src_dict)
        all_healthy = d.pop("all_healthy", UNSET)

        degraded = d.pop("degraded", UNSET)

        healthy = d.pop("healthy", UNSET)

        _installs = d.pop("installs", UNSET)
        installs: list[ServiceInstallHealthSummary] | Unset = UNSET
        if _installs is not UNSET:
            installs = []
            for installs_item_data in _installs:
                installs_item = ServiceInstallHealthSummary.from_dict(installs_item_data)

                installs.append(installs_item)

        total = d.pop("total", UNSET)

        unhealthy = d.pop("unhealthy", UNSET)

        unknown = d.pop("unknown", UNSET)

        unset = d.pop("unset", UNSET)

        service_installs_health_response = cls(
            all_healthy=all_healthy,
            degraded=degraded,
            healthy=healthy,
            installs=installs,
            total=total,
            unhealthy=unhealthy,
            unknown=unknown,
            unset=unset,
        )

        service_installs_health_response.additional_properties = d
        return service_installs_health_response

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
