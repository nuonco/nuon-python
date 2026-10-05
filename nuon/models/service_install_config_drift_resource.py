from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceInstallConfigDriftResource")


@_attrs_define
class ServiceInstallConfigDriftResource:
    """
    Attributes:
        applied_app_config_id (str | Unset):
        drifted (bool | Unset):
    """

    applied_app_config_id: str | Unset = UNSET
    drifted: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        applied_app_config_id = self.applied_app_config_id

        drifted = self.drifted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if applied_app_config_id is not UNSET:
            field_dict["applied_app_config_id"] = applied_app_config_id
        if drifted is not UNSET:
            field_dict["drifted"] = drifted

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        applied_app_config_id = d.pop("applied_app_config_id", UNSET)

        drifted = d.pop("drifted", UNSET)

        service_install_config_drift_resource = cls(
            applied_app_config_id=applied_app_config_id,
            drifted=drifted,
        )

        service_install_config_drift_resource.additional_properties = d
        return service_install_config_drift_resource

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
