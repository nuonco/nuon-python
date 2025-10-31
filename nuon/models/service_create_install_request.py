from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.helpers_create_install_config_params import HelpersCreateInstallConfigParams
    from ..models.helpers_install_metadata import HelpersInstallMetadata
    from ..models.service_create_install_request_aws_account import ServiceCreateInstallRequestAwsAccount
    from ..models.service_create_install_request_azure_account import ServiceCreateInstallRequestAzureAccount
    from ..models.service_create_install_request_inputs import ServiceCreateInstallRequestInputs


T = TypeVar("T", bound="ServiceCreateInstallRequest")


@_attrs_define
class ServiceCreateInstallRequest:
    """
    Attributes:
        name (str):
        aws_account (ServiceCreateInstallRequestAwsAccount | Unset):
        azure_account (ServiceCreateInstallRequestAzureAccount | Unset):
        inputs (ServiceCreateInstallRequestInputs | Unset):
        install_config (HelpersCreateInstallConfigParams | Unset):
        metadata (HelpersInstallMetadata | Unset):
    """

    name: str
    aws_account: ServiceCreateInstallRequestAwsAccount | Unset = UNSET
    azure_account: ServiceCreateInstallRequestAzureAccount | Unset = UNSET
    inputs: ServiceCreateInstallRequestInputs | Unset = UNSET
    install_config: HelpersCreateInstallConfigParams | Unset = UNSET
    metadata: HelpersInstallMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        aws_account: dict[str, Any] | Unset = UNSET
        if not isinstance(self.aws_account, Unset):
            aws_account = self.aws_account.to_dict()

        azure_account: dict[str, Any] | Unset = UNSET
        if not isinstance(self.azure_account, Unset):
            azure_account = self.azure_account.to_dict()

        inputs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.inputs, Unset):
            inputs = self.inputs.to_dict()

        install_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.install_config, Unset):
            install_config = self.install_config.to_dict()

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if aws_account is not UNSET:
            field_dict["aws_account"] = aws_account
        if azure_account is not UNSET:
            field_dict["azure_account"] = azure_account
        if inputs is not UNSET:
            field_dict["inputs"] = inputs
        if install_config is not UNSET:
            field_dict["install_config"] = install_config
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.helpers_create_install_config_params import HelpersCreateInstallConfigParams
        from ..models.helpers_install_metadata import HelpersInstallMetadata
        from ..models.service_create_install_request_aws_account import ServiceCreateInstallRequestAwsAccount
        from ..models.service_create_install_request_azure_account import ServiceCreateInstallRequestAzureAccount
        from ..models.service_create_install_request_inputs import ServiceCreateInstallRequestInputs

        d = dict(src_dict)
        name = d.pop("name")

        _aws_account = d.pop("aws_account", UNSET)
        aws_account: ServiceCreateInstallRequestAwsAccount | Unset
        if isinstance(_aws_account, Unset):
            aws_account = UNSET
        else:
            aws_account = ServiceCreateInstallRequestAwsAccount.from_dict(_aws_account)

        _azure_account = d.pop("azure_account", UNSET)
        azure_account: ServiceCreateInstallRequestAzureAccount | Unset
        if isinstance(_azure_account, Unset):
            azure_account = UNSET
        else:
            azure_account = ServiceCreateInstallRequestAzureAccount.from_dict(_azure_account)

        _inputs = d.pop("inputs", UNSET)
        inputs: ServiceCreateInstallRequestInputs | Unset
        if isinstance(_inputs, Unset):
            inputs = UNSET
        else:
            inputs = ServiceCreateInstallRequestInputs.from_dict(_inputs)

        _install_config = d.pop("install_config", UNSET)
        install_config: HelpersCreateInstallConfigParams | Unset
        if isinstance(_install_config, Unset):
            install_config = UNSET
        else:
            install_config = HelpersCreateInstallConfigParams.from_dict(_install_config)

        _metadata = d.pop("metadata", UNSET)
        metadata: HelpersInstallMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = HelpersInstallMetadata.from_dict(_metadata)

        service_create_install_request = cls(
            name=name,
            aws_account=aws_account,
            azure_account=azure_account,
            inputs=inputs,
            install_config=install_config,
            metadata=metadata,
        )

        service_create_install_request.additional_properties = d
        return service_create_install_request

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
