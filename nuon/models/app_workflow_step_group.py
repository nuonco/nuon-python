from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_composite_status import AppCompositeStatus
    from ..models.app_queue_signal import AppQueueSignal
    from ..models.app_workflow_step import AppWorkflowStep


T = TypeVar("T", bound="AppWorkflowStepGroup")


@_attrs_define
class AppWorkflowStepGroup:
    """
    Attributes:
        created_at (str | Unset):
        created_by_id (str | Unset):
        group_idx (int | Unset):
        id (str | Unset):
        name (str | Unset):
        parallel (bool | Unset):
        queue_signal (AppQueueSignal | Unset):
        result_directive (str | Unset):
        status (AppCompositeStatus | Unset):
        steps (list[AppWorkflowStep] | Unset):
        updated_at (str | Unset):
        workflow_id (str | Unset):
    """

    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    group_idx: int | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    parallel: bool | Unset = UNSET
    queue_signal: AppQueueSignal | Unset = UNSET
    result_directive: str | Unset = UNSET
    status: AppCompositeStatus | Unset = UNSET
    steps: list[AppWorkflowStep] | Unset = UNSET
    updated_at: str | Unset = UNSET
    workflow_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        created_by_id = self.created_by_id

        group_idx = self.group_idx

        id = self.id

        name = self.name

        parallel = self.parallel

        queue_signal: dict[str, Any] | Unset = UNSET
        if not isinstance(self.queue_signal, Unset):
            queue_signal = self.queue_signal.to_dict()

        result_directive = self.result_directive

        status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        steps: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.steps, Unset):
            steps = []
            for steps_item_data in self.steps:
                steps_item = steps_item_data.to_dict()
                steps.append(steps_item)

        updated_at = self.updated_at

        workflow_id = self.workflow_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if group_idx is not UNSET:
            field_dict["group_idx"] = group_idx
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if parallel is not UNSET:
            field_dict["parallel"] = parallel
        if queue_signal is not UNSET:
            field_dict["queue_signal"] = queue_signal
        if result_directive is not UNSET:
            field_dict["result_directive"] = result_directive
        if status is not UNSET:
            field_dict["status"] = status
        if steps is not UNSET:
            field_dict["steps"] = steps
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if workflow_id is not UNSET:
            field_dict["workflow_id"] = workflow_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_composite_status import AppCompositeStatus
        from ..models.app_queue_signal import AppQueueSignal
        from ..models.app_workflow_step import AppWorkflowStep

        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        group_idx = d.pop("group_idx", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        parallel = d.pop("parallel", UNSET)

        _queue_signal = d.pop("queue_signal", UNSET)
        queue_signal: AppQueueSignal | Unset
        if isinstance(_queue_signal, Unset):
            queue_signal = UNSET
        else:
            queue_signal = AppQueueSignal.from_dict(_queue_signal)

        result_directive = d.pop("result_directive", UNSET)

        _status = d.pop("status", UNSET)
        status: AppCompositeStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AppCompositeStatus.from_dict(_status)

        _steps = d.pop("steps", UNSET)
        steps: list[AppWorkflowStep] | Unset = UNSET
        if _steps is not UNSET:
            steps = []
            for steps_item_data in _steps:
                steps_item = AppWorkflowStep.from_dict(steps_item_data)

                steps.append(steps_item)

        updated_at = d.pop("updated_at", UNSET)

        workflow_id = d.pop("workflow_id", UNSET)

        app_workflow_step_group = cls(
            created_at=created_at,
            created_by_id=created_by_id,
            group_idx=group_idx,
            id=id,
            name=name,
            parallel=parallel,
            queue_signal=queue_signal,
            result_directive=result_directive,
            status=status,
            steps=steps,
            updated_at=updated_at,
            workflow_id=workflow_id,
        )

        app_workflow_step_group.additional_properties = d
        return app_workflow_step_group

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
