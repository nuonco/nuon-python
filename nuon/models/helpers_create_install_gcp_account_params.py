from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HelpersCreateInstallGCPAccountParams")


@_attrs_define
class HelpersCreateInstallGCPAccountParams:
    """
    Attributes:
        project_id (str | Unset): ProjectID is the GCP project this install targets. Required when the org has
            the phone-home-auth feature enabled. Immutable after creation.
        region (str | Unset):
    """

    project_id: str | Unset = UNSET
    region: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_id = self.project_id

        region = self.region

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if region is not UNSET:
            field_dict["region"] = region

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        project_id = d.pop("project_id", UNSET)

        region = d.pop("region", UNSET)

        helpers_create_install_gcp_account_params = cls(
            project_id=project_id,
            region=region,
        )

        helpers_create_install_gcp_account_params.additional_properties = d
        return helpers_create_install_gcp_account_params

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
