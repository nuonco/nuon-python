from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.service_app_awsiam_role_config_cloud_platform import ServiceAppAWSIAMRoleConfigCloudPlatform
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_app_awsiam_policy_config import ServiceAppAWSIAMPolicyConfig


T = TypeVar("T", bound="ServiceAppAWSIAMRoleConfig")


@_attrs_define
class ServiceAppAWSIAMRoleConfig:
    """
    Attributes:
        description (str):
        display_name (str):
        name (str):
        cloud_platform (ServiceAppAWSIAMRoleConfigCloudPlatform | Unset):
        enabled_in_stack (bool | None | Unset):
        permissions_boundary (str | Unset):
        policies (list[ServiceAppAWSIAMPolicyConfig] | Unset):
    """

    description: str
    display_name: str
    name: str
    cloud_platform: ServiceAppAWSIAMRoleConfigCloudPlatform | Unset = UNSET
    enabled_in_stack: bool | None | Unset = UNSET
    permissions_boundary: str | Unset = UNSET
    policies: list[ServiceAppAWSIAMPolicyConfig] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        display_name = self.display_name

        name = self.name

        cloud_platform: str | Unset = UNSET
        if not isinstance(self.cloud_platform, Unset):
            cloud_platform = self.cloud_platform.value

        enabled_in_stack: bool | None | Unset
        if isinstance(self.enabled_in_stack, Unset):
            enabled_in_stack = UNSET
        else:
            enabled_in_stack = self.enabled_in_stack

        permissions_boundary = self.permissions_boundary

        policies: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.policies, Unset):
            policies = []
            for policies_item_data in self.policies:
                policies_item = policies_item_data.to_dict()
                policies.append(policies_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "display_name": display_name,
                "name": name,
            }
        )
        if cloud_platform is not UNSET:
            field_dict["cloud_platform"] = cloud_platform
        if enabled_in_stack is not UNSET:
            field_dict["enabled_in_stack"] = enabled_in_stack
        if permissions_boundary is not UNSET:
            field_dict["permissions_boundary"] = permissions_boundary
        if policies is not UNSET:
            field_dict["policies"] = policies

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_app_awsiam_policy_config import ServiceAppAWSIAMPolicyConfig

        d = dict(src_dict)
        description = d.pop("description")

        display_name = d.pop("display_name")

        name = d.pop("name")

        _cloud_platform = d.pop("cloud_platform", UNSET)
        cloud_platform: ServiceAppAWSIAMRoleConfigCloudPlatform | Unset
        if isinstance(_cloud_platform, Unset):
            cloud_platform = UNSET
        else:
            cloud_platform = ServiceAppAWSIAMRoleConfigCloudPlatform(_cloud_platform)

        def _parse_enabled_in_stack(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enabled_in_stack = _parse_enabled_in_stack(d.pop("enabled_in_stack", UNSET))

        permissions_boundary = d.pop("permissions_boundary", UNSET)

        _policies = d.pop("policies", UNSET)
        policies: list[ServiceAppAWSIAMPolicyConfig] | Unset = UNSET
        if _policies is not UNSET:
            policies = []
            for policies_item_data in _policies:
                policies_item = ServiceAppAWSIAMPolicyConfig.from_dict(policies_item_data)

                policies.append(policies_item)

        service_app_awsiam_role_config = cls(
            description=description,
            display_name=display_name,
            name=name,
            cloud_platform=cloud_platform,
            enabled_in_stack=enabled_in_stack,
            permissions_boundary=permissions_boundary,
            policies=policies,
        )

        service_app_awsiam_role_config.additional_properties = d
        return service_app_awsiam_role_config

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
