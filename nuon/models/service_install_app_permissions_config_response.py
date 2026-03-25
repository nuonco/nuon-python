from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_install_permissions_role_status import ServiceInstallPermissionsRoleStatus


T = TypeVar("T", bound="ServiceInstallAppPermissionsConfigResponse")


@_attrs_define
class ServiceInstallAppPermissionsConfigResponse:
    """
    Attributes:
        break_glass_roles (list[ServiceInstallPermissionsRoleStatus] | Unset):
        custom_roles (list[ServiceInstallPermissionsRoleStatus] | Unset):
        deprovision_role (ServiceInstallPermissionsRoleStatus | Unset):
        maintenance_role (ServiceInstallPermissionsRoleStatus | Unset):
        provision_role (ServiceInstallPermissionsRoleStatus | Unset):
    """

    break_glass_roles: list[ServiceInstallPermissionsRoleStatus] | Unset = UNSET
    custom_roles: list[ServiceInstallPermissionsRoleStatus] | Unset = UNSET
    deprovision_role: ServiceInstallPermissionsRoleStatus | Unset = UNSET
    maintenance_role: ServiceInstallPermissionsRoleStatus | Unset = UNSET
    provision_role: ServiceInstallPermissionsRoleStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        break_glass_roles: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.break_glass_roles, Unset):
            break_glass_roles = []
            for break_glass_roles_item_data in self.break_glass_roles:
                break_glass_roles_item = break_glass_roles_item_data.to_dict()
                break_glass_roles.append(break_glass_roles_item)

        custom_roles: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.custom_roles, Unset):
            custom_roles = []
            for custom_roles_item_data in self.custom_roles:
                custom_roles_item = custom_roles_item_data.to_dict()
                custom_roles.append(custom_roles_item)

        deprovision_role: dict[str, Any] | Unset = UNSET
        if not isinstance(self.deprovision_role, Unset):
            deprovision_role = self.deprovision_role.to_dict()

        maintenance_role: dict[str, Any] | Unset = UNSET
        if not isinstance(self.maintenance_role, Unset):
            maintenance_role = self.maintenance_role.to_dict()

        provision_role: dict[str, Any] | Unset = UNSET
        if not isinstance(self.provision_role, Unset):
            provision_role = self.provision_role.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if break_glass_roles is not UNSET:
            field_dict["break_glass_roles"] = break_glass_roles
        if custom_roles is not UNSET:
            field_dict["custom_roles"] = custom_roles
        if deprovision_role is not UNSET:
            field_dict["deprovision_role"] = deprovision_role
        if maintenance_role is not UNSET:
            field_dict["maintenance_role"] = maintenance_role
        if provision_role is not UNSET:
            field_dict["provision_role"] = provision_role

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_install_permissions_role_status import ServiceInstallPermissionsRoleStatus

        d = dict(src_dict)
        _break_glass_roles = d.pop("break_glass_roles", UNSET)
        break_glass_roles: list[ServiceInstallPermissionsRoleStatus] | Unset = UNSET
        if _break_glass_roles is not UNSET:
            break_glass_roles = []
            for break_glass_roles_item_data in _break_glass_roles:
                break_glass_roles_item = ServiceInstallPermissionsRoleStatus.from_dict(break_glass_roles_item_data)

                break_glass_roles.append(break_glass_roles_item)

        _custom_roles = d.pop("custom_roles", UNSET)
        custom_roles: list[ServiceInstallPermissionsRoleStatus] | Unset = UNSET
        if _custom_roles is not UNSET:
            custom_roles = []
            for custom_roles_item_data in _custom_roles:
                custom_roles_item = ServiceInstallPermissionsRoleStatus.from_dict(custom_roles_item_data)

                custom_roles.append(custom_roles_item)

        _deprovision_role = d.pop("deprovision_role", UNSET)
        deprovision_role: ServiceInstallPermissionsRoleStatus | Unset
        if isinstance(_deprovision_role, Unset):
            deprovision_role = UNSET
        else:
            deprovision_role = ServiceInstallPermissionsRoleStatus.from_dict(_deprovision_role)

        _maintenance_role = d.pop("maintenance_role", UNSET)
        maintenance_role: ServiceInstallPermissionsRoleStatus | Unset
        if isinstance(_maintenance_role, Unset):
            maintenance_role = UNSET
        else:
            maintenance_role = ServiceInstallPermissionsRoleStatus.from_dict(_maintenance_role)

        _provision_role = d.pop("provision_role", UNSET)
        provision_role: ServiceInstallPermissionsRoleStatus | Unset
        if isinstance(_provision_role, Unset):
            provision_role = UNSET
        else:
            provision_role = ServiceInstallPermissionsRoleStatus.from_dict(_provision_role)

        service_install_app_permissions_config_response = cls(
            break_glass_roles=break_glass_roles,
            custom_roles=custom_roles,
            deprovision_role=deprovision_role,
            maintenance_role=maintenance_role,
            provision_role=provision_role,
        )

        service_install_app_permissions_config_response.additional_properties = d
        return service_install_app_permissions_config_response

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
