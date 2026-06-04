from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_otel_log_record import AppOtelLogRecord


T = TypeVar("T", bound="ServiceLogStreamTailLogsResponse")


@_attrs_define
class ServiceLogStreamTailLogsResponse:
    """
    Attributes:
        has_more (bool | Unset):
        logs (list[AppOtelLogRecord] | Unset):
        next_ (str | Unset):
    """

    has_more: bool | Unset = UNSET
    logs: list[AppOtelLogRecord] | Unset = UNSET
    next_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        has_more = self.has_more

        logs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.logs, Unset):
            logs = []
            for logs_item_data in self.logs:
                logs_item = logs_item_data.to_dict()
                logs.append(logs_item)

        next_ = self.next_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if has_more is not UNSET:
            field_dict["has_more"] = has_more
        if logs is not UNSET:
            field_dict["logs"] = logs
        if next_ is not UNSET:
            field_dict["next"] = next_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_otel_log_record import AppOtelLogRecord

        d = dict(src_dict)
        has_more = d.pop("has_more", UNSET)

        _logs = d.pop("logs", UNSET)
        logs: list[AppOtelLogRecord] | Unset = UNSET
        if _logs is not UNSET:
            logs = []
            for logs_item_data in _logs:
                logs_item = AppOtelLogRecord.from_dict(logs_item_data)

                logs.append(logs_item)

        next_ = d.pop("next", UNSET)

        service_log_stream_tail_logs_response = cls(
            has_more=has_more,
            logs=logs,
            next_=next_,
        )

        service_log_stream_tail_logs_response.additional_properties = d
        return service_log_stream_tail_logs_response

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
