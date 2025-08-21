from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

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
    """

    app_config_id: str
    deprovision_role: "ServiceAppAWSIAMRoleConfig"
    maintenance_role: "ServiceAppAWSIAMRoleConfig"
    provision_role: "ServiceAppAWSIAMRoleConfig"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_config_id = self.app_config_id

        deprovision_role = self.deprovision_role.to_dict()

        maintenance_role = self.maintenance_role.to_dict()

        provision_role = self.provision_role.to_dict()

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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_app_awsiam_role_config import ServiceAppAWSIAMRoleConfig

        d = dict(src_dict)
        app_config_id = d.pop("app_config_id")

        deprovision_role = ServiceAppAWSIAMRoleConfig.from_dict(d.pop("deprovision_role"))

        maintenance_role = ServiceAppAWSIAMRoleConfig.from_dict(d.pop("maintenance_role"))

        provision_role = ServiceAppAWSIAMRoleConfig.from_dict(d.pop("provision_role"))

        service_create_app_permissions_config_request = cls(
            app_config_id=app_config_id,
            deprovision_role=deprovision_role,
            maintenance_role=maintenance_role,
            provision_role=provision_role,
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
