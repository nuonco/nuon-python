from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_org import AppOrg


T = TypeVar("T", bound="AppAppOperationRoleRule")


@_attrs_define
class AppAppOperationRoleRule:
    """
    Attributes:
        app_operation_role_config_id (str | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        id (str | Unset):
        operation (str | Unset):
        org (AppOrg | Unset):
        org_id (str | Unset):
        principal_name (str | Unset):
        principal_type (str | Unset):
        role (str | Unset):
        updated_at (str | Unset):
    """

    app_operation_role_config_id: str | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    id: str | Unset = UNSET
    operation: str | Unset = UNSET
    org: AppOrg | Unset = UNSET
    org_id: str | Unset = UNSET
    principal_name: str | Unset = UNSET
    principal_type: str | Unset = UNSET
    role: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_operation_role_config_id = self.app_operation_role_config_id

        created_at = self.created_at

        created_by_id = self.created_by_id

        id = self.id

        operation = self.operation

        org: dict[str, Any] | Unset = UNSET
        if not isinstance(self.org, Unset):
            org = self.org.to_dict()

        org_id = self.org_id

        principal_name = self.principal_name

        principal_type = self.principal_type

        role = self.role

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_operation_role_config_id is not UNSET:
            field_dict["app_operation_role_config_id"] = app_operation_role_config_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if id is not UNSET:
            field_dict["id"] = id
        if operation is not UNSET:
            field_dict["operation"] = operation
        if org is not UNSET:
            field_dict["org"] = org
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if principal_name is not UNSET:
            field_dict["principal_name"] = principal_name
        if principal_type is not UNSET:
            field_dict["principal_type"] = principal_type
        if role is not UNSET:
            field_dict["role"] = role
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_org import AppOrg

        d = dict(src_dict)
        app_operation_role_config_id = d.pop("app_operation_role_config_id", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        id = d.pop("id", UNSET)

        operation = d.pop("operation", UNSET)

        _org = d.pop("org", UNSET)
        org: AppOrg | Unset
        if isinstance(_org, Unset):
            org = UNSET
        else:
            org = AppOrg.from_dict(_org)

        org_id = d.pop("org_id", UNSET)

        principal_name = d.pop("principal_name", UNSET)

        principal_type = d.pop("principal_type", UNSET)

        role = d.pop("role", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        app_app_operation_role_rule = cls(
            app_operation_role_config_id=app_operation_role_config_id,
            created_at=created_at,
            created_by_id=created_by_id,
            id=id,
            operation=operation,
            org=org,
            org_id=org_id,
            principal_name=principal_name,
            principal_type=principal_type,
            role=role,
            updated_at=updated_at,
        )

        app_app_operation_role_rule.additional_properties = d
        return app_app_operation_role_rule

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
