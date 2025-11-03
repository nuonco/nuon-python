from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_account_type import AppAccountType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_role import AppRole
    from ..models.app_user_journey import AppUserJourney
    from ..models.permissions_set import PermissionsSet


T = TypeVar("T", bound="AppAccount")


@_attrs_define
class AppAccount:
    """
    Attributes:
        account_type (AppAccountType | Unset):
        created_at (str | Unset):
        email (str | Unset):
        id (str | Unset):
        org_ids (list[str] | Unset): ReadOnly Fields
        permissions (PermissionsSet | Unset):
        roles (list[AppRole] | Unset):
        subject (str | Unset):
        updated_at (str | Unset):
        user_journeys (list[AppUserJourney] | Unset):
    """

    account_type: AppAccountType | Unset = UNSET
    created_at: str | Unset = UNSET
    email: str | Unset = UNSET
    id: str | Unset = UNSET
    org_ids: list[str] | Unset = UNSET
    permissions: PermissionsSet | Unset = UNSET
    roles: list[AppRole] | Unset = UNSET
    subject: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    user_journeys: list[AppUserJourney] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_type: str | Unset = UNSET
        if not isinstance(self.account_type, Unset):
            account_type = self.account_type.value

        created_at = self.created_at

        email = self.email

        id = self.id

        org_ids: list[str] | Unset = UNSET
        if not isinstance(self.org_ids, Unset):
            org_ids = self.org_ids

        permissions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions.to_dict()

        roles: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.roles, Unset):
            roles = []
            for roles_item_data in self.roles:
                roles_item = roles_item_data.to_dict()
                roles.append(roles_item)

        subject = self.subject

        updated_at = self.updated_at

        user_journeys: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.user_journeys, Unset):
            user_journeys = []
            for user_journeys_item_data in self.user_journeys:
                user_journeys_item = user_journeys_item_data.to_dict()
                user_journeys.append(user_journeys_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_type is not UNSET:
            field_dict["account_type"] = account_type
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if email is not UNSET:
            field_dict["email"] = email
        if id is not UNSET:
            field_dict["id"] = id
        if org_ids is not UNSET:
            field_dict["org_ids"] = org_ids
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if roles is not UNSET:
            field_dict["roles"] = roles
        if subject is not UNSET:
            field_dict["subject"] = subject
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if user_journeys is not UNSET:
            field_dict["user_journeys"] = user_journeys

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_role import AppRole
        from ..models.app_user_journey import AppUserJourney
        from ..models.permissions_set import PermissionsSet

        d = dict(src_dict)
        _account_type = d.pop("account_type", UNSET)
        account_type: AppAccountType | Unset
        if isinstance(_account_type, Unset):
            account_type = UNSET
        else:
            account_type = AppAccountType(_account_type)

        created_at = d.pop("created_at", UNSET)

        email = d.pop("email", UNSET)

        id = d.pop("id", UNSET)

        org_ids = cast(list[str], d.pop("org_ids", UNSET))

        _permissions = d.pop("permissions", UNSET)
        permissions: PermissionsSet | Unset
        if isinstance(_permissions, Unset):
            permissions = UNSET
        else:
            permissions = PermissionsSet.from_dict(_permissions)

        _roles = d.pop("roles", UNSET)
        roles: list[AppRole] | Unset = UNSET
        if _roles is not UNSET:
            roles = []
            for roles_item_data in _roles:
                roles_item = AppRole.from_dict(roles_item_data)

                roles.append(roles_item)

        subject = d.pop("subject", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        _user_journeys = d.pop("user_journeys", UNSET)
        user_journeys: list[AppUserJourney] | Unset = UNSET
        if _user_journeys is not UNSET:
            user_journeys = []
            for user_journeys_item_data in _user_journeys:
                user_journeys_item = AppUserJourney.from_dict(user_journeys_item_data)

                user_journeys.append(user_journeys_item)

        app_account = cls(
            account_type=account_type,
            created_at=created_at,
            email=email,
            id=id,
            org_ids=org_ids,
            permissions=permissions,
            roles=roles,
            subject=subject,
            updated_at=updated_at,
            user_journeys=user_journeys,
        )

        app_account.additional_properties = d
        return app_account

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
