from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppAzureAccount")


@_attrs_define
class AppAzureAccount:
    """
    Attributes:
        created_at (str | Unset):
        created_by_id (str | Unset):
        id (str | Unset):
        location (str | Unset):
        service_principal_app_id (str | Unset):
        service_principal_password (str | Unset):
        subscription_id (str | Unset):
        subscription_tenant_id (str | Unset):
        updated_at (str | Unset):
    """

    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    id: str | Unset = UNSET
    location: str | Unset = UNSET
    service_principal_app_id: str | Unset = UNSET
    service_principal_password: str | Unset = UNSET
    subscription_id: str | Unset = UNSET
    subscription_tenant_id: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        created_by_id = self.created_by_id

        id = self.id

        location = self.location

        service_principal_app_id = self.service_principal_app_id

        service_principal_password = self.service_principal_password

        subscription_id = self.subscription_id

        subscription_tenant_id = self.subscription_tenant_id

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if id is not UNSET:
            field_dict["id"] = id
        if location is not UNSET:
            field_dict["location"] = location
        if service_principal_app_id is not UNSET:
            field_dict["service_principal_app_id"] = service_principal_app_id
        if service_principal_password is not UNSET:
            field_dict["service_principal_password"] = service_principal_password
        if subscription_id is not UNSET:
            field_dict["subscription_id"] = subscription_id
        if subscription_tenant_id is not UNSET:
            field_dict["subscription_tenant_id"] = subscription_tenant_id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        id = d.pop("id", UNSET)

        location = d.pop("location", UNSET)

        service_principal_app_id = d.pop("service_principal_app_id", UNSET)

        service_principal_password = d.pop("service_principal_password", UNSET)

        subscription_id = d.pop("subscription_id", UNSET)

        subscription_tenant_id = d.pop("subscription_tenant_id", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        app_azure_account = cls(
            created_at=created_at,
            created_by_id=created_by_id,
            id=id,
            location=location,
            service_principal_app_id=service_principal_app_id,
            service_principal_password=service_principal_password,
            subscription_id=subscription_id,
            subscription_tenant_id=subscription_tenant_id,
            updated_at=updated_at,
        )

        app_azure_account.additional_properties = d
        return app_azure_account

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
