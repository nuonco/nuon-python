from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_step_change_state import AppStepChangeState
from ..models.app_workflow_step_approval_type import AppWorkflowStepApprovalType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_runner_job import AppRunnerJob
    from ..models.app_workflow_step import AppWorkflowStep
    from ..models.app_workflow_step_approval_response import AppWorkflowStepApprovalResponse


T = TypeVar("T", bound="AppWorkflowStepApproval")


@_attrs_define
class AppWorkflowStepApproval:
    """
    Attributes:
        app_branch_id (str | Unset):
        app_id (str | Unset):
        changes_create (int | Unset):
        changes_delete (int | Unset):
        changes_noop (int | Unset):
        changes_replace (int | Unset):
        changes_state (AppStepChangeState | Unset):
        changes_update (int | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        id (str | Unset):
        install_workflow_step (AppWorkflowStep | Unset):
        install_workflow_step_id (str | Unset): the step that this approval belongs too
        owner_id (str | Unset):
        owner_type (str | Unset):
        response (AppWorkflowStepApprovalResponse | Unset):
        runner_job (AppRunnerJob | Unset):
        runner_job_id (str | Unset): the runner job where this approval was created
        type_ (AppWorkflowStepApprovalType | Unset):
        updated_at (str | Unset):
        workflow_step (AppWorkflowStep | Unset):
        workflow_step_id (str | Unset): afterquery
    """

    app_branch_id: str | Unset = UNSET
    app_id: str | Unset = UNSET
    changes_create: int | Unset = UNSET
    changes_delete: int | Unset = UNSET
    changes_noop: int | Unset = UNSET
    changes_replace: int | Unset = UNSET
    changes_state: AppStepChangeState | Unset = UNSET
    changes_update: int | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    id: str | Unset = UNSET
    install_workflow_step: AppWorkflowStep | Unset = UNSET
    install_workflow_step_id: str | Unset = UNSET
    owner_id: str | Unset = UNSET
    owner_type: str | Unset = UNSET
    response: AppWorkflowStepApprovalResponse | Unset = UNSET
    runner_job: AppRunnerJob | Unset = UNSET
    runner_job_id: str | Unset = UNSET
    type_: AppWorkflowStepApprovalType | Unset = UNSET
    updated_at: str | Unset = UNSET
    workflow_step: AppWorkflowStep | Unset = UNSET
    workflow_step_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_branch_id = self.app_branch_id

        app_id = self.app_id

        changes_create = self.changes_create

        changes_delete = self.changes_delete

        changes_noop = self.changes_noop

        changes_replace = self.changes_replace

        changes_state: str | Unset = UNSET
        if not isinstance(self.changes_state, Unset):
            changes_state = self.changes_state.value

        changes_update = self.changes_update

        created_at = self.created_at

        created_by_id = self.created_by_id

        id = self.id

        install_workflow_step: dict[str, Any] | Unset = UNSET
        if not isinstance(self.install_workflow_step, Unset):
            install_workflow_step = self.install_workflow_step.to_dict()

        install_workflow_step_id = self.install_workflow_step_id

        owner_id = self.owner_id

        owner_type = self.owner_type

        response: dict[str, Any] | Unset = UNSET
        if not isinstance(self.response, Unset):
            response = self.response.to_dict()

        runner_job: dict[str, Any] | Unset = UNSET
        if not isinstance(self.runner_job, Unset):
            runner_job = self.runner_job.to_dict()

        runner_job_id = self.runner_job_id

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        updated_at = self.updated_at

        workflow_step: dict[str, Any] | Unset = UNSET
        if not isinstance(self.workflow_step, Unset):
            workflow_step = self.workflow_step.to_dict()

        workflow_step_id = self.workflow_step_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_branch_id is not UNSET:
            field_dict["app_branch_id"] = app_branch_id
        if app_id is not UNSET:
            field_dict["app_id"] = app_id
        if changes_create is not UNSET:
            field_dict["changes_create"] = changes_create
        if changes_delete is not UNSET:
            field_dict["changes_delete"] = changes_delete
        if changes_noop is not UNSET:
            field_dict["changes_noop"] = changes_noop
        if changes_replace is not UNSET:
            field_dict["changes_replace"] = changes_replace
        if changes_state is not UNSET:
            field_dict["changes_state"] = changes_state
        if changes_update is not UNSET:
            field_dict["changes_update"] = changes_update
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if id is not UNSET:
            field_dict["id"] = id
        if install_workflow_step is not UNSET:
            field_dict["installWorkflowStep"] = install_workflow_step
        if install_workflow_step_id is not UNSET:
            field_dict["installWorkflowStepID"] = install_workflow_step_id
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if owner_type is not UNSET:
            field_dict["owner_type"] = owner_type
        if response is not UNSET:
            field_dict["response"] = response
        if runner_job is not UNSET:
            field_dict["runner_job"] = runner_job
        if runner_job_id is not UNSET:
            field_dict["runner_job_id"] = runner_job_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if workflow_step is not UNSET:
            field_dict["workflow_step"] = workflow_step
        if workflow_step_id is not UNSET:
            field_dict["workflow_step_id"] = workflow_step_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_runner_job import AppRunnerJob  # noqa: PLC0415
        from ..models.app_workflow_step import AppWorkflowStep  # noqa: PLC0415
        from ..models.app_workflow_step_approval_response import AppWorkflowStepApprovalResponse  # noqa: PLC0415

        d = dict(src_dict)
        app_branch_id = d.pop("app_branch_id", UNSET)

        app_id = d.pop("app_id", UNSET)

        changes_create = d.pop("changes_create", UNSET)

        changes_delete = d.pop("changes_delete", UNSET)

        changes_noop = d.pop("changes_noop", UNSET)

        changes_replace = d.pop("changes_replace", UNSET)

        _changes_state = d.pop("changes_state", UNSET)
        changes_state: AppStepChangeState | Unset
        if isinstance(_changes_state, Unset):
            changes_state = UNSET
        else:
            changes_state = AppStepChangeState(_changes_state)

        changes_update = d.pop("changes_update", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        id = d.pop("id", UNSET)

        _install_workflow_step = d.pop("installWorkflowStep", UNSET)
        install_workflow_step: AppWorkflowStep | Unset
        if isinstance(_install_workflow_step, Unset):
            install_workflow_step = UNSET
        else:
            install_workflow_step = AppWorkflowStep.from_dict(_install_workflow_step)

        install_workflow_step_id = d.pop("installWorkflowStepID", UNSET)

        owner_id = d.pop("owner_id", UNSET)

        owner_type = d.pop("owner_type", UNSET)

        _response = d.pop("response", UNSET)
        response: AppWorkflowStepApprovalResponse | Unset
        if isinstance(_response, Unset):
            response = UNSET
        else:
            response = AppWorkflowStepApprovalResponse.from_dict(_response)

        _runner_job = d.pop("runner_job", UNSET)
        runner_job: AppRunnerJob | Unset
        if isinstance(_runner_job, Unset):
            runner_job = UNSET
        else:
            runner_job = AppRunnerJob.from_dict(_runner_job)

        runner_job_id = d.pop("runner_job_id", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: AppWorkflowStepApprovalType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = AppWorkflowStepApprovalType(_type_)

        updated_at = d.pop("updated_at", UNSET)

        _workflow_step = d.pop("workflow_step", UNSET)
        workflow_step: AppWorkflowStep | Unset
        if isinstance(_workflow_step, Unset):
            workflow_step = UNSET
        else:
            workflow_step = AppWorkflowStep.from_dict(_workflow_step)

        workflow_step_id = d.pop("workflow_step_id", UNSET)

        app_workflow_step_approval = cls(
            app_branch_id=app_branch_id,
            app_id=app_id,
            changes_create=changes_create,
            changes_delete=changes_delete,
            changes_noop=changes_noop,
            changes_replace=changes_replace,
            changes_state=changes_state,
            changes_update=changes_update,
            created_at=created_at,
            created_by_id=created_by_id,
            id=id,
            install_workflow_step=install_workflow_step,
            install_workflow_step_id=install_workflow_step_id,
            owner_id=owner_id,
            owner_type=owner_type,
            response=response,
            runner_job=runner_job,
            runner_job_id=runner_job_id,
            type_=type_,
            updated_at=updated_at,
            workflow_step=workflow_step,
            workflow_step_id=workflow_step_id,
        )

        app_workflow_step_approval.additional_properties = d
        return app_workflow_step_approval

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
