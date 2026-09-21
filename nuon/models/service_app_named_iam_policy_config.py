from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceAppNamedIAMPolicyConfig")


@_attrs_define
class ServiceAppNamedIAMPolicyConfig:
    """
    Attributes:
        contents (str):
        name (str):
        description (str | Unset):
        policy_name (str | Unset):
    """

    contents: str
    name: str
    description: str | Unset = UNSET
    policy_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contents = self.contents

        name = self.name

        description = self.description

        policy_name = self.policy_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contents": contents,
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if policy_name is not UNSET:
            field_dict["policy_name"] = policy_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        contents = d.pop("contents")

        name = d.pop("name")

        description = d.pop("description", UNSET)

        policy_name = d.pop("policy_name", UNSET)

        service_app_named_iam_policy_config = cls(
            contents=contents,
            name=name,
            description=description,
            policy_name=policy_name,
        )

        service_app_named_iam_policy_config.additional_properties = d
        return service_app_named_iam_policy_config

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
