from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.helpers_create_install_config_params import HelpersCreateInstallConfigParams
    from ..models.helpers_install_metadata import HelpersInstallMetadata
    from ..models.service_create_install_v2_request_aws_account import ServiceCreateInstallV2RequestAwsAccount
    from ..models.service_create_install_v2_request_azure_account import ServiceCreateInstallV2RequestAzureAccount
    from ..models.service_create_install_v2_request_gcp_account import ServiceCreateInstallV2RequestGcpAccount
    from ..models.service_create_install_v2_request_inputs import ServiceCreateInstallV2RequestInputs
    from ..models.service_create_install_v2_request_labels import ServiceCreateInstallV2RequestLabels


T = TypeVar("T", bound="ServiceCreateInstallV2Request")


@_attrs_define
class ServiceCreateInstallV2Request:
    """
    Attributes:
        app_id (str):
        name (str):
        aws_account (ServiceCreateInstallV2RequestAwsAccount | Unset):
        azure_account (ServiceCreateInstallV2RequestAzureAccount | Unset):
        gcp_account (ServiceCreateInstallV2RequestGcpAccount | Unset):
        inputs (ServiceCreateInstallV2RequestInputs | Unset):
        install_config (HelpersCreateInstallConfigParams | Unset):
        labels (ServiceCreateInstallV2RequestLabels | Unset): Labels are key/value pairs to attach to the install at
            creation time.
            They are merged into the install's existing labels (which is empty for a brand-new install).
        metadata (HelpersInstallMetadata | Unset):
    """

    app_id: str
    name: str
    aws_account: ServiceCreateInstallV2RequestAwsAccount | Unset = UNSET
    azure_account: ServiceCreateInstallV2RequestAzureAccount | Unset = UNSET
    gcp_account: ServiceCreateInstallV2RequestGcpAccount | Unset = UNSET
    inputs: ServiceCreateInstallV2RequestInputs | Unset = UNSET
    install_config: HelpersCreateInstallConfigParams | Unset = UNSET
    labels: ServiceCreateInstallV2RequestLabels | Unset = UNSET
    metadata: HelpersInstallMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_id = self.app_id

        name = self.name

        aws_account: dict[str, Any] | Unset = UNSET
        if not isinstance(self.aws_account, Unset):
            aws_account = self.aws_account.to_dict()

        azure_account: dict[str, Any] | Unset = UNSET
        if not isinstance(self.azure_account, Unset):
            azure_account = self.azure_account.to_dict()

        gcp_account: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gcp_account, Unset):
            gcp_account = self.gcp_account.to_dict()

        inputs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.inputs, Unset):
            inputs = self.inputs.to_dict()

        install_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.install_config, Unset):
            install_config = self.install_config.to_dict()

        labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "app_id": app_id,
                "name": name,
            }
        )
        if aws_account is not UNSET:
            field_dict["aws_account"] = aws_account
        if azure_account is not UNSET:
            field_dict["azure_account"] = azure_account
        if gcp_account is not UNSET:
            field_dict["gcp_account"] = gcp_account
        if inputs is not UNSET:
            field_dict["inputs"] = inputs
        if install_config is not UNSET:
            field_dict["install_config"] = install_config
        if labels is not UNSET:
            field_dict["labels"] = labels
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.helpers_create_install_config_params import HelpersCreateInstallConfigParams
        from ..models.helpers_install_metadata import HelpersInstallMetadata
        from ..models.service_create_install_v2_request_aws_account import ServiceCreateInstallV2RequestAwsAccount
        from ..models.service_create_install_v2_request_azure_account import ServiceCreateInstallV2RequestAzureAccount
        from ..models.service_create_install_v2_request_gcp_account import ServiceCreateInstallV2RequestGcpAccount
        from ..models.service_create_install_v2_request_inputs import ServiceCreateInstallV2RequestInputs
        from ..models.service_create_install_v2_request_labels import ServiceCreateInstallV2RequestLabels

        d = dict(src_dict)
        app_id = d.pop("app_id")

        name = d.pop("name")

        _aws_account = d.pop("aws_account", UNSET)
        aws_account: ServiceCreateInstallV2RequestAwsAccount | Unset
        if isinstance(_aws_account, Unset):
            aws_account = UNSET
        else:
            aws_account = ServiceCreateInstallV2RequestAwsAccount.from_dict(_aws_account)

        _azure_account = d.pop("azure_account", UNSET)
        azure_account: ServiceCreateInstallV2RequestAzureAccount | Unset
        if isinstance(_azure_account, Unset):
            azure_account = UNSET
        else:
            azure_account = ServiceCreateInstallV2RequestAzureAccount.from_dict(_azure_account)

        _gcp_account = d.pop("gcp_account", UNSET)
        gcp_account: ServiceCreateInstallV2RequestGcpAccount | Unset
        if isinstance(_gcp_account, Unset):
            gcp_account = UNSET
        else:
            gcp_account = ServiceCreateInstallV2RequestGcpAccount.from_dict(_gcp_account)

        _inputs = d.pop("inputs", UNSET)
        inputs: ServiceCreateInstallV2RequestInputs | Unset
        if isinstance(_inputs, Unset):
            inputs = UNSET
        else:
            inputs = ServiceCreateInstallV2RequestInputs.from_dict(_inputs)

        _install_config = d.pop("install_config", UNSET)
        install_config: HelpersCreateInstallConfigParams | Unset
        if isinstance(_install_config, Unset):
            install_config = UNSET
        else:
            install_config = HelpersCreateInstallConfigParams.from_dict(_install_config)

        _labels = d.pop("labels", UNSET)
        labels: ServiceCreateInstallV2RequestLabels | Unset
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = ServiceCreateInstallV2RequestLabels.from_dict(_labels)

        _metadata = d.pop("metadata", UNSET)
        metadata: HelpersInstallMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = HelpersInstallMetadata.from_dict(_metadata)

        service_create_install_v2_request = cls(
            app_id=app_id,
            name=name,
            aws_account=aws_account,
            azure_account=azure_account,
            gcp_account=gcp_account,
            inputs=inputs,
            install_config=install_config,
            labels=labels,
            metadata=metadata,
        )

        service_create_install_v2_request.additional_properties = d
        return service_create_install_v2_request

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
