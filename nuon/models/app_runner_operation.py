from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_runner_operation_type import AppRunnerOperationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_log_stream import AppLogStream


T = TypeVar("T", bound="AppRunnerOperation")


@_attrs_define
class AppRunnerOperation:
    """
    Attributes:
        created_at (str | Unset):
        created_by_id (str | Unset):
        id (str | Unset):
        log_stream (AppLogStream | Unset):
        operation_type (AppRunnerOperationType | Unset):
        runner_id (str | Unset):
        status (str | Unset):
        status_description (str | Unset):
        updated_at (str | Unset):
    """

    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    id: str | Unset = UNSET
    log_stream: AppLogStream | Unset = UNSET
    operation_type: AppRunnerOperationType | Unset = UNSET
    runner_id: str | Unset = UNSET
    status: str | Unset = UNSET
    status_description: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        created_by_id = self.created_by_id

        id = self.id

        log_stream: dict[str, Any] | Unset = UNSET
        if not isinstance(self.log_stream, Unset):
            log_stream = self.log_stream.to_dict()

        operation_type: str | Unset = UNSET
        if not isinstance(self.operation_type, Unset):
            operation_type = self.operation_type.value

        runner_id = self.runner_id

        status = self.status

        status_description = self.status_description

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if id is not UNSET:
            field_dict["id"] = id
        if log_stream is not UNSET:
            field_dict["log_stream"] = log_stream
        if operation_type is not UNSET:
            field_dict["operation_type"] = operation_type
        if runner_id is not UNSET:
            field_dict["runner_id"] = runner_id
        if status is not UNSET:
            field_dict["status"] = status
        if status_description is not UNSET:
            field_dict["status_description"] = status_description
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_log_stream import AppLogStream

        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        id = d.pop("id", UNSET)

        _log_stream = d.pop("log_stream", UNSET)
        log_stream: AppLogStream | Unset
        if isinstance(_log_stream, Unset):
            log_stream = UNSET
        else:
            log_stream = AppLogStream.from_dict(_log_stream)

        _operation_type = d.pop("operation_type", UNSET)
        operation_type: AppRunnerOperationType | Unset
        if isinstance(_operation_type, Unset):
            operation_type = UNSET
        else:
            operation_type = AppRunnerOperationType(_operation_type)

        runner_id = d.pop("runner_id", UNSET)

        status = d.pop("status", UNSET)

        status_description = d.pop("status_description", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        app_runner_operation = cls(
            created_at=created_at,
            created_by_id=created_by_id,
            id=id,
            log_stream=log_stream,
            operation_type=operation_type,
            runner_id=runner_id,
            status=status,
            status_description=status_description,
            updated_at=updated_at,
        )

        app_runner_operation.additional_properties = d
        return app_runner_operation

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
