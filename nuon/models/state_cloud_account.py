from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.state_aws_cloud_account import StateAWSCloudAccount
    from ..models.state_azure_cloud_account import StateAzureCloudAccount


T = TypeVar("T", bound="StateCloudAccount")


@_attrs_define
class StateCloudAccount:
    """
    Attributes:
        aws (StateAWSCloudAccount | Unset):
        azure (StateAzureCloudAccount | Unset):
    """

    aws: StateAWSCloudAccount | Unset = UNSET
    azure: StateAzureCloudAccount | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aws: dict[str, Any] | Unset = UNSET
        if not isinstance(self.aws, Unset):
            aws = self.aws.to_dict()

        azure: dict[str, Any] | Unset = UNSET
        if not isinstance(self.azure, Unset):
            azure = self.azure.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aws is not UNSET:
            field_dict["aws"] = aws
        if azure is not UNSET:
            field_dict["azure"] = azure

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.state_aws_cloud_account import StateAWSCloudAccount
        from ..models.state_azure_cloud_account import StateAzureCloudAccount

        d = dict(src_dict)
        _aws = d.pop("aws", UNSET)
        aws: StateAWSCloudAccount | Unset
        if isinstance(_aws, Unset):
            aws = UNSET
        else:
            aws = StateAWSCloudAccount.from_dict(_aws)

        _azure = d.pop("azure", UNSET)
        azure: StateAzureCloudAccount | Unset
        if isinstance(_azure, Unset):
            azure = UNSET
        else:
            azure = StateAzureCloudAccount.from_dict(_azure)

        state_cloud_account = cls(
            aws=aws,
            azure=azure,
        )

        state_cloud_account.additional_properties = d
        return state_cloud_account

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
