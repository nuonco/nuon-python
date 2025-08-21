from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_account_type import AppAccountType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_role import AppRole
    from ..models.permissions_set import PermissionsSet


T = TypeVar("T", bound="AppAccount")


@_attrs_define
class AppAccount:
    """
    Attributes:
        account_type (Union[Unset, AppAccountType]):
        created_at (Union[Unset, str]):
        email (Union[Unset, str]):
        id (Union[Unset, str]):
        org_ids (Union[Unset, list[str]]): ReadOnly Fields
        permissions (Union[Unset, PermissionsSet]):
        roles (Union[Unset, list['AppRole']]):
        subject (Union[Unset, str]):
        updated_at (Union[Unset, str]):
    """

    account_type: Union[Unset, AppAccountType] = UNSET
    created_at: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    org_ids: Union[Unset, list[str]] = UNSET
    permissions: Union[Unset, "PermissionsSet"] = UNSET
    roles: Union[Unset, list["AppRole"]] = UNSET
    subject: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_type: Union[Unset, str] = UNSET
        if not isinstance(self.account_type, Unset):
            account_type = self.account_type.value

        created_at = self.created_at

        email = self.email

        id = self.id

        org_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.org_ids, Unset):
            org_ids = self.org_ids

        permissions: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions.to_dict()

        roles: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.roles, Unset):
            roles = []
            for roles_item_data in self.roles:
                roles_item = roles_item_data.to_dict()
                roles.append(roles_item)

        subject = self.subject

        updated_at = self.updated_at

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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_role import AppRole
        from ..models.permissions_set import PermissionsSet

        d = dict(src_dict)
        _account_type = d.pop("account_type", UNSET)
        account_type: Union[Unset, AppAccountType]
        if isinstance(_account_type, Unset):
            account_type = UNSET
        else:
            account_type = AppAccountType(_account_type)

        created_at = d.pop("created_at", UNSET)

        email = d.pop("email", UNSET)

        id = d.pop("id", UNSET)

        org_ids = cast(list[str], d.pop("org_ids", UNSET))

        _permissions = d.pop("permissions", UNSET)
        permissions: Union[Unset, PermissionsSet]
        if isinstance(_permissions, Unset):
            permissions = UNSET
        else:
            permissions = PermissionsSet.from_dict(_permissions)

        roles = []
        _roles = d.pop("roles", UNSET)
        for roles_item_data in _roles or []:
            roles_item = AppRole.from_dict(roles_item_data)

            roles.append(roles_item)

        subject = d.pop("subject", UNSET)

        updated_at = d.pop("updated_at", UNSET)

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
