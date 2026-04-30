from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CctxSignalContext")


@_attrs_define
class CctxSignalContext:
    """
    Attributes:
        account_id (str | Unset):
        log_stream_id (str | Unset):
        org_id (str | Unset):
        trace_id (str | Unset):
    """

    account_id: str | Unset = UNSET
    log_stream_id: str | Unset = UNSET
    org_id: str | Unset = UNSET
    trace_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        log_stream_id = self.log_stream_id

        org_id = self.org_id

        trace_id = self.trace_id

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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("account_id", UNSET)

        log_stream_id = d.pop("log_stream_id", UNSET)

        org_id = d.pop("org_id", UNSET)

        trace_id = d.pop("trace_id", UNSET)

        cctx_signal_context = cls(
            account_id=account_id,
            log_stream_id=log_stream_id,
            org_id=org_id,
            trace_id=trace_id,
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
