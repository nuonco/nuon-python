from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppPhoneHomeAuthStatus")


@_attrs_define
class AppPhoneHomeAuthStatus:
    """
    Attributes:
        last_rejected_at (str | Unset):
        last_verified_at (str | Unset):
        provisioned_at (str | Unset): ProvisionedAt is omitzero because recordPhoneHomeAuthResult can create the column
            from an empty struct, so a row can carry verification timestamps but no
            provisioning one. Serializing that as year 1 would render as a bogus timestamp.
    """

    last_rejected_at: str | Unset = UNSET
    last_verified_at: str | Unset = UNSET
    provisioned_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        last_rejected_at = self.last_rejected_at

        last_verified_at = self.last_verified_at

        provisioned_at = self.provisioned_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if last_rejected_at is not UNSET:
            field_dict["last_rejected_at"] = last_rejected_at
        if last_verified_at is not UNSET:
            field_dict["last_verified_at"] = last_verified_at
        if provisioned_at is not UNSET:
            field_dict["provisioned_at"] = provisioned_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        last_rejected_at = d.pop("last_rejected_at", UNSET)

        last_verified_at = d.pop("last_verified_at", UNSET)

        provisioned_at = d.pop("provisioned_at", UNSET)

        app_phone_home_auth_status = cls(
            last_rejected_at=last_rejected_at,
            last_verified_at=last_verified_at,
            provisioned_at=provisioned_at,
        )

        app_phone_home_auth_status.additional_properties = d
        return app_phone_home_auth_status

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
