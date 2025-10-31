from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CredentialsServicePrincipalCredentials")


@_attrs_define
class CredentialsServicePrincipalCredentials:
    """
    Attributes:
        subscription_id (str | Unset):
        subscription_tenant_id (str | Unset):
    """

    subscription_id: str | Unset = UNSET
    subscription_tenant_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subscription_id = self.subscription_id

        subscription_tenant_id = self.subscription_tenant_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if subscription_id is not UNSET:
            field_dict["subscription_id"] = subscription_id
        if subscription_tenant_id is not UNSET:
            field_dict["subscription_tenant_id"] = subscription_tenant_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        subscription_id = d.pop("subscription_id", UNSET)

        subscription_tenant_id = d.pop("subscription_tenant_id", UNSET)

        credentials_service_principal_credentials = cls(
            subscription_id=subscription_id,
            subscription_tenant_id=subscription_tenant_id,
        )

        credentials_service_principal_credentials.additional_properties = d
        return credentials_service_principal_credentials

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
