from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.configs_oci_registry_type import ConfigsOCIRegistryType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.configs_oci_registry_auth import ConfigsOCIRegistryAuth
    from ..models.github_com_powertoolsdev_mono_pkg_aws_credentials_config import (
        GithubComPowertoolsdevMonoPkgAwsCredentialsConfig,
    )
    from ..models.github_com_powertoolsdev_mono_pkg_azure_credentials_config import (
        GithubComPowertoolsdevMonoPkgAzureCredentialsConfig,
    )


T = TypeVar("T", bound="ConfigsOCIRegistryRepository")


@_attrs_define
class ConfigsOCIRegistryRepository:
    """
    Attributes:
        acrauth (Union[Unset, GithubComPowertoolsdevMonoPkgAzureCredentialsConfig]):
        ecrauth (Union[Unset, GithubComPowertoolsdevMonoPkgAwsCredentialsConfig]):
        login_server (Union[Unset, str]):
        ociauth (Union[Unset, ConfigsOCIRegistryAuth]):
        plugin (Union[Unset, str]):
        region (Union[Unset, str]):
        registry_type (Union[Unset, ConfigsOCIRegistryType]):
        repository (Union[Unset, str]): based on the type of access, either the repository (ecr) or login server (acr)
            will be provided.
    """

    acrauth: Union[Unset, "GithubComPowertoolsdevMonoPkgAzureCredentialsConfig"] = UNSET
    ecrauth: Union[Unset, "GithubComPowertoolsdevMonoPkgAwsCredentialsConfig"] = UNSET
    login_server: Union[Unset, str] = UNSET
    ociauth: Union[Unset, "ConfigsOCIRegistryAuth"] = UNSET
    plugin: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    registry_type: Union[Unset, ConfigsOCIRegistryType] = UNSET
    repository: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        acrauth: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.acrauth, Unset):
            acrauth = self.acrauth.to_dict()

        ecrauth: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ecrauth, Unset):
            ecrauth = self.ecrauth.to_dict()

        login_server = self.login_server

        ociauth: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ociauth, Unset):
            ociauth = self.ociauth.to_dict()

        plugin = self.plugin

        region = self.region

        registry_type: Union[Unset, str] = UNSET
        if not isinstance(self.registry_type, Unset):
            registry_type = self.registry_type.value

        repository = self.repository

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if acrauth is not UNSET:
            field_dict["acrauth"] = acrauth
        if ecrauth is not UNSET:
            field_dict["ecrauth"] = ecrauth
        if login_server is not UNSET:
            field_dict["loginServer"] = login_server
        if ociauth is not UNSET:
            field_dict["ociauth"] = ociauth
        if plugin is not UNSET:
            field_dict["plugin"] = plugin
        if region is not UNSET:
            field_dict["region"] = region
        if registry_type is not UNSET:
            field_dict["registryType"] = registry_type
        if repository is not UNSET:
            field_dict["repository"] = repository

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.configs_oci_registry_auth import ConfigsOCIRegistryAuth
        from ..models.github_com_powertoolsdev_mono_pkg_aws_credentials_config import (
            GithubComPowertoolsdevMonoPkgAwsCredentialsConfig,
        )
        from ..models.github_com_powertoolsdev_mono_pkg_azure_credentials_config import (
            GithubComPowertoolsdevMonoPkgAzureCredentialsConfig,
        )

        d = dict(src_dict)
        _acrauth = d.pop("acrauth", UNSET)
        acrauth: Union[Unset, GithubComPowertoolsdevMonoPkgAzureCredentialsConfig]
        if isinstance(_acrauth, Unset):
            acrauth = UNSET
        else:
            acrauth = GithubComPowertoolsdevMonoPkgAzureCredentialsConfig.from_dict(_acrauth)

        _ecrauth = d.pop("ecrauth", UNSET)
        ecrauth: Union[Unset, GithubComPowertoolsdevMonoPkgAwsCredentialsConfig]
        if isinstance(_ecrauth, Unset):
            ecrauth = UNSET
        else:
            ecrauth = GithubComPowertoolsdevMonoPkgAwsCredentialsConfig.from_dict(_ecrauth)

        login_server = d.pop("loginServer", UNSET)

        _ociauth = d.pop("ociauth", UNSET)
        ociauth: Union[Unset, ConfigsOCIRegistryAuth]
        if isinstance(_ociauth, Unset):
            ociauth = UNSET
        else:
            ociauth = ConfigsOCIRegistryAuth.from_dict(_ociauth)

        plugin = d.pop("plugin", UNSET)

        region = d.pop("region", UNSET)

        _registry_type = d.pop("registryType", UNSET)
        registry_type: Union[Unset, ConfigsOCIRegistryType]
        if isinstance(_registry_type, Unset):
            registry_type = UNSET
        else:
            registry_type = ConfigsOCIRegistryType(_registry_type)

        repository = d.pop("repository", UNSET)

        configs_oci_registry_repository = cls(
            acrauth=acrauth,
            ecrauth=ecrauth,
            login_server=login_server,
            ociauth=ociauth,
            plugin=plugin,
            region=region,
            registry_type=registry_type,
            repository=repository,
        )

        configs_oci_registry_repository.additional_properties = d
        return configs_oci_registry_repository

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
