from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceInstallDeploymentPolicySummary")


@_attrs_define
class ServiceInstallDeploymentPolicySummary:
    """
    Attributes:
        deny_count (int | Unset):
        first_warn_message (str | Unset):
        warn_count (int | Unset):
    """

    deny_count: int | Unset = UNSET
    first_warn_message: str | Unset = UNSET
    warn_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        deny_count = self.deny_count

        first_warn_message = self.first_warn_message

        warn_count = self.warn_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if deny_count is not UNSET:
            field_dict["deny_count"] = deny_count
        if first_warn_message is not UNSET:
            field_dict["first_warn_message"] = first_warn_message
        if warn_count is not UNSET:
            field_dict["warn_count"] = warn_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        deny_count = d.pop("deny_count", UNSET)

        first_warn_message = d.pop("first_warn_message", UNSET)

        warn_count = d.pop("warn_count", UNSET)

        service_install_deployment_policy_summary = cls(
            deny_count=deny_count,
            first_warn_message=first_warn_message,
            warn_count=warn_count,
        )

        service_install_deployment_policy_summary.additional_properties = d
        return service_install_deployment_policy_summary

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
