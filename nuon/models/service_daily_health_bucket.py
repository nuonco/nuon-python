from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceDailyHealthBucket")


@_attrs_define
class ServiceDailyHealthBucket:
    """
    Attributes:
        date (str | Unset):
        degraded_seconds (int | Unset):
        health (str | Unset):
        observed_seconds (int | Unset):
        unhealthy_seconds (int | Unset):
        unknown_seconds (int | Unset):
    """

    date: str | Unset = UNSET
    degraded_seconds: int | Unset = UNSET
    health: str | Unset = UNSET
    observed_seconds: int | Unset = UNSET
    unhealthy_seconds: int | Unset = UNSET
    unknown_seconds: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        degraded_seconds = self.degraded_seconds

        health = self.health

        observed_seconds = self.observed_seconds

        unhealthy_seconds = self.unhealthy_seconds

        unknown_seconds = self.unknown_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if degraded_seconds is not UNSET:
            field_dict["degraded_seconds"] = degraded_seconds
        if health is not UNSET:
            field_dict["health"] = health
        if observed_seconds is not UNSET:
            field_dict["observed_seconds"] = observed_seconds
        if unhealthy_seconds is not UNSET:
            field_dict["unhealthy_seconds"] = unhealthy_seconds
        if unknown_seconds is not UNSET:
            field_dict["unknown_seconds"] = unknown_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        date = d.pop("date", UNSET)

        degraded_seconds = d.pop("degraded_seconds", UNSET)

        health = d.pop("health", UNSET)

        observed_seconds = d.pop("observed_seconds", UNSET)

        unhealthy_seconds = d.pop("unhealthy_seconds", UNSET)

        unknown_seconds = d.pop("unknown_seconds", UNSET)

        service_daily_health_bucket = cls(
            date=date,
            degraded_seconds=degraded_seconds,
            health=health,
            observed_seconds=observed_seconds,
            unhealthy_seconds=unhealthy_seconds,
            unknown_seconds=unknown_seconds,
        )

        service_daily_health_bucket.additional_properties = d
        return service_daily_health_bucket

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
