from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_log_stream_span_attributes import ServiceLogStreamSpanAttributes


T = TypeVar("T", bound="ServiceLogStreamSpan")


@_attrs_define
class ServiceLogStreamSpan:
    """
    Attributes:
        attributes (ServiceLogStreamSpanAttributes | Unset):
        duration_ns (int | Unset): DurationNs is the wall-clock span duration in nanoseconds, copied
            straight from the otel_traces.duration column.
        end_timestamp (str | Unset):
        parent_span_id (str | Unset):
        runner_job_execution_id (str | Unset):
        runner_job_execution_step (str | Unset):
        runner_job_id (str | Unset): Per-execution identifiers extracted server-side at ingest time.
            Empty if the span was emitted outside a job context.
        scope_name (str | Unset):
        service_name (str | Unset):
        span_id (str | Unset):
        span_kind (str | Unset):
        span_name (str | Unset):
        start_timestamp (str | Unset):
        status_code (str | Unset):
        status_message (str | Unset):
        trace_id (str | Unset):
    """

    attributes: ServiceLogStreamSpanAttributes | Unset = UNSET
    duration_ns: int | Unset = UNSET
    end_timestamp: str | Unset = UNSET
    parent_span_id: str | Unset = UNSET
    runner_job_execution_id: str | Unset = UNSET
    runner_job_execution_step: str | Unset = UNSET
    runner_job_id: str | Unset = UNSET
    scope_name: str | Unset = UNSET
    service_name: str | Unset = UNSET
    span_id: str | Unset = UNSET
    span_kind: str | Unset = UNSET
    span_name: str | Unset = UNSET
    start_timestamp: str | Unset = UNSET
    status_code: str | Unset = UNSET
    status_message: str | Unset = UNSET
    trace_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        duration_ns = self.duration_ns

        end_timestamp = self.end_timestamp

        parent_span_id = self.parent_span_id

        runner_job_execution_id = self.runner_job_execution_id

        runner_job_execution_step = self.runner_job_execution_step

        runner_job_id = self.runner_job_id

        scope_name = self.scope_name

        service_name = self.service_name

        span_id = self.span_id

        span_kind = self.span_kind

        span_name = self.span_name

        start_timestamp = self.start_timestamp

        status_code = self.status_code

        status_message = self.status_message

        trace_id = self.trace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if duration_ns is not UNSET:
            field_dict["duration_ns"] = duration_ns
        if end_timestamp is not UNSET:
            field_dict["end_timestamp"] = end_timestamp
        if parent_span_id is not UNSET:
            field_dict["parent_span_id"] = parent_span_id
        if runner_job_execution_id is not UNSET:
            field_dict["runner_job_execution_id"] = runner_job_execution_id
        if runner_job_execution_step is not UNSET:
            field_dict["runner_job_execution_step"] = runner_job_execution_step
        if runner_job_id is not UNSET:
            field_dict["runner_job_id"] = runner_job_id
        if scope_name is not UNSET:
            field_dict["scope_name"] = scope_name
        if service_name is not UNSET:
            field_dict["service_name"] = service_name
        if span_id is not UNSET:
            field_dict["span_id"] = span_id
        if span_kind is not UNSET:
            field_dict["span_kind"] = span_kind
        if span_name is not UNSET:
            field_dict["span_name"] = span_name
        if start_timestamp is not UNSET:
            field_dict["start_timestamp"] = start_timestamp
        if status_code is not UNSET:
            field_dict["status_code"] = status_code
        if status_message is not UNSET:
            field_dict["status_message"] = status_message
        if trace_id is not UNSET:
            field_dict["trace_id"] = trace_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_log_stream_span_attributes import ServiceLogStreamSpanAttributes

        d = dict(src_dict)
        _attributes = d.pop("attributes", UNSET)
        attributes: ServiceLogStreamSpanAttributes | Unset
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = ServiceLogStreamSpanAttributes.from_dict(_attributes)

        duration_ns = d.pop("duration_ns", UNSET)

        end_timestamp = d.pop("end_timestamp", UNSET)

        parent_span_id = d.pop("parent_span_id", UNSET)

        runner_job_execution_id = d.pop("runner_job_execution_id", UNSET)

        runner_job_execution_step = d.pop("runner_job_execution_step", UNSET)

        runner_job_id = d.pop("runner_job_id", UNSET)

        scope_name = d.pop("scope_name", UNSET)

        service_name = d.pop("service_name", UNSET)

        span_id = d.pop("span_id", UNSET)

        span_kind = d.pop("span_kind", UNSET)

        span_name = d.pop("span_name", UNSET)

        start_timestamp = d.pop("start_timestamp", UNSET)

        status_code = d.pop("status_code", UNSET)

        status_message = d.pop("status_message", UNSET)

        trace_id = d.pop("trace_id", UNSET)

        service_log_stream_span = cls(
            attributes=attributes,
            duration_ns=duration_ns,
            end_timestamp=end_timestamp,
            parent_span_id=parent_span_id,
            runner_job_execution_id=runner_job_execution_id,
            runner_job_execution_step=runner_job_execution_step,
            runner_job_id=runner_job_id,
            scope_name=scope_name,
            service_name=service_name,
            span_id=span_id,
            span_kind=span_kind,
            span_name=span_name,
            start_timestamp=start_timestamp,
            status_code=status_code,
            status_message=status_message,
            trace_id=trace_id,
        )

        service_log_stream_span.additional_properties = d
        return service_log_stream_span

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
