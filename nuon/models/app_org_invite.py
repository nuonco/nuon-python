from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_org_invite_status import AppOrgInviteStatus
from ..models.app_role_type import AppRoleType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AppOrgInvite")


@_attrs_define
class AppOrgInvite:
    """
    Attributes:
        created_at (str | Unset):
        created_by_id (str | Unset):
        email (str | Unset):
        id (str | Unset):
        org_id (str | Unset): parent relationship
        role_type (AppRoleType | Unset):
        status (AppOrgInviteStatus | Unset):
        updated_at (str | Unset):
    """

    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    email: str | Unset = UNSET
    id: str | Unset = UNSET
    org_id: str | Unset = UNSET
    role_type: AppRoleType | Unset = UNSET
    status: AppOrgInviteStatus | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        created_by_id = self.created_by_id

        email = self.email

        id = self.id

        org_id = self.org_id

        role_type: str | Unset = UNSET
        if not isinstance(self.role_type, Unset):
            role_type = self.role_type.value

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if email is not UNSET:
            field_dict["email"] = email
        if id is not UNSET:
            field_dict["id"] = id
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if role_type is not UNSET:
            field_dict["role_type"] = role_type
        if status is not UNSET:
            field_dict["status"] = status
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        email = d.pop("email", UNSET)

        id = d.pop("id", UNSET)

        org_id = d.pop("org_id", UNSET)

        _role_type = d.pop("role_type", UNSET)
        role_type: AppRoleType | Unset
        if isinstance(_role_type, Unset):
            role_type = UNSET
        else:
            role_type = AppRoleType(_role_type)

        _status = d.pop("status", UNSET)
        status: AppOrgInviteStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AppOrgInviteStatus(_status)

        updated_at = d.pop("updated_at", UNSET)

        app_org_invite = cls(
            created_at=created_at,
            created_by_id=created_by_id,
            email=email,
            id=id,
            org_id=org_id,
            role_type=role_type,
            status=status,
            updated_at=updated_at,
        )

        app_org_invite.additional_properties = d
        return app_org_invite

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
