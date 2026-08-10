from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_role_type import AppRoleType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_account import AppAccount
    from ..models.app_policy import AppPolicy


T = TypeVar("T", bound="AppRole")


@_attrs_define
class AppRole:
    """
    Attributes:
        applies_to (list[str] | Unset):
        created_by (AppAccount | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        description (str | Unset):
        id (str | Unset):
        managed (bool | Unset):
        policies (list[AppPolicy] | Unset):
        role_type (AppRoleType | Unset):
        title (str | Unset): display + assignability metadata; the single source of truth read by
            GET /v1/roles and every role picker. Managed roles are kept in sync
            with standardOrgRoles by the authz reconciler.
        updated_at (str | Unset):
    """

    applies_to: list[str] | Unset = UNSET
    created_by: AppAccount | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    description: str | Unset = UNSET
    id: str | Unset = UNSET
    managed: bool | Unset = UNSET
    policies: list[AppPolicy] | Unset = UNSET
    role_type: AppRoleType | Unset = UNSET
    title: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        applies_to: list[str] | Unset = UNSET
        if not isinstance(self.applies_to, Unset):
            applies_to = self.applies_to

        created_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        created_at = self.created_at

        created_by_id = self.created_by_id

        description = self.description

        id = self.id

        managed = self.managed

        policies: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.policies, Unset):
            policies = []
            for policies_item_data in self.policies:
                policies_item = policies_item_data.to_dict()
                policies.append(policies_item)

        role_type: str | Unset = UNSET
        if not isinstance(self.role_type, Unset):
            role_type = self.role_type.value

        title = self.title

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if applies_to is not UNSET:
            field_dict["applies_to"] = applies_to
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if managed is not UNSET:
            field_dict["managed"] = managed
        if policies is not UNSET:
            field_dict["policies"] = policies
        if role_type is not UNSET:
            field_dict["role_type"] = role_type
        if title is not UNSET:
            field_dict["title"] = title
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_account import AppAccount
        from ..models.app_policy import AppPolicy

        d = dict(src_dict)
        applies_to = cast(list[str], d.pop("applies_to", UNSET))

        _created_by = d.pop("createdBy", UNSET)
        created_by: AppAccount | Unset
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = AppAccount.from_dict(_created_by)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        managed = d.pop("managed", UNSET)

        _policies = d.pop("policies", UNSET)
        policies: list[AppPolicy] | Unset = UNSET
        if _policies is not UNSET:
            policies = []
            for policies_item_data in _policies:
                policies_item = AppPolicy.from_dict(policies_item_data)

                policies.append(policies_item)

        _role_type = d.pop("role_type", UNSET)
        role_type: AppRoleType | Unset
        if isinstance(_role_type, Unset):
            role_type = UNSET
        else:
            role_type = AppRoleType(_role_type)

        title = d.pop("title", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        app_role = cls(
            applies_to=applies_to,
            created_by=created_by,
            created_at=created_at,
            created_by_id=created_by_id,
            description=description,
            id=id,
            managed=managed,
            policies=policies,
            role_type=role_type,
            title=title,
            updated_at=updated_at,
        )

        app_role.additional_properties = d
        return app_role

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
