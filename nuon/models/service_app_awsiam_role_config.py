from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

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
        permissions_boundary (Union[Unset, str]):
        policies (Union[Unset, list['ServiceAppAWSIAMPolicyConfig']]):
    """

    description: str
    display_name: str
    name: str
    permissions_boundary: Union[Unset, str] = UNSET
    policies: Union[Unset, list["ServiceAppAWSIAMPolicyConfig"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        display_name = self.display_name

        name = self.name

        permissions_boundary = self.permissions_boundary

        policies: Union[Unset, list[dict[str, Any]]] = UNSET
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

        permissions_boundary = d.pop("permissions_boundary", UNSET)

        policies = []
        _policies = d.pop("policies", UNSET)
        for policies_item_data in _policies or []:
            policies_item = ServiceAppAWSIAMPolicyConfig.from_dict(policies_item_data)

            policies.append(policies_item)

        service_app_awsiam_role_config = cls(
            description=description,
            display_name=display_name,
            name=name,
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
