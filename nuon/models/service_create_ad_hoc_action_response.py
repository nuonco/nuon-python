from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_action_workflow_trigger_type import AppActionWorkflowTriggerType
from ..models.app_install_action_workflow_run_status import AppInstallActionWorkflowRunStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceCreateAdHocActionResponse")


@_attrs_define
class ServiceCreateAdHocActionResponse:
    """
    Attributes:
        created_at (str | Unset):
        id (str | Unset):
        install_id (str | Unset):
        status (AppInstallActionWorkflowRunStatus | Unset):
        status_description (str | Unset):
        trigger_type (AppActionWorkflowTriggerType | Unset):
        workflow_id (str | Unset):
    """

    created_at: str | Unset = UNSET
    id: str | Unset = UNSET
    install_id: str | Unset = UNSET
    status: AppInstallActionWorkflowRunStatus | Unset = UNSET
    status_description: str | Unset = UNSET
    trigger_type: AppActionWorkflowTriggerType | Unset = UNSET
    workflow_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        id = self.id

        install_id = self.install_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        status_description = self.status_description

        trigger_type: str | Unset = UNSET
        if not isinstance(self.trigger_type, Unset):
            trigger_type = self.trigger_type.value

        workflow_id = self.workflow_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if install_id is not UNSET:
            field_dict["install_id"] = install_id
        if status is not UNSET:
            field_dict["status"] = status
        if status_description is not UNSET:
            field_dict["status_description"] = status_description
        if trigger_type is not UNSET:
            field_dict["trigger_type"] = trigger_type
        if workflow_id is not UNSET:
            field_dict["workflow_id"] = workflow_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        id = d.pop("id", UNSET)

        install_id = d.pop("install_id", UNSET)

        _status = d.pop("status", UNSET)
        status: AppInstallActionWorkflowRunStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AppInstallActionWorkflowRunStatus(_status)

        status_description = d.pop("status_description", UNSET)

        _trigger_type = d.pop("trigger_type", UNSET)
        trigger_type: AppActionWorkflowTriggerType | Unset
        if isinstance(_trigger_type, Unset):
            trigger_type = UNSET
        else:
            trigger_type = AppActionWorkflowTriggerType(_trigger_type)

        workflow_id = d.pop("workflow_id", UNSET)

        service_create_ad_hoc_action_response = cls(
            created_at=created_at,
            id=id,
            install_id=install_id,
            status=status,
            status_description=status_description,
            trigger_type=trigger_type,
            workflow_id=workflow_id,
        )

        service_create_ad_hoc_action_response.additional_properties = d
        return service_create_ad_hoc_action_response

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
