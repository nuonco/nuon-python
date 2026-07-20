from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_token_type import AppTokenType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AppToken")


@_attrs_define
class AppToken:
    """
    Attributes:
        account_id (str | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        expires_at (str | Unset): claim data
        id (str | Unset):
        issued_at (str | Unset):
        issuer (str | Unset):
        name (str | Unset):
        org_id (str | Unset):
        token_type (AppTokenType | Unset):
        updated_at (str | Unset):
    """

    account_id: str | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    expires_at: str | Unset = UNSET
    id: str | Unset = UNSET
    issued_at: str | Unset = UNSET
    issuer: str | Unset = UNSET
    name: str | Unset = UNSET
    org_id: str | Unset = UNSET
    token_type: AppTokenType | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        created_at = self.created_at

        created_by_id = self.created_by_id

        expires_at = self.expires_at

        id = self.id

        issued_at = self.issued_at

        issuer = self.issuer

        name = self.name

        org_id = self.org_id

        token_type: str | Unset = UNSET
        if not isinstance(self.token_type, Unset):
            token_type = self.token_type.value

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
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if id is not UNSET:
            field_dict["id"] = id
        if issued_at is not UNSET:
            field_dict["issued_at"] = issued_at
        if issuer is not UNSET:
            field_dict["issuer"] = issuer
        if name is not UNSET:
            field_dict["name"] = name
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if token_type is not UNSET:
            field_dict["token_type"] = token_type
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("account_id", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        expires_at = d.pop("expires_at", UNSET)

        id = d.pop("id", UNSET)

        issued_at = d.pop("issued_at", UNSET)

        issuer = d.pop("issuer", UNSET)

        name = d.pop("name", UNSET)

        org_id = d.pop("org_id", UNSET)

        _token_type = d.pop("token_type", UNSET)
        token_type: AppTokenType | Unset
        if isinstance(_token_type, Unset):
            token_type = UNSET
        else:
            token_type = AppTokenType(_token_type)

        updated_at = d.pop("updated_at", UNSET)

        app_token = cls(
            account_id=account_id,
            created_at=created_at,
            created_by_id=created_by_id,
            expires_at=expires_at,
            id=id,
            issued_at=issued_at,
            issuer=issuer,
            name=name,
            org_id=org_id,
            token_type=token_type,
            updated_at=updated_at,
        )

        app_token.additional_properties = d
        return app_token

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
