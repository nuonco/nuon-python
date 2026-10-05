from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceInstallActivityPolicy")


@_attrs_define
class ServiceInstallActivityPolicy:
    """
    Attributes:
        component_name (str | Unset):
        deny_count (int | Unset):
        owner_id (str | Unset):
        owner_type (str | Unset):
        pass_count (int | Unset):
        report_id (str | Unset):
        warn_count (int | Unset):
    """

    component_name: str | Unset = UNSET
    deny_count: int | Unset = UNSET
    owner_id: str | Unset = UNSET
    owner_type: str | Unset = UNSET
    pass_count: int | Unset = UNSET
    report_id: str | Unset = UNSET
    warn_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        component_name = self.component_name

        deny_count = self.deny_count

        owner_id = self.owner_id

        owner_type = self.owner_type

        pass_count = self.pass_count

        report_id = self.report_id

        warn_count = self.warn_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if component_name is not UNSET:
            field_dict["component_name"] = component_name
        if deny_count is not UNSET:
            field_dict["deny_count"] = deny_count
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if owner_type is not UNSET:
            field_dict["owner_type"] = owner_type
        if pass_count is not UNSET:
            field_dict["pass_count"] = pass_count
        if report_id is not UNSET:
            field_dict["report_id"] = report_id
        if warn_count is not UNSET:
            field_dict["warn_count"] = warn_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        component_name = d.pop("component_name", UNSET)

        deny_count = d.pop("deny_count", UNSET)

        owner_id = d.pop("owner_id", UNSET)

        owner_type = d.pop("owner_type", UNSET)

        pass_count = d.pop("pass_count", UNSET)

        report_id = d.pop("report_id", UNSET)

        warn_count = d.pop("warn_count", UNSET)

        service_install_activity_policy = cls(
            component_name=component_name,
            deny_count=deny_count,
            owner_id=owner_id,
            owner_type=owner_type,
            pass_count=pass_count,
            report_id=report_id,
            warn_count=warn_count,
        )

        service_install_activity_policy.additional_properties = d
        return service_install_activity_policy

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
