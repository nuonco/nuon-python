from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_app_awsiam_role_config import AppAppAWSIAMRoleConfig


T = TypeVar("T", bound="AppInstallRoles")


@_attrs_define
class AppInstallRoles:
    """
    Attributes:
        app_role_config (AppAppAWSIAMRoleConfig | Unset):
        app_role_config_id (str | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        enabled (bool | Unset):
        id (str | Unset):
        install_id (str | Unset):
        last_used_at (str | Unset):
        org_id (str | Unset):
        provisioned (bool | Unset):
        role_id (str | Unset): cloud specific role identifier
        updated_at (str | Unset):
    """

    app_role_config: AppAppAWSIAMRoleConfig | Unset = UNSET
    app_role_config_id: str | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    enabled: bool | Unset = UNSET
    id: str | Unset = UNSET
    install_id: str | Unset = UNSET
    last_used_at: str | Unset = UNSET
    org_id: str | Unset = UNSET
    provisioned: bool | Unset = UNSET
    role_id: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_role_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.app_role_config, Unset):
            app_role_config = self.app_role_config.to_dict()

        app_role_config_id = self.app_role_config_id

        created_at = self.created_at

        created_by_id = self.created_by_id

        enabled = self.enabled

        id = self.id

        install_id = self.install_id

        last_used_at = self.last_used_at

        org_id = self.org_id

        provisioned = self.provisioned

        role_id = self.role_id

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_role_config is not UNSET:
            field_dict["app_role_config"] = app_role_config
        if app_role_config_id is not UNSET:
            field_dict["app_role_config_id"] = app_role_config_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if id is not UNSET:
            field_dict["id"] = id
        if install_id is not UNSET:
            field_dict["install_id"] = install_id
        if last_used_at is not UNSET:
            field_dict["last_used_at"] = last_used_at
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if provisioned is not UNSET:
            field_dict["provisioned"] = provisioned
        if role_id is not UNSET:
            field_dict["role_id"] = role_id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_app_awsiam_role_config import AppAppAWSIAMRoleConfig

        d = dict(src_dict)
        _app_role_config = d.pop("app_role_config", UNSET)
        app_role_config: AppAppAWSIAMRoleConfig | Unset
        if isinstance(_app_role_config, Unset):
            app_role_config = UNSET
        else:
            app_role_config = AppAppAWSIAMRoleConfig.from_dict(_app_role_config)

        app_role_config_id = d.pop("app_role_config_id", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        enabled = d.pop("enabled", UNSET)

        id = d.pop("id", UNSET)

        install_id = d.pop("install_id", UNSET)

        last_used_at = d.pop("last_used_at", UNSET)

        org_id = d.pop("org_id", UNSET)

        provisioned = d.pop("provisioned", UNSET)

        role_id = d.pop("role_id", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        app_install_roles = cls(
            app_role_config=app_role_config,
            app_role_config_id=app_role_config_id,
            created_at=created_at,
            created_by_id=created_by_id,
            enabled=enabled,
            id=id,
            install_id=install_id,
            last_used_at=last_used_at,
            org_id=org_id,
            provisioned=provisioned,
            role_id=role_id,
            updated_at=updated_at,
        )

        app_install_roles.additional_properties = d
        return app_install_roles

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
