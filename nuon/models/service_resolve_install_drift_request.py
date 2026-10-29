from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceResolveInstallDriftRequest")


@_attrs_define
class ServiceResolveInstallDriftRequest:
    """
    Attributes:
        request_id (str):
        resource_id (str):
        approved_plan_id (str | Unset):
    """

    request_id: str
    resource_id: str
    approved_plan_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        request_id = self.request_id

        resource_id = self.resource_id

        approved_plan_id = self.approved_plan_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "request_id": request_id,
                "resource_id": resource_id,
            }
        )
        if approved_plan_id is not UNSET:
            field_dict["approved_plan_id"] = approved_plan_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        request_id = d.pop("request_id")

        resource_id = d.pop("resource_id")

        approved_plan_id = d.pop("approved_plan_id", UNSET)

        service_resolve_install_drift_request = cls(
            request_id=request_id,
            resource_id=resource_id,
            approved_plan_id=approved_plan_id,
        )

        service_resolve_install_drift_request.additional_properties = d
        return service_resolve_install_drift_request

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
