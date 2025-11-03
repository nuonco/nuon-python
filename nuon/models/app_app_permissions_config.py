from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_app_awsiam_role_config import AppAppAWSIAMRoleConfig


T = TypeVar("T", bound="AppAppPermissionsConfig")


@_attrs_define
class AppAppPermissionsConfig:
    """
    Attributes:
        app_config_id (str | Unset):
        app_id (str | Unset):
        aws_iam_roles (list[AppAppAWSIAMRoleConfig] | Unset):
        break_glass_aws_iam_role (AppAppAWSIAMRoleConfig | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        deprovision_aws_iam_role (AppAppAWSIAMRoleConfig | Unset):
        id (str | Unset):
        maintenance_aws_iam_role (AppAppAWSIAMRoleConfig | Unset):
        org_id (str | Unset):
        provision_aws_iam_role (AppAppAWSIAMRoleConfig | Unset):
        updated_at (str | Unset):
    """

    app_config_id: str | Unset = UNSET
    app_id: str | Unset = UNSET
    aws_iam_roles: list[AppAppAWSIAMRoleConfig] | Unset = UNSET
    break_glass_aws_iam_role: AppAppAWSIAMRoleConfig | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    deprovision_aws_iam_role: AppAppAWSIAMRoleConfig | Unset = UNSET
    id: str | Unset = UNSET
    maintenance_aws_iam_role: AppAppAWSIAMRoleConfig | Unset = UNSET
    org_id: str | Unset = UNSET
    provision_aws_iam_role: AppAppAWSIAMRoleConfig | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_config_id = self.app_config_id

        app_id = self.app_id

        aws_iam_roles: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.aws_iam_roles, Unset):
            aws_iam_roles = []
            for aws_iam_roles_item_data in self.aws_iam_roles:
                aws_iam_roles_item = aws_iam_roles_item_data.to_dict()
                aws_iam_roles.append(aws_iam_roles_item)

        break_glass_aws_iam_role: dict[str, Any] | Unset = UNSET
        if not isinstance(self.break_glass_aws_iam_role, Unset):
            break_glass_aws_iam_role = self.break_glass_aws_iam_role.to_dict()

        created_at = self.created_at

        created_by_id = self.created_by_id

        deprovision_aws_iam_role: dict[str, Any] | Unset = UNSET
        if not isinstance(self.deprovision_aws_iam_role, Unset):
            deprovision_aws_iam_role = self.deprovision_aws_iam_role.to_dict()

        id = self.id

        maintenance_aws_iam_role: dict[str, Any] | Unset = UNSET
        if not isinstance(self.maintenance_aws_iam_role, Unset):
            maintenance_aws_iam_role = self.maintenance_aws_iam_role.to_dict()

        org_id = self.org_id

        provision_aws_iam_role: dict[str, Any] | Unset = UNSET
        if not isinstance(self.provision_aws_iam_role, Unset):
            provision_aws_iam_role = self.provision_aws_iam_role.to_dict()

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
        if break_glass_aws_iam_role is not UNSET:
            field_dict["break_glass_aws_iam_role"] = break_glass_aws_iam_role
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if deprovision_aws_iam_role is not UNSET:
            field_dict["deprovision_aws_iam_role"] = deprovision_aws_iam_role
        if id is not UNSET:
            field_dict["id"] = id
        if maintenance_aws_iam_role is not UNSET:
            field_dict["maintenance_aws_iam_role"] = maintenance_aws_iam_role
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if provision_aws_iam_role is not UNSET:
            field_dict["provision_aws_iam_role"] = provision_aws_iam_role
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_app_awsiam_role_config import AppAppAWSIAMRoleConfig

        d = dict(src_dict)
        app_config_id = d.pop("app_config_id", UNSET)

        app_id = d.pop("app_id", UNSET)

        _aws_iam_roles = d.pop("aws_iam_roles", UNSET)
        aws_iam_roles: list[AppAppAWSIAMRoleConfig] | Unset = UNSET
        if _aws_iam_roles is not UNSET:
            aws_iam_roles = []
            for aws_iam_roles_item_data in _aws_iam_roles:
                aws_iam_roles_item = AppAppAWSIAMRoleConfig.from_dict(aws_iam_roles_item_data)

                aws_iam_roles.append(aws_iam_roles_item)

        _break_glass_aws_iam_role = d.pop("break_glass_aws_iam_role", UNSET)
        break_glass_aws_iam_role: AppAppAWSIAMRoleConfig | Unset
        if isinstance(_break_glass_aws_iam_role, Unset):
            break_glass_aws_iam_role = UNSET
        else:
            break_glass_aws_iam_role = AppAppAWSIAMRoleConfig.from_dict(_break_glass_aws_iam_role)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        _deprovision_aws_iam_role = d.pop("deprovision_aws_iam_role", UNSET)
        deprovision_aws_iam_role: AppAppAWSIAMRoleConfig | Unset
        if isinstance(_deprovision_aws_iam_role, Unset):
            deprovision_aws_iam_role = UNSET
        else:
            deprovision_aws_iam_role = AppAppAWSIAMRoleConfig.from_dict(_deprovision_aws_iam_role)

        id = d.pop("id", UNSET)

        _maintenance_aws_iam_role = d.pop("maintenance_aws_iam_role", UNSET)
        maintenance_aws_iam_role: AppAppAWSIAMRoleConfig | Unset
        if isinstance(_maintenance_aws_iam_role, Unset):
            maintenance_aws_iam_role = UNSET
        else:
            maintenance_aws_iam_role = AppAppAWSIAMRoleConfig.from_dict(_maintenance_aws_iam_role)

        org_id = d.pop("org_id", UNSET)

        _provision_aws_iam_role = d.pop("provision_aws_iam_role", UNSET)
        provision_aws_iam_role: AppAppAWSIAMRoleConfig | Unset
        if isinstance(_provision_aws_iam_role, Unset):
            provision_aws_iam_role = UNSET
        else:
            provision_aws_iam_role = AppAppAWSIAMRoleConfig.from_dict(_provision_aws_iam_role)

        updated_at = d.pop("updated_at", UNSET)

        app_app_permissions_config = cls(
            app_config_id=app_config_id,
            app_id=app_id,
            aws_iam_roles=aws_iam_roles,
            break_glass_aws_iam_role=break_glass_aws_iam_role,
            created_at=created_at,
            created_by_id=created_by_id,
            deprovision_aws_iam_role=deprovision_aws_iam_role,
            id=id,
            maintenance_aws_iam_role=maintenance_aws_iam_role,
            org_id=org_id,
            provision_aws_iam_role=provision_aws_iam_role,
            updated_at=updated_at,
        )

        app_app_permissions_config.additional_properties = d
        return app_app_permissions_config

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
