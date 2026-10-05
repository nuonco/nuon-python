from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_composite_status import AppCompositeStatus


T = TypeVar("T", bound="ServiceInstallStatusResponse")


@_attrs_define
class ServiceInstallStatusResponse:
    """
    Attributes:
        deployments (AppCompositeStatus | Unset):
        health_checks (AppCompositeStatus | Unset):
        resources (AppCompositeStatus | Unset):
    """

    deployments: AppCompositeStatus | Unset = UNSET
    health_checks: AppCompositeStatus | Unset = UNSET
    resources: AppCompositeStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        deployments: dict[str, Any] | Unset = UNSET
        if not isinstance(self.deployments, Unset):
            deployments = self.deployments.to_dict()

        health_checks: dict[str, Any] | Unset = UNSET
        if not isinstance(self.health_checks, Unset):
            health_checks = self.health_checks.to_dict()

        resources: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resources, Unset):
            resources = self.resources.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if deployments is not UNSET:
            field_dict["deployments"] = deployments
        if health_checks is not UNSET:
            field_dict["health_checks"] = health_checks
        if resources is not UNSET:
            field_dict["resources"] = resources

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_composite_status import AppCompositeStatus  # noqa: PLC0415

        d = dict(src_dict)
        _deployments = d.pop("deployments", UNSET)
        deployments: AppCompositeStatus | Unset
        if isinstance(_deployments, Unset):
            deployments = UNSET
        else:
            deployments = AppCompositeStatus.from_dict(_deployments)

        _health_checks = d.pop("health_checks", UNSET)
        health_checks: AppCompositeStatus | Unset
        if isinstance(_health_checks, Unset):
            health_checks = UNSET
        else:
            health_checks = AppCompositeStatus.from_dict(_health_checks)

        _resources = d.pop("resources", UNSET)
        resources: AppCompositeStatus | Unset
        if isinstance(_resources, Unset):
            resources = UNSET
        else:
            resources = AppCompositeStatus.from_dict(_resources)

        service_install_status_response = cls(
            deployments=deployments,
            health_checks=health_checks,
            resources=resources,
        )

        service_install_status_response.additional_properties = d
        return service_install_status_response

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
