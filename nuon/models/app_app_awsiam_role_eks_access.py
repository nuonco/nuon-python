from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_app_awsiam_role_eks_access_policy import AppAppAWSIAMRoleEKSAccessPolicy


T = TypeVar("T", bound="AppAppAWSIAMRoleEKSAccess")


@_attrs_define
class AppAppAWSIAMRoleEKSAccess:
    """
    Attributes:
        cluster_name (str | Unset):
        kubernetes_groups (list[str] | Unset):
        policies (list[AppAppAWSIAMRoleEKSAccessPolicy] | Unset):
    """

    cluster_name: str | Unset = UNSET
    kubernetes_groups: list[str] | Unset = UNSET
    policies: list[AppAppAWSIAMRoleEKSAccessPolicy] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cluster_name = self.cluster_name

        kubernetes_groups: list[str] | Unset = UNSET
        if not isinstance(self.kubernetes_groups, Unset):
            kubernetes_groups = self.kubernetes_groups

        policies: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.policies, Unset):
            policies = []
            for policies_item_data in self.policies:
                policies_item = policies_item_data.to_dict()
                policies.append(policies_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cluster_name is not UNSET:
            field_dict["cluster_name"] = cluster_name
        if kubernetes_groups is not UNSET:
            field_dict["kubernetes_groups"] = kubernetes_groups
        if policies is not UNSET:
            field_dict["policies"] = policies

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_app_awsiam_role_eks_access_policy import AppAppAWSIAMRoleEKSAccessPolicy  # noqa: PLC0415

        d = dict(src_dict)
        cluster_name = d.pop("cluster_name", UNSET)

        kubernetes_groups = cast(list[str], d.pop("kubernetes_groups", UNSET))

        _policies = d.pop("policies", UNSET)
        policies: list[AppAppAWSIAMRoleEKSAccessPolicy] | Unset = UNSET
        if _policies is not UNSET:
            policies = []
            for policies_item_data in _policies:
                policies_item = AppAppAWSIAMRoleEKSAccessPolicy.from_dict(policies_item_data)

                policies.append(policies_item)

        app_app_awsiam_role_eks_access = cls(
            cluster_name=cluster_name,
            kubernetes_groups=kubernetes_groups,
            policies=policies,
        )

        app_app_awsiam_role_eks_access.additional_properties = d
        return app_app_awsiam_role_eks_access

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
