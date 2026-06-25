from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceToggleInstallComponentRequest")


@_attrs_define
class ServiceToggleInstallComponentRequest:
    """
    Attributes:
        enabled (bool | Unset):
        plan_only (bool | Unset):
        role (str | Unset):
    """

    enabled: bool | Unset = UNSET
    plan_only: bool | Unset = UNSET
    role: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        plan_only = self.plan_only

        role = self.role

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if plan_only is not UNSET:
            field_dict["plan_only"] = plan_only
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        plan_only = d.pop("plan_only", UNSET)

        role = d.pop("role", UNSET)

        service_toggle_install_component_request = cls(
            enabled=enabled,
            plan_only=plan_only,
            role=role,
        )

        service_toggle_install_component_request.additional_properties = d
        return service_toggle_install_component_request

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
