from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceAppAWSIAMPolicyConfig")


@_attrs_define
class ServiceAppAWSIAMPolicyConfig:
    """
    Attributes:
        contents (str | Unset):
        managed_policy_name (str | Unset):
        name (str | Unset):
    """

    contents: str | Unset = UNSET
    managed_policy_name: str | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contents = self.contents

        managed_policy_name = self.managed_policy_name

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if contents is not UNSET:
            field_dict["contents"] = contents
        if managed_policy_name is not UNSET:
            field_dict["managed_policy_name"] = managed_policy_name
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        contents = d.pop("contents", UNSET)

        managed_policy_name = d.pop("managed_policy_name", UNSET)

        name = d.pop("name", UNSET)

        service_app_awsiam_policy_config = cls(
            contents=contents,
            managed_policy_name=managed_policy_name,
            name=name,
        )

        service_app_awsiam_policy_config.additional_properties = d
        return service_app_awsiam_policy_config

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
