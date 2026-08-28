from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceUpdateAppBranchConfigRequest")


@_attrs_define
class ServiceUpdateAppBranchConfigRequest:
    """
    Attributes:
        disable_branch_triggers (bool | Unset):
    """

    disable_branch_triggers: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        disable_branch_triggers = self.disable_branch_triggers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if disable_branch_triggers is not UNSET:
            field_dict["disable_branch_triggers"] = disable_branch_triggers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        disable_branch_triggers = d.pop("disable_branch_triggers", UNSET)

        service_update_app_branch_config_request = cls(
            disable_branch_triggers=disable_branch_triggers,
        )

        service_update_app_branch_config_request.additional_properties = d
        return service_update_app_branch_config_request

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
