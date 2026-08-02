from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceExchangeOIDCTokenResponse")


@_attrs_define
class ServiceExchangeOIDCTokenResponse:
    """
    Attributes:
        authenticated (bool | Unset):
        expires_at (str | Unset):
        org_id (str | Unset):
        role (str | Unset):
        token (str | Unset):
        trust_policy_id (str | Unset):
    """

    authenticated: bool | Unset = UNSET
    expires_at: str | Unset = UNSET
    org_id: str | Unset = UNSET
    role: str | Unset = UNSET
    token: str | Unset = UNSET
    trust_policy_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        authenticated = self.authenticated

        expires_at = self.expires_at

        org_id = self.org_id

        role = self.role

        token = self.token

        trust_policy_id = self.trust_policy_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if authenticated is not UNSET:
            field_dict["authenticated"] = authenticated
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if role is not UNSET:
            field_dict["role"] = role
        if token is not UNSET:
            field_dict["token"] = token
        if trust_policy_id is not UNSET:
            field_dict["trust_policy_id"] = trust_policy_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        authenticated = d.pop("authenticated", UNSET)

        expires_at = d.pop("expires_at", UNSET)

        org_id = d.pop("org_id", UNSET)

        role = d.pop("role", UNSET)

        token = d.pop("token", UNSET)

        trust_policy_id = d.pop("trust_policy_id", UNSET)

        service_exchange_oidc_token_response = cls(
            authenticated=authenticated,
            expires_at=expires_at,
            org_id=org_id,
            role=role,
            token=token,
            trust_policy_id=trust_policy_id,
        )

        service_exchange_oidc_token_response.additional_properties = d
        return service_exchange_oidc_token_response

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
