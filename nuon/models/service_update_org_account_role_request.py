from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_role_type import AppRoleType

T = TypeVar("T", bound="ServiceUpdateOrgAccountRoleRequest")


@_attrs_define
class ServiceUpdateOrgAccountRoleRequest:
    """
    Attributes:
        role_type (AppRoleType):
    """

    role_type: AppRoleType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        role_type = self.role_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "role_type": role_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        role_type = AppRoleType(d.pop("role_type"))

        service_update_org_account_role_request = cls(
            role_type=role_type,
        )

        service_update_org_account_role_request.additional_properties = d
        return service_update_org_account_role_request

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
