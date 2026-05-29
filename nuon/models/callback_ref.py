from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CallbackRef")


@_attrs_define
class CallbackRef:
    """
    Attributes:
        namespace (str | Unset):
        signal_name (str | Unset):
        workflow_id (str | Unset):
    """

    namespace: str | Unset = UNSET
    signal_name: str | Unset = UNSET
    workflow_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        namespace = self.namespace

        signal_name = self.signal_name

        workflow_id = self.workflow_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if signal_name is not UNSET:
            field_dict["signal_name"] = signal_name
        if workflow_id is not UNSET:
            field_dict["workflow_id"] = workflow_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        namespace = d.pop("namespace", UNSET)

        signal_name = d.pop("signal_name", UNSET)

        workflow_id = d.pop("workflow_id", UNSET)

        callback_ref = cls(
            namespace=namespace,
            signal_name=signal_name,
            workflow_id=workflow_id,
        )

        callback_ref.additional_properties = d
        return callback_ref

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
