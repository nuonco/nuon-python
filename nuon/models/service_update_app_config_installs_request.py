from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceUpdateAppConfigInstallsRequest")


@_attrs_define
class ServiceUpdateAppConfigInstallsRequest:
    """
    Attributes:
        install_i_ds (list[str] | Unset):
        update_all (bool | Unset):
    """

    install_i_ds: list[str] | Unset = UNSET
    update_all: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        install_i_ds: list[str] | Unset = UNSET
        if not isinstance(self.install_i_ds, Unset):
            install_i_ds = self.install_i_ds

        update_all = self.update_all

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if install_i_ds is not UNSET:
            field_dict["installIDs"] = install_i_ds
        if update_all is not UNSET:
            field_dict["updateAll"] = update_all

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        install_i_ds = cast(list[str], d.pop("installIDs", UNSET))

        update_all = d.pop("updateAll", UNSET)

        service_update_app_config_installs_request = cls(
            install_i_ds=install_i_ds,
            update_all=update_all,
        )

        service_update_app_config_installs_request.additional_properties = d
        return service_update_app_config_installs_request

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
