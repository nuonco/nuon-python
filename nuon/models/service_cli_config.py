from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceCLIConfig")


@_attrs_define
class ServiceCLIConfig:
    """
    Attributes:
        auth_audience (str | Unset):
        auth_client_id (str | Unset):
        auth_domain (str | Unset):
        dashboard_url (str | Unset):
        nuon_auth_enabled (bool | Unset):
        root_domain (str | Unset):
    """

    auth_audience: str | Unset = UNSET
    auth_client_id: str | Unset = UNSET
    auth_domain: str | Unset = UNSET
    dashboard_url: str | Unset = UNSET
    nuon_auth_enabled: bool | Unset = UNSET
    root_domain: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auth_audience = self.auth_audience

        auth_client_id = self.auth_client_id

        auth_domain = self.auth_domain

        dashboard_url = self.dashboard_url

        nuon_auth_enabled = self.nuon_auth_enabled

        root_domain = self.root_domain

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auth_audience is not UNSET:
            field_dict["auth_audience"] = auth_audience
        if auth_client_id is not UNSET:
            field_dict["auth_client_id"] = auth_client_id
        if auth_domain is not UNSET:
            field_dict["auth_domain"] = auth_domain
        if dashboard_url is not UNSET:
            field_dict["dashboard_url"] = dashboard_url
        if nuon_auth_enabled is not UNSET:
            field_dict["nuon_auth_enabled"] = nuon_auth_enabled
        if root_domain is not UNSET:
            field_dict["root_domain"] = root_domain

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        auth_audience = d.pop("auth_audience", UNSET)

        auth_client_id = d.pop("auth_client_id", UNSET)

        auth_domain = d.pop("auth_domain", UNSET)

        dashboard_url = d.pop("dashboard_url", UNSET)

        nuon_auth_enabled = d.pop("nuon_auth_enabled", UNSET)

        root_domain = d.pop("root_domain", UNSET)

        service_cli_config = cls(
            auth_audience=auth_audience,
            auth_client_id=auth_client_id,
            auth_domain=auth_domain,
            dashboard_url=dashboard_url,
            nuon_auth_enabled=nuon_auth_enabled,
            root_domain=root_domain,
        )

        service_cli_config.additional_properties = d
        return service_cli_config

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
