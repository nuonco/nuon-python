from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_role_type import AppRoleType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceCreateOrgInviteRequest")


@_attrs_define
class ServiceCreateOrgInviteRequest:
    """
    Attributes:
        email (str):
        role_type (AppRoleType | Unset):
    """

    email: str
    role_type: AppRoleType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        role_type: str | Unset = UNSET
        if not isinstance(self.role_type, Unset):
            role_type = self.role_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
            }
        )
        if role_type is not UNSET:
            field_dict["role_type"] = role_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        _role_type = d.pop("role_type", UNSET)
        role_type: AppRoleType | Unset
        if isinstance(_role_type, Unset):
            role_type = UNSET
        else:
            role_type = AppRoleType(_role_type)

        service_create_org_invite_request = cls(
            email=email,
            role_type=role_type,
        )

        service_create_org_invite_request.additional_properties = d
        return service_create_org_invite_request

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
