from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubComNuoncoNuonServicesCtlApiInternalAppAccountsServiceStaticTokenResponse")


@_attrs_define
class GithubComNuoncoNuonServicesCtlApiInternalAppAccountsServiceStaticTokenResponse:
    """
    Attributes:
        api_token (str | Unset):
        id (str | Unset):
    """

    api_token: str | Unset = UNSET
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_token = self.api_token

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api_token is not UNSET:
            field_dict["api_token"] = api_token
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_token = d.pop("api_token", UNSET)

        id = d.pop("id", UNSET)

        github_com_nuonco_nuon_services_ctl_api_internal_app_accounts_service_static_token_response = cls(
            api_token=api_token,
            id=id,
        )

        github_com_nuonco_nuon_services_ctl_api_internal_app_accounts_service_static_token_response.additional_properties = d
        return github_com_nuonco_nuon_services_ctl_api_internal_app_accounts_service_static_token_response

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
