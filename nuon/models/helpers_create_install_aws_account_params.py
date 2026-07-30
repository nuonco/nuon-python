from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HelpersCreateInstallAWSAccountParams")


@_attrs_define
class HelpersCreateInstallAWSAccountParams:
    """
    Attributes:
        account_id (str | Unset): AccountID is the AWS account this install targets. Required when the org has
            the phone-home-auth feature enabled, optional otherwise. Immutable after
            creation — there is deliberately no equivalent field on UpdateInstallRequest.
        connection_id (str | Unset):
        region (str | Unset):
    """

    account_id: str | Unset = UNSET
    connection_id: str | Unset = UNSET
    region: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        connection_id = self.connection_id

        region = self.region

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if connection_id is not UNSET:
            field_dict["connection_id"] = connection_id
        if region is not UNSET:
            field_dict["region"] = region

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("account_id", UNSET)

        connection_id = d.pop("connection_id", UNSET)

        region = d.pop("region", UNSET)

        helpers_create_install_aws_account_params = cls(
            account_id=account_id,
            connection_id=connection_id,
            region=region,
        )

        helpers_create_install_aws_account_params.additional_properties = d
        return helpers_create_install_aws_account_params

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
