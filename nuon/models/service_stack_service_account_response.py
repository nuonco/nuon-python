from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceStackServiceAccountResponse")


@_attrs_define
class ServiceStackServiceAccountResponse:
    """
    Attributes:
        account_id (str | Unset):
        email (str | Unset):
        expires_at (str | Unset): ExpiresAt is the expiry of the longest-lived usable token; zero when
            HasLiveToken is false.
        has_live_token (bool | Unset): HasLiveToken is false whether no token was ever created or every one has
            expired or been revoked; the caller fixes both the same way.
        runner_api_url (str | Unset): Without it a dashboard points the module's provider at production.
    """

    account_id: str | Unset = UNSET
    email: str | Unset = UNSET
    expires_at: str | Unset = UNSET
    has_live_token: bool | Unset = UNSET
    runner_api_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        email = self.email

        expires_at = self.expires_at

        has_live_token = self.has_live_token

        runner_api_url = self.runner_api_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if email is not UNSET:
            field_dict["email"] = email
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if has_live_token is not UNSET:
            field_dict["has_live_token"] = has_live_token
        if runner_api_url is not UNSET:
            field_dict["runner_api_url"] = runner_api_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("account_id", UNSET)

        email = d.pop("email", UNSET)

        expires_at = d.pop("expires_at", UNSET)

        has_live_token = d.pop("has_live_token", UNSET)

        runner_api_url = d.pop("runner_api_url", UNSET)

        service_stack_service_account_response = cls(
            account_id=account_id,
            email=email,
            expires_at=expires_at,
            has_live_token=has_live_token,
            runner_api_url=runner_api_url,
        )

        service_stack_service_account_response.additional_properties = d
        return service_stack_service_account_response

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
