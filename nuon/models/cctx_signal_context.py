from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keys_workflow_telemetry import KeysWorkflowTelemetry


T = TypeVar("T", bound="CctxSignalContext")


@_attrs_define
class CctxSignalContext:
    """
    Attributes:
        account_id (str | Unset):
        log_stream_id (str | Unset):
        org_id (str | Unset):
        trace_id (str | Unset):
        workflow_telemetry (KeysWorkflowTelemetry | Unset):
    """

    account_id: str | Unset = UNSET
    log_stream_id: str | Unset = UNSET
    org_id: str | Unset = UNSET
    trace_id: str | Unset = UNSET
    workflow_telemetry: KeysWorkflowTelemetry | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        log_stream_id = self.log_stream_id

        org_id = self.org_id

        trace_id = self.trace_id

        workflow_telemetry: dict[str, Any] | Unset = UNSET
        if not isinstance(self.workflow_telemetry, Unset):
            workflow_telemetry = self.workflow_telemetry.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if log_stream_id is not UNSET:
            field_dict["log_stream_id"] = log_stream_id
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if trace_id is not UNSET:
            field_dict["trace_id"] = trace_id
        if workflow_telemetry is not UNSET:
            field_dict["workflow_telemetry"] = workflow_telemetry

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.keys_workflow_telemetry import KeysWorkflowTelemetry  # noqa: PLC0415

        d = dict(src_dict)
        account_id = d.pop("account_id", UNSET)

        log_stream_id = d.pop("log_stream_id", UNSET)

        org_id = d.pop("org_id", UNSET)

        trace_id = d.pop("trace_id", UNSET)

        _workflow_telemetry = d.pop("workflow_telemetry", UNSET)
        workflow_telemetry: KeysWorkflowTelemetry | Unset
        if isinstance(_workflow_telemetry, Unset):
            workflow_telemetry = UNSET
        else:
            workflow_telemetry = KeysWorkflowTelemetry.from_dict(_workflow_telemetry)

        cctx_signal_context = cls(
            account_id=account_id,
            log_stream_id=log_stream_id,
            org_id=org_id,
            trace_id=trace_id,
            workflow_telemetry=workflow_telemetry,
        )

        cctx_signal_context.additional_properties = d
        return cctx_signal_context

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
