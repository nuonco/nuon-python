from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubComNuoncoNuonServicesCtlApiInternalAppTokensServiceCreateTokenResponse")


@_attrs_define
class GithubComNuoncoNuonServicesCtlApiInternalAppTokensServiceCreateTokenResponse:
    """
    Attributes:
        account_id (str | Unset):
        created_at (str | Unset):
        expires_at (str | Unset):
        id (str | Unset):
        name (str | Unset):
        token (str | Unset):
    """

    account_id: str | Unset = UNSET
    created_at: str | Unset = UNSET
    expires_at: str | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        created_at = self.created_at

        expires_at = self.expires_at

        id = self.id

        name = self.name

        token = self.token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if token is not UNSET:
            field_dict["token"] = token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("account_id", UNSET)

        created_at = d.pop("created_at", UNSET)

        expires_at = d.pop("expires_at", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        token = d.pop("token", UNSET)

        github_com_nuonco_nuon_services_ctl_api_internal_app_tokens_service_create_token_response = cls(
            account_id=account_id,
            created_at=created_at,
            expires_at=expires_at,
            id=id,
            name=name,
            token=token,
        )

        github_com_nuonco_nuon_services_ctl_api_internal_app_tokens_service_create_token_response.additional_properties = d
        return github_com_nuonco_nuon_services_ctl_api_internal_app_tokens_service_create_token_response

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
