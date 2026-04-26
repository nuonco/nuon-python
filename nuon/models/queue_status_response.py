from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QueueStatusResponse")


@_attrs_define
class QueueStatusResponse:
    """
    Attributes:
        in_flight (list[str] | Unset):
        in_flight_count (int | Unset):
        paused (bool | Unset):
        queue_depth_count (int | Unset):
        ready (bool | Unset):
        stopped (bool | Unset):
    """

    in_flight: list[str] | Unset = UNSET
    in_flight_count: int | Unset = UNSET
    paused: bool | Unset = UNSET
    queue_depth_count: int | Unset = UNSET
    ready: bool | Unset = UNSET
    stopped: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        in_flight: list[str] | Unset = UNSET
        if not isinstance(self.in_flight, Unset):
            in_flight = self.in_flight

        in_flight_count = self.in_flight_count

        paused = self.paused

        queue_depth_count = self.queue_depth_count

        ready = self.ready

        stopped = self.stopped

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if in_flight is not UNSET:
            field_dict["inFlight"] = in_flight
        if in_flight_count is not UNSET:
            field_dict["inFlightCount"] = in_flight_count
        if paused is not UNSET:
            field_dict["paused"] = paused
        if queue_depth_count is not UNSET:
            field_dict["queueDepthCount"] = queue_depth_count
        if ready is not UNSET:
            field_dict["ready"] = ready
        if stopped is not UNSET:
            field_dict["stopped"] = stopped

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        in_flight = cast(list[str], d.pop("inFlight", UNSET))

        in_flight_count = d.pop("inFlightCount", UNSET)

        paused = d.pop("paused", UNSET)

        queue_depth_count = d.pop("queueDepthCount", UNSET)

        ready = d.pop("ready", UNSET)

        stopped = d.pop("stopped", UNSET)

        queue_status_response = cls(
            in_flight=in_flight,
            in_flight_count=in_flight_count,
            paused=paused,
            queue_depth_count=queue_depth_count,
            ready=ready,
            stopped=stopped,
        )

        queue_status_response.additional_properties = d
        return queue_status_response

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
