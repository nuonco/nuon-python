from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_runner_job_permission_trace_record import AppRunnerJobPermissionTraceRecord


T = TypeVar("T", bound="AppRunnerJobPermissionInfo")


@_attrs_define
class AppRunnerJobPermissionInfo:
    """
    Attributes:
        role (str | Unset):
        role_selection_trace (list[AppRunnerJobPermissionTraceRecord] | Unset):
        role_source (str | Unset):
    """

    role: str | Unset = UNSET
    role_selection_trace: list[AppRunnerJobPermissionTraceRecord] | Unset = UNSET
    role_source: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        role = self.role

        role_selection_trace: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.role_selection_trace, Unset):
            role_selection_trace = []
            for role_selection_trace_item_data in self.role_selection_trace:
                role_selection_trace_item = role_selection_trace_item_data.to_dict()
                role_selection_trace.append(role_selection_trace_item)

        role_source = self.role_source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if role is not UNSET:
            field_dict["role"] = role
        if role_selection_trace is not UNSET:
            field_dict["role_selection_trace"] = role_selection_trace
        if role_source is not UNSET:
            field_dict["role_source"] = role_source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_runner_job_permission_trace_record import AppRunnerJobPermissionTraceRecord

        d = dict(src_dict)
        role = d.pop("role", UNSET)

        _role_selection_trace = d.pop("role_selection_trace", UNSET)
        role_selection_trace: list[AppRunnerJobPermissionTraceRecord] | Unset = UNSET
        if _role_selection_trace is not UNSET:
            role_selection_trace = []
            for role_selection_trace_item_data in _role_selection_trace:
                role_selection_trace_item = AppRunnerJobPermissionTraceRecord.from_dict(role_selection_trace_item_data)

                role_selection_trace.append(role_selection_trace_item)

        role_source = d.pop("role_source", UNSET)

        app_runner_job_permission_info = cls(
            role=role,
            role_selection_trace=role_selection_trace,
            role_source=role_source,
        )

        app_runner_job_permission_info.additional_properties = d
        return app_runner_job_permission_info

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
