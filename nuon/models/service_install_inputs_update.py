from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceInstallInputsUpdate")


@_attrs_define
class ServiceInstallInputsUpdate:
    """
    Attributes:
        input_config_id (str | Unset):
        keys (list[str] | Unset):
    """

    input_config_id: str | Unset = UNSET
    keys: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        input_config_id = self.input_config_id

        keys: list[str] | Unset = UNSET
        if not isinstance(self.keys, Unset):
            keys = self.keys

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if input_config_id is not UNSET:
            field_dict["input_config_id"] = input_config_id
        if keys is not UNSET:
            field_dict["keys"] = keys

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        input_config_id = d.pop("input_config_id", UNSET)

        keys = cast(list[str], d.pop("keys", UNSET))

        service_install_inputs_update = cls(
            input_config_id=input_config_id,
            keys=keys,
        )

        service_install_inputs_update.additional_properties = d
        return service_install_inputs_update

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
