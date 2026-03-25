from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_update_install_inputs_request_inputs import ServiceUpdateInstallInputsRequestInputs


T = TypeVar("T", bound="ServiceUpdateInstallInputsRequest")


@_attrs_define
class ServiceUpdateInstallInputsRequest:
    """
    Attributes:
        inputs (ServiceUpdateInstallInputsRequestInputs):
        role (str | Unset):
    """

    inputs: ServiceUpdateInstallInputsRequestInputs
    role: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        inputs = self.inputs.to_dict()

        role = self.role

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "inputs": inputs,
            }
        )
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_update_install_inputs_request_inputs import ServiceUpdateInstallInputsRequestInputs

        d = dict(src_dict)
        inputs = ServiceUpdateInstallInputsRequestInputs.from_dict(d.pop("inputs"))

        role = d.pop("role", UNSET)

        service_update_install_inputs_request = cls(
            inputs=inputs,
            role=role,
        )

        service_update_install_inputs_request.additional_properties = d
        return service_update_install_inputs_request

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
