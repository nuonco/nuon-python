from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_app_awsiam_role_config import AppAppAWSIAMRoleConfig


T = TypeVar("T", bound="AppAppBreakGlassConfig")


@_attrs_define
class AppAppBreakGlassConfig:
    """
    Attributes:
        app_config_id (Union[Unset, str]):
        app_id (Union[Unset, str]):
        aws_iam_roles (Union[Unset, list['AppAppAWSIAMRoleConfig']]):
        created_at (Union[Unset, str]):
        created_by_id (Union[Unset, str]):
        id (Union[Unset, str]):
        org_id (Union[Unset, str]):
        updated_at (Union[Unset, str]):
    """

    app_config_id: Union[Unset, str] = UNSET
    app_id: Union[Unset, str] = UNSET
    aws_iam_roles: Union[Unset, list["AppAppAWSIAMRoleConfig"]] = UNSET
    created_at: Union[Unset, str] = UNSET
    created_by_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    org_id: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_config_id = self.app_config_id

        app_id = self.app_id

        aws_iam_roles: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.aws_iam_roles, Unset):
            aws_iam_roles = []
            for aws_iam_roles_item_data in self.aws_iam_roles:
                aws_iam_roles_item = aws_iam_roles_item_data.to_dict()
                aws_iam_roles.append(aws_iam_roles_item)

        created_at = self.created_at

        created_by_id = self.created_by_id

        id = self.id

        org_id = self.org_id

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_config_id is not UNSET:
            field_dict["app_config_id"] = app_config_id
        if app_id is not UNSET:
            field_dict["app_id"] = app_id
        if aws_iam_roles is not UNSET:
            field_dict["aws_iam_roles"] = aws_iam_roles
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if id is not UNSET:
            field_dict["id"] = id
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_app_awsiam_role_config import AppAppAWSIAMRoleConfig

        d = dict(src_dict)
        app_config_id = d.pop("app_config_id", UNSET)

        app_id = d.pop("app_id", UNSET)

        aws_iam_roles = []
        _aws_iam_roles = d.pop("aws_iam_roles", UNSET)
        for aws_iam_roles_item_data in _aws_iam_roles or []:
            aws_iam_roles_item = AppAppAWSIAMRoleConfig.from_dict(aws_iam_roles_item_data)

            aws_iam_roles.append(aws_iam_roles_item)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        id = d.pop("id", UNSET)

        org_id = d.pop("org_id", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        app_app_break_glass_config = cls(
            app_config_id=app_config_id,
            app_id=app_id,
            aws_iam_roles=aws_iam_roles,
            created_at=created_at,
            created_by_id=created_by_id,
            id=id,
            org_id=org_id,
            updated_at=updated_at,
        )

        app_app_break_glass_config.additional_properties = d
        return app_app_break_glass_config

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
