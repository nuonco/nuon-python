from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.service_complete_install_step_request_install_mode import ServiceCompleteInstallStepRequestInstallMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_complete_install_step_request_aws_account import ServiceCompleteInstallStepRequestAwsAccount
    from ..models.service_complete_install_step_request_azure_account import (
        ServiceCompleteInstallStepRequestAzureAccount,
    )
    from ..models.service_complete_install_step_request_inputs import ServiceCompleteInstallStepRequestInputs
    from ..models.service_complete_install_step_request_metadata import ServiceCompleteInstallStepRequestMetadata


T = TypeVar("T", bound="ServiceCompleteInstallStepRequest")


@_attrs_define
class ServiceCompleteInstallStepRequest:
    """
    Attributes:
        name (str):
        aws_account (ServiceCompleteInstallStepRequestAwsAccount | Unset):
        azure_account (ServiceCompleteInstallStepRequestAzureAccount | Unset):
        inputs (ServiceCompleteInstallStepRequestInputs | Unset):
        install_mode (ServiceCompleteInstallStepRequestInstallMode | Unset):
        metadata (ServiceCompleteInstallStepRequestMetadata | Unset):
    """

    name: str
    aws_account: ServiceCompleteInstallStepRequestAwsAccount | Unset = UNSET
    azure_account: ServiceCompleteInstallStepRequestAzureAccount | Unset = UNSET
    inputs: ServiceCompleteInstallStepRequestInputs | Unset = UNSET
    install_mode: ServiceCompleteInstallStepRequestInstallMode | Unset = UNSET
    metadata: ServiceCompleteInstallStepRequestMetadata | Unset = UNSET
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

        install_mode: str | Unset = UNSET
        if not isinstance(self.install_mode, Unset):
            install_mode = self.install_mode.value

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
        if install_mode is not UNSET:
            field_dict["install_mode"] = install_mode
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_complete_install_step_request_aws_account import (
            ServiceCompleteInstallStepRequestAwsAccount,
        )
        from ..models.service_complete_install_step_request_azure_account import (
            ServiceCompleteInstallStepRequestAzureAccount,
        )
        from ..models.service_complete_install_step_request_inputs import ServiceCompleteInstallStepRequestInputs
        from ..models.service_complete_install_step_request_metadata import ServiceCompleteInstallStepRequestMetadata

        d = dict(src_dict)
        name = d.pop("name")

        _aws_account = d.pop("aws_account", UNSET)
        aws_account: ServiceCompleteInstallStepRequestAwsAccount | Unset
        if isinstance(_aws_account, Unset):
            aws_account = UNSET
        else:
            aws_account = ServiceCompleteInstallStepRequestAwsAccount.from_dict(_aws_account)

        _azure_account = d.pop("azure_account", UNSET)
        azure_account: ServiceCompleteInstallStepRequestAzureAccount | Unset
        if isinstance(_azure_account, Unset):
            azure_account = UNSET
        else:
            azure_account = ServiceCompleteInstallStepRequestAzureAccount.from_dict(_azure_account)

        _inputs = d.pop("inputs", UNSET)
        inputs: ServiceCompleteInstallStepRequestInputs | Unset
        if isinstance(_inputs, Unset):
            inputs = UNSET
        else:
            inputs = ServiceCompleteInstallStepRequestInputs.from_dict(_inputs)

        _install_mode = d.pop("install_mode", UNSET)
        install_mode: ServiceCompleteInstallStepRequestInstallMode | Unset
        if isinstance(_install_mode, Unset):
            install_mode = UNSET
        else:
            install_mode = ServiceCompleteInstallStepRequestInstallMode(_install_mode)

        _metadata = d.pop("metadata", UNSET)
        metadata: ServiceCompleteInstallStepRequestMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ServiceCompleteInstallStepRequestMetadata.from_dict(_metadata)

        service_complete_install_step_request = cls(
            name=name,
            aws_account=aws_account,
            azure_account=azure_account,
            inputs=inputs,
            install_mode=install_mode,
            metadata=metadata,
        )

        service_complete_install_step_request.additional_properties = d
        return service_complete_install_step_request

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
