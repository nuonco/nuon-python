from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppAppAWSIAMPolicyConfig")


@_attrs_define
class AppAppAWSIAMPolicyConfig:
    """
    Attributes:
        app_aws_iam_role_config_id (Union[Unset, str]):
        app_config_id (Union[Unset, str]):
        cloudformation_stack_name (Union[Unset, str]):
        contents (Union[Unset, str]):
        created_at (Union[Unset, str]):
        created_by_id (Union[Unset, str]):
        id (Union[Unset, str]):
        managed_policy_name (Union[Unset, str]):
        name (Union[Unset, str]):
        org_id (Union[Unset, str]):
        updated_at (Union[Unset, str]):
    """

    app_aws_iam_role_config_id: Union[Unset, str] = UNSET
    app_config_id: Union[Unset, str] = UNSET
    cloudformation_stack_name: Union[Unset, str] = UNSET
    contents: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    created_by_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    managed_policy_name: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    org_id: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_aws_iam_role_config_id = self.app_aws_iam_role_config_id

        app_config_id = self.app_config_id

        cloudformation_stack_name = self.cloudformation_stack_name

        contents = self.contents

        created_at = self.created_at

        created_by_id = self.created_by_id

        id = self.id

        managed_policy_name = self.managed_policy_name

        name = self.name

        org_id = self.org_id

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_aws_iam_role_config_id is not UNSET:
            field_dict["app_aws_iam_role_config_id"] = app_aws_iam_role_config_id
        if app_config_id is not UNSET:
            field_dict["app_config_id"] = app_config_id
        if cloudformation_stack_name is not UNSET:
            field_dict["cloudformation_stack_name"] = cloudformation_stack_name
        if contents is not UNSET:
            field_dict["contents"] = contents
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if id is not UNSET:
            field_dict["id"] = id
        if managed_policy_name is not UNSET:
            field_dict["managed_policy_name"] = managed_policy_name
        if name is not UNSET:
            field_dict["name"] = name
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        app_aws_iam_role_config_id = d.pop("app_aws_iam_role_config_id", UNSET)

        app_config_id = d.pop("app_config_id", UNSET)

        cloudformation_stack_name = d.pop("cloudformation_stack_name", UNSET)

        contents = d.pop("contents", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        id = d.pop("id", UNSET)

        managed_policy_name = d.pop("managed_policy_name", UNSET)

        name = d.pop("name", UNSET)

        org_id = d.pop("org_id", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        app_app_awsiam_policy_config = cls(
            app_aws_iam_role_config_id=app_aws_iam_role_config_id,
            app_config_id=app_config_id,
            cloudformation_stack_name=cloudformation_stack_name,
            contents=contents,
            created_at=created_at,
            created_by_id=created_by_id,
            id=id,
            managed_policy_name=managed_policy_name,
            name=name,
            org_id=org_id,
            updated_at=updated_at,
        )

        app_app_awsiam_policy_config.additional_properties = d
        return app_app_awsiam_policy_config

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
