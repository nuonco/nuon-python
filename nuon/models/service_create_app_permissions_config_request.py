from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_app_awsiam_role_config import ServiceAppAWSIAMRoleConfig


T = TypeVar("T", bound="ServiceCreateAppPermissionsConfigRequest")


@_attrs_define
class ServiceCreateAppPermissionsConfigRequest:
    """
    Attributes:
        app_config_id (str):
        deprovision_role (ServiceAppAWSIAMRoleConfig):
        maintenance_role (ServiceAppAWSIAMRoleConfig):
        provision_role (ServiceAppAWSIAMRoleConfig):
        break_glass_roles (Union[Unset, list['ServiceAppAWSIAMRoleConfig']]):
    """

    app_config_id: str
    deprovision_role: "ServiceAppAWSIAMRoleConfig"
    maintenance_role: "ServiceAppAWSIAMRoleConfig"
    provision_role: "ServiceAppAWSIAMRoleConfig"
    break_glass_roles: Union[Unset, list["ServiceAppAWSIAMRoleConfig"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_config_id = self.app_config_id

        deprovision_role = self.deprovision_role.to_dict()

        maintenance_role = self.maintenance_role.to_dict()

        provision_role = self.provision_role.to_dict()

        break_glass_roles: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.break_glass_roles, Unset):
            break_glass_roles = []
            for break_glass_roles_item_data in self.break_glass_roles:
                break_glass_roles_item = break_glass_roles_item_data.to_dict()
                break_glass_roles.append(break_glass_roles_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "app_config_id": app_config_id,
                "deprovision_role": deprovision_role,
                "maintenance_role": maintenance_role,
                "provision_role": provision_role,
            }
        )
        if break_glass_roles is not UNSET:
            field_dict["break_glass_roles"] = break_glass_roles

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_app_awsiam_role_config import ServiceAppAWSIAMRoleConfig

        d = dict(src_dict)
        app_config_id = d.pop("app_config_id")

        deprovision_role = ServiceAppAWSIAMRoleConfig.from_dict(d.pop("deprovision_role"))

        maintenance_role = ServiceAppAWSIAMRoleConfig.from_dict(d.pop("maintenance_role"))

        provision_role = ServiceAppAWSIAMRoleConfig.from_dict(d.pop("provision_role"))

        break_glass_roles = []
        _break_glass_roles = d.pop("break_glass_roles", UNSET)
        for break_glass_roles_item_data in _break_glass_roles or []:
            break_glass_roles_item = ServiceAppAWSIAMRoleConfig.from_dict(break_glass_roles_item_data)

            break_glass_roles.append(break_glass_roles_item)

        service_create_app_permissions_config_request = cls(
            app_config_id=app_config_id,
            deprovision_role=deprovision_role,
            maintenance_role=maintenance_role,
            provision_role=provision_role,
            break_glass_roles=break_glass_roles,
        )

        service_create_app_permissions_config_request.additional_properties = d
        return service_create_app_permissions_config_request

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
