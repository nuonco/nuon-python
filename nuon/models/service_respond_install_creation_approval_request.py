from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.service_respond_install_creation_approval_request_response_type import (
    ServiceRespondInstallCreationApprovalRequestResponseType,
)

T = TypeVar("T", bound="ServiceRespondInstallCreationApprovalRequest")


@_attrs_define
class ServiceRespondInstallCreationApprovalRequest:
    """
    Attributes:
        response_type (ServiceRespondInstallCreationApprovalRequestResponseType):
    """

    response_type: ServiceRespondInstallCreationApprovalRequestResponseType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        response_type = self.response_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "response_type": response_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        response_type = ServiceRespondInstallCreationApprovalRequestResponseType(d.pop("response_type"))

        service_respond_install_creation_approval_request = cls(
            response_type=response_type,
        )

        service_respond_install_creation_approval_request.additional_properties = d
        return service_respond_install_creation_approval_request

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
