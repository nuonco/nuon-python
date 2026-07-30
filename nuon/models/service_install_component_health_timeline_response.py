from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_daily_health_bucket import ServiceDailyHealthBucket
    from ..models.service_health_transition_response import ServiceHealthTransitionResponse


T = TypeVar("T", bound="ServiceInstallComponentHealthTimelineResponse")


@_attrs_define
class ServiceInstallComponentHealthTimelineResponse:
    """
    Attributes:
        current_health (str | Unset):
        daily (list[ServiceDailyHealthBucket] | Unset):
        days (int | Unset):
        install_component_id (str | Unset):
        observed_seconds (int | Unset):
        transitions (list[ServiceHealthTransitionResponse] | Unset):
        uptime_percent (float | Unset):
    """

    current_health: str | Unset = UNSET
    daily: list[ServiceDailyHealthBucket] | Unset = UNSET
    days: int | Unset = UNSET
    install_component_id: str | Unset = UNSET
    observed_seconds: int | Unset = UNSET
    transitions: list[ServiceHealthTransitionResponse] | Unset = UNSET
    uptime_percent: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_health = self.current_health

        daily: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.daily, Unset):
            daily = []
            for daily_item_data in self.daily:
                daily_item = daily_item_data.to_dict()
                daily.append(daily_item)

        days = self.days

        install_component_id = self.install_component_id

        observed_seconds = self.observed_seconds

        transitions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.transitions, Unset):
            transitions = []
            for transitions_item_data in self.transitions:
                transitions_item = transitions_item_data.to_dict()
                transitions.append(transitions_item)

        uptime_percent = self.uptime_percent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_health is not UNSET:
            field_dict["current_health"] = current_health
        if daily is not UNSET:
            field_dict["daily"] = daily
        if days is not UNSET:
            field_dict["days"] = days
        if install_component_id is not UNSET:
            field_dict["install_component_id"] = install_component_id
        if observed_seconds is not UNSET:
            field_dict["observed_seconds"] = observed_seconds
        if transitions is not UNSET:
            field_dict["transitions"] = transitions
        if uptime_percent is not UNSET:
            field_dict["uptime_percent"] = uptime_percent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_daily_health_bucket import ServiceDailyHealthBucket
        from ..models.service_health_transition_response import ServiceHealthTransitionResponse

        d = dict(src_dict)
        current_health = d.pop("current_health", UNSET)

        _daily = d.pop("daily", UNSET)
        daily: list[ServiceDailyHealthBucket] | Unset = UNSET
        if _daily is not UNSET:
            daily = []
            for daily_item_data in _daily:
                daily_item = ServiceDailyHealthBucket.from_dict(daily_item_data)

                daily.append(daily_item)

        days = d.pop("days", UNSET)

        install_component_id = d.pop("install_component_id", UNSET)

        observed_seconds = d.pop("observed_seconds", UNSET)

        _transitions = d.pop("transitions", UNSET)
        transitions: list[ServiceHealthTransitionResponse] | Unset = UNSET
        if _transitions is not UNSET:
            transitions = []
            for transitions_item_data in _transitions:
                transitions_item = ServiceHealthTransitionResponse.from_dict(transitions_item_data)

                transitions.append(transitions_item)

        uptime_percent = d.pop("uptime_percent", UNSET)

        service_install_component_health_timeline_response = cls(
            current_health=current_health,
            daily=daily,
            days=days,
            install_component_id=install_component_id,
            observed_seconds=observed_seconds,
            transitions=transitions,
            uptime_percent=uptime_percent,
        )

        service_install_component_health_timeline_response.additional_properties = d
        return service_install_component_health_timeline_response

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
