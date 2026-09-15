from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppAppNamedIAMPolicyConfig")


@_attrs_define
class AppAppNamedIAMPolicyConfig:
    """
    Attributes:
        app_config_id (str | Unset):
        app_permissions_config_id (str | Unset):
        cloudformation_stack_name (str | Unset):
        contents (str | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        description (str | Unset):
        id (str | Unset):
        name (str | Unset): Name is the config identifier and the AWS IAM managed policy name.
            Roles attach this policy by repeating the same name.
        org_id (str | Unset):
        policy_name (str | Unset): PolicyName is the AWS IAM managed policy name. Empty means use Name.
        updated_at (str | Unset):
    """

    app_config_id: str | Unset = UNSET
    app_permissions_config_id: str | Unset = UNSET
    cloudformation_stack_name: str | Unset = UNSET
    contents: str | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    description: str | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    org_id: str | Unset = UNSET
    policy_name: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_config_id = self.app_config_id

        app_permissions_config_id = self.app_permissions_config_id

        cloudformation_stack_name = self.cloudformation_stack_name

        contents = self.contents

        created_at = self.created_at

        created_by_id = self.created_by_id

        description = self.description

        id = self.id

        name = self.name

        org_id = self.org_id

        policy_name = self.policy_name

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_config_id is not UNSET:
            field_dict["app_config_id"] = app_config_id
        if app_permissions_config_id is not UNSET:
            field_dict["app_permissions_config_id"] = app_permissions_config_id
        if cloudformation_stack_name is not UNSET:
            field_dict["cloudformation_stack_name"] = cloudformation_stack_name
        if contents is not UNSET:
            field_dict["contents"] = contents
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if policy_name is not UNSET:
            field_dict["policy_name"] = policy_name
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        app_config_id = d.pop("app_config_id", UNSET)

        app_permissions_config_id = d.pop("app_permissions_config_id", UNSET)

        cloudformation_stack_name = d.pop("cloudformation_stack_name", UNSET)

        contents = d.pop("contents", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        org_id = d.pop("org_id", UNSET)

        policy_name = d.pop("policy_name", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        app_app_named_iam_policy_config = cls(
            app_config_id=app_config_id,
            app_permissions_config_id=app_permissions_config_id,
            cloudformation_stack_name=cloudformation_stack_name,
            contents=contents,
            created_at=created_at,
            created_by_id=created_by_id,
            description=description,
            id=id,
            name=name,
            org_id=org_id,
            policy_name=policy_name,
            updated_at=updated_at,
        )

        app_app_named_iam_policy_config.additional_properties = d
        return app_app_named_iam_policy_config

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
