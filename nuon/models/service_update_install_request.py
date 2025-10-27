from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.helpers_install_metadata import HelpersInstallMetadata
    from ..models.service_patch_install_config_params import ServicePatchInstallConfigParams


T = TypeVar("T", bound="ServiceUpdateInstallRequest")


@_attrs_define
class ServiceUpdateInstallRequest:
    """
    Attributes:
        install_config (Union[Unset, ServicePatchInstallConfigParams]):
        metadata (Union[Unset, HelpersInstallMetadata]):
        name (Union[Unset, str]):
    """

    install_config: Union[Unset, "ServicePatchInstallConfigParams"] = UNSET
    metadata: Union[Unset, "HelpersInstallMetadata"] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        install_config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.install_config, Unset):
            install_config = self.install_config.to_dict()

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if install_config is not UNSET:
            field_dict["install_config"] = install_config
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.helpers_install_metadata import HelpersInstallMetadata
        from ..models.service_patch_install_config_params import ServicePatchInstallConfigParams

        d = dict(src_dict)
        _install_config = d.pop("install_config", UNSET)
        install_config: Union[Unset, ServicePatchInstallConfigParams]
        if isinstance(_install_config, Unset):
            install_config = UNSET
        else:
            install_config = ServicePatchInstallConfigParams.from_dict(_install_config)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, HelpersInstallMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = HelpersInstallMetadata.from_dict(_metadata)

        name = d.pop("name", UNSET)

        service_update_install_request = cls(
            install_config=install_config,
            metadata=metadata,
            name=name,
        )

        service_update_install_request.additional_properties = d
        return service_update_install_request

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
