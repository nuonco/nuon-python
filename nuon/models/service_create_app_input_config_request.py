from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_create_app_input_config_request_groups import ServiceCreateAppInputConfigRequestGroups
    from ..models.service_create_app_input_config_request_inputs import ServiceCreateAppInputConfigRequestInputs


T = TypeVar("T", bound="ServiceCreateAppInputConfigRequest")


@_attrs_define
class ServiceCreateAppInputConfigRequest:
    """
    Attributes:
        groups (ServiceCreateAppInputConfigRequestGroups):
        inputs (ServiceCreateAppInputConfigRequestInputs):
        app_config_id (Union[Unset, str]):
    """

    groups: "ServiceCreateAppInputConfigRequestGroups"
    inputs: "ServiceCreateAppInputConfigRequestInputs"
    app_config_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        groups = self.groups.to_dict()

        inputs = self.inputs.to_dict()

        app_config_id = self.app_config_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "groups": groups,
                "inputs": inputs,
            }
        )
        if app_config_id is not UNSET:
            field_dict["app_config_id"] = app_config_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_create_app_input_config_request_groups import ServiceCreateAppInputConfigRequestGroups
        from ..models.service_create_app_input_config_request_inputs import ServiceCreateAppInputConfigRequestInputs

        d = dict(src_dict)
        groups = ServiceCreateAppInputConfigRequestGroups.from_dict(d.pop("groups"))

        inputs = ServiceCreateAppInputConfigRequestInputs.from_dict(d.pop("inputs"))

        app_config_id = d.pop("app_config_id", UNSET)

        service_create_app_input_config_request = cls(
            groups=groups,
            inputs=inputs,
            app_config_id=app_config_id,
        )

        service_create_app_input_config_request.additional_properties = d
        return service_create_app_input_config_request

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
