from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_com_nuonco_nuon_pkg_aws_credentials_config import GithubComNuoncoNuonPkgAwsCredentialsConfig
    from ..models.github_com_nuonco_nuon_pkg_azure_credentials_config import (
        GithubComNuoncoNuonPkgAzureCredentialsConfig,
    )


T = TypeVar("T", bound="PlantypesPlanAuth")


@_attrs_define
class PlantypesPlanAuth:
    """
    Attributes:
        aws_auth (GithubComNuoncoNuonPkgAwsCredentialsConfig | Unset):
        azure_auth (GithubComNuoncoNuonPkgAzureCredentialsConfig | Unset):
    """

    aws_auth: GithubComNuoncoNuonPkgAwsCredentialsConfig | Unset = UNSET
    azure_auth: GithubComNuoncoNuonPkgAzureCredentialsConfig | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aws_auth: dict[str, Any] | Unset = UNSET
        if not isinstance(self.aws_auth, Unset):
            aws_auth = self.aws_auth.to_dict()

        azure_auth: dict[str, Any] | Unset = UNSET
        if not isinstance(self.azure_auth, Unset):
            azure_auth = self.azure_auth.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aws_auth is not UNSET:
            field_dict["aws_auth"] = aws_auth
        if azure_auth is not UNSET:
            field_dict["azure_auth"] = azure_auth

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_com_nuonco_nuon_pkg_aws_credentials_config import (
            GithubComNuoncoNuonPkgAwsCredentialsConfig,
        )
        from ..models.github_com_nuonco_nuon_pkg_azure_credentials_config import (
            GithubComNuoncoNuonPkgAzureCredentialsConfig,
        )

        d = dict(src_dict)
        _aws_auth = d.pop("aws_auth", UNSET)
        aws_auth: GithubComNuoncoNuonPkgAwsCredentialsConfig | Unset
        if isinstance(_aws_auth, Unset):
            aws_auth = UNSET
        else:
            aws_auth = GithubComNuoncoNuonPkgAwsCredentialsConfig.from_dict(_aws_auth)

        _azure_auth = d.pop("azure_auth", UNSET)
        azure_auth: GithubComNuoncoNuonPkgAzureCredentialsConfig | Unset
        if isinstance(_azure_auth, Unset):
            azure_auth = UNSET
        else:
            azure_auth = GithubComNuoncoNuonPkgAzureCredentialsConfig.from_dict(_azure_auth)

        plantypes_plan_auth = cls(
            aws_auth=aws_auth,
            azure_auth=azure_auth,
        )

        plantypes_plan_auth.additional_properties = d
        return plantypes_plan_auth

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
