from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.service_app_awsiam_role_config import ServiceAppAWSIAMRoleConfig


T = TypeVar("T", bound="ServiceCreateAppBreakGlassConfigRequest")


@_attrs_define
class ServiceCreateAppBreakGlassConfigRequest:
    """
    Attributes:
        app_config_id (str):
        roles (list['ServiceAppAWSIAMRoleConfig']):
    """

    app_config_id: str
    roles: list["ServiceAppAWSIAMRoleConfig"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_config_id = self.app_config_id

        roles = []
        for roles_item_data in self.roles:
            roles_item = roles_item_data.to_dict()
            roles.append(roles_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "app_config_id": app_config_id,
                "roles": roles,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_app_awsiam_role_config import ServiceAppAWSIAMRoleConfig

        d = dict(src_dict)
        app_config_id = d.pop("app_config_id")

        roles = []
        _roles = d.pop("roles")
        for roles_item_data in _roles:
            roles_item = ServiceAppAWSIAMRoleConfig.from_dict(roles_item_data)

            roles.append(roles_item)

        service_create_app_break_glass_config_request = cls(
            app_config_id=app_config_id,
            roles=roles,
        )

        service_create_app_break_glass_config_request.additional_properties = d
        return service_create_app_break_glass_config_request

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
