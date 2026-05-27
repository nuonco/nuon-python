from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_workflow_queue_item import ServiceWorkflowQueueItem


T = TypeVar("T", bound="ServiceWorkflowQueuePositionResponse")


@_attrs_define
class ServiceWorkflowQueuePositionResponse:
    """
    Attributes:
        position (int | Unset): Position is the 1-based queue position (1 = next to execute).
        queue_depth (int | Unset): QueueDepth is the total number of signals waiting in the queue.
        signals_ahead (list[ServiceWorkflowQueueItem] | Unset): SignalsAhead are the workflows ahead in the queue,
            ordered from front to back.
    """

    position: int | Unset = UNSET
    queue_depth: int | Unset = UNSET
    signals_ahead: list[ServiceWorkflowQueueItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        position = self.position

        queue_depth = self.queue_depth

        signals_ahead: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.signals_ahead, Unset):
            signals_ahead = []
            for signals_ahead_item_data in self.signals_ahead:
                signals_ahead_item = signals_ahead_item_data.to_dict()
                signals_ahead.append(signals_ahead_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if position is not UNSET:
            field_dict["position"] = position
        if queue_depth is not UNSET:
            field_dict["queue_depth"] = queue_depth
        if signals_ahead is not UNSET:
            field_dict["signals_ahead"] = signals_ahead

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_workflow_queue_item import ServiceWorkflowQueueItem

        d = dict(src_dict)
        position = d.pop("position", UNSET)

        queue_depth = d.pop("queue_depth", UNSET)

        _signals_ahead = d.pop("signals_ahead", UNSET)
        signals_ahead: list[ServiceWorkflowQueueItem] | Unset = UNSET
        if _signals_ahead is not UNSET:
            signals_ahead = []
            for signals_ahead_item_data in _signals_ahead:
                signals_ahead_item = ServiceWorkflowQueueItem.from_dict(signals_ahead_item_data)

                signals_ahead.append(signals_ahead_item)

        service_workflow_queue_position_response = cls(
            position=position,
            queue_depth=queue_depth,
            signals_ahead=signals_ahead,
        )

        service_workflow_queue_position_response.additional_properties = d
        return service_workflow_queue_position_response

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
