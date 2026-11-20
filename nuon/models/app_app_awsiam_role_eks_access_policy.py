from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppAppAWSIAMRoleEKSAccessPolicy")


@_attrs_define
class AppAppAWSIAMRoleEKSAccessPolicy:
    """
    Attributes:
        access_scope (str | Unset):
        namespaces (list[str] | Unset):
        policy_arn (str | Unset):
    """

    access_scope: str | Unset = UNSET
    namespaces: list[str] | Unset = UNSET
    policy_arn: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_scope = self.access_scope

        namespaces: list[str] | Unset = UNSET
        if not isinstance(self.namespaces, Unset):
            namespaces = self.namespaces

        policy_arn = self.policy_arn

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access_scope is not UNSET:
            field_dict["access_scope"] = access_scope
        if namespaces is not UNSET:
            field_dict["namespaces"] = namespaces
        if policy_arn is not UNSET:
            field_dict["policy_arn"] = policy_arn

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access_scope = d.pop("access_scope", UNSET)

        namespaces = cast(list[str], d.pop("namespaces", UNSET))

        policy_arn = d.pop("policy_arn", UNSET)

        app_app_awsiam_role_eks_access_policy = cls(
            access_scope=access_scope,
            namespaces=namespaces,
            policy_arn=policy_arn,
        )

        app_app_awsiam_role_eks_access_policy.additional_properties = d
        return app_app_awsiam_role_eks_access_policy

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
