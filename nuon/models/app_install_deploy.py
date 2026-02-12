from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_install_deploy_type import AppInstallDeployType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_account import AppAccount
    from ..models.app_component_build import AppComponentBuild
    from ..models.app_composite_status import AppCompositeStatus
    from ..models.app_install_action_workflow_run import AppInstallActionWorkflowRun
    from ..models.app_install_deploy_outputs import AppInstallDeployOutputs
    from ..models.app_log_stream import AppLogStream
    from ..models.app_oci_artifact import AppOCIArtifact
    from ..models.app_policy_report import AppPolicyReport
    from ..models.app_runner_job import AppRunnerJob
    from ..models.app_workflow import AppWorkflow


T = TypeVar("T", bound="AppInstallDeploy")


@_attrs_define
class AppInstallDeploy:
    """
    Attributes:
        action_workflow_runs (list[AppInstallActionWorkflowRun] | Unset):
        build_id (str | Unset):
        component_build (AppComponentBuild | Unset):
        component_config_version (int | Unset):
        component_id (str | Unset):
        component_name (str | Unset):
        created_at (str | Unset):
        created_by (AppAccount | Unset):
        created_by_id (str | Unset):
        id (str | Unset):
        install_component_id (str | Unset):
        install_deploy_type (AppInstallDeployType | Unset):
        install_id (str | Unset): Fields that are de-nested at read time using AfterQuery
        install_workflow_id (str | Unset): DEPRECATED: use WorkflowID
        log_stream (AppLogStream | Unset):
        oci_artifact (AppOCIArtifact | Unset):
        outputs (AppInstallDeployOutputs | Unset):
        plan_only (bool | Unset):
        policy_reports (list[AppPolicyReport] | Unset):
        release_id (str | Unset):
        runner_jobs (list[AppRunnerJob] | Unset): runner details
        status (str | Unset):
        status_description (str | Unset):
        status_v2 (AppCompositeStatus | Unset):
        updated_at (str | Unset):
        workflow (AppWorkflow | Unset):
        workflow_id (str | Unset):
    """

    action_workflow_runs: list[AppInstallActionWorkflowRun] | Unset = UNSET
    build_id: str | Unset = UNSET
    component_build: AppComponentBuild | Unset = UNSET
    component_config_version: int | Unset = UNSET
    component_id: str | Unset = UNSET
    component_name: str | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by: AppAccount | Unset = UNSET
    created_by_id: str | Unset = UNSET
    id: str | Unset = UNSET
    install_component_id: str | Unset = UNSET
    install_deploy_type: AppInstallDeployType | Unset = UNSET
    install_id: str | Unset = UNSET
    install_workflow_id: str | Unset = UNSET
    log_stream: AppLogStream | Unset = UNSET
    oci_artifact: AppOCIArtifact | Unset = UNSET
    outputs: AppInstallDeployOutputs | Unset = UNSET
    plan_only: bool | Unset = UNSET
    policy_reports: list[AppPolicyReport] | Unset = UNSET
    release_id: str | Unset = UNSET
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

        build_id = self.build_id

        component_build: dict[str, Any] | Unset = UNSET
        if not isinstance(self.component_build, Unset):
            component_build = self.component_build.to_dict()

        component_config_version = self.component_config_version

        component_id = self.component_id

        component_name = self.component_name

        created_at = self.created_at

        created_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        created_by_id = self.created_by_id

        id = self.id

        install_component_id = self.install_component_id

        install_deploy_type: str | Unset = UNSET
        if not isinstance(self.install_deploy_type, Unset):
            install_deploy_type = self.install_deploy_type.value

        install_id = self.install_id

        install_workflow_id = self.install_workflow_id

        log_stream: dict[str, Any] | Unset = UNSET
        if not isinstance(self.log_stream, Unset):
            log_stream = self.log_stream.to_dict()

        oci_artifact: dict[str, Any] | Unset = UNSET
        if not isinstance(self.oci_artifact, Unset):
            oci_artifact = self.oci_artifact.to_dict()

        outputs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.outputs, Unset):
            outputs = self.outputs.to_dict()

        plan_only = self.plan_only

        policy_reports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.policy_reports, Unset):
            policy_reports = []
            for policy_reports_item_data in self.policy_reports:
                policy_reports_item = policy_reports_item_data.to_dict()
                policy_reports.append(policy_reports_item)

        release_id = self.release_id

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
        if build_id is not UNSET:
            field_dict["build_id"] = build_id
        if component_build is not UNSET:
            field_dict["component_build"] = component_build
        if component_config_version is not UNSET:
            field_dict["component_config_version"] = component_config_version
        if component_id is not UNSET:
            field_dict["component_id"] = component_id
        if component_name is not UNSET:
            field_dict["component_name"] = component_name
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if id is not UNSET:
            field_dict["id"] = id
        if install_component_id is not UNSET:
            field_dict["install_component_id"] = install_component_id
        if install_deploy_type is not UNSET:
            field_dict["install_deploy_type"] = install_deploy_type
        if install_id is not UNSET:
            field_dict["install_id"] = install_id
        if install_workflow_id is not UNSET:
            field_dict["install_workflow_id"] = install_workflow_id
        if log_stream is not UNSET:
            field_dict["log_stream"] = log_stream
        if oci_artifact is not UNSET:
            field_dict["oci_artifact"] = oci_artifact
        if outputs is not UNSET:
            field_dict["outputs"] = outputs
        if plan_only is not UNSET:
            field_dict["plan_only"] = plan_only
        if policy_reports is not UNSET:
            field_dict["policy_reports"] = policy_reports
        if release_id is not UNSET:
            field_dict["release_id"] = release_id
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
        from ..models.app_component_build import AppComponentBuild
        from ..models.app_composite_status import AppCompositeStatus
        from ..models.app_install_action_workflow_run import AppInstallActionWorkflowRun
        from ..models.app_install_deploy_outputs import AppInstallDeployOutputs
        from ..models.app_log_stream import AppLogStream
        from ..models.app_oci_artifact import AppOCIArtifact
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

        build_id = d.pop("build_id", UNSET)

        _component_build = d.pop("component_build", UNSET)
        component_build: AppComponentBuild | Unset
        if isinstance(_component_build, Unset):
            component_build = UNSET
        else:
            component_build = AppComponentBuild.from_dict(_component_build)

        component_config_version = d.pop("component_config_version", UNSET)

        component_id = d.pop("component_id", UNSET)

        component_name = d.pop("component_name", UNSET)

        created_at = d.pop("created_at", UNSET)

        _created_by = d.pop("created_by", UNSET)
        created_by: AppAccount | Unset
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = AppAccount.from_dict(_created_by)

        created_by_id = d.pop("created_by_id", UNSET)

        id = d.pop("id", UNSET)

        install_component_id = d.pop("install_component_id", UNSET)

        _install_deploy_type = d.pop("install_deploy_type", UNSET)
        install_deploy_type: AppInstallDeployType | Unset
        if isinstance(_install_deploy_type, Unset):
            install_deploy_type = UNSET
        else:
            install_deploy_type = AppInstallDeployType(_install_deploy_type)

        install_id = d.pop("install_id", UNSET)

        install_workflow_id = d.pop("install_workflow_id", UNSET)

        _log_stream = d.pop("log_stream", UNSET)
        log_stream: AppLogStream | Unset
        if isinstance(_log_stream, Unset):
            log_stream = UNSET
        else:
            log_stream = AppLogStream.from_dict(_log_stream)

        _oci_artifact = d.pop("oci_artifact", UNSET)
        oci_artifact: AppOCIArtifact | Unset
        if isinstance(_oci_artifact, Unset):
            oci_artifact = UNSET
        else:
            oci_artifact = AppOCIArtifact.from_dict(_oci_artifact)

        _outputs = d.pop("outputs", UNSET)
        outputs: AppInstallDeployOutputs | Unset
        if isinstance(_outputs, Unset):
            outputs = UNSET
        else:
            outputs = AppInstallDeployOutputs.from_dict(_outputs)

        plan_only = d.pop("plan_only", UNSET)

        _policy_reports = d.pop("policy_reports", UNSET)
        policy_reports: list[AppPolicyReport] | Unset = UNSET
        if _policy_reports is not UNSET:
            policy_reports = []
            for policy_reports_item_data in _policy_reports:
                policy_reports_item = AppPolicyReport.from_dict(policy_reports_item_data)

                policy_reports.append(policy_reports_item)

        release_id = d.pop("release_id", UNSET)

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

        app_install_deploy = cls(
            action_workflow_runs=action_workflow_runs,
            build_id=build_id,
            component_build=component_build,
            component_config_version=component_config_version,
            component_id=component_id,
            component_name=component_name,
            created_at=created_at,
            created_by=created_by,
            created_by_id=created_by_id,
            id=id,
            install_component_id=install_component_id,
            install_deploy_type=install_deploy_type,
            install_id=install_id,
            install_workflow_id=install_workflow_id,
            log_stream=log_stream,
            oci_artifact=oci_artifact,
            outputs=outputs,
            plan_only=plan_only,
            policy_reports=policy_reports,
            release_id=release_id,
            runner_jobs=runner_jobs,
            status=status,
            status_description=status_description,
            status_v2=status_v2,
            updated_at=updated_at,
            workflow=workflow,
            workflow_id=workflow_id,
        )

        app_install_deploy.additional_properties = d
        return app_install_deploy

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
