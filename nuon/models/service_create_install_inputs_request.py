from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.service_create_install_inputs_request_inputs import ServiceCreateInstallInputsRequestInputs


T = TypeVar("T", bound="ServiceCreateInstallInputsRequest")


@_attrs_define
class ServiceCreateInstallInputsRequest:
    """
    Attributes:
        inputs (ServiceCreateInstallInputsRequestInputs):
    """

    inputs: "ServiceCreateInstallInputsRequestInputs"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        inputs = self.inputs.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "inputs": inputs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_create_install_inputs_request_inputs import ServiceCreateInstallInputsRequestInputs

        d = dict(src_dict)
        inputs = ServiceCreateInstallInputsRequestInputs.from_dict(d.pop("inputs"))

        service_create_install_inputs_request = cls(
            inputs=inputs,
        )

        service_create_install_inputs_request.additional_properties = d
        return service_create_install_inputs_request

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
