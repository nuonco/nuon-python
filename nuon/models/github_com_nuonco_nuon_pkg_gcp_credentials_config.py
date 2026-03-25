from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubComNuoncoNuonPkgGcpCredentialsConfig")


@_attrs_define
class GithubComNuoncoNuonPkgGcpCredentialsConfig:
    """
    Attributes:
        impersonate_service_account (str | Unset):
        project_id (str | Unset):
        region (str | Unset):
    """

    impersonate_service_account: str | Unset = UNSET
    project_id: str | Unset = UNSET
    region: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        impersonate_service_account = self.impersonate_service_account

        project_id = self.project_id

        region = self.region

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if impersonate_service_account is not UNSET:
            field_dict["impersonate_service_account"] = impersonate_service_account
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if region is not UNSET:
            field_dict["region"] = region

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        impersonate_service_account = d.pop("impersonate_service_account", UNSET)

        project_id = d.pop("project_id", UNSET)

        region = d.pop("region", UNSET)

        github_com_nuonco_nuon_pkg_gcp_credentials_config = cls(
            impersonate_service_account=impersonate_service_account,
            project_id=project_id,
            region=region,
        )

        github_com_nuonco_nuon_pkg_gcp_credentials_config.additional_properties = d
        return github_com_nuonco_nuon_pkg_gcp_credentials_config

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
