from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_managed_service_account_purpose import AppManagedServiceAccountPurpose
from ..types import UNSET, Unset

T = TypeVar("T", bound="AppManagedServiceAccount")


@_attrs_define
class AppManagedServiceAccount:
    """
    Attributes:
        account_id (str | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        instance_key (str | Unset):
        org_id (str | Unset):
        owner_id (str | Unset):
        owner_type (str | Unset):
        purpose (AppManagedServiceAccountPurpose | Unset):
        updated_at (str | Unset):
    """

    account_id: str | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    instance_key: str | Unset = UNSET
    org_id: str | Unset = UNSET
    owner_id: str | Unset = UNSET
    owner_type: str | Unset = UNSET
    purpose: AppManagedServiceAccountPurpose | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        created_at = self.created_at

        created_by_id = self.created_by_id

        instance_key = self.instance_key

        org_id = self.org_id

        owner_id = self.owner_id

        owner_type = self.owner_type

        purpose: str | Unset = UNSET
        if not isinstance(self.purpose, Unset):
            purpose = self.purpose.value

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if instance_key is not UNSET:
            field_dict["instance_key"] = instance_key
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if owner_type is not UNSET:
            field_dict["owner_type"] = owner_type
        if purpose is not UNSET:
            field_dict["purpose"] = purpose
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("account_id", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        instance_key = d.pop("instance_key", UNSET)

        org_id = d.pop("org_id", UNSET)

        owner_id = d.pop("owner_id", UNSET)

        owner_type = d.pop("owner_type", UNSET)

        _purpose = d.pop("purpose", UNSET)
        purpose: AppManagedServiceAccountPurpose | Unset
        if isinstance(_purpose, Unset):
            purpose = UNSET
        else:
            purpose = AppManagedServiceAccountPurpose(_purpose)

        updated_at = d.pop("updated_at", UNSET)

        app_managed_service_account = cls(
            account_id=account_id,
            created_at=created_at,
            created_by_id=created_by_id,
            instance_key=instance_key,
            org_id=org_id,
            owner_id=owner_id,
            owner_type=owner_type,
            purpose=purpose,
            updated_at=updated_at,
        )

        app_managed_service_account.additional_properties = d
        return app_managed_service_account

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
