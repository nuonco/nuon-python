from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_put_install_component_health_check_request_details import (
        ServicePutInstallComponentHealthCheckRequestDetails,
    )


T = TypeVar("T", bound="ServicePutInstallComponentHealthCheckRequest")


@_attrs_define
class ServicePutInstallComponentHealthCheckRequest:
    """
    Attributes:
        status (str):
        details (ServicePutInstallComponentHealthCheckRequestDetails | Unset):
        message (str | Unset):
        stale_after (str | Unset): StaleAfter is how long this report stays trustworthy, e.g. "30m"; past
            it the check reads as unknown. Defaults to 5m — set higher for slower pushers.
    """

    status: str
    details: ServicePutInstallComponentHealthCheckRequestDetails | Unset = UNSET
    message: str | Unset = UNSET
    stale_after: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        message = self.message

        stale_after = self.stale_after

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if details is not UNSET:
            field_dict["details"] = details
        if message is not UNSET:
            field_dict["message"] = message
        if stale_after is not UNSET:
            field_dict["stale_after"] = stale_after

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_put_install_component_health_check_request_details import (
            ServicePutInstallComponentHealthCheckRequestDetails,
        )

        d = dict(src_dict)
        status = d.pop("status")

        _details = d.pop("details", UNSET)
        details: ServicePutInstallComponentHealthCheckRequestDetails | Unset
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = ServicePutInstallComponentHealthCheckRequestDetails.from_dict(_details)

        message = d.pop("message", UNSET)

        stale_after = d.pop("stale_after", UNSET)

        service_put_install_component_health_check_request = cls(
            status=status,
            details=details,
            message=message,
            stale_after=stale_after,
        )

        service_put_install_component_health_check_request.additional_properties = d
        return service_put_install_component_health_check_request

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
