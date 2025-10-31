from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_install_action_workflow_run_step_status import AppInstallActionWorkflowRunStepStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="AppInstallActionWorkflowRunStep")


@_attrs_define
class AppInstallActionWorkflowRunStep:
    """
    Attributes:
        created_at (str | Unset):
        created_by_id (str | Unset):
        execution_duration (int | Unset):
        id (str | Unset):
        install_action_workflow_run_id (str | Unset):
        status (AppInstallActionWorkflowRunStepStatus | Unset):
        step_id (str | Unset):
        updated_at (str | Unset):
    """

    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    execution_duration: int | Unset = UNSET
    id: str | Unset = UNSET
    install_action_workflow_run_id: str | Unset = UNSET
    status: AppInstallActionWorkflowRunStepStatus | Unset = UNSET
    step_id: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        created_by_id = self.created_by_id

        execution_duration = self.execution_duration

        id = self.id

        install_action_workflow_run_id = self.install_action_workflow_run_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        step_id = self.step_id

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if execution_duration is not UNSET:
            field_dict["execution_duration"] = execution_duration
        if id is not UNSET:
            field_dict["id"] = id
        if install_action_workflow_run_id is not UNSET:
            field_dict["install_action_workflow_run_id"] = install_action_workflow_run_id
        if status is not UNSET:
            field_dict["status"] = status
        if step_id is not UNSET:
            field_dict["step_id"] = step_id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        execution_duration = d.pop("execution_duration", UNSET)

        id = d.pop("id", UNSET)

        install_action_workflow_run_id = d.pop("install_action_workflow_run_id", UNSET)

        _status = d.pop("status", UNSET)
        status: AppInstallActionWorkflowRunStepStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AppInstallActionWorkflowRunStepStatus(_status)

        step_id = d.pop("step_id", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        app_install_action_workflow_run_step = cls(
            created_at=created_at,
            created_by_id=created_by_id,
            execution_duration=execution_duration,
            id=id,
            install_action_workflow_run_id=install_action_workflow_run_id,
            status=status,
            step_id=step_id,
            updated_at=updated_at,
        )

        app_install_action_workflow_run_step.additional_properties = d
        return app_install_action_workflow_run_step

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
