from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_org_member_status import AppOrgMemberStatus
from ..models.app_role_type import AppRoleType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AppOrgMember")


@_attrs_define
class AppOrgMember:
    """
    Attributes:
        account_id (str | Unset):
        created_at (str | Unset):
        email (str | Unset):
        id (str | Unset):
        invite_id (str | Unset):
        joined_at (str | Unset):
        name (str | Unset):
        role_type (AppRoleType | Unset):
        status (AppOrgMemberStatus | Unset):
    """

    account_id: str | Unset = UNSET
    created_at: str | Unset = UNSET
    email: str | Unset = UNSET
    id: str | Unset = UNSET
    invite_id: str | Unset = UNSET
    joined_at: str | Unset = UNSET
    name: str | Unset = UNSET
    role_type: AppRoleType | Unset = UNSET
    status: AppOrgMemberStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        created_at = self.created_at

        email = self.email

        id = self.id

        invite_id = self.invite_id

        joined_at = self.joined_at

        name = self.name

        role_type: str | Unset = UNSET
        if not isinstance(self.role_type, Unset):
            role_type = self.role_type.value

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if email is not UNSET:
            field_dict["email"] = email
        if id is not UNSET:
            field_dict["id"] = id
        if invite_id is not UNSET:
            field_dict["invite_id"] = invite_id
        if joined_at is not UNSET:
            field_dict["joined_at"] = joined_at
        if name is not UNSET:
            field_dict["name"] = name
        if role_type is not UNSET:
            field_dict["role_type"] = role_type
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("account_id", UNSET)

        created_at = d.pop("created_at", UNSET)

        email = d.pop("email", UNSET)

        id = d.pop("id", UNSET)

        invite_id = d.pop("invite_id", UNSET)

        joined_at = d.pop("joined_at", UNSET)

        name = d.pop("name", UNSET)

        _role_type = d.pop("role_type", UNSET)
        role_type: AppRoleType | Unset
        if isinstance(_role_type, Unset):
            role_type = UNSET
        else:
            role_type = AppRoleType(_role_type)

        _status = d.pop("status", UNSET)
        status: AppOrgMemberStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AppOrgMemberStatus(_status)

        app_org_member = cls(
            account_id=account_id,
            created_at=created_at,
            email=email,
            id=id,
            invite_id=invite_id,
            joined_at=joined_at,
            name=name,
            role_type=role_type,
            status=status,
        )

        app_org_member.additional_properties = d
        return app_org_member

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
