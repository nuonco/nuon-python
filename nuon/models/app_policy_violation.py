from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppPolicyViolation")


@_attrs_define
class AppPolicyViolation:
    """
    Attributes:
        input_identity (str | Unset): Human-readable input reference (e.g., "Deployment/default/nginx")
        input_index (int | Unset):
        message (str | Unset):
        policy_id (str | Unset):
        severity (str | Unset): "deny" or "warn"
    """

    input_identity: str | Unset = UNSET
    input_index: int | Unset = UNSET
    message: str | Unset = UNSET
    policy_id: str | Unset = UNSET
    severity: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        input_identity = self.input_identity

        input_index = self.input_index

        message = self.message

        policy_id = self.policy_id

        severity = self.severity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if input_identity is not UNSET:
            field_dict["input_identity"] = input_identity
        if input_index is not UNSET:
            field_dict["input_index"] = input_index
        if message is not UNSET:
            field_dict["message"] = message
        if policy_id is not UNSET:
            field_dict["policy_id"] = policy_id
        if severity is not UNSET:
            field_dict["severity"] = severity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        input_identity = d.pop("input_identity", UNSET)

        input_index = d.pop("input_index", UNSET)

        message = d.pop("message", UNSET)

        policy_id = d.pop("policy_id", UNSET)

        severity = d.pop("severity", UNSET)

        app_policy_violation = cls(
            input_identity=input_identity,
            input_index=input_index,
            message=message,
            policy_id=policy_id,
            severity=severity,
        )

        app_policy_violation.additional_properties = d
        return app_policy_violation

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
