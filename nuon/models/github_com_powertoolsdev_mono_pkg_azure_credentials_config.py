from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.credentials_service_principal_credentials import CredentialsServicePrincipalCredentials


T = TypeVar("T", bound="GithubComPowertoolsdevMonoPkgAzureCredentialsConfig")


@_attrs_define
class GithubComPowertoolsdevMonoPkgAzureCredentialsConfig:
    """
    Attributes:
        service_principal (CredentialsServicePrincipalCredentials | Unset):
        use_default (bool | Unset):
    """

    service_principal: CredentialsServicePrincipalCredentials | Unset = UNSET
    use_default: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        service_principal: dict[str, Any] | Unset = UNSET
        if not isinstance(self.service_principal, Unset):
            service_principal = self.service_principal.to_dict()

        use_default = self.use_default

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service_principal is not UNSET:
            field_dict["service_principal"] = service_principal
        if use_default is not UNSET:
            field_dict["use_default"] = use_default

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.credentials_service_principal_credentials import CredentialsServicePrincipalCredentials

        d = dict(src_dict)
        _service_principal = d.pop("service_principal", UNSET)
        service_principal: CredentialsServicePrincipalCredentials | Unset
        if isinstance(_service_principal, Unset):
            service_principal = UNSET
        else:
            service_principal = CredentialsServicePrincipalCredentials.from_dict(_service_principal)

        use_default = d.pop("use_default", UNSET)

        github_com_powertoolsdev_mono_pkg_azure_credentials_config = cls(
            service_principal=service_principal,
            use_default=use_default,
        )

        github_com_powertoolsdev_mono_pkg_azure_credentials_config.additional_properties = d
        return github_com_powertoolsdev_mono_pkg_azure_credentials_config

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
