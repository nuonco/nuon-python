from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_workflow_run_type import AppWorkflowRunType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_composite_status import AppCompositeStatus


T = TypeVar("T", bound="AppWorkflowRun")


@_attrs_define
class AppWorkflowRun:
    """
    Attributes:
        created_at (str | Unset):
        created_by_id (str | Unset):
        finished_at (str | Unset):
        id (str | Unset):
        start_from_idx (int | Unset): StartFromIdx is the step index to start execution from.
        started_at (str | Unset):
        status (AppCompositeStatus | Unset):
        trigger_step_id (str | Unset): TriggerStepID is the step that triggered this run (empty for initial runs).
        type_ (AppWorkflowRunType | Unset):
        updated_at (str | Unset):
        workflow_id (str | Unset):
    """

    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    finished_at: str | Unset = UNSET
    id: str | Unset = UNSET
    start_from_idx: int | Unset = UNSET
    started_at: str | Unset = UNSET
    status: AppCompositeStatus | Unset = UNSET
    trigger_step_id: str | Unset = UNSET
    type_: AppWorkflowRunType | Unset = UNSET
    updated_at: str | Unset = UNSET
    workflow_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        created_by_id = self.created_by_id

        finished_at = self.finished_at

        id = self.id

        start_from_idx = self.start_from_idx

        started_at = self.started_at

        status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        trigger_step_id = self.trigger_step_id

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        updated_at = self.updated_at

        workflow_id = self.workflow_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if finished_at is not UNSET:
            field_dict["finished_at"] = finished_at
        if id is not UNSET:
            field_dict["id"] = id
        if start_from_idx is not UNSET:
            field_dict["start_from_idx"] = start_from_idx
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if status is not UNSET:
            field_dict["status"] = status
        if trigger_step_id is not UNSET:
            field_dict["trigger_step_id"] = trigger_step_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if workflow_id is not UNSET:
            field_dict["workflow_id"] = workflow_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_composite_status import AppCompositeStatus

        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        finished_at = d.pop("finished_at", UNSET)

        id = d.pop("id", UNSET)

        start_from_idx = d.pop("start_from_idx", UNSET)

        started_at = d.pop("started_at", UNSET)

        _status = d.pop("status", UNSET)
        status: AppCompositeStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AppCompositeStatus.from_dict(_status)

        trigger_step_id = d.pop("trigger_step_id", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: AppWorkflowRunType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = AppWorkflowRunType(_type_)

        updated_at = d.pop("updated_at", UNSET)

        workflow_id = d.pop("workflow_id", UNSET)

        app_workflow_run = cls(
            created_at=created_at,
            created_by_id=created_by_id,
            finished_at=finished_at,
            id=id,
            start_from_idx=start_from_idx,
            started_at=started_at,
            status=status,
            trigger_step_id=trigger_step_id,
            type_=type_,
            updated_at=updated_at,
            workflow_id=workflow_id,
        )

        app_workflow_run.additional_properties = d
        return app_workflow_run

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
