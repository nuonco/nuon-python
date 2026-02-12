from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppPolicyResult")


@_attrs_define
class AppPolicyResult:
    """
    Attributes:
        deny_count (int | Unset):
        input_count (int | Unset):
        pass_count (int | Unset):
        policy_id (str | Unset):
        policy_name (str | Unset):
        status (str | Unset): "deny", "warn", or "pass"
        warn_count (int | Unset):
    """

    deny_count: int | Unset = UNSET
    input_count: int | Unset = UNSET
    pass_count: int | Unset = UNSET
    policy_id: str | Unset = UNSET
    policy_name: str | Unset = UNSET
    status: str | Unset = UNSET
    warn_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        deny_count = self.deny_count

        input_count = self.input_count

        pass_count = self.pass_count

        policy_id = self.policy_id

        policy_name = self.policy_name

        status = self.status

        warn_count = self.warn_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if deny_count is not UNSET:
            field_dict["deny_count"] = deny_count
        if input_count is not UNSET:
            field_dict["input_count"] = input_count
        if pass_count is not UNSET:
            field_dict["pass_count"] = pass_count
        if policy_id is not UNSET:
            field_dict["policy_id"] = policy_id
        if policy_name is not UNSET:
            field_dict["policy_name"] = policy_name
        if status is not UNSET:
            field_dict["status"] = status
        if warn_count is not UNSET:
            field_dict["warn_count"] = warn_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        deny_count = d.pop("deny_count", UNSET)

        input_count = d.pop("input_count", UNSET)

        pass_count = d.pop("pass_count", UNSET)

        policy_id = d.pop("policy_id", UNSET)

        policy_name = d.pop("policy_name", UNSET)

        status = d.pop("status", UNSET)

        warn_count = d.pop("warn_count", UNSET)

        app_policy_result = cls(
            deny_count=deny_count,
            input_count=input_count,
            pass_count=pass_count,
            policy_id=policy_id,
            policy_name=policy_name,
            status=status,
            warn_count=warn_count,
        )

        app_policy_result.additional_properties = d
        return app_policy_result

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
