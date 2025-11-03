from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_awsiam_role_type import AppAWSIAMRoleType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_app_awsiam_policy_config import AppAppAWSIAMPolicyConfig


T = TypeVar("T", bound="AppAppAWSIAMRoleConfig")


@_attrs_define
class AppAppAWSIAMRoleConfig:
    """
    Attributes:
        app_config_id (str | Unset):
        cloudformation_param_name (str | Unset):
        cloudformation_stack_name (str | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        description (str | Unset):
        display_name (str | Unset):
        id (str | Unset):
        name (str | Unset):
        org_id (str | Unset):
        owner_id (str | Unset):
        owner_type (str | Unset):
        permissions_boundary (str | Unset):
        policies (list[AppAppAWSIAMPolicyConfig] | Unset):
        type_ (AppAWSIAMRoleType | Unset):
        updated_at (str | Unset):
    """

    app_config_id: str | Unset = UNSET
    cloudformation_param_name: str | Unset = UNSET
    cloudformation_stack_name: str | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    description: str | Unset = UNSET
    display_name: str | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    org_id: str | Unset = UNSET
    owner_id: str | Unset = UNSET
    owner_type: str | Unset = UNSET
    permissions_boundary: str | Unset = UNSET
    policies: list[AppAppAWSIAMPolicyConfig] | Unset = UNSET
    type_: AppAWSIAMRoleType | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_config_id = self.app_config_id

        cloudformation_param_name = self.cloudformation_param_name

        cloudformation_stack_name = self.cloudformation_stack_name

        created_at = self.created_at

        created_by_id = self.created_by_id

        description = self.description

        display_name = self.display_name

        id = self.id

        name = self.name

        org_id = self.org_id

        owner_id = self.owner_id

        owner_type = self.owner_type

        permissions_boundary = self.permissions_boundary

        policies: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.policies, Unset):
            policies = []
            for policies_item_data in self.policies:
                policies_item = policies_item_data.to_dict()
                policies.append(policies_item)

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_config_id is not UNSET:
            field_dict["app_config_id"] = app_config_id
        if cloudformation_param_name is not UNSET:
            field_dict["cloudformation_param_name"] = cloudformation_param_name
        if cloudformation_stack_name is not UNSET:
            field_dict["cloudformation_stack_name"] = cloudformation_stack_name
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if description is not UNSET:
            field_dict["description"] = description
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if owner_type is not UNSET:
            field_dict["owner_type"] = owner_type
        if permissions_boundary is not UNSET:
            field_dict["permissions_boundary"] = permissions_boundary
        if policies is not UNSET:
            field_dict["policies"] = policies
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_app_awsiam_policy_config import AppAppAWSIAMPolicyConfig

        d = dict(src_dict)
        app_config_id = d.pop("app_config_id", UNSET)

        cloudformation_param_name = d.pop("cloudformation_param_name", UNSET)

        cloudformation_stack_name = d.pop("cloudformation_stack_name", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        description = d.pop("description", UNSET)

        display_name = d.pop("display_name", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        org_id = d.pop("org_id", UNSET)

        owner_id = d.pop("owner_id", UNSET)

        owner_type = d.pop("owner_type", UNSET)

        permissions_boundary = d.pop("permissions_boundary", UNSET)

        _policies = d.pop("policies", UNSET)
        policies: list[AppAppAWSIAMPolicyConfig] | Unset = UNSET
        if _policies is not UNSET:
            policies = []
            for policies_item_data in _policies:
                policies_item = AppAppAWSIAMPolicyConfig.from_dict(policies_item_data)

                policies.append(policies_item)

        _type_ = d.pop("type", UNSET)
        type_: AppAWSIAMRoleType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = AppAWSIAMRoleType(_type_)

        updated_at = d.pop("updated_at", UNSET)

        app_app_awsiam_role_config = cls(
            app_config_id=app_config_id,
            cloudformation_param_name=cloudformation_param_name,
            cloudformation_stack_name=cloudformation_stack_name,
            created_at=created_at,
            created_by_id=created_by_id,
            description=description,
            display_name=display_name,
            id=id,
            name=name,
            org_id=org_id,
            owner_id=owner_id,
            owner_type=owner_type,
            permissions_boundary=permissions_boundary,
            policies=policies,
            type_=type_,
            updated_at=updated_at,
        )

        app_app_awsiam_role_config.additional_properties = d
        return app_app_awsiam_role_config

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
