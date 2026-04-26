from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_install_role_selection_record import AppInstallRoleSelectionRecord
    from ..models.app_runner_job import AppRunnerJob
    from ..models.app_workflow import AppWorkflow


T = TypeVar("T", bound="AppInstallRoleUsage")


@_attrs_define
class AppInstallRoleUsage:
    """
    Attributes:
        created_at (str | Unset):
        created_by_id (str | Unset):
        id (str | Unset):
        install_role_id (str | Unset):
        org_id (str | Unset):
        role_name (str | Unset):
        role_selection_trace (list[AppInstallRoleSelectionRecord] | Unset):
        role_source (str | Unset):
        runner_job (AppRunnerJob | Unset):
        runner_job_id (str | Unset):
        updated_at (str | Unset):
        workflow (AppWorkflow | Unset):
        workflow_step_id (str | Unset):
    """

    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    id: str | Unset = UNSET
    install_role_id: str | Unset = UNSET
    org_id: str | Unset = UNSET
    role_name: str | Unset = UNSET
    role_selection_trace: list[AppInstallRoleSelectionRecord] | Unset = UNSET
    role_source: str | Unset = UNSET
    runner_job: AppRunnerJob | Unset = UNSET
    runner_job_id: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    workflow: AppWorkflow | Unset = UNSET
    workflow_step_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        created_by_id = self.created_by_id

        id = self.id

        install_role_id = self.install_role_id

        org_id = self.org_id

        role_name = self.role_name

        role_selection_trace: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.role_selection_trace, Unset):
            role_selection_trace = []
            for role_selection_trace_item_data in self.role_selection_trace:
                role_selection_trace_item = role_selection_trace_item_data.to_dict()
                role_selection_trace.append(role_selection_trace_item)

        role_source = self.role_source

        runner_job: dict[str, Any] | Unset = UNSET
        if not isinstance(self.runner_job, Unset):
            runner_job = self.runner_job.to_dict()

        runner_job_id = self.runner_job_id

        updated_at = self.updated_at

        workflow: dict[str, Any] | Unset = UNSET
        if not isinstance(self.workflow, Unset):
            workflow = self.workflow.to_dict()

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
        if install_role_id is not UNSET:
            field_dict["install_role_id"] = install_role_id
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if role_name is not UNSET:
            field_dict["role_name"] = role_name
        if role_selection_trace is not UNSET:
            field_dict["role_selection_trace"] = role_selection_trace
        if role_source is not UNSET:
            field_dict["role_source"] = role_source
        if runner_job is not UNSET:
            field_dict["runner_job"] = runner_job
        if runner_job_id is not UNSET:
            field_dict["runner_job_id"] = runner_job_id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if workflow is not UNSET:
            field_dict["workflow"] = workflow
        if workflow_step_id is not UNSET:
            field_dict["workflow_step_id"] = workflow_step_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_install_role_selection_record import AppInstallRoleSelectionRecord
        from ..models.app_runner_job import AppRunnerJob
        from ..models.app_workflow import AppWorkflow

        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        id = d.pop("id", UNSET)

        install_role_id = d.pop("install_role_id", UNSET)

        org_id = d.pop("org_id", UNSET)

        role_name = d.pop("role_name", UNSET)

        _role_selection_trace = d.pop("role_selection_trace", UNSET)
        role_selection_trace: list[AppInstallRoleSelectionRecord] | Unset = UNSET
        if _role_selection_trace is not UNSET:
            role_selection_trace = []
            for role_selection_trace_item_data in _role_selection_trace:
                role_selection_trace_item = AppInstallRoleSelectionRecord.from_dict(role_selection_trace_item_data)

                role_selection_trace.append(role_selection_trace_item)

        role_source = d.pop("role_source", UNSET)

        _runner_job = d.pop("runner_job", UNSET)
        runner_job: AppRunnerJob | Unset
        if isinstance(_runner_job, Unset):
            runner_job = UNSET
        else:
            runner_job = AppRunnerJob.from_dict(_runner_job)

        runner_job_id = d.pop("runner_job_id", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        _workflow = d.pop("workflow", UNSET)
        workflow: AppWorkflow | Unset
        if isinstance(_workflow, Unset):
            workflow = UNSET
        else:
            workflow = AppWorkflow.from_dict(_workflow)

        workflow_step_id = d.pop("workflow_step_id", UNSET)

        app_install_role_usage = cls(
            created_at=created_at,
            created_by_id=created_by_id,
            id=id,
            install_role_id=install_role_id,
            org_id=org_id,
            role_name=role_name,
            role_selection_trace=role_selection_trace,
            role_source=role_source,
            runner_job=runner_job,
            runner_job_id=runner_job_id,
            updated_at=updated_at,
            workflow=workflow,
            workflow_step_id=workflow_step_id,
        )

        app_install_role_usage.additional_properties = d
        return app_install_role_usage

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
