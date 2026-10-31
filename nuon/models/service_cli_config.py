from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_min_cli_version_policy import ServiceMinCLIVersionPolicy


T = TypeVar("T", bound="ServiceCLIConfig")


@_attrs_define
class ServiceCLIConfig:
    """
    Attributes:
        auth_audience (str | Unset):
        auth_client_id (str | Unset):
        auth_domain (str | Unset):
        dashboard_url (str | Unset):
        min_cli_version (str | Unset): Deprecated: older CLIs read this warning floor. New CLIs use
            min_cli_version_policy.
        min_cli_version_policy (ServiceMinCLIVersionPolicy | Unset):
        nuon_auth_enabled (bool | Unset):
        oidc_federation_enabled (bool | Unset):
        root_domain (str | Unset):
    """

    auth_audience: str | Unset = UNSET
    auth_client_id: str | Unset = UNSET
    auth_domain: str | Unset = UNSET
    dashboard_url: str | Unset = UNSET
    min_cli_version: str | Unset = UNSET
    min_cli_version_policy: ServiceMinCLIVersionPolicy | Unset = UNSET
    nuon_auth_enabled: bool | Unset = UNSET
    oidc_federation_enabled: bool | Unset = UNSET
    root_domain: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auth_audience = self.auth_audience

        auth_client_id = self.auth_client_id

        auth_domain = self.auth_domain

        dashboard_url = self.dashboard_url

        min_cli_version = self.min_cli_version

        min_cli_version_policy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.min_cli_version_policy, Unset):
            min_cli_version_policy = self.min_cli_version_policy.to_dict()

        nuon_auth_enabled = self.nuon_auth_enabled

        oidc_federation_enabled = self.oidc_federation_enabled

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
        if min_cli_version is not UNSET:
            field_dict["min_cli_version"] = min_cli_version
        if min_cli_version_policy is not UNSET:
            field_dict["min_cli_version_policy"] = min_cli_version_policy
        if nuon_auth_enabled is not UNSET:
            field_dict["nuon_auth_enabled"] = nuon_auth_enabled
        if oidc_federation_enabled is not UNSET:
            field_dict["oidc_federation_enabled"] = oidc_federation_enabled
        if root_domain is not UNSET:
            field_dict["root_domain"] = root_domain

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_min_cli_version_policy import ServiceMinCLIVersionPolicy  # noqa: PLC0415

        d = dict(src_dict)
        auth_audience = d.pop("auth_audience", UNSET)

        auth_client_id = d.pop("auth_client_id", UNSET)

        auth_domain = d.pop("auth_domain", UNSET)

        dashboard_url = d.pop("dashboard_url", UNSET)

        min_cli_version = d.pop("min_cli_version", UNSET)

        _min_cli_version_policy = d.pop("min_cli_version_policy", UNSET)
        min_cli_version_policy: ServiceMinCLIVersionPolicy | Unset
        if isinstance(_min_cli_version_policy, Unset):
            min_cli_version_policy = UNSET
        else:
            min_cli_version_policy = ServiceMinCLIVersionPolicy.from_dict(_min_cli_version_policy)

        nuon_auth_enabled = d.pop("nuon_auth_enabled", UNSET)

        oidc_federation_enabled = d.pop("oidc_federation_enabled", UNSET)

        root_domain = d.pop("root_domain", UNSET)

        service_cli_config = cls(
            auth_audience=auth_audience,
            auth_client_id=auth_client_id,
            auth_domain=auth_domain,
            dashboard_url=dashboard_url,
            min_cli_version=min_cli_version,
            min_cli_version_policy=min_cli_version_policy,
            nuon_auth_enabled=nuon_auth_enabled,
            oidc_federation_enabled=oidc_federation_enabled,
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
