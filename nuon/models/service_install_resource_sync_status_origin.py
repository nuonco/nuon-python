from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_workflow_type import AppWorkflowType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_install_overview_commit import ServiceInstallOverviewCommit


T = TypeVar("T", bound="ServiceInstallResourceSyncStatusOrigin")


@_attrs_define
class ServiceInstallResourceSyncStatusOrigin:
    """
    Attributes:
        run (ServiceInstallOverviewCommit | Unset):
        workflow_id (str | Unset):
        workflow_type (AppWorkflowType | Unset):
    """

    run: ServiceInstallOverviewCommit | Unset = UNSET
    workflow_id: str | Unset = UNSET
    workflow_type: AppWorkflowType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        run: dict[str, Any] | Unset = UNSET
        if not isinstance(self.run, Unset):
            run = self.run.to_dict()

        workflow_id = self.workflow_id

        workflow_type: str | Unset = UNSET
        if not isinstance(self.workflow_type, Unset):
            workflow_type = self.workflow_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if run is not UNSET:
            field_dict["run"] = run
        if workflow_id is not UNSET:
            field_dict["workflow_id"] = workflow_id
        if workflow_type is not UNSET:
            field_dict["workflow_type"] = workflow_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_install_overview_commit import ServiceInstallOverviewCommit  # noqa: PLC0415

        d = dict(src_dict)
        _run = d.pop("run", UNSET)
        run: ServiceInstallOverviewCommit | Unset
        if isinstance(_run, Unset):
            run = UNSET
        else:
            run = ServiceInstallOverviewCommit.from_dict(_run)

        workflow_id = d.pop("workflow_id", UNSET)

        _workflow_type = d.pop("workflow_type", UNSET)
        workflow_type: AppWorkflowType | Unset
        if isinstance(_workflow_type, Unset):
            workflow_type = UNSET
        else:
            workflow_type = AppWorkflowType(_workflow_type)

        service_install_resource_sync_status_origin = cls(
            run=run,
            workflow_id=workflow_id,
            workflow_type=workflow_type,
        )

        service_install_resource_sync_status_origin.additional_properties = d
        return service_install_resource_sync_status_origin

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
