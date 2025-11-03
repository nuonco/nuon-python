from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_install_approval_option import AppInstallApprovalOption
from ..models.app_step_error_behavior import AppStepErrorBehavior
from ..models.app_workflow_type import AppWorkflowType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_account import AppAccount
    from ..models.app_composite_status import AppCompositeStatus
    from ..models.app_install_action_workflow_run import AppInstallActionWorkflowRun
    from ..models.app_install_deploy import AppInstallDeploy
    from ..models.app_install_sandbox_run import AppInstallSandboxRun
    from ..models.app_workflow_links import AppWorkflowLinks
    from ..models.app_workflow_metadata import AppWorkflowMetadata
    from ..models.app_workflow_step import AppWorkflowStep


T = TypeVar("T", bound="AppWorkflow")


@_attrs_define
class AppWorkflow:
    """
    Attributes:
        approval_option (AppInstallApprovalOption | Unset):
        created_at (str | Unset):
        created_by (AppAccount | Unset):
        created_by_id (str | Unset):
        execution_time (int | Unset):
        finished (bool | Unset):
        finished_at (str | Unset):
        id (str | Unset):
        install_action_workflow_runs (list[AppInstallActionWorkflowRun] | Unset):
        install_deploys (list[AppInstallDeploy] | Unset):
        install_sandbox_runs (list[AppInstallSandboxRun] | Unset):
        links (AppWorkflowLinks | Unset):
        metadata (AppWorkflowMetadata | Unset):
        name (str | Unset):
        owner_id (str | Unset):
        owner_type (str | Unset):
        plan_only (bool | Unset):
        started_at (str | Unset):
        status (AppCompositeStatus | Unset):
        step_error_behavior (AppStepErrorBehavior | Unset):
        steps (list[AppWorkflowStep] | Unset): steps represent each piece of the workflow
        type_ (AppWorkflowType | Unset):
        updated_at (str | Unset):
    """

    approval_option: AppInstallApprovalOption | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by: AppAccount | Unset = UNSET
    created_by_id: str | Unset = UNSET
    execution_time: int | Unset = UNSET
    finished: bool | Unset = UNSET
    finished_at: str | Unset = UNSET
    id: str | Unset = UNSET
    install_action_workflow_runs: list[AppInstallActionWorkflowRun] | Unset = UNSET
    install_deploys: list[AppInstallDeploy] | Unset = UNSET
    install_sandbox_runs: list[AppInstallSandboxRun] | Unset = UNSET
    links: AppWorkflowLinks | Unset = UNSET
    metadata: AppWorkflowMetadata | Unset = UNSET
    name: str | Unset = UNSET
    owner_id: str | Unset = UNSET
    owner_type: str | Unset = UNSET
    plan_only: bool | Unset = UNSET
    started_at: str | Unset = UNSET
    status: AppCompositeStatus | Unset = UNSET
    step_error_behavior: AppStepErrorBehavior | Unset = UNSET
    steps: list[AppWorkflowStep] | Unset = UNSET
    type_: AppWorkflowType | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        approval_option: str | Unset = UNSET
        if not isinstance(self.approval_option, Unset):
            approval_option = self.approval_option.value

        created_at = self.created_at

        created_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        created_by_id = self.created_by_id

        execution_time = self.execution_time

        finished = self.finished

        finished_at = self.finished_at

        id = self.id

        install_action_workflow_runs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.install_action_workflow_runs, Unset):
            install_action_workflow_runs = []
            for install_action_workflow_runs_item_data in self.install_action_workflow_runs:
                install_action_workflow_runs_item = install_action_workflow_runs_item_data.to_dict()
                install_action_workflow_runs.append(install_action_workflow_runs_item)

        install_deploys: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.install_deploys, Unset):
            install_deploys = []
            for install_deploys_item_data in self.install_deploys:
                install_deploys_item = install_deploys_item_data.to_dict()
                install_deploys.append(install_deploys_item)

        install_sandbox_runs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.install_sandbox_runs, Unset):
            install_sandbox_runs = []
            for install_sandbox_runs_item_data in self.install_sandbox_runs:
                install_sandbox_runs_item = install_sandbox_runs_item_data.to_dict()
                install_sandbox_runs.append(install_sandbox_runs_item)

        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        name = self.name

        owner_id = self.owner_id

        owner_type = self.owner_type

        plan_only = self.plan_only

        started_at = self.started_at

        status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        step_error_behavior: str | Unset = UNSET
        if not isinstance(self.step_error_behavior, Unset):
            step_error_behavior = self.step_error_behavior.value

        steps: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.steps, Unset):
            steps = []
            for steps_item_data in self.steps:
                steps_item = steps_item_data.to_dict()
                steps.append(steps_item)

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if approval_option is not UNSET:
            field_dict["approval_option"] = approval_option
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if execution_time is not UNSET:
            field_dict["execution_time"] = execution_time
        if finished is not UNSET:
            field_dict["finished"] = finished
        if finished_at is not UNSET:
            field_dict["finished_at"] = finished_at
        if id is not UNSET:
            field_dict["id"] = id
        if install_action_workflow_runs is not UNSET:
            field_dict["install_action_workflow_runs"] = install_action_workflow_runs
        if install_deploys is not UNSET:
            field_dict["install_deploys"] = install_deploys
        if install_sandbox_runs is not UNSET:
            field_dict["install_sandbox_runs"] = install_sandbox_runs
        if links is not UNSET:
            field_dict["links"] = links
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if name is not UNSET:
            field_dict["name"] = name
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if owner_type is not UNSET:
            field_dict["owner_type"] = owner_type
        if plan_only is not UNSET:
            field_dict["plan_only"] = plan_only
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if status is not UNSET:
            field_dict["status"] = status
        if step_error_behavior is not UNSET:
            field_dict["step_error_behavior"] = step_error_behavior
        if steps is not UNSET:
            field_dict["steps"] = steps
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_account import AppAccount
        from ..models.app_composite_status import AppCompositeStatus
        from ..models.app_install_action_workflow_run import AppInstallActionWorkflowRun
        from ..models.app_install_deploy import AppInstallDeploy
        from ..models.app_install_sandbox_run import AppInstallSandboxRun
        from ..models.app_workflow_links import AppWorkflowLinks
        from ..models.app_workflow_metadata import AppWorkflowMetadata
        from ..models.app_workflow_step import AppWorkflowStep

        d = dict(src_dict)
        _approval_option = d.pop("approval_option", UNSET)
        approval_option: AppInstallApprovalOption | Unset
        if isinstance(_approval_option, Unset):
            approval_option = UNSET
        else:
            approval_option = AppInstallApprovalOption(_approval_option)

        created_at = d.pop("created_at", UNSET)

        _created_by = d.pop("created_by", UNSET)
        created_by: AppAccount | Unset
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = AppAccount.from_dict(_created_by)

        created_by_id = d.pop("created_by_id", UNSET)

        execution_time = d.pop("execution_time", UNSET)

        finished = d.pop("finished", UNSET)

        finished_at = d.pop("finished_at", UNSET)

        id = d.pop("id", UNSET)

        _install_action_workflow_runs = d.pop("install_action_workflow_runs", UNSET)
        install_action_workflow_runs: list[AppInstallActionWorkflowRun] | Unset = UNSET
        if _install_action_workflow_runs is not UNSET:
            install_action_workflow_runs = []
            for install_action_workflow_runs_item_data in _install_action_workflow_runs:
                install_action_workflow_runs_item = AppInstallActionWorkflowRun.from_dict(
                    install_action_workflow_runs_item_data
                )

                install_action_workflow_runs.append(install_action_workflow_runs_item)

        _install_deploys = d.pop("install_deploys", UNSET)
        install_deploys: list[AppInstallDeploy] | Unset = UNSET
        if _install_deploys is not UNSET:
            install_deploys = []
            for install_deploys_item_data in _install_deploys:
                install_deploys_item = AppInstallDeploy.from_dict(install_deploys_item_data)

                install_deploys.append(install_deploys_item)

        _install_sandbox_runs = d.pop("install_sandbox_runs", UNSET)
        install_sandbox_runs: list[AppInstallSandboxRun] | Unset = UNSET
        if _install_sandbox_runs is not UNSET:
            install_sandbox_runs = []
            for install_sandbox_runs_item_data in _install_sandbox_runs:
                install_sandbox_runs_item = AppInstallSandboxRun.from_dict(install_sandbox_runs_item_data)

                install_sandbox_runs.append(install_sandbox_runs_item)

        _links = d.pop("links", UNSET)
        links: AppWorkflowLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = AppWorkflowLinks.from_dict(_links)

        _metadata = d.pop("metadata", UNSET)
        metadata: AppWorkflowMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = AppWorkflowMetadata.from_dict(_metadata)

        name = d.pop("name", UNSET)

        owner_id = d.pop("owner_id", UNSET)

        owner_type = d.pop("owner_type", UNSET)

        plan_only = d.pop("plan_only", UNSET)

        started_at = d.pop("started_at", UNSET)

        _status = d.pop("status", UNSET)
        status: AppCompositeStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AppCompositeStatus.from_dict(_status)

        _step_error_behavior = d.pop("step_error_behavior", UNSET)
        step_error_behavior: AppStepErrorBehavior | Unset
        if isinstance(_step_error_behavior, Unset):
            step_error_behavior = UNSET
        else:
            step_error_behavior = AppStepErrorBehavior(_step_error_behavior)

        _steps = d.pop("steps", UNSET)
        steps: list[AppWorkflowStep] | Unset = UNSET
        if _steps is not UNSET:
            steps = []
            for steps_item_data in _steps:
                steps_item = AppWorkflowStep.from_dict(steps_item_data)

                steps.append(steps_item)

        _type_ = d.pop("type", UNSET)
        type_: AppWorkflowType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = AppWorkflowType(_type_)

        updated_at = d.pop("updated_at", UNSET)

        app_workflow = cls(
            approval_option=approval_option,
            created_at=created_at,
            created_by=created_by,
            created_by_id=created_by_id,
            execution_time=execution_time,
            finished=finished,
            finished_at=finished_at,
            id=id,
            install_action_workflow_runs=install_action_workflow_runs,
            install_deploys=install_deploys,
            install_sandbox_runs=install_sandbox_runs,
            links=links,
            metadata=metadata,
            name=name,
            owner_id=owner_id,
            owner_type=owner_type,
            plan_only=plan_only,
            started_at=started_at,
            status=status,
            step_error_behavior=step_error_behavior,
            steps=steps,
            type_=type_,
            updated_at=updated_at,
        )

        app_workflow.additional_properties = d
        return app_workflow

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
