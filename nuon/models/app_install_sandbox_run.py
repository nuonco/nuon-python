from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_sandbox_run_type import AppSandboxRunType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_account import AppAccount
    from ..models.app_app_sandbox_config import AppAppSandboxConfig
    from ..models.app_composite_status import AppCompositeStatus
    from ..models.app_install_action_workflow_run import AppInstallActionWorkflowRun
    from ..models.app_install_sandbox_run_outputs import AppInstallSandboxRunOutputs
    from ..models.app_log_stream import AppLogStream
    from ..models.app_policy_report import AppPolicyReport
    from ..models.app_runner_job import AppRunnerJob
    from ..models.app_workflow import AppWorkflow


T = TypeVar("T", bound="AppInstallSandboxRun")


@_attrs_define
class AppInstallSandboxRun:
    """
    Attributes:
        action_workflow_runs (list[AppInstallActionWorkflowRun] | Unset):
        app_sandbox_config (AppAppSandboxConfig | Unset):
        created_at (str | Unset):
        created_by (AppAccount | Unset):
        created_by_id (str | Unset):
        id (str | Unset):
        install_id (str | Unset):
        install_sandbox_id (str | Unset): TODO: once we run a backfill we can make this non pointer
        install_workflow_id (str | Unset):
        log_stream (AppLogStream | Unset):
        outputs (AppInstallSandboxRunOutputs | Unset):
        policy_reports (list[AppPolicyReport] | Unset):
        run_type (AppSandboxRunType | Unset):
        runner_jobs (list[AppRunnerJob] | Unset): runner details
        status (str | Unset):
        status_description (str | Unset):
        status_v2 (AppCompositeStatus | Unset):
        updated_at (str | Unset):
        workflow (AppWorkflow | Unset):
        workflow_id (str | Unset): Fields that are de-nested at read time using AfterQuery
    """

    action_workflow_runs: list[AppInstallActionWorkflowRun] | Unset = UNSET
    app_sandbox_config: AppAppSandboxConfig | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by: AppAccount | Unset = UNSET
    created_by_id: str | Unset = UNSET
    id: str | Unset = UNSET
    install_id: str | Unset = UNSET
    install_sandbox_id: str | Unset = UNSET
    install_workflow_id: str | Unset = UNSET
    log_stream: AppLogStream | Unset = UNSET
    outputs: AppInstallSandboxRunOutputs | Unset = UNSET
    policy_reports: list[AppPolicyReport] | Unset = UNSET
    run_type: AppSandboxRunType | Unset = UNSET
    runner_jobs: list[AppRunnerJob] | Unset = UNSET
    status: str | Unset = UNSET
    status_description: str | Unset = UNSET
    status_v2: AppCompositeStatus | Unset = UNSET
    updated_at: str | Unset = UNSET
    workflow: AppWorkflow | Unset = UNSET
    workflow_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action_workflow_runs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.action_workflow_runs, Unset):
            action_workflow_runs = []
            for action_workflow_runs_item_data in self.action_workflow_runs:
                action_workflow_runs_item = action_workflow_runs_item_data.to_dict()
                action_workflow_runs.append(action_workflow_runs_item)

        app_sandbox_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.app_sandbox_config, Unset):
            app_sandbox_config = self.app_sandbox_config.to_dict()

        created_at = self.created_at

        created_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        created_by_id = self.created_by_id

        id = self.id

        install_id = self.install_id

        install_sandbox_id = self.install_sandbox_id

        install_workflow_id = self.install_workflow_id

        log_stream: dict[str, Any] | Unset = UNSET
        if not isinstance(self.log_stream, Unset):
            log_stream = self.log_stream.to_dict()

        outputs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.outputs, Unset):
            outputs = self.outputs.to_dict()

        policy_reports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.policy_reports, Unset):
            policy_reports = []
            for policy_reports_item_data in self.policy_reports:
                policy_reports_item = policy_reports_item_data.to_dict()
                policy_reports.append(policy_reports_item)

        run_type: str | Unset = UNSET
        if not isinstance(self.run_type, Unset):
            run_type = self.run_type.value

        runner_jobs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.runner_jobs, Unset):
            runner_jobs = []
            for runner_jobs_item_data in self.runner_jobs:
                runner_jobs_item = runner_jobs_item_data.to_dict()
                runner_jobs.append(runner_jobs_item)

        status = self.status

        status_description = self.status_description

        status_v2: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status_v2, Unset):
            status_v2 = self.status_v2.to_dict()

        updated_at = self.updated_at

        workflow: dict[str, Any] | Unset = UNSET
        if not isinstance(self.workflow, Unset):
            workflow = self.workflow.to_dict()

        workflow_id = self.workflow_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action_workflow_runs is not UNSET:
            field_dict["action_workflow_runs"] = action_workflow_runs
        if app_sandbox_config is not UNSET:
            field_dict["app_sandbox_config"] = app_sandbox_config
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if id is not UNSET:
            field_dict["id"] = id
        if install_id is not UNSET:
            field_dict["install_id"] = install_id
        if install_sandbox_id is not UNSET:
            field_dict["install_sandbox_id"] = install_sandbox_id
        if install_workflow_id is not UNSET:
            field_dict["install_workflow_id"] = install_workflow_id
        if log_stream is not UNSET:
            field_dict["log_stream"] = log_stream
        if outputs is not UNSET:
            field_dict["outputs"] = outputs
        if policy_reports is not UNSET:
            field_dict["policy_reports"] = policy_reports
        if run_type is not UNSET:
            field_dict["run_type"] = run_type
        if runner_jobs is not UNSET:
            field_dict["runner_jobs"] = runner_jobs
        if status is not UNSET:
            field_dict["status"] = status
        if status_description is not UNSET:
            field_dict["status_description"] = status_description
        if status_v2 is not UNSET:
            field_dict["status_v2"] = status_v2
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if workflow is not UNSET:
            field_dict["workflow"] = workflow
        if workflow_id is not UNSET:
            field_dict["workflow_id"] = workflow_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_account import AppAccount
        from ..models.app_app_sandbox_config import AppAppSandboxConfig
        from ..models.app_composite_status import AppCompositeStatus
        from ..models.app_install_action_workflow_run import AppInstallActionWorkflowRun
        from ..models.app_install_sandbox_run_outputs import AppInstallSandboxRunOutputs
        from ..models.app_log_stream import AppLogStream
        from ..models.app_policy_report import AppPolicyReport
        from ..models.app_runner_job import AppRunnerJob
        from ..models.app_workflow import AppWorkflow

        d = dict(src_dict)
        _action_workflow_runs = d.pop("action_workflow_runs", UNSET)
        action_workflow_runs: list[AppInstallActionWorkflowRun] | Unset = UNSET
        if _action_workflow_runs is not UNSET:
            action_workflow_runs = []
            for action_workflow_runs_item_data in _action_workflow_runs:
                action_workflow_runs_item = AppInstallActionWorkflowRun.from_dict(action_workflow_runs_item_data)

                action_workflow_runs.append(action_workflow_runs_item)

        _app_sandbox_config = d.pop("app_sandbox_config", UNSET)
        app_sandbox_config: AppAppSandboxConfig | Unset
        if isinstance(_app_sandbox_config, Unset):
            app_sandbox_config = UNSET
        else:
            app_sandbox_config = AppAppSandboxConfig.from_dict(_app_sandbox_config)

        created_at = d.pop("created_at", UNSET)

        _created_by = d.pop("created_by", UNSET)
        created_by: AppAccount | Unset
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = AppAccount.from_dict(_created_by)

        created_by_id = d.pop("created_by_id", UNSET)

        id = d.pop("id", UNSET)

        install_id = d.pop("install_id", UNSET)

        install_sandbox_id = d.pop("install_sandbox_id", UNSET)

        install_workflow_id = d.pop("install_workflow_id", UNSET)

        _log_stream = d.pop("log_stream", UNSET)
        log_stream: AppLogStream | Unset
        if isinstance(_log_stream, Unset):
            log_stream = UNSET
        else:
            log_stream = AppLogStream.from_dict(_log_stream)

        _outputs = d.pop("outputs", UNSET)
        outputs: AppInstallSandboxRunOutputs | Unset
        if isinstance(_outputs, Unset):
            outputs = UNSET
        else:
            outputs = AppInstallSandboxRunOutputs.from_dict(_outputs)

        _policy_reports = d.pop("policy_reports", UNSET)
        policy_reports: list[AppPolicyReport] | Unset = UNSET
        if _policy_reports is not UNSET:
            policy_reports = []
            for policy_reports_item_data in _policy_reports:
                policy_reports_item = AppPolicyReport.from_dict(policy_reports_item_data)

                policy_reports.append(policy_reports_item)

        _run_type = d.pop("run_type", UNSET)
        run_type: AppSandboxRunType | Unset
        if isinstance(_run_type, Unset):
            run_type = UNSET
        else:
            run_type = AppSandboxRunType(_run_type)

        _runner_jobs = d.pop("runner_jobs", UNSET)
        runner_jobs: list[AppRunnerJob] | Unset = UNSET
        if _runner_jobs is not UNSET:
            runner_jobs = []
            for runner_jobs_item_data in _runner_jobs:
                runner_jobs_item = AppRunnerJob.from_dict(runner_jobs_item_data)

                runner_jobs.append(runner_jobs_item)

        status = d.pop("status", UNSET)

        status_description = d.pop("status_description", UNSET)

        _status_v2 = d.pop("status_v2", UNSET)
        status_v2: AppCompositeStatus | Unset
        if isinstance(_status_v2, Unset):
            status_v2 = UNSET
        else:
            status_v2 = AppCompositeStatus.from_dict(_status_v2)

        updated_at = d.pop("updated_at", UNSET)

        _workflow = d.pop("workflow", UNSET)
        workflow: AppWorkflow | Unset
        if isinstance(_workflow, Unset):
            workflow = UNSET
        else:
            workflow = AppWorkflow.from_dict(_workflow)

        workflow_id = d.pop("workflow_id", UNSET)

        app_install_sandbox_run = cls(
            action_workflow_runs=action_workflow_runs,
            app_sandbox_config=app_sandbox_config,
            created_at=created_at,
            created_by=created_by,
            created_by_id=created_by_id,
            id=id,
            install_id=install_id,
            install_sandbox_id=install_sandbox_id,
            install_workflow_id=install_workflow_id,
            log_stream=log_stream,
            outputs=outputs,
            policy_reports=policy_reports,
            run_type=run_type,
            runner_jobs=runner_jobs,
            status=status,
            status_description=status_description,
            status_v2=status_v2,
            updated_at=updated_at,
            workflow=workflow,
            workflow_id=workflow_id,
        )

        app_install_sandbox_run.additional_properties = d
        return app_install_sandbox_run

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
