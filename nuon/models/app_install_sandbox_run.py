from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

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
    from ..models.app_runner_job import AppRunnerJob
    from ..models.app_workflow import AppWorkflow


T = TypeVar("T", bound="AppInstallSandboxRun")


@_attrs_define
class AppInstallSandboxRun:
    """
    Attributes:
        action_workflow_runs (Union[Unset, list['AppInstallActionWorkflowRun']]):
        app_sandbox_config (Union[Unset, AppAppSandboxConfig]):
        created_at (Union[Unset, str]):
        created_by (Union[Unset, AppAccount]):
        created_by_id (Union[Unset, str]):
        id (Union[Unset, str]):
        install_id (Union[Unset, str]):
        install_sandbox_id (Union[Unset, str]): TODO: once we run a backfill we can make this non pointer
        install_workflow_id (Union[Unset, str]):
        log_stream (Union[Unset, AppLogStream]):
        outputs (Union[Unset, AppInstallSandboxRunOutputs]):
        run_type (Union[Unset, AppSandboxRunType]):
        runner_jobs (Union[Unset, list['AppRunnerJob']]): runner details
        status (Union[Unset, str]):
        status_description (Union[Unset, str]):
        status_v2 (Union[Unset, AppCompositeStatus]):
        updated_at (Union[Unset, str]):
        workflow (Union[Unset, AppWorkflow]):
        workflow_id (Union[Unset, str]): Fields that are de-nested at read time using AfterQuery
    """

    action_workflow_runs: Union[Unset, list["AppInstallActionWorkflowRun"]] = UNSET
    app_sandbox_config: Union[Unset, "AppAppSandboxConfig"] = UNSET
    created_at: Union[Unset, str] = UNSET
    created_by: Union[Unset, "AppAccount"] = UNSET
    created_by_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    install_id: Union[Unset, str] = UNSET
    install_sandbox_id: Union[Unset, str] = UNSET
    install_workflow_id: Union[Unset, str] = UNSET
    log_stream: Union[Unset, "AppLogStream"] = UNSET
    outputs: Union[Unset, "AppInstallSandboxRunOutputs"] = UNSET
    run_type: Union[Unset, AppSandboxRunType] = UNSET
    runner_jobs: Union[Unset, list["AppRunnerJob"]] = UNSET
    status: Union[Unset, str] = UNSET
    status_description: Union[Unset, str] = UNSET
    status_v2: Union[Unset, "AppCompositeStatus"] = UNSET
    updated_at: Union[Unset, str] = UNSET
    workflow: Union[Unset, "AppWorkflow"] = UNSET
    workflow_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action_workflow_runs: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.action_workflow_runs, Unset):
            action_workflow_runs = []
            for action_workflow_runs_item_data in self.action_workflow_runs:
                action_workflow_runs_item = action_workflow_runs_item_data.to_dict()
                action_workflow_runs.append(action_workflow_runs_item)

        app_sandbox_config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.app_sandbox_config, Unset):
            app_sandbox_config = self.app_sandbox_config.to_dict()

        created_at = self.created_at

        created_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        created_by_id = self.created_by_id

        id = self.id

        install_id = self.install_id

        install_sandbox_id = self.install_sandbox_id

        install_workflow_id = self.install_workflow_id

        log_stream: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.log_stream, Unset):
            log_stream = self.log_stream.to_dict()

        outputs: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.outputs, Unset):
            outputs = self.outputs.to_dict()

        run_type: Union[Unset, str] = UNSET
        if not isinstance(self.run_type, Unset):
            run_type = self.run_type.value

        runner_jobs: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.runner_jobs, Unset):
            runner_jobs = []
            for runner_jobs_item_data in self.runner_jobs:
                runner_jobs_item = runner_jobs_item_data.to_dict()
                runner_jobs.append(runner_jobs_item)

        status = self.status

        status_description = self.status_description

        status_v2: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.status_v2, Unset):
            status_v2 = self.status_v2.to_dict()

        updated_at = self.updated_at

        workflow: Union[Unset, dict[str, Any]] = UNSET
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
        from ..models.app_runner_job import AppRunnerJob
        from ..models.app_workflow import AppWorkflow

        d = dict(src_dict)
        action_workflow_runs = []
        _action_workflow_runs = d.pop("action_workflow_runs", UNSET)
        for action_workflow_runs_item_data in _action_workflow_runs or []:
            action_workflow_runs_item = AppInstallActionWorkflowRun.from_dict(action_workflow_runs_item_data)

            action_workflow_runs.append(action_workflow_runs_item)

        _app_sandbox_config = d.pop("app_sandbox_config", UNSET)
        app_sandbox_config: Union[Unset, AppAppSandboxConfig]
        if isinstance(_app_sandbox_config, Unset):
            app_sandbox_config = UNSET
        else:
            app_sandbox_config = AppAppSandboxConfig.from_dict(_app_sandbox_config)

        created_at = d.pop("created_at", UNSET)

        _created_by = d.pop("created_by", UNSET)
        created_by: Union[Unset, AppAccount]
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
        log_stream: Union[Unset, AppLogStream]
        if isinstance(_log_stream, Unset):
            log_stream = UNSET
        else:
            log_stream = AppLogStream.from_dict(_log_stream)

        _outputs = d.pop("outputs", UNSET)
        outputs: Union[Unset, AppInstallSandboxRunOutputs]
        if isinstance(_outputs, Unset):
            outputs = UNSET
        else:
            outputs = AppInstallSandboxRunOutputs.from_dict(_outputs)

        _run_type = d.pop("run_type", UNSET)
        run_type: Union[Unset, AppSandboxRunType]
        if isinstance(_run_type, Unset):
            run_type = UNSET
        else:
            run_type = AppSandboxRunType(_run_type)

        runner_jobs = []
        _runner_jobs = d.pop("runner_jobs", UNSET)
        for runner_jobs_item_data in _runner_jobs or []:
            runner_jobs_item = AppRunnerJob.from_dict(runner_jobs_item_data)

            runner_jobs.append(runner_jobs_item)

        status = d.pop("status", UNSET)

        status_description = d.pop("status_description", UNSET)

        _status_v2 = d.pop("status_v2", UNSET)
        status_v2: Union[Unset, AppCompositeStatus]
        if isinstance(_status_v2, Unset):
            status_v2 = UNSET
        else:
            status_v2 = AppCompositeStatus.from_dict(_status_v2)

        updated_at = d.pop("updated_at", UNSET)

        _workflow = d.pop("workflow", UNSET)
        workflow: Union[Unset, AppWorkflow]
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
