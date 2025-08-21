from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

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
        created_at (Union[Unset, str]):
        created_by_id (Union[Unset, str]):
        id (Union[Unset, str]):
        install_workflow_step (Union[Unset, AppWorkflowStep]):
        install_workflow_step_id (Union[Unset, str]): the step that this approval belongs too
        owner_id (Union[Unset, str]):
        owner_type (Union[Unset, str]):
        response (Union[Unset, AppWorkflowStepApprovalResponse]):
        runner_job (Union[Unset, AppRunnerJob]):
        runner_job_id (Union[Unset, str]): the runner job where this approval was created
        type_ (Union[Unset, AppWorkflowStepApprovalType]):
        updated_at (Union[Unset, str]):
        workflow_step (Union[Unset, AppWorkflowStep]):
        workflow_step_id (Union[Unset, str]): afterquery
    """

    created_at: Union[Unset, str] = UNSET
    created_by_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    install_workflow_step: Union[Unset, "AppWorkflowStep"] = UNSET
    install_workflow_step_id: Union[Unset, str] = UNSET
    owner_id: Union[Unset, str] = UNSET
    owner_type: Union[Unset, str] = UNSET
    response: Union[Unset, "AppWorkflowStepApprovalResponse"] = UNSET
    runner_job: Union[Unset, "AppRunnerJob"] = UNSET
    runner_job_id: Union[Unset, str] = UNSET
    type_: Union[Unset, AppWorkflowStepApprovalType] = UNSET
    updated_at: Union[Unset, str] = UNSET
    workflow_step: Union[Unset, "AppWorkflowStep"] = UNSET
    workflow_step_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        created_by_id = self.created_by_id

        id = self.id

        install_workflow_step: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.install_workflow_step, Unset):
            install_workflow_step = self.install_workflow_step.to_dict()

        install_workflow_step_id = self.install_workflow_step_id

        owner_id = self.owner_id

        owner_type = self.owner_type

        response: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.response, Unset):
            response = self.response.to_dict()

        runner_job: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.runner_job, Unset):
            runner_job = self.runner_job.to_dict()

        runner_job_id = self.runner_job_id

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        updated_at = self.updated_at

        workflow_step: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.workflow_step, Unset):
            workflow_step = self.workflow_step.to_dict()

        workflow_step_id = self.workflow_step_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
            field_dict["runnerJob"] = runner_job
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
        from ..models.app_runner_job import AppRunnerJob
        from ..models.app_workflow_step import AppWorkflowStep
        from ..models.app_workflow_step_approval_response import AppWorkflowStepApprovalResponse

        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        id = d.pop("id", UNSET)

        _install_workflow_step = d.pop("installWorkflowStep", UNSET)
        install_workflow_step: Union[Unset, AppWorkflowStep]
        if isinstance(_install_workflow_step, Unset):
            install_workflow_step = UNSET
        else:
            install_workflow_step = AppWorkflowStep.from_dict(_install_workflow_step)

        install_workflow_step_id = d.pop("installWorkflowStepID", UNSET)

        owner_id = d.pop("owner_id", UNSET)

        owner_type = d.pop("owner_type", UNSET)

        _response = d.pop("response", UNSET)
        response: Union[Unset, AppWorkflowStepApprovalResponse]
        if isinstance(_response, Unset):
            response = UNSET
        else:
            response = AppWorkflowStepApprovalResponse.from_dict(_response)

        _runner_job = d.pop("runnerJob", UNSET)
        runner_job: Union[Unset, AppRunnerJob]
        if isinstance(_runner_job, Unset):
            runner_job = UNSET
        else:
            runner_job = AppRunnerJob.from_dict(_runner_job)

        runner_job_id = d.pop("runner_job_id", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, AppWorkflowStepApprovalType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = AppWorkflowStepApprovalType(_type_)

        updated_at = d.pop("updated_at", UNSET)

        _workflow_step = d.pop("workflow_step", UNSET)
        workflow_step: Union[Unset, AppWorkflowStep]
        if isinstance(_workflow_step, Unset):
            workflow_step = UNSET
        else:
            workflow_step = AppWorkflowStep.from_dict(_workflow_step)

        workflow_step_id = d.pop("workflow_step_id", UNSET)

        app_workflow_step_approval = cls(
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
