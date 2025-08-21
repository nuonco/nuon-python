from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_otel_log_record_log_attributes import AppOtelLogRecordLogAttributes
    from ..models.app_otel_log_record_resource_attributes import AppOtelLogRecordResourceAttributes
    from ..models.app_otel_log_record_scope_attributes import AppOtelLogRecordScopeAttributes


T = TypeVar("T", bound="AppOtelLogRecord")


@_attrs_define
class AppOtelLogRecord:
    """
    Attributes:
        body (Union[Unset, str]):
        created_at (Union[Unset, str]):
        created_by_id (Union[Unset, str]):
        id (Union[Unset, str]):
        log_attributes (Union[Unset, AppOtelLogRecordLogAttributes]):
        log_stream_id (Union[Unset, str]):
        org_id (Union[Unset, str]): internal attributes
        resource_attributes (Union[Unset, AppOtelLogRecordResourceAttributes]):
        resource_schema_url (Union[Unset, str]):
        runner_group_id (Union[Unset, str]):
        runner_id (Union[Unset, str]):
        runner_job_execution_id (Union[Unset, str]):
        runner_job_execution_step (Union[Unset, str]):
        runner_job_id (Union[Unset, str]):
        scope_attributes (Union[Unset, AppOtelLogRecordScopeAttributes]):
        scope_name (Union[Unset, str]):
        scope_schema_url (Union[Unset, str]):
        scope_version (Union[Unset, str]):
        service_name (Union[Unset, str]):
        severity_number (Union[Unset, int]):
        severity_text (Union[Unset, str]):
        span_id (Union[Unset, str]):
        timestamp (Union[Unset, str]): OTEL log message attributes
        timestamp_date (Union[Unset, str]):
        timestamp_time (Union[Unset, str]):
        trace_flags (Union[Unset, int]):
        trace_id (Union[Unset, str]):
        updated_at (Union[Unset, str]):
    """

    body: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    created_by_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    log_attributes: Union[Unset, "AppOtelLogRecordLogAttributes"] = UNSET
    log_stream_id: Union[Unset, str] = UNSET
    org_id: Union[Unset, str] = UNSET
    resource_attributes: Union[Unset, "AppOtelLogRecordResourceAttributes"] = UNSET
    resource_schema_url: Union[Unset, str] = UNSET
    runner_group_id: Union[Unset, str] = UNSET
    runner_id: Union[Unset, str] = UNSET
    runner_job_execution_id: Union[Unset, str] = UNSET
    runner_job_execution_step: Union[Unset, str] = UNSET
    runner_job_id: Union[Unset, str] = UNSET
    scope_attributes: Union[Unset, "AppOtelLogRecordScopeAttributes"] = UNSET
    scope_name: Union[Unset, str] = UNSET
    scope_schema_url: Union[Unset, str] = UNSET
    scope_version: Union[Unset, str] = UNSET
    service_name: Union[Unset, str] = UNSET
    severity_number: Union[Unset, int] = UNSET
    severity_text: Union[Unset, str] = UNSET
    span_id: Union[Unset, str] = UNSET
    timestamp: Union[Unset, str] = UNSET
    timestamp_date: Union[Unset, str] = UNSET
    timestamp_time: Union[Unset, str] = UNSET
    trace_flags: Union[Unset, int] = UNSET
    trace_id: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        body = self.body

        created_at = self.created_at

        created_by_id = self.created_by_id

        id = self.id

        log_attributes: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.log_attributes, Unset):
            log_attributes = self.log_attributes.to_dict()

        log_stream_id = self.log_stream_id

        org_id = self.org_id

        resource_attributes: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.resource_attributes, Unset):
            resource_attributes = self.resource_attributes.to_dict()

        resource_schema_url = self.resource_schema_url

        runner_group_id = self.runner_group_id

        runner_id = self.runner_id

        runner_job_execution_id = self.runner_job_execution_id

        runner_job_execution_step = self.runner_job_execution_step

        runner_job_id = self.runner_job_id

        scope_attributes: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.scope_attributes, Unset):
            scope_attributes = self.scope_attributes.to_dict()

        scope_name = self.scope_name

        scope_schema_url = self.scope_schema_url

        scope_version = self.scope_version

        service_name = self.service_name

        severity_number = self.severity_number

        severity_text = self.severity_text

        span_id = self.span_id

        timestamp = self.timestamp

        timestamp_date = self.timestamp_date

        timestamp_time = self.timestamp_time

        trace_flags = self.trace_flags

        trace_id = self.trace_id

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if body is not UNSET:
            field_dict["body"] = body
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if id is not UNSET:
            field_dict["id"] = id
        if log_attributes is not UNSET:
            field_dict["log_attributes"] = log_attributes
        if log_stream_id is not UNSET:
            field_dict["log_stream_id"] = log_stream_id
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if resource_attributes is not UNSET:
            field_dict["resource_attributes"] = resource_attributes
        if resource_schema_url is not UNSET:
            field_dict["resource_schema_url"] = resource_schema_url
        if runner_group_id is not UNSET:
            field_dict["runner_group_id"] = runner_group_id
        if runner_id is not UNSET:
            field_dict["runner_id"] = runner_id
        if runner_job_execution_id is not UNSET:
            field_dict["runner_job_execution_id"] = runner_job_execution_id
        if runner_job_execution_step is not UNSET:
            field_dict["runner_job_execution_step"] = runner_job_execution_step
        if runner_job_id is not UNSET:
            field_dict["runner_job_id"] = runner_job_id
        if scope_attributes is not UNSET:
            field_dict["scope_attributes"] = scope_attributes
        if scope_name is not UNSET:
            field_dict["scope_name"] = scope_name
        if scope_schema_url is not UNSET:
            field_dict["scope_schema_url"] = scope_schema_url
        if scope_version is not UNSET:
            field_dict["scope_version"] = scope_version
        if service_name is not UNSET:
            field_dict["service_name"] = service_name
        if severity_number is not UNSET:
            field_dict["severity_number"] = severity_number
        if severity_text is not UNSET:
            field_dict["severity_text"] = severity_text
        if span_id is not UNSET:
            field_dict["span_id"] = span_id
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if timestamp_date is not UNSET:
            field_dict["timestamp_date"] = timestamp_date
        if timestamp_time is not UNSET:
            field_dict["timestamp_time"] = timestamp_time
        if trace_flags is not UNSET:
            field_dict["trace_flags"] = trace_flags
        if trace_id is not UNSET:
            field_dict["trace_id"] = trace_id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_otel_log_record_log_attributes import AppOtelLogRecordLogAttributes
        from ..models.app_otel_log_record_resource_attributes import AppOtelLogRecordResourceAttributes
        from ..models.app_otel_log_record_scope_attributes import AppOtelLogRecordScopeAttributes

        d = dict(src_dict)
        body = d.pop("body", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        id = d.pop("id", UNSET)

        _log_attributes = d.pop("log_attributes", UNSET)
        log_attributes: Union[Unset, AppOtelLogRecordLogAttributes]
        if isinstance(_log_attributes, Unset):
            log_attributes = UNSET
        else:
            log_attributes = AppOtelLogRecordLogAttributes.from_dict(_log_attributes)

        log_stream_id = d.pop("log_stream_id", UNSET)

        org_id = d.pop("org_id", UNSET)

        _resource_attributes = d.pop("resource_attributes", UNSET)
        resource_attributes: Union[Unset, AppOtelLogRecordResourceAttributes]
        if isinstance(_resource_attributes, Unset):
            resource_attributes = UNSET
        else:
            resource_attributes = AppOtelLogRecordResourceAttributes.from_dict(_resource_attributes)

        resource_schema_url = d.pop("resource_schema_url", UNSET)

        runner_group_id = d.pop("runner_group_id", UNSET)

        runner_id = d.pop("runner_id", UNSET)

        runner_job_execution_id = d.pop("runner_job_execution_id", UNSET)

        runner_job_execution_step = d.pop("runner_job_execution_step", UNSET)

        runner_job_id = d.pop("runner_job_id", UNSET)

        _scope_attributes = d.pop("scope_attributes", UNSET)
        scope_attributes: Union[Unset, AppOtelLogRecordScopeAttributes]
        if isinstance(_scope_attributes, Unset):
            scope_attributes = UNSET
        else:
            scope_attributes = AppOtelLogRecordScopeAttributes.from_dict(_scope_attributes)

        scope_name = d.pop("scope_name", UNSET)

        scope_schema_url = d.pop("scope_schema_url", UNSET)

        scope_version = d.pop("scope_version", UNSET)

        service_name = d.pop("service_name", UNSET)

        severity_number = d.pop("severity_number", UNSET)

        severity_text = d.pop("severity_text", UNSET)

        span_id = d.pop("span_id", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        timestamp_date = d.pop("timestamp_date", UNSET)

        timestamp_time = d.pop("timestamp_time", UNSET)

        trace_flags = d.pop("trace_flags", UNSET)

        trace_id = d.pop("trace_id", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        app_otel_log_record = cls(
            body=body,
            created_at=created_at,
            created_by_id=created_by_id,
            id=id,
            log_attributes=log_attributes,
            log_stream_id=log_stream_id,
            org_id=org_id,
            resource_attributes=resource_attributes,
            resource_schema_url=resource_schema_url,
            runner_group_id=runner_group_id,
            runner_id=runner_id,
            runner_job_execution_id=runner_job_execution_id,
            runner_job_execution_step=runner_job_execution_step,
            runner_job_id=runner_job_id,
            scope_attributes=scope_attributes,
            scope_name=scope_name,
            scope_schema_url=scope_schema_url,
            scope_version=scope_version,
            service_name=service_name,
            severity_number=severity_number,
            severity_text=severity_text,
            span_id=span_id,
            timestamp=timestamp,
            timestamp_date=timestamp_date,
            timestamp_time=timestamp_time,
            trace_flags=trace_flags,
            trace_id=trace_id,
            updated_at=updated_at,
        )

        app_otel_log_record.additional_properties = d
        return app_otel_log_record

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
