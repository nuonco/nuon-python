from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_install_branch_tracking import ServiceInstallBranchTracking
    from ..models.service_install_config_drift import ServiceInstallConfigDrift
    from ..models.service_install_resource_sync_status import ServiceInstallResourceSyncStatus


T = TypeVar("T", bound="ServiceInstallOverviewResponse")


@_attrs_define
class ServiceInstallOverviewResponse:
    """
    Attributes:
        branch_tracking (ServiceInstallBranchTracking | Unset):
        config_drift (ServiceInstallConfigDrift | Unset):
        resource_sync_status (ServiceInstallResourceSyncStatus | Unset):
    """

    branch_tracking: ServiceInstallBranchTracking | Unset = UNSET
    config_drift: ServiceInstallConfigDrift | Unset = UNSET
    resource_sync_status: ServiceInstallResourceSyncStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        branch_tracking: dict[str, Any] | Unset = UNSET
        if not isinstance(self.branch_tracking, Unset):
            branch_tracking = self.branch_tracking.to_dict()

        config_drift: dict[str, Any] | Unset = UNSET
        if not isinstance(self.config_drift, Unset):
            config_drift = self.config_drift.to_dict()

        resource_sync_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resource_sync_status, Unset):
            resource_sync_status = self.resource_sync_status.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if branch_tracking is not UNSET:
            field_dict["branch_tracking"] = branch_tracking
        if config_drift is not UNSET:
            field_dict["config_drift"] = config_drift
        if resource_sync_status is not UNSET:
            field_dict["resource_sync_status"] = resource_sync_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_install_branch_tracking import ServiceInstallBranchTracking  # noqa: PLC0415
        from ..models.service_install_config_drift import ServiceInstallConfigDrift  # noqa: PLC0415
        from ..models.service_install_resource_sync_status import ServiceInstallResourceSyncStatus  # noqa: PLC0415

        d = dict(src_dict)
        _branch_tracking = d.pop("branch_tracking", UNSET)
        branch_tracking: ServiceInstallBranchTracking | Unset
        if isinstance(_branch_tracking, Unset):
            branch_tracking = UNSET
        else:
            branch_tracking = ServiceInstallBranchTracking.from_dict(_branch_tracking)

        _config_drift = d.pop("config_drift", UNSET)
        config_drift: ServiceInstallConfigDrift | Unset
        if isinstance(_config_drift, Unset):
            config_drift = UNSET
        else:
            config_drift = ServiceInstallConfigDrift.from_dict(_config_drift)

        _resource_sync_status = d.pop("resource_sync_status", UNSET)
        resource_sync_status: ServiceInstallResourceSyncStatus | Unset
        if isinstance(_resource_sync_status, Unset):
            resource_sync_status = UNSET
        else:
            resource_sync_status = ServiceInstallResourceSyncStatus.from_dict(_resource_sync_status)

        service_install_overview_response = cls(
            branch_tracking=branch_tracking,
            config_drift=config_drift,
            resource_sync_status=resource_sync_status,
        )

        service_install_overview_response.additional_properties = d
        return service_install_overview_response

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
