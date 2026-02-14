from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_action_workflow_trigger_type import AppActionWorkflowTriggerType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_account import AppAccount
    from ..models.app_action_workflow_config import AppActionWorkflowConfig
    from ..models.app_composite_status import AppCompositeStatus
    from ..models.app_install_action_workflow import AppInstallActionWorkflow
    from ..models.app_install_action_workflow_run_outputs import AppInstallActionWorkflowRunOutputs
    from ..models.app_install_action_workflow_run_run_env_vars import AppInstallActionWorkflowRunRunEnvVars
    from ..models.app_install_action_workflow_run_step import AppInstallActionWorkflowRunStep
    from ..models.app_log_stream import AppLogStream
    from ..models.app_runner_job import AppRunnerJob
    from ..models.app_workflow import AppWorkflow
    from ..models.generics_null_string import GenericsNullString


T = TypeVar("T", bound="AppInstallActionWorkflowRun")


@_attrs_define
class AppInstallActionWorkflowRun:
    """
    Attributes:
        action_workflow_config_id (GenericsNullString | Unset):
        config (AppActionWorkflowConfig | Unset):
        created_at (str | Unset):
        created_by (AppAccount | Unset):
        created_by_id (str | Unset):
        execution_time (int | Unset): after query
        id (str | Unset):
        install_action_workflow (AppInstallActionWorkflow | Unset):
        install_action_workflow_id (GenericsNullString | Unset):
        install_id (str | Unset):
        install_workflow_id (str | Unset):
        log_stream (AppLogStream | Unset):
        outputs (AppInstallActionWorkflowRunOutputs | Unset):
        run_env_vars (AppInstallActionWorkflowRunRunEnvVars | Unset):
        runner_job (AppRunnerJob | Unset):
        status (str | Unset):
        status_description (str | Unset):
        status_v2 (AppCompositeStatus | Unset):
        steps (list[AppInstallActionWorkflowRunStep] | Unset):
        trigger_type (AppActionWorkflowTriggerType | Unset):
        triggered_by_id (str | Unset):
        triggered_by_type (str | Unset):
        updated_at (str | Unset):
        workflow (AppWorkflow | Unset):
        workflow_id (str | Unset):
    """

    action_workflow_config_id: GenericsNullString | Unset = UNSET
    config: AppActionWorkflowConfig | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by: AppAccount | Unset = UNSET
    created_by_id: str | Unset = UNSET
    execution_time: int | Unset = UNSET
    id: str | Unset = UNSET
    install_action_workflow: AppInstallActionWorkflow | Unset = UNSET
    install_action_workflow_id: GenericsNullString | Unset = UNSET
    install_id: str | Unset = UNSET
    install_workflow_id: str | Unset = UNSET
    log_stream: AppLogStream | Unset = UNSET
    outputs: AppInstallActionWorkflowRunOutputs | Unset = UNSET
    run_env_vars: AppInstallActionWorkflowRunRunEnvVars | Unset = UNSET
    runner_job: AppRunnerJob | Unset = UNSET
    status: str | Unset = UNSET
    status_description: str | Unset = UNSET
    status_v2: AppCompositeStatus | Unset = UNSET
    steps: list[AppInstallActionWorkflowRunStep] | Unset = UNSET
    trigger_type: AppActionWorkflowTriggerType | Unset = UNSET
    triggered_by_id: str | Unset = UNSET
    triggered_by_type: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    workflow: AppWorkflow | Unset = UNSET
    workflow_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action_workflow_config_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.action_workflow_config_id, Unset):
            action_workflow_config_id = self.action_workflow_config_id.to_dict()

        config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        created_at = self.created_at

        created_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        created_by_id = self.created_by_id

        execution_time = self.execution_time

        id = self.id

        install_action_workflow: dict[str, Any] | Unset = UNSET
        if not isinstance(self.install_action_workflow, Unset):
            install_action_workflow = self.install_action_workflow.to_dict()

        install_action_workflow_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.install_action_workflow_id, Unset):
            install_action_workflow_id = self.install_action_workflow_id.to_dict()

        install_id = self.install_id

        install_workflow_id = self.install_workflow_id

        log_stream: dict[str, Any] | Unset = UNSET
        if not isinstance(self.log_stream, Unset):
            log_stream = self.log_stream.to_dict()

        outputs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.outputs, Unset):
            outputs = self.outputs.to_dict()

        run_env_vars: dict[str, Any] | Unset = UNSET
        if not isinstance(self.run_env_vars, Unset):
            run_env_vars = self.run_env_vars.to_dict()

        runner_job: dict[str, Any] | Unset = UNSET
        if not isinstance(self.runner_job, Unset):
            runner_job = self.runner_job.to_dict()

        status = self.status

        status_description = self.status_description

        status_v2: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status_v2, Unset):
            status_v2 = self.status_v2.to_dict()

        steps: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.steps, Unset):
            steps = []
            for steps_item_data in self.steps:
                steps_item = steps_item_data.to_dict()
                steps.append(steps_item)

        trigger_type: str | Unset = UNSET
        if not isinstance(self.trigger_type, Unset):
            trigger_type = self.trigger_type.value

        triggered_by_id = self.triggered_by_id

        triggered_by_type = self.triggered_by_type

        updated_at = self.updated_at

        workflow: dict[str, Any] | Unset = UNSET
        if not isinstance(self.workflow, Unset):
            workflow = self.workflow.to_dict()

        workflow_id = self.workflow_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action_workflow_config_id is not UNSET:
            field_dict["action_workflow_config_id"] = action_workflow_config_id
        if config is not UNSET:
            field_dict["config"] = config
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if execution_time is not UNSET:
            field_dict["execution_time"] = execution_time
        if id is not UNSET:
            field_dict["id"] = id
        if install_action_workflow is not UNSET:
            field_dict["install_action_workflow"] = install_action_workflow
        if install_action_workflow_id is not UNSET:
            field_dict["install_action_workflow_id"] = install_action_workflow_id
        if install_id is not UNSET:
            field_dict["install_id"] = install_id
        if install_workflow_id is not UNSET:
            field_dict["install_workflow_id"] = install_workflow_id
        if log_stream is not UNSET:
            field_dict["log_stream"] = log_stream
        if outputs is not UNSET:
            field_dict["outputs"] = outputs
        if run_env_vars is not UNSET:
            field_dict["run_env_vars"] = run_env_vars
        if runner_job is not UNSET:
            field_dict["runner_job"] = runner_job
        if status is not UNSET:
            field_dict["status"] = status
        if status_description is not UNSET:
            field_dict["status_description"] = status_description
        if status_v2 is not UNSET:
            field_dict["status_v2"] = status_v2
        if steps is not UNSET:
            field_dict["steps"] = steps
        if trigger_type is not UNSET:
            field_dict["trigger_type"] = trigger_type
        if triggered_by_id is not UNSET:
            field_dict["triggered_by_id"] = triggered_by_id
        if triggered_by_type is not UNSET:
            field_dict["triggered_by_type"] = triggered_by_type
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
        from ..models.app_action_workflow_config import AppActionWorkflowConfig
        from ..models.app_composite_status import AppCompositeStatus
        from ..models.app_install_action_workflow import AppInstallActionWorkflow
        from ..models.app_install_action_workflow_run_outputs import AppInstallActionWorkflowRunOutputs
        from ..models.app_install_action_workflow_run_run_env_vars import AppInstallActionWorkflowRunRunEnvVars
        from ..models.app_install_action_workflow_run_step import AppInstallActionWorkflowRunStep
        from ..models.app_log_stream import AppLogStream
        from ..models.app_runner_job import AppRunnerJob
        from ..models.app_workflow import AppWorkflow
        from ..models.generics_null_string import GenericsNullString

        d = dict(src_dict)
        _action_workflow_config_id = d.pop("action_workflow_config_id", UNSET)
        action_workflow_config_id: GenericsNullString | Unset
        if isinstance(_action_workflow_config_id, Unset):
            action_workflow_config_id = UNSET
        else:
            action_workflow_config_id = GenericsNullString.from_dict(_action_workflow_config_id)

        _config = d.pop("config", UNSET)
        config: AppActionWorkflowConfig | Unset
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = AppActionWorkflowConfig.from_dict(_config)

        created_at = d.pop("created_at", UNSET)

        _created_by = d.pop("created_by", UNSET)
        created_by: AppAccount | Unset
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = AppAccount.from_dict(_created_by)

        created_by_id = d.pop("created_by_id", UNSET)

        execution_time = d.pop("execution_time", UNSET)

        id = d.pop("id", UNSET)

        _install_action_workflow = d.pop("install_action_workflow", UNSET)
        install_action_workflow: AppInstallActionWorkflow | Unset
        if isinstance(_install_action_workflow, Unset):
            install_action_workflow = UNSET
        else:
            install_action_workflow = AppInstallActionWorkflow.from_dict(_install_action_workflow)

        _install_action_workflow_id = d.pop("install_action_workflow_id", UNSET)
        install_action_workflow_id: GenericsNullString | Unset
        if isinstance(_install_action_workflow_id, Unset):
            install_action_workflow_id = UNSET
        else:
            install_action_workflow_id = GenericsNullString.from_dict(_install_action_workflow_id)

        install_id = d.pop("install_id", UNSET)

        install_workflow_id = d.pop("install_workflow_id", UNSET)

        _log_stream = d.pop("log_stream", UNSET)
        log_stream: AppLogStream | Unset
        if isinstance(_log_stream, Unset):
            log_stream = UNSET
        else:
            log_stream = AppLogStream.from_dict(_log_stream)

        _outputs = d.pop("outputs", UNSET)
        outputs: AppInstallActionWorkflowRunOutputs | Unset
        if isinstance(_outputs, Unset):
            outputs = UNSET
        else:
            outputs = AppInstallActionWorkflowRunOutputs.from_dict(_outputs)

        _run_env_vars = d.pop("run_env_vars", UNSET)
        run_env_vars: AppInstallActionWorkflowRunRunEnvVars | Unset
        if isinstance(_run_env_vars, Unset):
            run_env_vars = UNSET
        else:
            run_env_vars = AppInstallActionWorkflowRunRunEnvVars.from_dict(_run_env_vars)

        _runner_job = d.pop("runner_job", UNSET)
        runner_job: AppRunnerJob | Unset
        if isinstance(_runner_job, Unset):
            runner_job = UNSET
        else:
            runner_job = AppRunnerJob.from_dict(_runner_job)

        status = d.pop("status", UNSET)

        status_description = d.pop("status_description", UNSET)

        _status_v2 = d.pop("status_v2", UNSET)
        status_v2: AppCompositeStatus | Unset
        if isinstance(_status_v2, Unset):
            status_v2 = UNSET
        else:
            status_v2 = AppCompositeStatus.from_dict(_status_v2)

        _steps = d.pop("steps", UNSET)
        steps: list[AppInstallActionWorkflowRunStep] | Unset = UNSET
        if _steps is not UNSET:
            steps = []
            for steps_item_data in _steps:
                steps_item = AppInstallActionWorkflowRunStep.from_dict(steps_item_data)

                steps.append(steps_item)

        _trigger_type = d.pop("trigger_type", UNSET)
        trigger_type: AppActionWorkflowTriggerType | Unset
        if isinstance(_trigger_type, Unset):
            trigger_type = UNSET
        else:
            trigger_type = AppActionWorkflowTriggerType(_trigger_type)

        triggered_by_id = d.pop("triggered_by_id", UNSET)

        triggered_by_type = d.pop("triggered_by_type", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        _workflow = d.pop("workflow", UNSET)
        workflow: AppWorkflow | Unset
        if isinstance(_workflow, Unset):
            workflow = UNSET
        else:
            workflow = AppWorkflow.from_dict(_workflow)

        workflow_id = d.pop("workflow_id", UNSET)

        app_install_action_workflow_run = cls(
            action_workflow_config_id=action_workflow_config_id,
            config=config,
            created_at=created_at,
            created_by=created_by,
            created_by_id=created_by_id,
            execution_time=execution_time,
            id=id,
            install_action_workflow=install_action_workflow,
            install_action_workflow_id=install_action_workflow_id,
            install_id=install_id,
            install_workflow_id=install_workflow_id,
            log_stream=log_stream,
            outputs=outputs,
            run_env_vars=run_env_vars,
            runner_job=runner_job,
            status=status,
            status_description=status_description,
            status_v2=status_v2,
            steps=steps,
            trigger_type=trigger_type,
            triggered_by_id=triggered_by_id,
            triggered_by_type=triggered_by_type,
            updated_at=updated_at,
            workflow=workflow,
            workflow_id=workflow_id,
        )

        app_install_action_workflow_run.additional_properties = d
        return app_install_action_workflow_run

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
